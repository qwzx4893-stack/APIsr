"""Search the reviewed catalog offline. Python 3.10+, no dependencies."""
import argparse, json, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description='Search APIsr without making API calls or using credentials.')
parser.add_argument('query', nargs='?', default='')
parser.add_argument('--category')
parser.add_argument('--auth')
parser.add_argument('--free-type', choices=['recurring_quota','unmetered_public'])
parser.add_argument('--commercial', choices=['allowed','restricted','non_commercial','development_only','unknown'])
parser.add_argument('--no-card', action='store_true', help='Only explicit no-card or keyless entries; unknown is excluded.')
parser.add_argument('--json', action='store_true')
args = parser.parse_args()
entries = json.loads((root/'data/catalog.json').read_text(encoding='utf-8'))['services']
matches = []
for item in entries:
    if args.query.casefold() not in json.dumps(item,ensure_ascii=False).casefold(): continue
    if args.category and item['category'] != args.category: continue
    if args.auth and item['auth'] != args.auth: continue
    if args.free_type and item['free_type'] != args.free_type: continue
    if args.commercial and item['commercial_use'] != args.commercial: continue
    if args.no_card and item['credit_card_required'] is not False: continue
    matches.append(item)
if args.json:
    print(json.dumps(matches,ensure_ascii=False,indent=2))
else:
    for item in matches:
        print(f"{item['name']} [{item['category']}, {item['auth']}]\n  {item['quota']}\n  {item['get_access_url']}\n  {item['limitations_ar']}\n")
    print(f'{len(matches)} matching services')
