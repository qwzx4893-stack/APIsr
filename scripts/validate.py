"""Validate catalog consistency and prevent accidental private credential commits."""
import csv, json, re, sys
from collections import Counter
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
root = Path(__file__).resolve().parents[1]
errors = []
def check(condition, message):
    if not condition: errors.append(message)

data = json.loads((root/'data/catalog.json').read_text(encoding='utf-8'))
entries = data['services']
check(data['total_services']==len(entries),'total_services mismatch')
check(dict(Counter(x['category'] for x in entries))==data['category_counts'],'category counts mismatch')
check(dict(Counter(x['free_type'] for x in entries))==data['free_type_counts'],'free_type counts mismatch')
check(len({x['id'] for x in entries})==len(entries),'duplicate IDs')
check(len({x['name'].casefold() for x in entries})==len(entries),'duplicate service names')
auths={'no_key','api_key','account_token','api_key_or_no_key','api_key_or_public_demo','username','public_demo_key'}
commercial={'allowed','restricted','non_commercial','development_only','unknown'}
for x in entries:
    prefix=x['id']
    for field in ['name','category','category_ar','auth','free_type','quota','reset','base_url','get_access_url','limitations_ar']:
        check(isinstance(x.get(field),str) and bool(x[field]),f'{prefix}: missing {field}')
    check(x['auth'] in auths,f'{prefix}: unknown auth')
    check(x['free_type'] in {'recurring_quota','unmetered_public'},f'{prefix}: nonrecurring trial admitted')
    check(x['commercial_use'] in commercial,f'{prefix}: invalid commercial status')
    check(x['price_usd_within_free_scope']==0,f'{prefix}: nonzero free-scope price')
    check(x['private_credentials_included'] is False,f'{prefix}: private credentials flag')
    check(x['credit_card_required'] in (None,True,False),f'{prefix}: card field')
    verification=x['verification']
    check(verification['status']=='official_documentation_reviewed',f'{prefix}: unreviewed record')
    check(bool(verification['evidence']),f'{prefix}: missing primary evidence')
    for proof in verification['evidence']:
        check(proof['url'].startswith('https://'),f'{prefix}: evidence must use HTTPS')
        check(bool(re.fullmatch(r'\d{4}-\d{2}-\d{2}',proof['checked_on'])),f'{prefix}: evidence date missing')
    check(x['get_access_url'].startswith('https://'),f'{prefix}: access URL')
    check(prefix in (root/'README.md').read_text(encoding='utf-8') or x['name'] in (root/'README.md').read_text(encoding='utf-8'),f'{prefix}: absent from README')

with (root/'data/catalog.csv').open(encoding='utf-8-sig',newline='') as fp:
    csv_rows=list(csv.DictReader(fp))
check(len(csv_rows)==len(entries),'CSV row count mismatch')
check({x['id'] for x in csv_rows}=={x['id'] for x in entries},'CSV IDs mismatch')
indexed={x['id']:x for x in entries}
for row in csv_rows:
    x=indexed[row['id']]
    for field in ['name','category','auth','free_type','quota','reset','limitations_ar']:
        check(row[field]==x[field],f"CSV mismatch: {row['id']}:{field}")

excluded=json.loads((root/'data/excluded-and-unconfirmed.json').read_text(encoding='utf-8'))
check(all(x['status'] in {'excluded','excluded_by_rule','pending_verification'} for x in excluded),'invalid exclusion status')
for demo in json.loads((root/'data/public-demo-keys.json').read_text(encoding='utf-8'))['examples']:
    check(demo['service_id'] in indexed,'demo missing catalog service')
    check(demo['provider_published_public_example'] is True,'private demo key')
    check(demo['key'] in {'DEMO_KEY','1','demo','helloworld'},'unknown literal demo credential')

shared=json.loads((root/'data/public-shared-keys.json').read_text(encoding='utf-8'))
shared_rows=shared['services']
summary=shared['summary']
check(summary['services']==len(shared_rows),'shared service count mismatch')
check(summary['unique_public_key_values']==len({x['key'] for x in shared_rows}),'shared distinct-key count mismatch')
check(summary['category_counts']==dict(Counter(x['category'] for x in shared_rows)),'shared categories mismatch')
check(summary['access_scope_counts']==dict(Counter(x['access_scope'] for x in shared_rows)),'shared scopes mismatch')
check(len({x['id'] for x in shared_rows})==len(shared_rows),'duplicate shared service IDs')
check(summary['synthetic_practice_services']==sum(x['access_scope']=='synthetic_practice' for x in shared_rows),'synthetic practice count mismatch')
check(summary['recurring_quota_services']==sum(x['free_type']=='recurring_quota' for x in shared_rows),'shared recurring count mismatch')
check(summary['practical_services']==sum(x['project_use']['practical'] for x in shared_rows),'practical service count mismatch')
check(summary['pending_failed_candidates']==len(json.loads((root/'research/public-key-unconfirmed.json').read_text(encoding='utf-8'))['candidates']),'pending shared count mismatch')
approved_keys={
 'DEMO_KEY','1','demo','helloworld','123','FREE','mc_demo_public','dm_demo_public',
 'learn_api_demo_key','demo-key-abc123','tw_demo_explore','thumbapi_test',
 'AEP7KDgcD904RFSNxX82kpe2zDGJHwawQE2Bu4ZCO0c',
 'clix_fxC9tzt_I7fiKMpvTQbU5CNiL647PQu9ssvE3C4jAlPyw3sf3hY',
 'sbi_live_84fdd6cc6a6b2df3e38a9f19a49537a5',
 'or_sk5T_yGimzi2EF8CaG-JS_OA6_Eruw_r-eoCLSM8yMU',
 'corx_wurhkSx9Z5GkXBs85bu8iyqJ-963qATW','gk_demo_public_v1',
 'kt_demo_00000000000000000000000000','3','YOUR_API_KEY_HERE',
}
shared_doc=(root/'docs/public-shared-keys.ar.md').read_text(encoding='utf-8')
shared_tests=json.loads((root/'research/public-key-tests.json').read_text(encoding='utf-8'))
shared_test_ids={x['id'] for x in shared_tests['results'] if x['ok']}
check(shared_test_ids=={x['id'] for x in shared_rows},'live-tested shared IDs mismatch')
check(shared_tests['primary_passed']==len(shared_rows),'shared passing count mismatch')
check(shared_tests['primary_attempted']==len(shared_tests['results']),'shared attempted count mismatch')
for x in shared_rows:
 prefix=x['id']
 check(x['key'] in approved_keys,f'{prefix}: unreviewed public literal')
 check(x['provider_published_for_public_use'] is True and x['private_credentials_included'] is False,f'{prefix}: private shared credential')
 check(x['requires_signup'] is False and x['requires_credit_card'] is False,f'{prefix}: signup or card required')
 check(x['price_usd_in_documented_scope']==0,f'{prefix}: nonzero shared price')
 check(x['free_type'] in {'recurring_quota','ongoing_public_demo'},f'{prefix}: one-time trial admitted')
 check(x['access_scope'] in {'public_data','development_data','restricted_sample_data','sandbox_data','synthetic_practice'},f'{prefix}: invalid shared scope')
 verification=x['verification']
 check(verification['status']=='official_docs_and_live_request_verified',f'{prefix}: unverified shared record')
 check(bool(verification['evidence']) and all(e['url'].startswith('https://') for e in verification['evidence']),f'{prefix}: missing shared evidence')
 check(verification['live_test']['ok'] is True and verification['live_test']['http_status']==200,f'{prefix}: failed shared test admitted')
 check(verification['live_test']['uses_private_key'] is False,f'{prefix}: private key test')
 check(x['name'] in shared_doc and x['key'] in shared_doc,f'{prefix}: absent from shared guide')
 check(bool(x['project_use']['examples_ar']),f'{prefix}: missing project example')
 check(x['project_use']['practical']==(x['access_scope'] not in {'sandbox_data','synthetic_practice'}),f'{prefix}: fictional data marked practical')
 request=x['example_request']
 check(request['method'] in {'GET','POST'} and request['url'].startswith('https://'),f'{prefix}: invalid request')
 check(request['url']==verification['live_test']['url'],f'{prefix}: untested example URL')
 check(x['key'] in json.dumps(request),f'{prefix}: example does not include key')
 check(verification.get('semantic_check',{}).get('semantic_check_passed',True) is True,f'{prefix}: failed semantic check')
with (root/'data/public-shared-keys.csv').open(encoding='utf-8-sig',newline='') as fp:
 shared_csv=list(csv.DictReader(fp))
check(len(shared_csv)==len(shared_rows),'shared CSV count mismatch')
check({x['id']:x['key'] for x in shared_csv}=={x['id']:x['key'] for x in shared_rows},'shared CSV key mismatch')
check({x['id']:x['practical'] for x in shared_csv}=={x['id']:str(x['project_use']['practical']) for x in shared_rows},'shared CSV practical mismatch')
shared_ledger=json.loads((root/'research/public-key-sources.json').read_text(encoding='utf-8'))
check({x['url'] for x in shared_ledger}=={e['url'] for x in shared_rows for e in x['verification']['evidence']},'shared source ledger mismatch')

coverage=json.loads((root/'research/coverage.json').read_text(encoding='utf-8'))
check(coverage['verified_services']==len(entries),'coverage count mismatch')
check(coverage['auth_counts']==dict(Counter(x['auth'] for x in entries)),'coverage auth mismatch')
check(coverage['official_evidence_pages']==len(json.loads((root/'research/official-sources.json').read_text(encoding='utf-8'))),'source-ledger count mismatch')
rounds=json.loads((root/'research/research-rounds.json').read_text(encoding='utf-8'))['rounds']
check(rounds[-1]['verified_services']==len(entries),'research-round total mismatch')
check(rounds[-1]['previous_services']+rounds[-1]['added_services']==len(entries),'research-round additions mismatch')
for report_path in (root/'research').glob('smoke-tests*.json'):
    report=json.loads(report_path.read_text(encoding='utf-8'))
    check(report['attempted']==len(report['results']),f'{report_path.name}: count mismatch')
    check(report['passed']==sum(x['ok'] for x in report['results']),f'{report_path.name}: passed mismatch')
    check(all(x['service_id'] in indexed and x['uses_private_key'] is False for x in report['results']),f'{report_path.name}: unknown service or private key')

pattern=re.compile(r'(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[A-Z0-9]{16}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----)')
for file in root.rglob('*'):
    if not file.is_file() or '.git' in file.parts or '__pycache__' in file.parts: continue
    if file.suffix.lower() not in {'.json','.csv','.md','.py','.yml','.yaml','.txt',''}: continue
    try: content=file.read_text(encoding='utf-8-sig')
    except UnicodeDecodeError: continue
    check(not pattern.search(content),f'Possible private credential in {file.relative_to(root)} (value suppressed)')
    check(file.name not in {'.env','.env.local','credentials.json','token.txt'},f'Forbidden credential file: {file.name}')

if errors:
    print('\n'.join(errors));sys.exit(1)
print(f'PASS: {len(entries)} reviewed catalog services; {len(shared_rows)} live-tested shared-key services, {summary["unique_public_key_values"]} distinct public values; JSON/CSV consistent; no recognized private credential patterns.')
