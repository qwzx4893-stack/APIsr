# خدمات بمفاتيح عامة تفيد المشاريع

**36 خدمة من أصل 42 مفيدة لنموذج مشروع ببيانات فعلية أو تحويل حقيقي، ضمن الحدود الموثقة.** تحتاج بعضها إلى مفتاح شخصي أو ترخيص مناسب عند الانتقال إلى الإنتاج. خدمات sandbox الوهمية والتدريب ليست ضمن هذا الرقم.

## ما أضيف في الجولة الموجهة للمشاريع

| الخدمة | مثال مشروع | الحصة المهمة | شرط الاستخدام |
|---|---|---|---|
| CORX | نموذج موقع يستدعي بيانات عامة عبر CORS | 3000 طلب/يوم لكل موقع و100000 للمثيل، مع حدود أخرى | بيانات عامة فقط؛ المفتاح المشترك للتجربة والنماذج |
| DocRaptor | تطوير تصميم تقارير أو فواتير PDF من HTML/CSS | وثائق test مجانية غير محدودة معلنة | test=true وPDF بعلامة اختبار؛ ليس ملف الإنتاج النهائي |
| Attestwire | تجربة مدقق JSON لفواتير EN 16931 | 6/دقيقة و30 مستندًا/يوم/IP | validate وgenerate وrecipient فقط؛ لا إرسال أو MCP |
| TheVehicleDB | نموذج كتالوج طرازات سيارات | 30/دقيقة وسجل واحد في الرد | المفتاح 3 اختبار عام؛ تحقق من ترخيص artwork |
| KeepTrack | تطبيق تعليمي يعرض مدار ISS | 30/ساعة للمفتاح demo | الاستخدام الخاص والبحثي والتعليمي؛ CC BY-NC 4.0 |
| Genji Crowd | نموذج مشهد لعبة أو صفحة Three.js | 5000 طلب/يوم و50 إنشاء crowd/يوم/IP | البيانات المنشأة تنتهي بعد 24 ساعة؛ ترخيص الأصول يحتاج مراجعة |
| OddiWire | نموذج لوحة fixtures وأسعار رياضية | 10 طلبات/5 دقائق مشتركة | REST فقط، والمزود يمنع اعتباره اعتماد إنتاج |
| GSA Site Scanning | عرض نتائج فحص منشورة للمواقع الحكومية | header أظهر حدًا 10، نافذته غير محسومة | قراءة نتائج قائمة، وليس إطلاق فحوص على مواقع المستخدمين |
| DAP analytics | عرض إحصاءات زيارات حكومية مجمعة | header أظهر حدًا 10، نافذته غير محسومة | ليس خدمة analytics لموقعك الخاص |

## أفكار باستخدام جميع الخدمات العملية

| الخدمة | فكرة قابلة للنمذجة | نوع الوصول | المصدر |
|---|---|---|---|
| NASA Open APIs | عارض تعليمي للكويكبات القريبة من الأرض. | بيانات عامة فعلية | [القيود والطلب](public-shared-keys.ar.md) · [المصدر](https://api.nasa.gov/assets/html/authentication.html) |
| TheMealDB | نموذج تطبيق وصفات للتطوير والتعليم. | تطوير بخدمة فعلية أو محدودة | [القيود والطلب](public-shared-keys.ar.md) · [المصدر](https://www.themealdb.com/api.php) |
| TheCocktailDB | نموذج كتالوج مشروبات للتطوير والتعليم. | تطوير بخدمة فعلية أو محدودة | [القيود والطلب](public-shared-keys.ar.md) · [المصدر](https://www.thecocktaildb.com/api.php) |
| Alpha Vantage demo | لوحة تجريبية لبيانات IBM المسموح بها في أمثلة demo. | أمثلة أو بيانات محددة | [القيود والطلب](public-shared-keys.ar.md) · [المصدر](https://www.alphavantage.co/documentation/) |
| GovInfo | باحث في مجموعات الوثائق الحكومية العامة. | بيانات عامة فعلية | [القيود والطلب](public-shared-keys.ar.md) · [المصدر](https://api.data.gov/docs/developer-manual/) |
| OCR.space public GET examples | تجربة استخراج النص من صور المثال عبر OCR. | أمثلة أو بيانات محددة | [القيود والطلب](public-shared-keys.ar.md) · [المصدر](https://ocr.space/ocrapi) |
| TheSportsDB v1 | نموذج بطاقات فرق ولاعبين ضمن قيود البحث المجاني. | بيانات عامة فعلية | [القيود والطلب](public-shared-keys.ar.md) · [المصدر](https://api.thesportsdb.com/documentation) |
| TheAudioDB v1 | نموذج عرض بيانات موسيقى للفنانين المتاحين للمفتاح. | تطوير بخدمة فعلية أو محدودة | [القيود والطلب](public-shared-keys.ar.md) · [المصدر](https://www.theaudiodb.com/free_music_api) |
| Twelve Data demo | تجربة عرض سعر AAPL أو رموز demo المسموح بها. | أمثلة أو بيانات محددة | [القيود والطلب](public-shared-keys.ar.md) · [المصدر](https://twelvedata.com/docs) |
| EODHD demo | نموذج رسم بياني لأسعار AAPL.US المتاحة للمثال. | أمثلة أو بيانات محددة | [القيود والطلب](public-shared-keys.ar.md) · [المصدر](https://eodhd.com/financial-apis/quick-start-with-our-financial-data-apis) |
| Mapconvert | أداة تطوير تحول رابط خرائط إلى إحداثيات. | تطوير بخدمة فعلية أو محدودة | [القيود والطلب](public-shared-keys.ar.md) · [المصدر](https://mapconvert.dev/api) |
| TradeWave public demo | نموذج عرض بيانات الأنماط للمجموعة المحددة في demo. | أمثلة أو بيانات محددة | [القيود والطلب](public-shared-keys.ar.md) · [المصدر](https://developers.tradewave.ai/docs/quickstart.html) |
| SportsBookISH public data demo | نموذج عرض بيانات أسعار رياضية من الخدمة المستقلة. | أمثلة أو بيانات محددة | [القيود والطلب](public-shared-keys.ar.md) · [المصدر](https://raw.githubusercontent.com/kennyhyder/sportsbookish-docs/main/README.md) |
| National Park Service | نموذج دليل حدائق ومعلومات زيارة من البيانات العامة. | بيانات عامة فعلية | [القيود والطلب](public-shared-keys.ar.md) · [المصدر](https://www.nps.gov/subjects/developer/get-started.htm) |
| Congress.gov v3 | نموذج متابعة تشريعات عامة أو البحث في فهرس bills. | بيانات عامة فعلية | [القيود والطلب](public-shared-keys.ar.md) · [المصدر](https://raw.githubusercontent.com/LibraryOfCongress/api.congress.gov/main/README.md) |
| OpenFEC | لوحة بيانات عامة عن المرشحين وتمويل الحملات. | بيانات عامة فعلية | [القيود والطلب](public-shared-keys.ar.md) · [المصدر](https://api.open.fec.gov/developers/) |
| Federal Audit Clearinghouse | باحث في سجلات التدقيق الحكومي المتاحة للعامة. | بيانات عامة فعلية | [القيود والطلب](public-shared-keys.ar.md) · [المصدر](https://www.fac.gov/api/getting-started/) |
| Data.gov Catalog v4 | محرك بحث في metadata مجموعات البيانات الحكومية. | بيانات عامة فعلية | [القيود والطلب](public-shared-keys.ar.md) · [المصدر](https://resources.data.gov/catalog-api/) |
| api.data.gov public metrics | عرض المقاييس العامة لخدمة api.data.gov. | بيانات عامة فعلية | [القيود والطلب](public-shared-keys.ar.md) · [المصدر](https://open.gsa.gov/api/apidatagov-metrics/) |
| GSA Per Diem | عرض بدلات السفر الحكومية حسب المكان والسنة. | بيانات عامة فعلية | [القيود والطلب](public-shared-keys.ar.md) · [المصدر](https://open.gsa.gov/api/perdiem/) |
| NLR Developer APIs, formerly NREL | نموذج خريطة محطات الوقود البديل أو الشحن. | بيانات عامة فعلية | [القيود والطلب](public-shared-keys.ar.md) · [المصدر](https://developer.nlr.gov/docs/api-key/) |
| USGS Water Data OGC API | لوحة تعرض قياسات المياه اليومية المنشورة. | بيانات عامة فعلية | [القيود والطلب](public-shared-keys.ar.md) · [المصدر](https://api.waterdata.usgs.gov/docs/ogcapi/) |
| EPA ATTAINS water assessments | نموذج يعرض تصنيفات تقييم المياه المنشورة. | بيانات عامة فعلية | [القيود والطلب](public-shared-keys.ar.md) · [المصدر](https://www.epa.gov/system/files/documents/2026-04/attains_web_services_api_key_2026-04-28.pdf) |
| Smithsonian Open Access | باحث في فهرس المتاحف والمواد ذات الترخيص المناسب. | بيانات عامة فعلية | [القيود والطلب](public-shared-keys.ar.md) · [المصدر](https://edan.si.edu/openaccess/apidocs/) |
| College Scorecard | نموذج مقارنة بيانات جامعات من البيانات الحكومية. | بيانات عامة فعلية | [القيود والطلب](public-shared-keys.ar.md) · [المصدر](https://collegescorecard.ed.gov/data/api/) |
| OrbitRoute shared evaluation key | تجربة قرارات توجيه الحوسبة دون تشغيل أعمال فعلية. | تطوير بخدمة فعلية أو محدودة | [القيود والطلب](public-shared-keys.ar.md) · [المصدر](https://www.orbitroute.ai/api-reference) |
| InkTranslator FREE | تجربة ترجمة نصوص قصيرة حتى 50 حرفًا. | تطوير بخدمة فعلية أو محدودة | [القيود والطلب](public-shared-keys.ar.md) · [المصدر](https://inktranslator.com/lang/en) |
| CORX public CORS proxy | تحويل استدعاءات بيانات عامة في نموذج موقع إلى طلبات تدعم CORS. | تطوير بخدمة فعلية أو محدودة | [القيود والطلب](public-shared-keys.ar.md) · [المصدر](https://corx.envx.cn/en) |
| Attestwire invoice validation demo | تطوير مدقق لفواتير EN 16931 من JSON وتجربة رسائل الأخطاء قبل الربط الإنتاجي. | تطوير بخدمة فعلية أو محدودة | [القيود والطلب](public-shared-keys.ar.md) · [المصدر](https://attestwire.com/pricing) |
| Genji Crowd public development key | نموذج لعبة أو صفحة WebGL/Three.js تعرض حشودًا وشخصيات ثلاثية الأبعاد. | تطوير بخدمة فعلية أو محدودة | [القيود والطلب](public-shared-keys.ar.md) · [المصدر](https://www.genjicrowd.com/docs) |
| KeepTrack satellite-data demo | تطبيق تعليمي لمتابعة محطة ISS أو عرض عناصر المدارات وحساب المواقع محليًا. | بيانات عامة فعلية | [القيود والطلب](public-shared-keys.ar.md) · [المصدر](https://keeptrack.space/api) |
| TheVehicleDB public test API | نموذج كتالوج سيارات يعرض الطراز والعلامة وبلد التصنيع والسنوات. | تطوير بخدمة فعلية أو محدودة | [القيود والطلب](public-shared-keys.ar.md) · [المصدر](https://www.thevehicledb.com/free_car_api) |
| DocRaptor public PDF test key | تطوير تصميم تقارير وفواتير HTML/CSS إلى PDF وتجربة جودة التنسيق. | تطوير بخدمة فعلية أو محدودة | [القيود والطلب](public-shared-keys.ar.md) · [المصدر](https://docraptor.com/documentation) |
| OddiWire public REST preview | نموذج لوحة يعرض fixtures وأسعارًا رياضية من قراءة JSON محدودة. | أمثلة أو بيانات محددة | [القيود والطلب](public-shared-keys.ar.md) · [المصدر](https://oddiwire.com/llms-full.txt) |
| GSA Site Scanning public demo | لوحة بيانات تعرض حالة HTTPS وخصائص المواقع الحكومية من نتائج الفحص المنشورة. | بيانات عامة فعلية | [القيود والطلب](public-shared-keys.ar.md) · [المصدر](https://open.gsa.gov/api/site-scanning-api/) |
| analytics.usa.gov DAP public demo | لوحة عرض لإحصاءات لغات زوار المواقع الحكومية ومقارنة التقارير العامة. | بيانات عامة فعلية | [القيود والطلب](public-shared-keys.ar.md) · [المصدر](https://open.gsa.gov/api/dap/) |

## اختيار الخدمة لمشروعك

ابدأ بنوع البيانات والطلب المثبت، ثم راجع الحصة وقيود النشر في JSON. المفتاح الذي يعطي IBM فقط لا يغطي كل الأسهم، وPDF ذو watermark لا يحل محل مستند نهائي، وبيانات شركة sandbox لا تصبح بيانات شركتك. عدد practical يصف فائدتها للنموذج ولا يمنح ترخيص إنتاج.

كل مفتاح هنا متاح دون تسجيل، لكن الحصة قد تكون مشتركة بين المستخدمين. لا يوجد استنتاج بأن كل APIs الموجودة تقدم مفاتيح مشتركة؛ خدمات كثيرة تنشر قراءة بلا مفتاح أو تطلب إنشاء مفتاح حساب. هذان النوعان منفصلان عن هذه القائمة.

```sh
python scripts/public_keys.py --practical
python scripts/public_keys.py --practical --category vehicles
python scripts/public_keys.py --service attestwire-demo --request
```
