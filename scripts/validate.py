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
    check(demo['key'] in {'DEMO_KEY','1','demo'},'unknown literal demo credential')

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
print(f'PASS: {len(entries)} reviewed services, {len(data["category_counts"])} categories; JSON/CSV consistent; no recognized private credential patterns.')
