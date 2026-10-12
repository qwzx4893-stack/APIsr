# المفاتيح العامة دون تسجيل

**33 خدمة نجح طلبها، 16 قيمة مفتاح مختلفة، 21 مجالًا. المراجعة: 2026-10-13 بتوقيت بغداد.**

[JSON بالمفاتيح والطلبات](../data/public-shared-keys.json) · [CSV](../data/public-shared-keys.csv) · [نتائج الاختبار](../research/public-key-tests.json) · [المصادر الرسمية](../research/public-key-sources.json) · [غير المحسوم](../research/public-key-unconfirmed.json)

هذا القسم يحقق شرط عدم إنشاء حساب أو تسجيل للحصول على القيمة المدرجة. عدد الخدمات لا يساوي عدد المفاتيح: `DEMO_KEY` و`demo` و`123` مشتركة بين أكثر من خدمة. **3 خدمات تدريبية أو placeholder تظهر منفصلة أدناه ولا تمثل APIs بيانات إنتاجية.** القائمة العامة ذات 260 خدمة في README تشمل خدمات تحتاج حسابًا، وليست هذه القائمة الخاصة.

كل قيمة هنا منشورة بإذن صاحب الخدمة للاستخدام العام في النطاق المحدد. لا نجمع مفاتيح شخصية ظاهرة في مستودعات الآخرين. صلاحية المثال لا تعطي حق استخدام كل endpoints، ولا تجعل مفتاح sandbox مفتاح إنتاج. حصص api.data.gov للمفتاح التجريبي محدودة حسب IP وقد تكون مشتركة؛ لا تجمع 50 طلبًا لكل صف كحصص مستقلة. لا ننسب حصة المفتاح الشخصي إلى مفتاح الأمثلة.

المزود الذي لا ينشر حدًا رقميًا موضح كذلك؛ ذلك لا يعني طلبات غير محدودة. القيم العامة قد تدور، والمجانية هنا للنطاق الحالي المنشور وليست ضمان استمرار الخدمة للأبد.

## المفاتيح ذات البيانات الفعلية أو sandbox

| الخدمة | المفتاح العام | المجال | النطاق | الحصة والتجديد | الطلب والمصدر |
|---|---|---|---|---|---|
| NASA Open APIs | `DEMO_KEY` | الفضاء | بيانات عامة فعلية | 30/hour and 50/day/IP — hour/day | [GET example](https://api.nasa.gov/neo/rest/v1/neo/browse?page=0&size=1&api_key=DEMO_KEY) · [المصدر](https://api.nasa.gov/assets/html/authentication.html) |
| TheMealDB | `1` | الطعام والمشروبات | تطوير مع بيانات فعلية أو خدمة محدودة | Numeric shared-key quota not published — ongoing public development access | [GET example](https://www.themealdb.com/api/json/v1/1/search.php?s=Arrabiata) · [المصدر](https://www.themealdb.com/api.php) |
| TheCocktailDB | `1` | الطعام والمشروبات | تطوير مع بيانات فعلية أو خدمة محدودة | Numeric shared-key quota not published — ongoing public development access | [GET example](https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita) · [المصدر](https://www.thecocktaildb.com/api.php) |
| Alpha Vantage demo | `demo` | البيانات المالية | أمثلة ورموز محددة | Only documented demo queries; no numeric shared quota published — ongoing published examples | [GET example](https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo) · [المصدر](https://www.alphavantage.co/documentation/) |
| GovInfo | `DEMO_KEY` | البيانات الحكومية | بيانات عامة فعلية | api.data.gov default: 30/hour and 50/day/IP — hour/day | [GET example](https://api.govinfo.gov/collections?api_key=DEMO_KEY) · [المصدر](https://api.data.gov/docs/developer-manual/) |
| OCR.space public GET examples | `helloworld` | التعرف على النص | أمثلة ورموز محددة | Numeric shared-key quota not separately published — ongoing published examples | [GET example](https://api.ocr.space/parse/imageurl?apikey=helloworld&url=https://dl.a9t9.com/ocr/solarcell.jpg) · [المصدر](https://ocr.space/ocrapi) |
| TheSportsDB v1 | `123` | الرياضة | بيانات عامة فعلية | 30 requests/minute; result limits by endpoint — minute | [GET example](https://www.thesportsdb.com/api/v1/json/123/searchteams.php?t=Arsenal) · [المصدر](https://api.thesportsdb.com/documentation) |
| TheAudioDB v1 | `123` | الموسيقى | تطوير مع بيانات فعلية أو خدمة محدودة | 30 requests/minute; limited results — minute | [GET example](https://www.theaudiodb.com/api/v1/json/123/search.php?s=coldplay) · [المصدر](https://www.theaudiodb.com/free_music_api) |
| Twelve Data demo | `demo` | البيانات المالية | أمثلة ورموز محددة | Numeric shared demo quota not separately published — ongoing published examples | [GET example](https://api.twelvedata.com/price?symbol=AAPL&apikey=demo) · [المصدر](https://twelvedata.com/docs) |
| EODHD demo | `demo` | البيانات المالية | أمثلة ورموز محددة | Numeric shared demo quota not separately published — ongoing published examples | [GET example](https://eodhd.com/api/eod/AAPL.US?api_token=demo&fmt=json&from=2026-09-01&to=2026-09-02) · [المصدر](https://eodhd.com/financial-apis/quick-start-with-our-financial-data-apis) |
| ERPDocs public sandbox | `AEP7KDgcD904RFSNxX82kpe2zDGJHwawQE2Bu4ZCO0c` | المستندات | بيانات sandbox | 30 requests/minute — minute | [GET example](https://www.erpdocs.com/api/v1/ping) · [المصدر](https://www.erpdocs.com/developers) |
| Mapconvert | `mc_demo_public` | الخرائط والإحداثيات | تطوير مع بيانات فعلية أو خدمة محدودة | 1 request/minute — minute | [POST example](https://api.mapconvert.dev/coordinates) · [المصدر](https://mapconvert.dev/api) |
| Clix public invoicing sandbox | `clix_fxC9tzt_I7fiKMpvTQbU5CNiL647PQu9ssvE3C4jAlPyw3sf3hY` | خدمات الأعمال | بيانات sandbox | 200 created invoices/month shared; reads remain available — month | [GET example](https://sandbox.api.goclix.ai/v1/api/invoices/) · [المصدر](https://docs.goclix.ai/developers/try-the-api/) |
| TradeWave public demo | `tw_demo_explore` | البيانات المالية | أمثلة ورموز محددة | 30 requests/minute; 1000/day in documented demo /me example — minute/day | [GET example](https://api.tradewave.ai/v1/scan?markets=2&limit=1) · [المصدر](https://developers.tradewave.ai/docs/quickstart.html) |
| SportsBookISH public data demo | `sbi_live_84fdd6cc6a6b2df3e38a9f19a49537a5` | الرياضة | أمثلة ورموز محددة | Numeric shared-key quota not published — ongoing public demo offer | [GET example](https://sportsbookish.com/api/v1/edges?min_edge=0.03) · [المصدر](https://raw.githubusercontent.com/kennyhyder/sportsbookish-docs/main/README.md) |
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
| OrbitRoute shared evaluation key | `or_sk5T_yGimzi2EF8CaG-JS_OA6_Eruw_r-eoCLSM8yMU` | توجيه الحوسبة | تطوير مع بيانات فعلية أو خدمة محدودة | 100 routing decisions/day shared — day | [GET example](https://www.orbitroute.ai/api/v1/usage) · [المصدر](https://www.orbitroute.ai/api-reference) |
| InkTranslator FREE | `FREE` | الترجمة | تطوير مع بيانات فعلية أو خدمة محدودة | 50 characters/request; numeric aggregate rate cap not published — ongoing public free test scope | [POST example](https://inktranslator.com/api/translate) · [المصدر](https://inktranslator.com/lang/en) |

## مفاتيح تدريب وplaceholder

| الخدمة | المفتاح العام | المجال | النطاق | الحصة والتجديد | الطلب والمصدر |
|---|---|---|---|---|
| Learn API authentication lab | `learn_api_demo_key` | تعلم واختبار APIs | تدريب أو placeholder فقط | Numeric quota not published — ongoing public practice endpoint | [GET example](https://learn-api.com/wp-json/learn-api/v1/labs/api-key) · [المصدر](https://learn-api.com/api-basics/read-api-documentation/) |
| QA Bash API-key practice | `demo-key-abc123` | تعلم واختبار APIs | تدريب أو placeholder فقط | Numeric quota not published for auth exercise — ongoing public practice endpoint | [GET example](https://www.qabash.com/api/tools/sample-api/auth/api-key) · [المصدر](https://www.qabash.com/learning/api-playground) |
| ThumbAPI integration test | `thumbapi_test` | الصور | تدريب أو placeholder فقط | No credits consumed by documented test key; numeric rate cap not published — ongoing public placeholder endpoint | [POST example](https://api.thumbapi.dev/v1/generate) · [المصدر](https://thumbapi.dev/docs/quickstart) |

## الطلبات الجاهزة والقيود

روابط POST وروابط المصادقة في header لن تعمل بمجرد فتحها في المتصفح. استخدم الطلب الكامل في JSON أو أداة البحث التالية. عرض الطلب لا يرسل شيئًا:

```sh
python scripts/public_keys.py
python scripts/public_keys.py --category translation
python scripts/public_keys.py --service mapconvert-demo --request
python scripts/public_keys.py --scope sandbox_data
```

`--request` يطبع method وURL وheaders وbody بالمفتاح العام. لا يُجري طلبًا ولا يُنشئ حسابًا.

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

## حدود الاختبار

جرى اختبار 41 طلبًا أساسيًا لمرشحين أو قيم مختلفة؛ المقبول 33 والباقي 8 خارج القائمة الجاهزة. مثال NASA APOD فشل، فاختُبر NeoWs ونجح؛ لذلك لا يُعرض APOD كطلب ناجح. بعض الفشل بسبب DNS أو timeout وليس إثبات توقف عالمي. اختُبرت استجابات خمسة مزودين دلاليًا، منها ترجمة غير فارغة ونجاح مصادقة OrbitRoute بالحصة المنشورة.

المصادر الرسمية تدعم إتاحة المفتاح ونطاقه، والاختبار يدعم نجاح المثال وقت الفحص. لا يضمن أي منهما SLA أو كل الرموز والخصائص. POST المختبر اقتصر على تحويل رابط أو ترجمة نص اختبار أو بيانات وهمية أو قراءة MCP؛ لم يُرسل شيء إلى أشخاص.
