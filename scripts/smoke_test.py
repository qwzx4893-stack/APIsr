"""A few public read-only GETs. Liveness is separate from pricing verification."""
import concurrent.futures, datetime, json, urllib.request, urllib.error
from pathlib import Path

root=Path(__file__).resolve().parents[1]
tests=[
 ('jsonplaceholder','https://jsonplaceholder.typicode.com/todos/1'),
 ('dummyjson','https://dummyjson.com/products/1'),
 ('pokeapi','https://pokeapi.co/api/v2/pokemon/1'),
 ('free-dictionary-api','https://api.dictionaryapi.dev/api/v2/entries/en/hello'),
 ('frankfurter','https://api.frankfurter.dev/v1/latest?base=USD'),
 ('open-meteo','https://api.open-meteo.com/v1/forecast?latitude=40.71&longitude=-74.01&current=temperature_2m'),
 ('tvmaze-public-api','https://api.tvmaze.com/shows/1'),
 ('open-trivia-db','https://opentdb.com/api.php?amount=1'),
 ('themealdb-development-api','https://www.themealdb.com/api/json/v1/1/search.php?s=Arrabiata'),
 ('thecocktaildb-development-api','https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita'),
 ('nasa-open-apis','https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'),
 ('art-institute-of-chicago','https://api.artic.edu/api/v1/artworks/129884?fields=id,title'),
 ('github-rest-api','https://api.github.com/repos/public-apis/public-apis'),
 ('world-bank-indicators-api','https://api.worldbank.org/v2/country/USA/indicator/SP.POP.TOTL?format=json&per_page=1'),
 ('nager-holiday-public-holiday-api','https://nagerholidays.com/api/v4/Holidays/AT/2026'),
]
def test(item):
    name,url=item
    out={'service_id':name,'url':url,'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'uses_private_key':False}
    try:
        request=urllib.request.Request(url,headers={'User-Agent':'APIsr-catalog-check/1.0 (read-only sample request)','Accept':'application/json'})
        with urllib.request.urlopen(request,timeout=20) as response:
            body=response.read(2_000_000)
            parsed=json.loads(body)
            semantic_error=isinstance(parsed,dict) and ('error' in parsed or ('Error Message' in parsed) or (parsed.get('response_code',0)!=0))
            out.update({'http_status':response.status,'valid_json':True,'payload_has_error':semantic_error,'ok':response.status==200 and not semantic_error,'response_bytes':len(body)})
    except Exception as exc:
        out.update({'ok':False,'error':str(exc)[:250]})
    return out
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool: results=list(pool.map(test,tests))
report={'note_ar':'هذه استجابات عينات فقط، ليست إثباتًا للمجانية ولا اختبارًا لكل الخدمات. لا يتجاوز الفحص rate limits ولا يعيد المحاولات تلقائيًا. فشل اتصال هذه البيئة لا يعني توقف الخدمة عالميًا.','attempted':len(results),'passed':sum(x['ok'] for x in results),'results':results}
(root/'research/smoke-tests.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'attempted':report['attempted'],'passed':report['passed'],'failed':[x['service_id'] for x in results if not x['ok']]},ensure_ascii=False))
