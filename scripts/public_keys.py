"""Search provider-published shared keys; printing a request never sends it."""
import argparse,json,sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--service',help='Exact service ID')
parser.add_argument('--category')
parser.add_argument('--scope',choices=['public_data','development_data','restricted_sample_data','sandbox_data','synthetic_practice'])
parser.add_argument('--practical',action='store_true',help='Show real-data or transformation prototypes; exclude fictional sandbox and practice-only services')
parser.add_argument('--request',action='store_true',help='Print complete request JSON without executing it')
parser.add_argument('--json',action='store_true',help='Print selected records as JSON')
args=parser.parse_args()
data=json.loads((Path(__file__).resolve().parents[1]/'data/public-shared-keys.json').read_text(encoding='utf-8'))
rows=[x for x in data['services'] if (not args.service or x['id']==args.service) and (not args.category or x['category']==args.category) and (not args.scope or x['access_scope']==args.scope) and (not args.practical or x['project_use']['practical'])]
if not rows:
 print('No matching service.',file=sys.stderr);sys.exit(1)
if args.request:
 print(json.dumps([{'service_id':x['id'],**x['example_request']} for x in rows],ensure_ascii=False,indent=2))
elif args.json:
 print(json.dumps(rows,ensure_ascii=False,indent=2))
else:
 print(f"{len(rows)} services; {len({x['key'] for x in rows})} distinct public key values")
 for x in rows:print(f"{x['id']}\t{x['key']}\t{x['access_scope']}\t{x['quota']}")
