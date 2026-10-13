# المفاتيح العامة دون تسجيل

**47 خدمة نجح طلبها، 26 قيمة مفتاح مختلفة، 28 مجالًا. المراجعة: 2026-10-13 بتوقيت بغداد.**

[JSON بالمفاتيح والطلبات](../data/public-shared-keys.json) · [CSV](../data/public-shared-keys.csv) · [أمثلة المشاريع العملية](practical-projects.ar.md) · [نتائج الاختبار](../research/public-key-tests.json) · [المصادر الرسمية](../research/public-key-sources.json) · [غير المحسوم](../research/public-key-unconfirmed.json)

القائمة الحالية ليست حصرًا لكل الخدمات الموجودة. أضافت جولة الاستكمال 5 خدمات و5 قيم مفتاح جديدة: ثلاث لبيانات أو وظائف فعلية واثنتان لمحاكاة التكامل. يمكن تصفية **39 خدمة تفيد نموذج مشروع ببيانات عامة أو تحويل محتوى فعلي**؛ تبقى 5 خدمات sandbox ببيانات وهمية وثلاث للتدريب أو placeholder منفصلة. تصنيف practical لا يعني إباحة الإنتاج التجاري.

كل قيمة في هذه القائمة متاحة من المزود دون إنشاء حساب أو تسجيل أو بطاقة، داخل النطاق المحدد. أرقام الخدمات تختلف عن أرقام المفاتيح: DEMO_KEY وdemo و123 مشتركة بين أكثر من خدمة. الكتالوج العام ذا 260 خدمة يشمل خدمات تتطلب حسابًا؛ ليس 260 مفتاحًا مشتركًا.

المفتاح منشور بإذن صاحبه، ولم تجمع مفاتيح حسابات أشخاص من مشاريعهم. بعض القيم للتطوير فقط أو لرموز محددة أو لغير التجاري. لا تُنسخ حصة المفتاح الشخصي إلى المفتاح العام. عدم نشر حد رقمي لا يعني unlimited، ومدة انتهاء البيانات التجريبية تختلف عن تجديد حصة الطلبات.

لـ api.data.gov افتراض وثائقي 30 طلبًا/ساعة و50/يوم حسب IP، لكنه يسمح باختلاف الخدمات. أظهرت خدمتا GSA Site Scanning وDAP حدًا 10 في header؛ نافذته لم تثبت، لذلك هذا ظاهر في الصفوف ولا ننسب إليهما 30 كحصة فعلية. الحصص المشتركة لا تجمع تلقائيًا لكل endpoint.

## المفاتيح ذات البيانات الفعلية أو التحويل الحقيقي أو sandbox

| الخدمة | المفتاح | المجال | النطاق | الحصة والتجديد | الطلب والمصدر |
|---|---|---|---|---|---|
| NASA Open APIs | `DEMO_KEY` | الفضاء | بيانات عامة فعلية | 30/hour and 50/day/IP — hour/day | [GET example](https://api.nasa.gov/neo/rest/v1/neo/browse?page=0&size=1&api_key=DEMO_KEY) · [المصدر](https://api.nasa.gov/assets/html/authentication.html) |
| TheMealDB | `1` | الطعام والمشروبات | تطوير بخدمة فعلية أو محدودة | Numeric shared-key quota not published — ongoing public development access | [GET example](https://www.themealdb.com/api/json/v1/1/search.php?s=Arrabiata) · [المصدر](https://www.themealdb.com/api.php) |
| TheCocktailDB | `1` | الطعام والمشروبات | تطوير بخدمة فعلية أو محدودة | Numeric shared-key quota not published — ongoing public development access | [GET example](https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita) · [المصدر](https://www.thecocktaildb.com/api.php) |
| Alpha Vantage demo | `demo` | البيانات المالية | أمثلة أو بيانات محددة | Only documented demo queries; no numeric shared quota published — ongoing published examples | [GET example](https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo) · [المصدر](https://www.alphavantage.co/documentation/) |
| GovInfo | `DEMO_KEY` | البيانات الحكومية | بيانات عامة فعلية | api.data.gov default: 30/hour and 50/day/IP — hour/day | [GET example](https://api.govinfo.gov/collections?api_key=DEMO_KEY) · [المصدر](https://api.data.gov/docs/developer-manual/) |
| OCR.space public GET examples | `helloworld` | التعرف على النص | أمثلة أو بيانات محددة | Numeric shared-key quota not separately published — ongoing published examples | [GET example](https://api.ocr.space/parse/imageurl?apikey=helloworld&url=https://dl.a9t9.com/ocr/solarcell.jpg) · [المصدر](https://ocr.space/ocrapi) |
| TheSportsDB v1 | `123` | الرياضة | بيانات عامة فعلية | 30 requests/minute; result limits by endpoint — minute | [GET example](https://www.thesportsdb.com/api/v1/json/123/searchteams.php?t=Arsenal) · [المصدر](https://api.thesportsdb.com/documentation) |
| TheAudioDB v1 | `123` | الموسيقى | تطوير بخدمة فعلية أو محدودة | 30 requests/minute; limited results — minute | [GET example](https://www.theaudiodb.com/api/v1/json/123/search.php?s=coldplay) · [المصدر](https://www.theaudiodb.com/free_music_api) |
| Twelve Data demo | `demo` | البيانات المالية | أمثلة أو بيانات محددة | Numeric shared demo quota not separately published — ongoing published examples | [GET example](https://api.twelvedata.com/price?symbol=AAPL&apikey=demo) · [المصدر](https://twelvedata.com/docs) |
| EODHD demo | `demo` | البيانات المالية | أمثلة أو بيانات محددة | Numeric shared demo quota not separately published — ongoing published examples | [GET example](https://eodhd.com/api/eod/AAPL.US?api_token=demo&fmt=json&from=2026-09-01&to=2026-09-02) · [المصدر](https://eodhd.com/financial-apis/quick-start-with-our-financial-data-apis) |
| ERPDocs public sandbox | `AEP7KDgcD904RFSNxX82kpe2zDGJHwawQE2Bu4ZCO0c` | المستندات | بيانات sandbox | 30 requests/minute — minute | [GET example](https://www.erpdocs.com/api/v1/ping) · [المصدر](https://www.erpdocs.com/developers) |
| Mapconvert | `mc_demo_public` | الخرائط والإحداثيات | تطوير بخدمة فعلية أو محدودة | 1 request/minute — minute | [POST example](https://api.mapconvert.dev/coordinates) · [المصدر](https://mapconvert.dev/api) |
| Clix public invoicing sandbox | `clix_fxC9tzt_I7fiKMpvTQbU5CNiL647PQu9ssvE3C4jAlPyw3sf3hY` | خدمات الأعمال | بيانات sandbox | 200 created invoices/month shared; reads remain available — month | [GET example](https://sandbox.api.goclix.ai/v1/api/invoices/) · [المصدر](https://docs.goclix.ai/developers/try-the-api/) |
| TradeWave public demo | `tw_demo_explore` | البيانات المالية | أمثلة أو بيانات محددة | 30 requests/minute; 1000/day in documented demo /me example — minute/day | [GET example](https://api.tradewave.ai/v1/scan?markets=2&limit=1) · [المصدر](https://developers.tradewave.ai/docs/quickstart.html) |
| SportsBookISH public data demo | `sbi_live_84fdd6cc6a6b2df3e38a9f19a49537a5` | الرياضة | أمثلة أو بيانات محددة | Numeric shared-key quota not published — ongoing public demo offer | [GET example](https://sportsbookish.com/api/v1/edges?min_edge=0.03) · [المصدر](https://raw.githubusercontent.com/kennyhyder/sportsbookish-docs/main/README.md) |
| National Park Service | `DEMO_KEY` | الحدائق | بيانات عامة فعلية | api.data.gov demo default: 30/hour and 50/day/IP — hour/day | [GET example](https://developer.nps.gov/api/v1/parks?parkCode=acad&limit=1&api_key=DEMO_KEY) · [المصدر](https://www.nps.gov/subjects/developer/get-started.htm) |
| Congress.gov v3 | `DEMO_KEY` | البيانات الحكومية | بيانات عامة فعلية | api.data.gov demo default: 30/hour and 50/day/IP — hour/day | [GET example](https://api.congress.gov/v3/bill?format=json&limit=1&api_key=DEMO_KEY) · [المصدر](https://raw.githubusercontent.com/LibraryOfCongress/api.congress.gov/main/README.md) |
| OpenFEC | `DEMO_KEY` | البيانات الحكومية | بيانات عامة فعلية | api.data.gov demo default: 30/hour and 50/day/IP — hour/day | [GET example](https://api.open.fec.gov/v1/candidates/?per_page=1&api_key=DEMO_KEY) · [المصدر](https://api.open.fec.gov/developers/) |
| Federal Audit Clearinghouse | `DEMO_KEY` | البيانات الحكومية | بيانات عامة فعلية | 30/hour and 50/day/IP — hour/day | [GET example](https://api.fac.gov/general?limit=1) · [المصدر](https://www.fac.gov/api/getting-started/) |
| Data.gov Catalog v4 | `DEMO_KEY` | البيانات الحكومية | بيانات عامة فعلية | 30/hour and 50/day/IP — hour/day | [GET example](https://api.gsa.gov/technology/datagov/v4/search?q=climate&limit=1) · [المصدر](https://resources.data.gov/catalog-api/) |
| api.data.gov public metrics | `DEMO_KEY` | البيانات الحكومية | بيانات عامة فعلية | api.data.gov demo default: 30/hour and 50/day/IP — hour/day | [GET example](https://api.gsa.gov/operations/api-data-gov/v0/analytics/summary.json) · [المصدر](https://open.gsa.gov/api/apidatagov-metrics/) |
| GSA Per Diem | `DEMO_KEY` | السفر | بيانات عامة فعلية | api.data.gov demo default: 30/hour and 50/day/IP — hour/day | [GET example](https://api.gsa.gov/travel/perdiem/v2/rates/conus/lodging/2026?api_key=DEMO_KEY) · [المصدر](https://open.gsa.gov/api/perdiem/) |
| NLR Developer APIs, formerly NREL | `DEMO_KEY` | الطاقة | بيانات عامة فعلية | 30/hour and 50/day/IP — hour/day | [GET example](https://developer.nlr.gov/api/alt-fuel-stations/v1.json?limit=1&api_key=DEMO_KEY) · [المصدر](https://developer.nlr.gov/docs/api-key/) |
| USGS Water Data OGC API | `DEMO_KEY` | البيئة | بيانات عامة فعلية | api.data.gov demo default: 30/hour and 50/day/IP — hour/day | [GET example](https://api.waterdata.usgs.gov/ogcapi/v1/collections/daily/items?limit=1&api_key=DEMO_KEY) · [المصدر](https://api.waterdata.usgs.gov/docs/ogcapi/) |
| EPA ATTAINS water assessments | `DEMO_KEY` | البيئة | بيانات عامة فعلية | api.data.gov demo default: 30/hour and 50/day/IP — hour/day | [GET example](https://api.epa.gov/attains/domains?domainName=ParameterStatus&api_key=DEMO_KEY) · [المصدر](https://www.epa.gov/system/files/documents/2026-04/attains_web_services_api_key_2026-04-28.pdf) |
| Smithsonian Open Access | `DEMO_KEY` | الثقافة والمتاحف | بيانات عامة فعلية | api.data.gov demo default: 30/hour and 50/day/IP — hour/day | [GET example](https://api.si.edu/openaccess/api/v1.0/search?q=moon&rows=1&api_key=DEMO_KEY) · [المصدر](https://edan.si.edu/openaccess/apidocs/) |
| College Scorecard | `DEMO_KEY` | التعليم | بيانات عامة فعلية | api.data.gov demo default: 30/hour and 50/day/IP — hour/day | [GET example](https://api.data.gov/ed/collegescorecard/v1/schools?per_page=1&fields=id,school.name&api_key=DEMO_KEY) · [المصدر](https://collegescorecard.ed.gov/data/api/) |
| TheDeskMonitor public MCP demo | `dm_demo_public` | إدارة العمل | بيانات sandbox | Numeric shared demo quota not published — ongoing public demo offer | [POST example](https://api.thedeskmonitor.com/api/mcp/v1/) · [المصدر](https://thedeskmonitor.com/integrations/ai-connect) |
| OrbitRoute shared evaluation key | `or_sk5T_yGimzi2EF8CaG-JS_OA6_Eruw_r-eoCLSM8yMU` | توجيه الحوسبة | تطوير بخدمة فعلية أو محدودة | 100 routing decisions/day shared — day | [GET example](https://www.orbitroute.ai/api/v1/usage) · [المصدر](https://www.orbitroute.ai/api-reference) |
| InkTranslator FREE | `FREE` | الترجمة | تطوير بخدمة فعلية أو محدودة | 50 characters/request; numeric aggregate rate cap not published — ongoing public free test scope | [POST example](https://inktranslator.com/api/translate) · [المصدر](https://inktranslator.com/lang/en) |
| CORX public CORS proxy | `corx_wurhkSx9Z5GkXBs85bu8iyqJ-963qATW` | طلبات المواقع | تطوير بخدمة فعلية أو محدودة | 3000 requests/day/calling site; 100000/day/whole instance; target-host caps also apply — day (UTC) | [GET example](https://corx.envx.cn/fetch?url=https%3A%2F%2Fexample.com%2F&corx-key=corx_wurhkSx9Z5GkXBs85bu8iyqJ-963qATW) · [المصدر](https://corx.envx.cn/en) |
| Attestwire invoice validation demo | `demo` | المستندات | تطوير بخدمة فعلية أو محدودة | 6 requests/minute; 30 documents/day/IP shared across validate, generate and recipient — minute/day (UTC) | [POST example](https://api.attestwire.com/v1/validate) · [المصدر](https://attestwire.com/pricing) |
| Genji Crowd public development key | `gk_demo_public_v1` | رسوم ومشاهد ثلاثية الأبعاد | تطوير بخدمة فعلية أو محدودة | 60 requests/minute/IP; 5000/day/IP; 50 crowd creations/day/IP; up to 5000 characters/crowd — minute/day | [GET example](https://www.genjicrowd.com/v1/projects) · [المصدر](https://www.genjicrowd.com/docs) |
| KeepTrack satellite-data demo | `kt_demo_00000000000000000000000000` | الفضاء | بيانات عامة فعلية | 30 requests/hour with the public demo key — hour | [GET example](https://api.keeptrack.space/v4/sats/25544) · [المصدر](https://keeptrack.space/api) |
| TheVehicleDB public test API | `3` | السيارات والمركبات | تطوير بخدمة فعلية أو محدودة | 30 requests/minute; 1 returned item/request — minute | [GET example](https://www.thevehicledb.com/api/v1/json/3/searchmodel.php?m=cobra) · [المصدر](https://www.thevehicledb.com/free_car_api) |
| DocRaptor public PDF test key | `YOUR_API_KEY_HERE` | المستندات | تطوير بخدمة فعلية أو محدودة | Unlimited test documents advertised; shared-key numeric throttling limit not separately published — ongoing public test mode | [POST example](https://api.docraptor.com/docs) · [المصدر](https://docraptor.com/documentation) |
| OddiWire public REST preview | `demo` | الرياضة | أمثلة أو بيانات محددة | 10 requests/5 minutes pooled across all demo callers — 5 minutes | [GET example](https://oddiwire.com/v1/fixtures?key=demo&limit=1) · [المصدر](https://oddiwire.com/llms-full.txt) |
| GSA Site Scanning public demo | `DEMO_KEY` | تعلم واختبار APIs | بيانات عامة فعلية | Observed X-RateLimit-Limit=10; header did not identify its time window; api.data.gov default demo policy is 30/hour and 50/day/IP with service overrides — recurring api.data.gov windows; exact service header window unconfirmed | [GET example](https://api.gsa.gov/technology/site-scanning/v1/websites?limit=1) · [المصدر](https://open.gsa.gov/api/site-scanning-api/) |
| analytics.usa.gov DAP public demo | `DEMO_KEY` | إحصاءات استخدام المواقع | بيانات عامة فعلية | Observed X-RateLimit-Limit=10; header did not identify its time window; api.data.gov default demo policy is 30/hour and 50/day/IP with service overrides — recurring api.data.gov windows; exact service header window unconfirmed | [GET example](https://api.gsa.gov/analytics/dap/v2/reports/language/data?limit=1) · [المصدر](https://open.gsa.gov/api/dap/) |
| Meducate public educational demo | `d3m0000000000000000000000000key1.MEDUCATE_PUBLIC_DEMO_2026` | مراجع صحية وتعليمية | بيانات عامة فعلية | 50 requests/day shared demo key; observed limit=50 and UTC-day reset header — day (UTC) | [GET example](https://api.meducateapi.com/api/v1/topics/search?query=asthma) · [المصدر](https://meducateapi.com/docs) |
| AIPower shared AI-model demo | `sk-aipower-demo-public` | الذكاء الاصطناعي | تطوير بخدمة فعلية أو محدودة | 5 calls/IP/day; restricted to demo models DeepSeek, Qwen Turbo and GLM-4 Flash — day; exact reset time not published | [POST example](https://api.aipower.me/v1/chat/completions) · [المصدر](https://aipower.me/docs) |
| NYX Suite synthetic fund-data demo | `nyx_dk_demo000000000000000000000000000000000000000` | البيانات المالية | بيانات sandbox | Observed shared demo limit: 10 requests/600-second window — 600 seconds (observed header) | [GET example](https://nyxsuite.com/api/v1/fund/overview) · [المصدر](https://nyxsuite.com/developers/quickstart) |
| unmap shared mapping development key | `um_test_793cf0c9cb8f4f5cf12bbdebdd96b59532b38876fbe5d14d` | الخرائط والمواقع | تطوير بخدمة فعلية أو محدودة | Public demo is shared and rate-limited; gateway documents 1000 requests/60 seconds/location for every key; a separate demo allocation is not published — ongoing public development access; gateway rate window 60 seconds | [GET example](https://api.unmap.dev/geocode/search?q=Calgary%20Tower&limit=1) · [المصدر](https://unmap.dev/docs/start/quickstart) |
| Blue Reacher public messaging simulator | `brk_test_Dc815ar0WQChF5odYSeB8k2ovmVf1zG2` | محاكاة تكامل الرسائل | بيانات sandbox | 60 requests/minute/shared key across /v1; 10/minute for simulated instant sends — minute | [GET example](https://api.bluereacher.com/v1/usage) · [المصدر](https://docs.bluereacher.com/docs/guides/sandbox) |

## مفاتيح تدريب وplaceholder

| الخدمة | المفتاح | المجال | النطاق | الحصة والتجديد | الطلب والمصدر |
|---|---|---|---|---|---|
| Learn API authentication lab | `learn_api_demo_key` | تعلم واختبار APIs | تدريب أو placeholder فقط | Numeric quota not published — ongoing public practice endpoint | [GET example](https://learn-api.com/wp-json/learn-api/v1/labs/api-key) · [المصدر](https://learn-api.com/api-basics/read-api-documentation/) |
| QA Bash API-key practice | `demo-key-abc123` | تعلم واختبار APIs | تدريب أو placeholder فقط | Numeric quota not published for auth exercise — ongoing public practice endpoint | [GET example](https://www.qabash.com/api/tools/sample-api/auth/api-key) · [المصدر](https://www.qabash.com/learning/api-playground) |
| ThumbAPI integration test | `thumbapi_test` | الصور | تدريب أو placeholder فقط | No credits consumed by documented test key; numeric rate cap not published — ongoing public placeholder endpoint | [POST example](https://api.thumbapi.dev/v1/generate) · [المصدر](https://thumbapi.dev/docs/quickstart) |

## الطلبات الجاهزة

رابط POST أو طلب مصادقة في header لا يكفي فتحه في المتصفح. اعرض الطلب الكامل بهذه الأداة؛ لا ترسل الأداة شيئًا:

```sh
python scripts/public_keys.py --practical
python scripts/public_keys.py --practical --category documents
python scripts/public_keys.py --service docraptor-public-test --request
python scripts/public_keys.py --scope sandbox_data
```

DocRaptor يستخدم Basic Auth باسم المستخدم الذي يساوي المفتاح العام وكلمة مرور فارغة؛ يظهر header الصحيح وبيانات المصادقة في JSON. يشترط test=true لإخراج PDF مجاني بعلامة اختبار.

## القيود حسب الخدمة

- **NASA Open APIs**: مفتاح استكشاف رسمي. نجح مثال الكويكبات NeoWs؛ مثال APOD الافتراضي أعاد HTTP 500 في هذه الجولة.
- **TheMealDB**: للتطوير والتعليم. نشر تطبيق على متجر التطبيقات يحتاج مفتاح supporter؛ بعض عمليات البحث والمحتوى Premium.
- **TheCocktailDB**: للتطوير والتعليم. مفتاح الإنتاج وخصائص Premium مدفوعة؛ لا تفترض إباحة النشر التجاري بهذا المفتاح.
- **Alpha Vantage demo**: المثال المختبر بيانات IBM اليومية. المفتاح لا يمنح كل الرموز أو endpoints؛ حصة المفتاح المسجل لا تنطبق تلقائيًا عليه.
- **GovInfo**: قراءة الوثائق الحكومية العامة للاستكشاف. مثال collections مختبر؛ قيود الخدمة قد تختلف.
- **OCR.space public GET examples**: helloworld منشور لأمثلة GET الرسمية. نجح استخراج نص الصورة المثال؛ لا ننسب إليه حصة المفتاح المسجل البالغة 25000 طلب شهريًا.
- **TheSportsDB v1**: المفتاح الحالي 123. بحث الفرق المجاني مقيد بـ Arsenal؛ نتائج عمليات أخرى مقيدة بعدد قليل. v2 وميزات موسعة مدفوعة.
- **TheAudioDB v1**: المفتاح الحالي في الوثائق 123 ونجح بحث Coldplay. المفتاح القديم 2 فشل. إرشادات المزود القديمة تمنع استخدام مفتاح الاختبار في الإنتاج؛ التزم بالتطوير.
- **Twelve Data demo**: demo رسمي للأمثلة؛ نجح price لـ AAPL. الرموز وخصائص Premium مقيدة، ولا يساوي المفتاح الشخصي أو حصته.
- **EODHD demo**: المزود يتيح تجربة البيانات دون تسجيل لرموز محددة. المثال المختبر AAPL.US؛ بيانات أخرى وحقوق إعادة توزيعها تحتاج الخطة المناسبة.
- **ERPDocs public sandbox**: مؤسسة تجريبية بقوالب ومظاريف مثال. قراءة فقط؛ الإرسال محظور، والمفتاح قابل للتدوير ولا يستخدم للإنتاج.
- **Mapconvert**: تحويل رابط Google Maps إلى إحداثيات. مفتاح التجربة العام؛ المفتاح الشخصي مطلوب لما يتجاوز الاختبار.
- **Clix public invoicing sandbox**: بيانات sandbox فقط، وليس نظام إصدار فواتيرك الفعلي. القراءة المختبرة لا تنشئ فاتورة؛ حد الإنشاء مشترك ويتجدد شهريًا والمفتاح قد يتغير.
- **Learn API authentication lab**: قيمة تدريب عامة تعيد استجابة توضيحية؛ ليست اعتماد حساب ولا خدمة بيانات فعلية.
- **QA Bash API-key practice**: تمرين API-Key ببيانات وهمية ونطاق sample-api:read؛ ليس خدمة إنتاج لإدارة المستخدمين.
- **TradeWave public demo**: الرمز العام مقيد بسوق S&P 500 وخمسة tickers: AAPL وMSFT وNVDA وAMZN وTSLA؛ حتى 5 فرص. لا ينفذ معاملات مالية.
- **SportsBookISH public data demo**: المفتاح معلن صراحةً كمفتاح مشترك دون تسجيل في مستودع المزود. القراءة تعيد بيانات احتمالات وأسعار؛ لا ينفذ رهانات. ترخيص CSV لا يفترض تلقائيًا لكل استخدام API.
- **ThumbAPI integration test**: يعيد صورة placeholder ثابتة لا صورة مولدة بحسب عنوانك؛ مخصص لاختبار الربط فقط.
- **National Park Service**: قراءة معلومات الحدائق العامة. المصدر يربط نظام api.data.gov؛ نجح المفتاح المشترك في parks. راجع حقوق الصور.
- **Congress.gov v3**: استكشاف التشريعات العامة. نظام المفتاح موثق في مستودع LibraryOfCongress الرسمي؛ لا ننسب حصة 5000/hour للمفتاح التجريبي.
- **OpenFEC**: قراءة بيانات الانتخابات وتمويل الحملات العامة. توثيق المزود يستخدم api.data.gov؛ لا وصول إداري.
- **Federal Audit Clearinghouse**: DEMO_KEY منشور رسميًا للاستكشاف. لا يسمح بالوصول إلى بيانات التدقيق القبلي المحجوبة؛ القراءة العامة فقط.
- **Data.gov Catalog v4**: البحث في metadata مجموعات البيانات وليس تنزيل كل محتوياتها. يحل v4 محل CKAN القديم. المزود لا يوصي بالمفتاح للتشغيل الآلي الإنتاجي.
- **api.data.gov public metrics**: مقاييس عامة لخدمة API. المصدر ينشر DEMO_KEY للأمثلة؛ ليست Admin API التي تتطلب رمز إدارة إضافيًا.
- **GSA Per Diem**: بدلات السفر الحكومية. توثيق المزود يحدد نظام api.data.gov؛ نجح مثال بدل السكن لعام 2026.
- **NLR Developer APIs, formerly NREL**: المجال الحالي developer.nlr.gov. نجح مثال محطات الوقود البديل. الحصة مشتركة عبر APIs المختبر وليست حصة إضافية لكل endpoint.
- **USGS Water Data OGC API**: المثال الرسمي يضع DEMO_KEY في استعلام القياسات اليومية. نجحت قراءة سجل واحد؛ لا نحول عدد datasets إلى عدد مفاتيح.
- **EPA ATTAINS water assessments**: تحديث وثائق أبريل 2026 يصرح بصلاحية DEMO_KEY بحد منخفض. نجح مثال ParameterStatus؛ البنية الحالية api.epa.gov/attains.
- **Smithsonian Open Access**: استكشاف سجل المتاحف العام عبر نظام api.data.gov. نجح search؛ تراخيص المواد والصور تختلف ويجب مراجعتها.
- **College Scorecard**: بيانات الجامعات العامة. مصدر التعليم يوثق نظام المفتاح؛ نجح schools. حصة 1000/hour هي الحصة العادية وليست حصة DEMO_KEY.
- **TheDeskMonitor public MCP demo**: شركة وهمية من 8 موظفين. المفتاح المجاني دون حساب يتيح القراءة؛ الكتابة تتطلب dm_live. نجح get_dashboard_summary دون إنشاء سجل أو دعوة شخص.
- **OrbitRoute shared evaluation key**: GET /api/v1/keys/demo يعطي المفتاح المشترك بلا حساب. نجح /usage وأكد free و100/day. توثيق /route يصف قرار توجيه فقط؛ التنفيذ الفعلي له شروط مستقلة. المفتاح قد يدور.
- **InkTranslator FREE**: المزود يسمح مباشرة بمفتاح FREE دون تسجيل؛ نجحت ترجمة Hello إلى العربية. حد 2000 حرف خاص بالمفاتيح المدفوعة.
- **CORX public CORS proxy**: GET وHEAD لبيانات عامة فقط. يزيل Cookie وAuthorization من الطلب المرسل للمصدر ويستخدم cache مشتركًا وسجلات 30 يومًا. مفتاح عام للتجربة والنماذج؛ لا يصلح لبيانات خاصة أو أسرار.
- **Attestwire invoice validation demo**: المفتاح يقبل ثلاثة مسارات فقط؛ لا /parse ولا إرسال فواتير ولا سجلات تحقق ولا MCP. نجحت فاتورة المثال مع valid=true. للاستخدام المعتاد يوصي المزود بمفتاحك الشخصي.
- **Genji Crowd public development key**: المفتاح معلن وآمن للتضمين في JavaScript بحسب المزود. crowds المنشأة تنتهي بعد 24 ساعة؛ هذه مدة البيانات وليست رصيد تجربة لمرة واحدة. اختُبر GET /v1/projects ونجحت القائمة الفارغة؛ لم تنشأ crowd ولم تختبر كل خصائص التوليد. راجع ترخيص الأصول قبل توزيعها.
- **KeepTrack satellite-data demo**: مجانية الاستخدام الخاص والبحثي والتعليمي تحت CC BY-NC 4.0؛ ليست إذنًا لتطبيق تجاري. نجحت عناصر مدار ISS. احسب المواقع محليًا بواسطة OOTK بدل افتراض أن حصة positions هي نفسها حصة العناصر المدارية.
- **TheVehicleDB public test API**: المفتاح العام 3 موثق لـ v1 وv2. نجح مثال Cobra وأعاد حقول نموذج سيارة تحت search. لم تُختبر v2، ولا تعني إتاحة artwork ترخيصًا مستقلًا لإعادة توزيعه.
- **DocRaptor public PDF test key**: القيمة الحرفية YOUR_API_KEY_HERE تعمل رسميًا دون حساب بشرط test=true. نجح إخراج PDF فعلي. PDF يحمل علامة اختبار، وExcel في test يقف عند 20 صفًا. لا تستخدمه كمستند إنتاج نهائي بلا علامة.
- **OddiWire public REST preview**: REST فقط؛ لا SSE بالمفتاح العام. المزود يصرح أنه preview وليس اعتماد إنتاج. البيانات من خدمة مستقلة، ولا ينفذ الطلب رهانًا أو معاملة.
- **GSA Site Scanning public demo**: المصدر ينشر DEMO_KEY صراحةً. نجحت قراءة بيانات scan منشورة لمواقع حكومية؛ لا يطلب تشغيل فحص جديد على أي موقع. الحد 10 المشاهد أقل من الافتراضي، فلا تعتمد 30 كحصة فعلية لهذه الخدمة.
- **analytics.usa.gov DAP public demo**: قراءة إحصاءات مجمعة منشورة لزيارات المواقع الحكومية، وليست حساب تحليلات موقعك. نجح تقرير اللغات. الحد 10 المشاهد خاص بالاستجابة؛ نافذته لم تثبت من header.
- **Meducate public educational demo**: المفتاح في حقل readonly موسوم Public demo key بالوثائق. أعاد البحث سجلين فعليين؛ البيانات ملخصات يعالجها المزود بنماذج لغوية، ومخصصة للتعليم والمعلومات. ليست بيانات مرضى ولا إثباتًا لدقة سريرية. حصة 1000/يوم تخص المفتاح المسجل ولا تنسب إلى هذا المفتاح.
- **AIPower shared AI-model demo**: المفتاح عام ومذكور صراحة دون تسجيل أو بطاقة. نجحت إجابة نصية غير فارغة من نموذج demo. لا يشمل GPT أو Claude أو بقية النماذج المدفوعة. رصيد 10 مكالمات عند إنشاء حساب عرض مختلف ولم يقبل هنا.
- **NYX Suite synthetic fund-data demo**: بيانات صندوق استثمار اصطناعية فقط؛ ليست بيانات صندوقك أو حساب عميل. نجحت حقول fund وshareClasses وlatestNav. حاسبات NYX بلا مفتاح وحصتها 500/يوم سطح مختلف؛ لم تنسب إلى هذا المفتاح. لا يمكن للمفتاح العام إنشاء مقترحات إدارة الصندوق.
- **unmap shared mapping development key**: المزود ينشر القيمة الكاملة في quickstart ويجيز تضمينها للتجربة. نجح البحث عن Calgary Tower وأعاد اسمًا وإحداثيات فعلية. للتطوير والنماذج، لا يفترض إذن تشغيل نطاق إنتاج. حصة Hobby البالغة 10000/شهر لا تنسب إلى المفتاح المشترك. لم يرسل الاختبار Origin مصطنعًا ولم يختبر جميع خدمات الخرائط أو التوجيه.
- **Blue Reacher public messaging simulator**: المفتاح يعمل في simulator دون حساب أو مساحة عمل حقيقية. اختُبر GET /v1/usage لبيانات sample فقط. لا يرسل رسائل حقيقية؛ تسجيل webhook قد يرسل اختبارًا إلى رابطك ولم ينفذ هنا. سجل المحادثات وبعض إعدادات الاتصال تحتاج مفتاح live.

## نتائج التحقق وحدودها

القائمة تجمع نتائج جولات البحث، وليست إعادة اختبار لكل خدمة في كل جولة. 47 خدمة لديها طلب ناجح موثق، و13 مرشحين فشلت طلباتهم خارج القائمة الجاهزة. تأريخ الاختبار وURL ونوع الاستجابة محفوظة لكل سجل. نجح توليد نص قصير بواسطة AIPower وقراءة سجل جغرافي من unmap وسجلين مرجعيين من Meducate. نجح PDF فعلي وJSON فاتورة الاختبار، ونتائج المركبات تحققت من idModel وstrModel، وعناصر مدار ISS من TLE_LINE_1 وTLE_LINE_2. نجاح قائمة Genji الفارغة يثبت مثال القراءة والمصادقة؛ لم تُنشأ حشود.

PinnWire أعاد 429 لأن الحصة العامة المشتركة اليومية استُهلكت؛ لم نصنفه كمفتاح باطل، ولم نضعه كطلب جاهز الآن. SnapForge أعاد 429 لحصة 50/يوم المستهلكة. مفتاح Agent Winds للعقارات أعاد 401، وKnockout تجاوز مهلة القراءة في محاولتين محدودتين. USDA وRegulations.gov ما زالا غير محسومين في هذه البيئة. GSA eMuseum أعاد 503. لا نكرر الطلبات لتجاوز الحصص ولا نتحايل بتدوير مفاتيح أو IP.

الإثبات الوثائقي يثبت النطاق المجاني المعلن، والطلب يثبت نجاح المثال وقت الفحص؛ لا يثبت كل endpoints أو SLA أو أن الخطة ستبقى للأبد. اختبارات POST اقتصرت على نص/رابط اختبار، وبيانات وهمية، وقراءة MCP، وتنسيق PDF، والتحقق من JSON فاتورة دون إرسالها.
