# APIsr — دليل APIs المجانية

**110 خدمة في 31 مجالًا، مراجعة في 2026-10-13 بتوقيت بغداد.**

دليل للحصول على APIs مجانية قانونية، مع الحصة ودورة التجديد ورابط إنشاء مفتاحك والمصدر الرسمي وقيود الاستخدام. يغطي خدمات عامة ومتخصصة. **ليس مخزنًا لمفاتيح حسابات الآخرين، ولم تُنشأ حسابات لدى هذه المزودات نيابة عنك.**

## النتائج والملفات

- [القائمة الآلية JSON](data/catalog.json) · [CSV قابل للبحث](data/catalog.csv).
- [المفاتيح التجريبية العامة الرسمية](data/public-demo-keys.json) · [طريقة الحصول على مفاتيحك](docs/access-guide.ar.md).
- [المستبعد وغير المحسوم](data/excluded-and-unconfirmed.json) · [منهجية التحقق](docs/methodology.ar.md).
- [مستودعات الاكتشاف](research/discovery-repositories.json) · [صفحات الإثبات الرسمية](research/official-sources.json) · [حدود التغطية](research/coverage.json).

تمت قراءة 11 قوائم على GitHub واستخراج 4613 رابطًا مرشحًا فريدًا، ثم مراجعة المصادر الرسمية للصفوف المقبولة. **الروابط المرشحة ليست عدد APIs مجانية مؤكدة، ولا نعد هذا مسحًا لكل الإنترنت.**

## معنى المجانية

- `recurring_quota`: الحصة تعود كل ثانية/دقيقة/ساعة/يوم/شهر؛ ليست رصيد تسجيل أو تجربة تنتهي.
- `unmetered_public`: وصول مجاني مستمر دون رصيد مدفوع/حصة billing منشورة للنطاق المحدد. بعض المزودات تصرح بعدم وجود سقف وبعضها لا تنشر حدًا رقميًا؛ **لا يُفهم هذا كضمان unlimited**. قد توجد سياسة fair use أو throttling.
- المجانية تثبت للنطاق الموضح فقط. خصائص Premium والاشتراكات والـoverages المدفوعة ليست ضمنها.
- «مسموح بشروط» ليست ترخيصًا تلقائيًا لكل المحتوى. بعض العروض للتعلم أو لغير التجاري حصراً؛ اقرأ الملاحظات قبل الإنتاج.
- `credit_card_required: null` تعني أن شرط البطاقة لم يثبت، وليست نفيًا لوجوده.
- بعض الحصص متجددة ومؤكدة لكن مقدارها يتحدد داخل لوحة الحساب؛ تُذكر كذلك بدل اختراع رقم.

## البحث محليًا

لا توجد dependencies خارج Python 3.10+:

```sh
python scripts/search.py weather
python scripts/search.py --auth no_key
python scripts/search.py --free-type recurring_quota --category geolocation
python scripts/search.py --commercial allowed --no-card
python scripts/validate.py
```

## فهرس المجالات

- [الذكاء الاصطناعي (4)](#ai)
- [الخدمات الخلفية وقواعد البيانات (9)](#backend)
- [البلوكشين (4)](#blockchain)
- [الكتب (1)](#books)
- [التقاويم والعطلات (2)](#calendar)
- [إدارة المحتوى (2)](#content)
- [المتاحف والثقافة (1)](#culture)
- [التطوير والاختبار (4)](#development)
- [البريد الإلكتروني (4)](#email)
- [الترفيه (1)](#entertainment)
- [البيئة (2)](#environment)
- [الأسواق والعملات (9)](#finance)
- [الأغذية والوصفات (3)](#food)
- [الألعاب (2)](#games)
- [الخرائط والمواقع وIP (10)](#geolocation)
- [البيانات الحكومية والإحصاءات (5)](#government)
- [الصور والرسوم (4)](#images)
- [المعرفة (1)](#knowledge)
- [اللغة (3)](#language)
- [الأفلام والتلفاز والموسيقى (4)](#media)
- [معالجة الوسائط (3)](#media_processing)
- [الرسائل والإشعارات (4)](#messaging)
- [APIs متعددة المجالات (1)](#multi_domain)
- [الأخبار (3)](#news)
- [التعرف الضوئي على النص (1)](#ocr)
- [الأبحاث العلمية (3)](#science)
- [البحث واستخراج المحتوى (4)](#search)
- [الأمن (3)](#security)
- [الرياضة (2)](#sports)
- [التحقق من البيانات (5)](#validation)
- [الطقس (6)](#weather)

<a id="ai"></a>

## الذكاء الاصطناعي

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai/platform/pricing/) · [الحصول على الوصول](https://dash.cloudflare.com/) | رمز حساب / OAuth | 10000 neurons/day on Workers Free | day; 00:00 UTC | غير محسوم من المصدر | ليست neurons عدد tokens أو طلبات؛ بعض النماذج تتطلب الدفع وتستبعد؛ تجاوز المجاني يفشل ولا يستمر دون ترقية. |
| [Google Gemini Developer API](https://ai.google.dev/gemini-api/docs/pricing) · [الحصول على الوصول](https://aistudio.google.com/apikey) | مفتاح شخصي | Free input/output for eligible models; RPM, TPM and RPD depend on model and project | minute/day | مقيّد بشروط | اختر نموذجًا يظهر Free of charge؛ حدود الطلبات يوميًا تتجدد بتوقيت المحيط الهادئ؛ المحتوى قد يستخدم لتحسين المنتجات؛ توجد قيود جغرافية وعمرية. |
| [Groq](https://console.groq.com/docs/rate-limits) · [الحصول على الوصول](https://console.groq.com/keys) | مفتاح شخصي | Model-dependent RPM, RPD, TPM and TPD; example gpt-oss-120b: 30 RPM, 1000 RPD, 8000 TPM, 200000 TPD | minute/day | غير محسوم من المصدر | الحدود على مستوى المؤسسة وتختلف بالنموذج؛ راجع لوحة Limits؛ المجاني لا يشمل كل ميزات الخطة المدفوعة. |
| [Mistral Studio Free mode](https://docs.mistral.ai/admin/billing-usage/usage-limits) · [الحصول على الوصول](https://docs.mistral.ai/getting-started/quickstarts/studio/activate-and-generate-api-key) | مفتاح شخصي | Included monthly usage; model-specific RPS and TPM shown in account Limits | month/second/minute | غير محسوم من المصدر | المصدر يثبت الحصة الشهرية لكنه لا ينشر رقمًا موحدًا؛ ابق في Free mode؛ الدفع حسب الاستخدام منفصل. |

<a id="backend"></a>

## الخدمات الخلفية وقواعد البيانات

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [Airtable](https://support.airtable.com/docs/managing-api-call-limits-in-airtable) · [الحصول على الوصول](https://airtable.com/create/tokens) | رمز حساب / OAuth | 1000 API calls/workspace/month; 5 requests/second/base | month/second | غير محسوم من المصدر | Free workspace؛ PAT مع أضيق نطاق للقاعدة؛ حد شهري مشترك بين المستخدمين؛ عدد السجلات والملفات محدود. |
| [Cloudflare D1](https://developers.cloudflare.com/d1/platform/pricing/) · [الحصول على الوصول](https://dash.cloudflare.com/) | رمز حساب / OAuth | 5 million rows read/day; 100000 rows written/day; 5 GB total storage | day; 00:00 UTC | غير محسوم من المصدر | Rows لا queries؛ الفهارس قد تزيد write counts؛ التزم Free لتجنب billing؛ التخزين سعة ثابتة. |
| [Cloudflare Workers Free](https://developers.cloudflare.com/workers/platform/pricing/) · [الحصول على الوصول](https://dash.cloudflare.com/) | رمز حساب / OAuth | 100000 dynamic requests/day; 10 ms CPU/invocation | day | غير محسوم من المصدر | خطة Workers Free منفصلة عن Paid؛ static assets مجانية دون حصة requests لكن limits الأخرى تبقى؛ التزم وقت CPU. |
| [Cloudflare Workers KV](https://developers.cloudflare.com/kv/platform/pricing/) · [الحصول على الوصول](https://dash.cloudflare.com/) | رمز حساب / OAuth | 100000 reads/day; 1000 writes, deletes and lists/day each | day; 00:00 UTC | غير محسوم من المصدر | Workers Free فقط؛ 1 GB تخزين ثابت؛ تجاوز نوع العملية يوقفه حتى التجديد؛ بعض batch operations تحسب لكل key. |
| [Convex Free](https://www.convex.dev/pricing) · [الحصول على الوصول](https://dashboard.convex.dev/) | رمز حساب / OAuth | 1 million function calls/month; 20 GB-hours action compute included | month | غير محسوم من المصدر | اختر Free لا Starter ذات الدفع حسب الاستخدام؛ حدود تخزين وbandwidth ووظائف متزامنة؛ compute وحدات مختلفة عن calls. |
| [Firebase Cloud Firestore](https://firebase.google.com/docs/firestore/quotas) · [الحصول على الوصول](https://console.firebase.google.com/) | رمز حساب / OAuth | 50000 document reads/day; 20000 writes/day; 20000 deletes/day; 10 GiB transfer/month | day; midnight Pacific / month | غير محسوم من المصدر | Spark بلا billing؛ قاعدة مجانية واحدة لكل project؛ 1 GiB تخزين ثابت؛ TTL/PITR/backups وغيرها قد تتطلب billing وتستبعد. |
| [Firebase Realtime Database](https://firebase.google.com/docs/database/usage/billing) · [الحصول على الوصول](https://console.firebase.google.com/) | رمز حساب / OAuth | 10 GB downloads/month; 1 GB storage | month | غير محسوم من المصدر | Spark دون فاتورة؛ 100 اتصال متزامن وفق جدول الخطة؛ احم البيانات بـRules؛ ترقية Blaze تضيف دفعًا عند التجاوز. |
| [Firebase Remote Config](https://firebase.google.com/pricing) · [الحصول على الوصول](https://console.firebase.google.com/) | رمز حساب / OAuth | 100000 fetch requests/day/project on Spark | day | غير محسوم من المصدر | حسب تسعير بدأ 1 سبتمبر 2026؛ quota للـfetch لا تعني معدل admin REST؛ لا تعتمد وصف unlimited القديم؛ Spark فقط. |
| [Supabase](https://supabase.com/pricing) · [الحصول على الوصول](https://supabase.com/dashboard) | مفتاح شخصي | Unlimited API requests; 50000 monthly active users; 5 GB egress/month | month for egress and MAU; API requests unmetered | غير محسوم من المصدر | 2 مشاريع؛ 500 MB database و1 GB file storage ثابتان؛ pause بعد أسبوع خمول؛ publishable/anon key لا يعطي صلاحية admin ويجب ضبط RLS. |

<a id="blockchain"></a>

## البلوكشين

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [Alchemy](https://www.alchemy.com/pricing) · [الحصول على الوصول](https://dashboard.alchemy.com/) | مفتاح شخصي | 30 million compute units/month; 15 requests/second | month/second | غير محسوم من المصدر | الحصة compute units وليست عدد طلبات ثابتًا؛ 5 apps و5 webhooks؛ عمليات الشبكة والمعاملات قد لها gas مستقل غير مجاني. |
| [Etherscan](https://docs.etherscan.io/resources/rate-limits) · [الحصول على الوصول](https://etherscan.io/register) | مفتاح شخصي | 3 calls/second; 100000 calls/day | second/day | غير محسوم من المصدر | selected chains only؛ PRO endpoints غير مجانية؛ V2 والمفتاح موحد للشبكات المدعومة. |
| [Helius](https://www.helius.dev/pricing) · [الحصول على الوصول](https://dashboard.helius.dev/) | مفتاح شخصي | 1 million credits/month; 10 requests/second; 1 sendTransaction/second | month/second | غير محسوم من المصدر | Solana؛ credits تختلف حسب endpoint؛ لا تفعّل autoscaling مدفوع؛ fees للمعاملات منفصلة. |
| [Infura](https://www.infura.io/pricing) · [الحصول على الوصول](https://app.infura.io/register) | مفتاح شخصي | 3 million credits/day; 500 credits/second on Core | day/second | غير محسوم من المصدر | Core مجانية؛ مفتاح واحد؛ الأرصدة حسب طريقة RPC؛ رسوم blockchain ليست مشمولة بالمجانية. |

<a id="books"></a>

## الكتب

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [Open Library](https://openlibrary.org/developers/api) · [الحصول على الوصول](https://openlibrary.org/developers/api) | بلا مفتاح | 1 request/second default; 3/second with identified User-Agent and contact email | second | مقيّد بشروط | للبحث والقراءة البشرية بكمية منخفضة؛ ليست بنية خلفية bulk أو high-traffic تجارية؛ cache وdumps للأعمال الكبيرة. |

<a id="calendar"></a>

## التقاويم والعطلات

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [Calendarific](https://calendarific.com/) · [الحصول على الوصول](https://calendarific.com/signup) | مفتاح شخصي | 500 calls/month | month | مقيّد بشروط | attribution مطلوب؛ لغة واحدة وتاريخ/مستقبل محدودان؛ الجدول الحالي 500 وليس 1000 كما في قوائم أقدم. |
| [Nager.Holiday public holiday API](https://date.nager.at/API) · [الحصول على الوصول](https://date.nager.at/API) | بلا مفتاح | Official page states no rate limits and unlimited queries; no key | no stated rate limit | غير محسوم من المصدر | الموقع الرسمي انتقل إلى API v4 على nagerholidays.com؛ لا تعتمد endpoint v3 من القوائم القديمة؛ تحققت من استجابة مثال عطلات AT/2026. |

<a id="content"></a>

## إدارة المحتوى

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [Contentstack](https://www.contentstack.com/pricing/) · [الحصول على الوصول](https://www.contentstack.com/) | مفتاح شخصي | 100000 API calls/month; 100 GB bandwidth/month | month | غير محسوم من المصدر | Free forever؛ production stack واحد و3 مستخدمين و10 أنواع محتوى؛ عدد entries/assets ثابت؛ ليس كل Agent OS مجانيًا بلا سقف. |
| [Sanity](https://www.sanity.io/pricing) · [الحصول على الوصول](https://www.sanity.io/get-started) | شخصي أو بلا مفتاح | 1 million CDN API requests/month; 250000 API requests/month; 100 GB bandwidth/month | month | غير محسوم من المصدر | Free forever؛ datasets عامة فقط؛ حصة CDN مستقلة عن API المباشر؛ لا تنشر write token. |

<a id="culture"></a>

## المتاحف والثقافة

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [Art Institute of Chicago](https://api.artic.edu/docs/) · [الحصول على الوصول](https://api.artic.edu/docs/) | بلا مفتاح | 60 requests/minute/IP; scraping at most 1 request/second | minute/second | مقيّد بشروط | بيانات عامة دون auth؛ public-domain artworks فقط للاستعمال الحر للصور؛ استخدم dumps للتحميل الكبير وHTTPS. |

<a id="development"></a>

## التطوير والاختبار

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [DummyJSON](https://dummyjson.com/) · [الحصول على الوصول](https://dummyjson.com/docs) | بلا مفتاح | Free fake REST API; no paid usage credit for public sample endpoints | ongoing; fair use | غير محسوم من المصدر | بيانات وهمية؛ auth endpoints للتجريب لا تعني حسابات مستخدمين حقيقية؛ لا تعد خدمة إنتاج خلفية دائمة. |
| [GitHub REST API](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api) · [الحصول على الوصول](https://github.com/settings/tokens) | شخصي أو بلا مفتاح | 60 requests/hour unauthenticated; 5000/hour authenticated | rolling hour | غير محسوم من المصدر | GitHub Free يدعم API؛ search وGraphQL لهما حدود أخرى؛ secondary limits مشتركة؛ لا تشمل الحصة تكاليف Actions أوCopilot؛ لا تنشر PAT. |
| [GitLab.com REST API](https://docs.gitlab.com/user/gitlab_com/rate_limits/) · [الحصول على الوصول](https://gitlab.com/-/user_settings/personal_access_tokens) | شخصي أو بلا مفتاح | Authenticated API up to 2000/minute; anonymous and endpoint-specific limits also apply | minute | غير محسوم من المصدر | خطة Free صفر دولار؛ الصفحة تفصل حدودًا مقترحة غير مفعلة عن الحدود الحالية؛ 100/minute للـFree ضمن proposal لا يعتمد كواقع نافذ؛ تحقق من headers. |
| [JSONPlaceholder](https://jsonplaceholder.typicode.com/) · [الحصول على الوصول](https://jsonplaceholder.typicode.com/guide/) | بلا مفتاح | Free for everyone; no signup or API key; no published recurring billing quota | ongoing; fair use | غير محسوم من المصدر | بيانات وهمية للتجريب؛ POST/PUT لا تحفظ تغييرات فعلية؛ عدم نشر quota لا يعني SLA أو عدم throttling. |

<a id="email"></a>

## البريد الإلكتروني

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [Brevo](https://www.brevo.com/pricing/) · [الحصول على الوصول](https://www.brevo.com/) | مفتاح شخصي | 300 emails/day on Free | day | مقيّد بشروط | خطة Free forever بعد اعتماد الحساب للإرسال؛ البريد فقط، SMS وWhatsApp ليست مجانية؛ التزم الموافقة وسياسات الإرسال. |
| [MailerSend](https://www.mailersend.com/pricing) · [الحصول على الوصول](https://www.mailersend.com/) | مفتاح شخصي | 500 emails/month; 100 daily API requests in Free | month/day | مقيّد بشروط | اختر Free، وليس تجربة Professional 14 يومًا ولا Hobby المدفوعة؛ نطاق واحد وقيود تحقق الحساب. |
| [Mailjet](https://www.mailjet.com/pricing/) · [الحصول على الوصول](https://app.mailjet.com/signup) | مفتاح شخصي | 6000 emails/month; 200/day | month/day | مقيّد بشروط | خطة Free؛ سقف contacts وخصائص الإحصاء؛ التحقق من المرسل وسياسات البريد مطلوبة. |
| [Resend](https://resend.com/pricing) · [الحصول على الوصول](https://resend.com/signup) | مفتاح شخصي | 3000 emails/month; 100 emails/day | month/day | مقيّد بشروط | المجانية تخص البريد ضمن الحصة؛ يحتاج الإرسال نطاقًا موثقًا وسياسات مكافحة الرسائل المزعجة؛ عدد domains محدود. |

<a id="entertainment"></a>

## الترفيه

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [icanhazdadjoke](https://icanhazdadjoke.com/api) · [الحصول على الوصول](https://icanhazdadjoke.com/api) | بلا مفتاح | Public API requires no authentication and no usage credit | ongoing; fair use | غير محسوم من المصدر | أرسل Accept: application/json وUser-Agent؛ أضف نسبة المصدر عند إعادة عرض المحتوى؛ لا ضمان استضافة. |

<a id="environment"></a>

## البيئة

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [NOAA Climate Data Online](https://www.ncei.noaa.gov/cdo-web/webservices/v2) · [الحصول على الوصول](https://www.ncei.noaa.gov/cdo-web/token) | مفتاح شخصي | 5 requests/second; 10000 requests/day | second/day | غير محسوم من المصدر | مفتاح خاص بطلب مجاني عبر البريد؛ ليس هو مفتاح NASA؛ البيانات الأمريكية والمناخية فقط. |
| [WAQI / AQICN](https://aqicn.org/api/) · [الحصول على الوصول](https://aqicn.org/data-platform/token/) | مفتاح شخصي | Default quota 1000 requests/second | second | مقيّد بشروط | يلزم نسبة المصدر؛ لا إعادة توزيع كبيانات مخزنة ولا إعادة بيع؛ راجع acceptable usage قبل الاستخدام التجاري. |

<a id="finance"></a>

## الأسواق والعملات

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [Alpha Vantage](https://www.alphavantage.co/support/) · [الحصول على الوصول](https://www.alphavantage.co/support/#api-key) | مفتاح شخصي | 25 API requests/day; higher free access requires verified educational/open-source eligibility | day | مقيّد بشروط | الحصة الأساسية 25 فقط؛ البيانات اللحظية الأمريكية وميزات Premium ليست مجانية؛ لا تفترض قبول الإعفاء التعليمي. |
| [CoinGecko Demo](https://www.coingecko.com/en/api/pricing) · [الحصول على الوصول](https://www.coingecko.com/en/developers/dashboard) | مفتاح شخصي | 10000 call credits/month; 100 calls/minute | month/minute | مقيّد بشروط | خطة Demo صفر دولار متجددة؛ attribution مطلوب؛ البيانات والأسواق ونطاق السجل أقل من الخطط المدفوعة. |
| [coinlayer](https://coinlayer.com/product) · [الحصول على الوصول](https://coinlayer.com/signup/free) | مفتاح شخصي | 100 requests/month | month | غير تجاري فقط | لا انتهاء؛ USD target currency؛ الخطة المجانية وبياناتها أضيق من المدفوع. |
| [currencylayer](https://currencylayer.com/product) · [الحصول على الوصول](https://currencylayer.com/signup/free) | مفتاح شخصي | 100 API calls/month | month | غير تجاري فقط | Free بلا مدة انتهاء؛ لا currency switching والتحويل الموسع؛ صفحة الأسعار أولى من أرقام القوائم القديمة. |
| [ExchangeRate-API](https://www.exchangerate-api.com/docs/free) · [الحصول على الوصول](https://www.exchangerate-api.com/) | شخصي أو بلا مفتاح | Registered Free: 1500 requests/month; Open Access: rate-limited, daily data refresh | month; open endpoint rate window unpublished | مقيّد بشروط | المسار المفتوح يتطلب attribution ويمنع إعادة توزيع البيانات؛ المسار ذو المفتاح مختلف؛ لا تختَر تجربة Pro. |
| [ExchangeRatesAPI.io](https://exchangeratesapi.io/pricing/) · [الحصول على الوصول](https://exchangeratesapi.io/signup/free) | مفتاح شخصي | 100 requests/month | month | غير تجاري فقط | تحديث يومي وخطة محدودة؛ تبديل العملة الأساسية والتحويل وHTTPS قد يكونان مدفوعين بحسب endpoint والخطة. |
| [Fixer on APILayer](https://apilayer.com/marketplace/fixer-api) · [الحصول على الوصول](https://apilayer.com/marketplace/fixer-api) | مفتاح شخصي | 100 requests/month | month | مقيّد بشروط | Free for Lifetime؛ لا تخلط API السوق مع خطة fixer.io أخرى؛ العملات الأساسية والتحويل قد تختلف حسب الخطة. |
| [Frankfurter](https://frankfurter.dev/) · [الحصول على الوصول](https://frankfurter.dev/) | بلا مفتاح | No daily or monthly quota; abuse rate limits apply | no monthly/daily cap | مسموح بشروط البيانات | أسعار مرجعية وليست live trading؛ ترخيص المصادر المركزية يظل نافذًا؛ self-host للتدفق الكثيف. |
| [Twelve Data](https://twelvedata.com/pricing) · [الحصول على الوصول](https://twelvedata.com/register) | مفتاح شخصي | 8 API credits/minute; 800/day on Basic | minute/day | مقيّد بشروط | Basic فقط؛ كل رمز في الطلب قد يستهلك credit؛ اعرض بيانات الأسواق وفق ترخيصها؛ websocket trial غير محسوب. |

<a id="food"></a>

## الأغذية والوصفات

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [Open Food Facts](https://world.openfoodfacts.org/data) · [الحصول على الوصول](https://openfoodfacts.github.io/openfoodfacts-server/api/) | بلا مفتاح | Database and API 100% free of charge and open to all; endpoint rate limits apply | ongoing; endpoint-specific rate windows | مسموح بشروط البيانات | ODbL attribution وshare-alike؛ التوصيف الغذائي بيانات لا نصيحة طبية؛ bulk عبر dumps لا scraping كثيف. |
| [TheCocktailDB development API](https://www.thecocktaildb.com/api.php) · [الحصول على الوصول](https://www.thecocktaildb.com/api.php) | مفتاح اختبار عام رسمي | Official public test key 1 for development/education; no paid trial credits | ongoing; fair use | تطوير/تعليم/تقييم فقط | مفتاح 1 رسمي؛ production/app store يتطلب Premium؛ random selection/popular/recent الموسعة مدفوعة. |
| [TheMealDB development API](https://www.themealdb.com/api.php) · [الحصول على الوصول](https://www.themealdb.com/api.php) | مفتاح اختبار عام رسمي | Official public test key 1 for development/education; no paid trial credits | ongoing; fair use | تطوير/تعليم/تقييم فقط | مفتاح 1 رسمي؛ النشر العام على app store يتطلب supporter؛ multi-ingredient/full database مزايا مدفوعة؛ الاستخدام المجاني هنا تعليمي فقط. |

<a id="games"></a>

## الألعاب

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [Open Trivia DB](https://opentdb.com/api_config.php) · [الحصول على الوصول](https://opentdb.com/api_config.php) | بلا مفتاح | 1 API request/5 seconds/IP; up to 50 questions/request | 5 seconds | مقيّد بشروط | المجاني كامل؛ CC BY-SA 4.0؛ session token لمنع تكرار الأسئلة لا يمثل مفتاح دفع. |
| [PokeAPI](https://pokeapi.co/docs/v2) · [الحصول على الوصول](https://pokeapi.co/docs/v2) | بلا مفتاح | Rate limiting removed since move to static hosting; all resources open | no request quota documented | مقيّد بشروط | GET فقط؛ التخزين المؤقت وfair use مطلوبان؛ علامة Pokémon والمحتوى ليست ترخيصًا تجاريًا عامًا. |

<a id="geolocation"></a>

## الخرائط والمواقع وIP

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [Abstract IP Geolocation](https://www.abstractapi.com/pricing) · [الحصول على الوصول](https://www.abstractapi.com/api/ip-geolocation-api) | مفتاح شخصي | 1000 requests/month | month | غير محسوم من المصدر | حصة مستقلة لمنتج IP؛ الصفحة تؤكد monthly free tier؛ الميزات المتقدمة تختلف بالخطة. |
| [Geoapify](https://www.geoapify.com/pricing/) · [الحصول على الوصول](https://myprojects.geoapify.com/) | مفتاح شخصي | 3000 credits/day; up to 5 requests/second | day/second | مسموح بشروط البيانات | يلزم attribution لـGeoapify ومصادر البيانات؛ بعض endpoints تستهلك عدة credits؛ المجاني يصلح للإنتاج ضمن حدوده. |
| [GeoNames](https://www.geonames.org/export/) · [الحصول على الوصول](https://www.geonames.org/login) | اسم مستخدم مجاني | 10000 credits/day; 1000 credits/hour | day/hour | مسموح بشروط البيانات | أنشئ اسم مستخدمك وفعّل web services؛ لا تستخدم demo username؛ attribution مطلوب؛ معظم الطلبات تستهلك credit واحدًا. |
| [ip-api](https://ip-api.com/docs/api:json) · [الحصول على الوصول](https://ip-api.com/docs/legal) | بلا مفتاح | 45 HTTP requests/minute/IP | minute | غير تجاري فقط | المجاني HTTP فقط؛ لا تستخدمه لبيانات حساسة؛ ترخيص تجاري وHTTPS مدفوعان؛ راجع أمثلة الاستخدام المسموح. |
| [ipdata](https://ipdata.co/pricing.html) · [الحصول على الوصول](https://dashboard.ipdata.co/sign-up.html) | مفتاح شخصي | 1500 requests/day | day | غير تجاري فقط | عند نفاد الحصة المجانية تُحجب الطلبات؛ لا تستخدم بيانات الخطة المجانية تجاريًا. |
| [IPGeolocation.io](https://ipgeolocation.io/pricing.html) · [الحصول على الوصول](https://ipgeolocation.io/signup.html) | مفتاح شخصي | 1000 API credits/day for life | day | مقيّد بشروط | للتجريب والمشاريع الصغيرة؛ لا overages بالمجاني؛ APIs المتخصصة قد تختلف في طريقة احتساب credits. |
| [IPinfo Lite](https://ipinfo.io/pricing) · [الحصول على الوصول](https://ipinfo.io/signup) | مفتاح شخصي | Unlimited country-level IP and ASN lookups on Lite | no monthly request cap | مقيّد بشروط | Lite يختلف عن بيانات المدينة وVPN المدفوعة؛ يتطلب مفتاح الحساب وترخيص/attribution الخطة؛ ليس كل endpoint مجانيًا. |
| [ipwho.is](https://ipwhois.io/documentation) · [الحصول على الوصول](https://ipwhois.io/documentation) | بلا مفتاح | 1000 requests/day/IP; browser CORS traffic counted per domain | day; access restored after 24h | مسموح بشروط البيانات | المسار Free فقط؛ لا bulk ولا security أو currency data؛ لا SLA؛ لا تفترض أن تبديل مفتاح يجدد حصة IP. |
| [LocationIQ](https://locationiq.com/pricing) · [الحصول على الوصول](https://my.locationiq.com/register) | مفتاح شخصي | 5000 requests/day; 60 requests/minute; 2 requests/second | day/minute/second | مقيّد بشروط | الاستخدام التجاري المجاني يتطلب رابطًا واضحًا للمزود؛ رمز وصول واحد؛ حدود الخرائط والتوجيه تختلف حسب المنتج. |
| [positionstack](https://positionstack.com/product) · [الحصول على الوصول](https://positionstack.com/signup/free) | مفتاح شخصي | 100 requests/month | month | غير تجاري فقط | للاستخدام الشخصي؛ التوجيه الأمامي والعكسي فقط؛ خصائص batch وGeoJSON الموسعة مدفوعة. |

<a id="government"></a>

## البيانات الحكومية والإحصاءات

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [BLS Public Data API](https://www.bls.gov/developers/api_faqs.htm) · [الحصول على الوصول](https://data.bls.gov/registrationEngine/) | شخصي أو بلا مفتاح | Registered v2: 500 queries/day; unregistered v1: 25/day; 50 requests/10 seconds | day/10 seconds | مقيّد بشروط | تجديد تسجيل المفتاح سنويًا؛ 50 سلسلة و20 سنة/طلب للمسجل مقابل 25 سلسلة و10 سنوات لغير المسجل؛ إحصاءات عامة لا real-time markets. |
| [NASA Open APIs](https://api.nasa.gov/assets/html/authentication.html) · [الحصول على الوصول](https://api.nasa.gov/) | شخصي أو demo رسمي | Registered key: 1000 requests/hour; DEMO_KEY: 30/hour and 50/day/IP | hour rolling/day | مقيّد بشروط | الحصة مشتركة عبر خدمات api.nasa.gov؛ بعض APIs تختلف؛ صور الأطراف الثالثة قد تحمل حقوقًا منفصلة. |
| [National Park Service](https://www.nps.gov/subjects/developer/guides.htm) · [الحصول على الوصول](https://www.nps.gov/subjects/developer/get-started.htm) | مفتاح شخصي | 1000 requests/hour by default | hour rolling | مقيّد بشروط | مفتاح شخصي مجاني؛ يرسل في X-Api-Key؛ احترام Disclaimer وحقوق المحتوى والصور. |
| [US EIA Open Data](https://www.eia.gov/opendata/documentation.php) · [الحصول على الوصول](https://www.eia.gov/opendata/register.php) | مفتاح شخصي | Data and keys free; per-second/hour traffic tolerances apply | ongoing; temporary throttle | مقيّد بشروط | يلزم مفتاح عبر البريد؛ الحظر الزائد مؤقت؛ راجع شروط الخدمة وCopyrights and Reuse؛ لم أنسب حدًا رقميًا غير موثق. |
| [World Bank Indicators API](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation) · [الحصول على الوصول](https://data.worldbank.org/summary-terms-of-use) | بلا مفتاح | Open public indicators with no key or paid request credit | ongoing; no numerical quota stated | مقيّد بشروط | V2؛ ترخيص CC BY 4.0 مع بعض بيانات أطراف ثالثة قد تختلف؛ لا افتراض SLA أو أن عدم نشر quota يلغي throttling. |

<a id="images"></a>

## الصور والرسوم

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [DiceBear hosted Avatar API](https://www.dicebear.com/how-to-use/http-api/) · [الحصول على الوصول](https://www.dicebear.com/how-to-use/http-api/) | بلا مفتاح | 50 requests/second for SVG; 10/second for raster/JSON | second | غير تجاري فقط | المسار المستضاف لغير التجاري؛ تراخيص styles مختلفة؛ raster حتى 256×256؛ self-host له متطلبات وترخيص منفصلان. |
| [Pixabay](https://pixabay.com/api/docs/) · [الحصول على الوصول](https://pixabay.com/accounts/register/) | مفتاح شخصي | 100 requests/60 seconds by default | 60 seconds | مقيّد بشروط | تخزين نتائج API مؤقتًا 24 ساعة مطلوب؛ لا تحميل جماعي ولا hotlinking دائم؛ التزم Content License ونسبة المصدر. |
| [TheCatAPI](https://thecatapi.com/) · [الحصول على الوصول](https://thecatapi.com/) | مفتاح شخصي | 10000 requests/month | month | غير تجاري فقط | خطة التعلم المجانية؛ ترخيص بيانات الاستخدام التجاري في Startup؛ لا تفترض شمول جميع حقول السلالات والمزايا. |
| [Unsplash](https://unsplash.com/documentation) · [الحصول على الوصول](https://unsplash.com/developers) | مفتاح شخصي | 50 requests/hour in demo mode; production requires approval | hour | مقيّد بشروط | احترام attribution وhotlinking وإبلاغ تنزيل الصور؛ لا تفترض الموافقة على حصة الإنتاج؛ حقوق الصور منفصلة. |

<a id="knowledge"></a>

## المعرفة

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [Wikimedia public read APIs](https://api.wikimedia.org/wiki/Rate_limits) · [الحصول على الوصول](https://www.mediawiki.org/wiki/API:Etiquette) | بلا مفتاح | Free open knowledge; public REST/Action APIs with access-policy rate limits | ongoing; rate windows depend on identity | مقيّد بشروط | User-Agent ونسبة المصدر وترخيص CC BY-SA؛ Enterprise API المدفوعة ليست هذه الخدمة؛ limites تختلف حسب الهوية والحمل. |

<a id="language"></a>

## اللغة

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [Datamuse](https://www.datamuse.com/api/) · [الحصول على الوصول](https://www.datamuse.com/api/) | بلا مفتاح | 100000 requests/day | day | مقيّد بشروط | لا مفتاح حتى 1 فبراير 2027؛ ابتداءً منه يلزم مفتاح والحصة نفسها يومية؛ نسبة المصدر والتواصل للتطبيقات الواسعة مطلوبان. |
| [Free Dictionary API](https://dictionaryapi.dev/) · [الحصول على الوصول](https://dictionaryapi.dev/) | بلا مفتاح | Always free public word definitions; no billing quota documented | ongoing; fair use | مقيّد بشروط | القاموس الإنجليزي؛ تراخيص المصادر والصوت في الرد؛ عدم نشر حد ليس ضمانًا لطلبات غير محدودة. |
| [LanguageTool Public HTTP API](https://dev.languagetool.org/public-http-api.html) · [الحصول على الوصول](https://dev.languagetool.org/public-http-api.html) | بلا مفتاح | 20 requests/minute/IP; 75 KB text/minute/IP; 20 KB/request | minute | مقيّد بشروط | مسموح للطلبات الفردية فقط؛ automated requests ممنوعة حسب الصفحة؛ لا ضمان خدمة ولا كل ميزات Premium. |

<a id="media"></a>

## الأفلام والتلفاز والموسيقى

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [MusicBrainz read API](https://musicbrainz.org/doc/MusicBrainz_API) · [الحصول على الوصول](https://musicbrainz.org/doc/MusicBrainz_API) | بلا مفتاح | 1 request/second/application | second | غير تجاري فقط | قراءة البيانات عامة؛ write/user requests تتطلب auth؛ User-Agent واضح؛ خطط تجارية منفصلة. |
| [OMDb](https://www.omdbapi.com/apikey.aspx) · [الحصول على الوصول](https://www.omdbapi.com/apikey.aspx) | مفتاح شخصي | 1000 requests/day on FREE account | day | غير تجاري فقط | بيانات CC BY-NC 4.0؛ Poster API للمشتركين؛ اختر FREE بدل Patreon. |
| [TMDB](https://developer.themoviedb.org/docs/faq) · [الحصول على الوصول](https://www.themoviedb.org/settings/api) | مفتاح شخصي | Free API for non-commercial use; rate limiting applies | ongoing; no paid usage credit in non-commercial API | غير تجاري فقط | attribution مطلوب؛ الترخيص التجاري يحتاج تواصلًا وموافقة منفصلة؛ لا تنشر مفتاح حسابك. |
| [TVmaze Public API](https://www.tvmaze.com/api) · [الحصول على الوصول](https://www.tvmaze.com/api) | بلا مفتاح | At least 20 calls/10 seconds/IP | 10 seconds | مقيّد بشروط | CC BY-SA وترخيص الصور منفصل؛ بيانات cache قد تتأخر ساعة؛ user-level API Premium خارج النطاق. |

<a id="media_processing"></a>

## معالجة الوسائط

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [Filestack](https://www.filestack.com/pricing/) · [الحصول على الوصول](https://dev.filestack.com/signup/) | مفتاح شخصي | 500 uploads; 1000 transformations; 1 GB bandwidth in free monthly plan | month | غير محسوم من المصدر | Free forever؛ 1 GB storage ثابت؛ OCR وعمليات premium ليست ضمن المجاني؛ راجع دورة الحساب في لوحة الاشتراك. |
| [ImageKit](https://imagekit.io/plans/) · [الحصول على الوصول](https://imagekit.io/registration/) | مفتاح شخصي | 20 GB bandwidth/month; 500 video units/month; 650 extension units/month | month | غير محسوم من المصدر | Forever free؛ 3 GB تخزين ثابت لا يتجدد كرصيد جديد؛ ميزات AI لها حصص منفصلة؛ الخطة Lite المدفوعة مختلفة. |
| [screenshotlayer](https://screenshotlayer.com/product) · [الحصول على الوصول](https://screenshotlayer.com/signup/free) | مفتاح شخصي | 100 snapshots/month; no time limit | month | غير تجاري فقط | الحصة snapshots شهرية؛ الخصائص وتدفق HTTPS تختلف بالخطة؛ لا يشمل المجاني احتياجات معالجة مدفوعة. |

<a id="messaging"></a>

## الرسائل والإشعارات

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [Ably](https://ably.com/pricing) · [الحصول على الوصول](https://ably.com/sign-up) | مفتاح شخصي | 6 million messages/month; 200 concurrent connections; 500 messages/second | month/second | تطوير/تعليم/تقييم فقط | خطة Free لبناء proof of concept؛ الرسائل ومجموع الدقائق قنوات/اتصالات قد يحتسبان بصورة مختلفة في الخطط المدفوعة. |
| [Cloudflare Queues](https://developers.cloudflare.com/queues/platform/pricing/) · [الحصول على الوصول](https://dash.cloudflare.com/) | رمز حساب / OAuth | 10000 operations/day; 24-hour message retention | day | غير محسوم من المصدر | Workers Free؛ رسالة read/write/delete تستهلك غالبًا 3 operations؛ حجم أكثر من 64 KB يزيد الاحتساب؛ مليون operation شهريًا للخطة المدفوعة لا للمجاني. |
| [Firebase Cloud Messaging](https://firebase.google.com/pricing) · [الحصول على الوصول](https://console.firebase.google.com/) | رمز حساب / OAuth | FCM messaging service is no-cost; request and delivery quotas still apply | ongoing; service-specific quota windows | مقيّد بشروط | الإشعارات push لا SMS؛ تكاليف خادمك أوFunctions منفصلة؛ service account/OAuth لا ينشر؛ limits للإرسال والأجهزة باقية. |
| [Pusher Channels](https://pusher.com/channels/pricing/) · [الحصول على الوصول](https://dashboard.pusher.com/accounts/sign_up) | مفتاح شخصي | 200000 messages/day; 100 concurrent connections | day | تطوير/تعليم/تقييم فقط | Sandbox المجانية؛ سر التطبيق يستخدم على السيرفر فقط؛ broadcasting قد يستهلك رسائل لكل مستلم. |

<a id="multi_domain"></a>

## APIs متعددة المجالات

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [API Ninjas](https://api-ninjas.com/pricing) · [الحصول على الوصول](https://api-ninjas.com/register) | مفتاح شخصي | 3000 API calls/month; 100 calls/hour | month/hour | تطوير/تعليم/تقييم فقط | للتقييم والعروض فقط؛ يلزم attribution؛ تخزين البيانات واستخدامها التجاري غير مسموحين بالمجاني؛ الميزات Premium مستثناة. |

<a id="news"></a>

## الأخبار

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [Currents](https://www.currentsapi.services/en/pricing) · [الحصول على الوصول](https://www.currentsapi.services/en/register) | مفتاح شخصي | 250 requests/day | day | مقيّد بشروط | خطة Free developer؛ نطاق التاريخ والنتائج محدود؛ إعادة نشر محتوى المصادر تحتاج حقوقًا منفصلة. |
| [GNews](https://gnews.io/pricing) · [الحصول على الوصول](https://gnews.io/register) | مفتاح شخصي | 100 requests/day; up to 10 articles/request | day | غير تجاري فقط | للتطوير والاختبار والمشاريع غير التجارية؛ تأخير 12 ساعة؛ CORS على localhost؛ النص الكامل مدفوع. |
| [mediastack](https://mediastack.com/product) · [الحصول على الوصول](https://mediastack.com/signup/free) | مفتاح شخصي | 100 calls/month | month | غير تجاري فقط | أخبار مؤخرة؛ لا historical data بالمجاني؛ حقوق المحتوى لا تنتقل بمجرد استعمال API. |

<a id="ocr"></a>

## التعرف الضوئي على النص

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [OCR.space](https://ocr.space/ocrapi) · [الحصول على الوصول](https://ocr.space/ocrapi) | مفتاح شخصي | 25000 requests/month and 500 requests/day/IP | month/day | غير محسوم من المصدر | المجاني محدود بحجم ملف 1 MB وثلاث صفحات PDF؛ حد IP مشترك؛ لا ضمان أداء الخطة المدفوعة. |

<a id="science"></a>

## الأبحاث العلمية

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [arXiv legacy API](https://info.arxiv.org/help/api/tou.html) · [الحصول على الوصول](https://info.arxiv.org/help/api/user-manual.html) | بلا مفتاح | 1 request/3 seconds; one connection at a time | 3 seconds | مقيّد بشروط | metadata تحت CC0؛ المقالات لها تراخيص مستقلة؛ لا parallel requests ولا تجاوز rate limits. |
| [Crossref REST API](https://www.crossref.org/documentation/retrieve-metadata/rest-api/) · [الحصول على الوصول](https://api.crossref.org/swagger-ui/index.html) | بلا مفتاح | Free metadata APIs; endpoint and pool rate limits apply | ongoing; response headers expose limits | مقيّد بشروط | استخدم mailto مع User-Agent للاستفادة من polite pool؛ تراخيص abstracts/full text قد تختلف عن metadata. |
| [OpenAlex](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication) · [الحصول على الوصول](https://openalex.org/settings/api) | شخصي أو بلا مفتاح | Free daily budget; key gives 10x keyless budget; 10 RPS without key, 30 RPS with free key | day/second | مقيّد بشروط | ميزانية يومية تختلف بتكلفة query؛ الرقم النقدي الحالي لم يثبت من الصفحة لذا لم يُخمن؛ الدفع للتوسع اختياري. |

<a id="search"></a>

## البحث واستخراج المحتوى

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [Algolia Build](https://www.algolia.com/pricing) · [الحصول على الوصول](https://dashboard.algolia.com/users/sign_up) | مفتاح شخصي | 10000 search requests/month; 5000 recommendation requests/month; 50000 records | month | تطوير/تعليم/تقييم فقط | اختر Build المجانية؛ Grow قد يحتسب overages؛ لا تنشر admin key؛ عدد records ثابت وليس رصيدًا يتراكم كل شهر. |
| [Jina Reader without API key](https://jina.ai/reader/) · [الحصول على الوصول](https://jina.ai/reader/) | بلا مفتاح | 20 requests/minute for keyless Reader | minute | غير محسوم من المصدر | المسار المجاني هو Reader بلا مفتاح فقط؛ رصيد المفتاح الجديد 10M tokens لمرة واحدة ليس ضمن القائمة؛ خدمة البحث s.jina.ai ليست مشمولة. |
| [serpstack](https://serpstack.com/product) · [الحصول على الوصول](https://serpstack.com/signup/free) | مفتاح شخصي | 100 searches/month | month | غير تجاري فقط | Free forever؛ JSON فقط؛ لا تفترض أن عدد المواقع المستخرجة يساوي search requests. |
| [Tavily](https://www.tavily.com/pricing) · [الحصول على الوصول](https://app.tavily.com/) | مفتاح شخصي | 1000 API credits/month | month | غير محسوم من المصدر | عدد credits يختلف حسب endpoint ونمط البحث؛ لا تفعّل الدفع حسب الاستخدام للحصول على المزيد. |

<a id="security"></a>

## الأمن

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [AbuseIPDB](https://www.abuseipdb.com/pricing) · [الحصول على الوصول](https://www.abuseipdb.com/register) | مفتاح شخصي | 1000 IP checks/reports/day; 100 block checks/day; 5 bulk reports/day | day | مقيّد بشروط | Individual Free forever؛ blacklist حتى 10000 IP وقيود يومية؛ لا تنسب حدود تجربة الخطة المدفوعة للمجاني. |
| [urlscan.io](https://urlscan.io/pricing) · [الحصول على الوصول](https://urlscan.io/user/signup) | مفتاح شخصي | Free $0 plan; separate daily submission, result and search quotas shown in account | minute/hour/day | مقيّد بشروط | الحصص تختلف حسب نوع الفعل؛ لم أضع رقمًا من جدول غير واضح؛ public scan قد يكشف URL المرسل، فلا ترسل روابط خاصة. |
| [VirusTotal Public API](https://docs.virustotal.com/reference/public-vs-premium-api) · [الحصول على الوصول](https://www.virustotal.com/gui/join-us) | مفتاح شخصي | 500 requests/day; 4 requests/minute | day/minute | غير تجاري فقط | لا منتجات تجارية ولا business workflows التي لا تساهم بملفات جديدة؛ يمنع تعدد الحسابات لتجاوز الحصة؛ احذر خصوصية الملفات التي ترفعها. |

<a id="sports"></a>

## الرياضة

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [Chess.com Published Data API](https://www.chess.com/news/view/published-data-api) · [الحصول على الوصول](https://www.chess.com/news/view/published-data-api) | بلا مفتاح | Unlimited serial requests; parallel requests may be throttled | no serial request quota | مقيّد بشروط | قراءة بيانات عامة فقط؛ انتظر انتهاء الطلب قبل التالي؛ البيانات قد تُحدّث كل 24 ساعة؛ احترم حقوق وخصوصية البيانات. |
| [football-data.org](https://www.football-data.org/pricing) · [الحصول على الوصول](https://www.football-data.org/client/register) | مفتاح شخصي | 10 calls/minute; free coverage of 12 competitions | minute | مقيّد بشروط | Free forever؛ النتائج والجداول مؤخرة؛ الإحصاءات الموسعة والاحتمالات والإضافات مدفوعة. |

<a id="validation"></a>

## التحقق من البيانات

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [Abstract Email Validation](https://www.abstractapi.com/pricing) · [الحصول على الوصول](https://www.abstractapi.com/api/email-verification-validation-api) | مفتاح شخصي | 100 requests/month; 3 requests/second | month/second | غير محسوم من المصدر | حصة مستقلة لمنتج Email؛ اختَر الخطة المجانية؛ نتائج التحقق تقديرية وليست ضمان تسليم. |
| [Abstract Phone Validation](https://www.abstractapi.com/pricing) · [الحصول على الوصول](https://www.abstractapi.com/api/phone-validation-api) | مفتاح شخصي | 100 requests/month | month | غير محسوم من المصدر | حصة مستقلة لمنتج Phone؛ لا يساوي توفر metadata إثبات امتلاك الرقم ولا إرسال SMS مجانيًا. |
| [mailboxlayer](https://mailboxlayer.com/product) · [الحصول على الوصول](https://mailboxlayer.com/signup/free) | مفتاح شخصي | 100 API requests/month | month | غير تجاري فقط | تقييم جودة البريد فقط؛ لا bulk endpoint بالمجاني؛ راجع تفعيل HTTPS والشروط من لوحة الحساب. |
| [numverify](https://numverify.com/product) · [الحصول على الوصول](https://numverify.com/signup/free) | مفتاح شخصي | 100 requests/month; free without time limit | month | غير تجاري فقط | خطة Free موصوفة trial without time limit لكنها حصة شهرية مستمرة؛ تحقق من دعم HTTPS في الحساب لأن جدول الميزات والFAQ لا يتطابقان دائمًا. |
| [userstack](https://userstack.com/product) · [الحصول على الوصول](https://userstack.com/signup/free) | مفتاح شخصي | 100 lookups/month | month | غير تجاري فقط | جدول Free الحالي 100؛ FAQ أقدم يذكر 10000، استخدمت الرقم الأقل من جدول السعر الحالي؛ لا bulk بالمجاني. |

<a id="weather"></a>

## الطقس

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [National Weather Service](https://www.weather.gov/documentation/services-web-api) · [الحصول على الوصول](https://www.weather.gov/documentation/services-web-api) | بلا مفتاح | Free public data; reasonable unpublished rate limits | ongoing; throttle clears after waiting | مسموح بشروط البيانات | يلزم User-Agent واضح؛ الخدمة تخص الولايات المتحدة؛ عدم نشر حد رقمي لا يعني عدم وجود throttling. |
| [Open-Meteo](https://open-meteo.com/en/pricing) · [الحصول على الوصول](https://open-meteo.com/en/docs) | بلا مفتاح | 600 calls/minute; 5000/hour; 10000/day; 300000/month | minute/hour/day/month | غير تجاري فقط | الاستخدام غير التجاري؛ لا مفتاح للمسار المفتوح؛ الحصة مشتركة مع APIs المفتوحة للمزود؛ الترخيص التجاري مدفوع. |
| [OpenWeather Free APIs](https://openweathermap.org/price) · [الحصول على الوصول](https://home.openweathermap.org/users/sign_up) | مفتاح شخصي | 60 calls/minute; 1000000 calls/month | minute/month | مقيّد بشروط | اختر Free Weather API access؛ يشمل الطقس الحالي وتوقع 5 أيام والتلوث والخرائط والترميز الجغرافي؛ One Call المدفوع منفصل ومستبعد هنا. |
| [Visual Crossing](https://www.visualcrossing.com/weather-api/) · [الحصول على الوصول](https://www.visualcrossing.com/sign-up) | مفتاح شخصي | 1000 weather records/day | day | غير محسوم من المصدر | الحصة records وليست requests؛ الطلب التاريخي متعدد الأيام قد يستهلك أكثر من سجل؛ تجنب تفعيل الاستخدام المدفوع. |
| [WeatherAPI.com](https://www.weatherapi.com/pricing.aspx) · [الحصول على الوصول](https://www.weatherapi.com/signup.aspx) | مفتاح شخصي | 100000 calls/month | month; first day 00:00 UTC | مسموح بشروط البيانات | الخصائص والمدة التاريخية تختلف عن المدفوع؛ عند نفاد الحصة يتوقف الرد حتى التجديد أو الترقية. |
| [Weatherbit](https://www.weatherbit.io/pricing) · [الحصول على الوصول](https://www.weatherbit.io/account/create) | مفتاح شخصي | 50 requests/day; 1 request/second | day/second | غير تجاري فقط | خطة always-free مختلفة عن تجربة Business لمدة 21 يومًا؛ للاستخدام غير التجاري؛ الطقس الحالي وتوقع يومي 7 أيام. |

## الصيانة والمساهمة

لتغيير صف، حدّث JSON وCSV والدليل ومصدرًا رسميًا وتاريخ المراجعة. [قواعد المساهمة](CONTRIBUTING.md). فحص CI يراجع التكرار والحقول واتساق النسخ وعدم تسريب أسرار؛ لا يثبت السعر تلقائيًا ولا يسجل حسابات.

توثيق المجانية مختلف عن فحص استجابة endpoint. أمثلة [smoke-test](research/smoke-tests.json) قليلة وخالية من مفاتيح شخصية؛ لم تختبر كل الخدمات ولا الاستحقاق الجغرافي لكل مستخدم.

الكتالوج والكتابة الأصلية تحت [CC0](LICENSE). المحتوى وAPIs وشروط المزودين ليست ضمن هذا الترخيص. قد تتغير الحصص بعد تاريخ المراجعة.
