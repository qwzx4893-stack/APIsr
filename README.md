# APIsr — دليل APIs المجانية

**260 خدمة في 37 مجالًا، مراجعة في 2026-10-13 بتوقيت بغداد.**

**للمفاتيح العامة دون تسجيل تحديدًا:** [قائمة مستقلة تضم 47 خدمة مختبرة و26 قيمة مفتاح مختلفة](docs/public-shared-keys.ar.md) · [JSON بالمفاتيح والطلبات الكاملة](data/public-shared-keys.json) · [CSV](data/public-shared-keys.csv). منها 44 خدمة ببيانات فعلية أو sandbox، وثلاث للتدريب أو placeholder فقط. توجد [39 خدمة مفيدة لنماذج المشاريع](docs/practical-projects.ar.md). هذه الأعداد مستقلة عن الكتالوج العام، وليست 260 مفتاحًا مشتركًا.

دليل للحصول على APIs مجانية قانونية، مع الحصة ودورة التجديد ورابط إنشاء مفتاحك والمصدر الرسمي وقيود الاستخدام. يغطي خدمات عامة ومتخصصة. **ليس مخزنًا لمفاتيح حسابات الآخرين، ولم تُنشأ حسابات لدى هذه المزودات نيابة عنك.**

## النتائج والملفات

- [القائمة الآلية JSON](data/catalog.json) · [CSV قابل للبحث](data/catalog.csv).
- [المفاتيح العامة المختبرة دون تسجيل](docs/public-shared-keys.ar.md) · [الأمثلة الستة الأصلية](data/public-demo-keys.json) · [طريقة الحصول على مفاتيحك](docs/access-guide.ar.md).
- [المستبعد وغير المحسوم](data/excluded-and-unconfirmed.json) · [منهجية التحقق](docs/methodology.ar.md).
- [مستودعات الاكتشاف](research/discovery-repositories.json) · [صفحات الإثبات الرسمية](research/official-sources.json) · [حدود التغطية](research/coverage.json).

تمت قراءة 24 قوائم على GitHub واستخراج 7154 رابطًا مرشحًا فريدًا، ثم مراجعة المصادر الرسمية للصفوف المقبولة. **الروابط المرشحة ليست عدد APIs مجانية مؤكدة، ولا نعد هذا مسحًا لكل الإنترنت.**

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
python scripts/public_keys.py --category translation
python scripts/public_keys.py --service mapconvert-demo --request
```

## فهرس المجالات

- [الذكاء الاصطناعي (5)](#ai)
- [المصادقة وإدارة الهوية (6)](#authentication)
- [الخدمات الخلفية وقواعد البيانات (19)](#backend)
- [التنوع الحيوي (1)](#biodiversity)
- [البلوكشين (6)](#blockchain)
- [الكتب (2)](#books)
- [التقاويم والعطلات (5)](#calendar)
- [إدارة المحتوى (6)](#content)
- [المتاحف والثقافة (3)](#culture)
- [التطوير والاختبار (8)](#development)
- [التعليم (1)](#education)
- [البريد الإلكتروني (9)](#email)
- [الترفيه (5)](#entertainment)
- [البيئة (4)](#environment)
- [إعدادات التطبيقات وFeature flags (2)](#feature_flags)
- [الأسواق والعملات (18)](#finance)
- [الأغذية والوصفات (3)](#food)
- [الألعاب (3)](#games)
- [الخرائط والمواقع وIP (21)](#geolocation)
- [البيانات الحكومية والإحصاءات (11)](#government)
- [الصحة والبيانات الطبية (1)](#health)
- [الصور والرسوم (6)](#images)
- [المعرفة (1)](#knowledge)
- [اللغة (7)](#language)
- [الأفلام والتلفاز والموسيقى (6)](#media)
- [معالجة الوسائط (9)](#media_processing)
- [الرسائل والإشعارات (9)](#messaging)
- [APIs متعددة المجالات (1)](#multi_domain)
- [الأخبار (7)](#news)
- [التعرف الضوئي على النص (1)](#ocr)
- [المستندات والإنتاجية (5)](#productivity)
- [الأبحاث العلمية (26)](#science)
- [البحث واستخراج المحتوى (11)](#search)
- [الأمن (8)](#security)
- [الرياضة (2)](#sports)
- [التحقق من البيانات (11)](#validation)
- [الطقس (11)](#weather)

<a id="ai"></a>

## الذكاء الاصطناعي

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [Azure AI Speech F0](https://azure.microsoft.com/en-us/pricing/details/cognitive-services/speech-services/) · [الحصول على الوصول](https://portal.azure.com/) | مفتاح شخصي | 5 audio hours/month real-time standard transcription; neural text-to-speech 0.5 million characters/month | month | مقيّد بشروط | فقطF0 والخصائص المذكورة؛ batch/fast/custom/ترجمةspeech لها قواعد منفصلة؛ بعض المناطق تفتقرF0؛ لا تفترض كل إمكاناتSpeech مجانية. |
| [Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai/platform/pricing/) · [الحصول على الوصول](https://dash.cloudflare.com/) | رمز حساب / OAuth | 10000 neurons/day on Workers Free | day; 00:00 UTC | غير محسوم من المصدر | ليست neurons عدد tokens أو طلبات؛ بعض النماذج تتطلب الدفع وتستبعد؛ تجاوز المجاني يفشل ولا يستمر دون ترقية. |
| [Google Gemini Developer API](https://ai.google.dev/gemini-api/docs/pricing) · [الحصول على الوصول](https://aistudio.google.com/apikey) | مفتاح شخصي | Free input/output for eligible models; RPM, TPM and RPD depend on model and project | minute/day | مقيّد بشروط | اختر نموذجًا يظهر Free of charge؛ حدود الطلبات يوميًا تتجدد بتوقيت المحيط الهادئ؛ المحتوى قد يستخدم لتحسين المنتجات؛ توجد قيود جغرافية وعمرية. |
| [Groq](https://console.groq.com/docs/rate-limits) · [الحصول على الوصول](https://console.groq.com/keys) | مفتاح شخصي | Model-dependent RPM, RPD, TPM and TPD; example gpt-oss-120b: 30 RPM, 1000 RPD, 8000 TPM, 200000 TPD | minute/day | غير محسوم من المصدر | الحدود على مستوى المؤسسة وتختلف بالنموذج؛ راجع لوحة Limits؛ المجاني لا يشمل كل ميزات الخطة المدفوعة. |
| [Mistral Studio Free mode](https://docs.mistral.ai/admin/billing-usage/usage-limits) · [الحصول على الوصول](https://docs.mistral.ai/getting-started/quickstarts/studio/activate-and-generate-api-key) | مفتاح شخصي | Included monthly usage; model-specific RPS and TPM shown in account Limits | month/second/minute | غير محسوم من المصدر | المصدر يثبت الحصة الشهرية لكنه لا ينشر رقمًا موحدًا؛ ابق في Free mode؛ الدفع حسب الاستخدام منفصل. |

<a id="authentication"></a>

## المصادقة وإدارة الهوية

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [Auth0 Free](https://auth0.com/pricing) · [الحصول على الوصول](https://auth0.com/signup) | رمز حساب / OAuth | 25000 monthly active users; 5 organizations within Free scope | month | غير محسوم من المصدر | لا بطاقة للتسجيل؛ custom domain قد يتطلب تحقق بطاقة. حدود Auth/API وconnections/Enterprise وMFA المتقدم تختلف عن المجاني. |
| [Clerk Hobby](https://www.clerk.com/pricing) · [الحصول على الوصول](https://dashboard.clerk.com/) | مفتاح شخصي | 50000 monthly retained users per app; 3 dashboard seats; unlimited applications | month | غير محسوم من المصدر | MRU ليست MAU؛ جلسة Hobby7 أيام. بعض machine authentication وميزات المؤسسات محدودة؛ SMS وPro منفصلان. |
| [Descope Free Forever](https://www.descope.com/pricing) · [الحصول على الوصول](https://app.descope.com/) | مفتاح شخصي | 7500 MAU; 10 monthly active tenants; 3 SSO connections; 10000 M2M exchanges | month | غير محسوم من المصدر | لا overages للمجاني؛ تحتاج ترقية لتجاوز الحصة. تطبيق federated واحد و5 test users؛ ليست كل ميزات Enterprise مجانية. |
| [Stytch Free allowance](https://www.stytch.com/pricing) · [الحصول على الوصول](https://stytch.com/dashboard) | مفتاح شخصي | 10000 monthly active users and AI agents; 1000 M2M tokens; 5 SSO/SCIM connections | month | غير محسوم من المصدر | Always free للحصة المذكورة. SMS وDevice Fingerprint وميزات أخرى بأسعار منفصلة؛ الزيادة عن الحصة تدخل PAYG. |
| [SuperTokens managed free allowance](https://www.supertokens.com/pricing) · [الحصول على الوصول](https://supertokens.com/dashboard-saas) | مفتاح شخصي | Managed cloud free under 5000 monthly active users | month | غير محسوم من المصدر | Managed cloud مجاني under5K MAU كما ينص المزود. البريد وSMS قد يكلفان عبر مزود خارجي؛ self-hosted software ليس استضافة مجانية من المزود. |
| [WorkOS AuthKit](https://workos.com/pricing) · [الحصول على الوصول](https://dashboard.workos.com/) | مفتاح شخصي | First 1 million monthly active users free for User Management/AuthKit | month | غير محسوم من المصدر | المجانية User Management/AuthKit فقط. SSO وDirectory Sync/SCIM وRadar منتجات وأسعار منفصلة؛ لا تعمم الحصة على WorkOS كله. |

<a id="backend"></a>

## الخدمات الخلفية وقواعد البيانات

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [Airtable](https://support.airtable.com/docs/managing-api-call-limits-in-airtable) · [الحصول على الوصول](https://airtable.com/create/tokens) | رمز حساب / OAuth | 1000 API calls/workspace/month; 5 requests/second/base | month/second | غير محسوم من المصدر | Free workspace؛ PAT مع أضيق نطاق للقاعدة؛ حد شهري مشترك بين المستخدمين؛ عدد السجلات والملفات محدود. |
| [Appwrite Cloud Free](https://appwrite.io/pricing?_hsmi=269457680) · [الحصول على الوصول](https://cloud.appwrite.io/) | مفتاح شخصي | 75000 MAU; 5GB bandwidth/month; 2GB storage; 2 projects sharing resources | month | غير محسوم من المصدر | مشروعان بموارد مشتركة؛ المشروع يتوقف بعد أسبوع خمول. auth/database/storage/functions ضمن منصة واحدة؛ Education وPro trial خارج هذا الصف. |
| [Back4app BaaS Free](https://www.back4app.com/pricing/backend-as-a-service) · [الحصول على الوصول](https://www.back4app.com/) | مفتاح شخصي | 25000 requests/month; 250MB database; 1GB transfer; 1GB files | month | تطوير/تعليم/تقييم فقط | للتطوير والتعلم والنماذج الأولية؛25K طلب شهريًا. أنواع مفاتيح application/REST/master تختلف بالصلاحيات؛ master key لا ينشر في العميل. |
| [Cloudflare D1](https://developers.cloudflare.com/d1/platform/pricing/) · [الحصول على الوصول](https://dash.cloudflare.com/) | رمز حساب / OAuth | 5 million rows read/day; 100000 rows written/day; 5 GB total storage | day; 00:00 UTC | غير محسوم من المصدر | Rows لا queries؛ الفهارس قد تزيد write counts؛ التزم Free لتجنب billing؛ التخزين سعة ثابتة. |
| [Cloudflare Durable Objects SQLite](https://developers.cloudflare.com/durable-objects/platform/pricing/) · [الحصول على الوصول](https://dash.cloudflare.com/) | رمز حساب / OAuth | 100000 requests/day; 13000 GB-seconds/day; SQLite storage free limits apply | day | غير محسوم من المصدر | المجاني SQLite فقط ويحتاج Worker يقدّم واجهة HTTP. HTTP/RPC/WebSocket/alarm تدخل الاستهلاك وفق الوثائق؛ KV-backend ليس مجانيًا هنا. |
| [Cloudflare R2 Standard](https://developers.cloudflare.com/r2/pricing/) · [الحصول على الوصول](https://dash.cloudflare.com/) | رمز حساب / OAuth | 10GB-month storage, 1 million Class A and 10 million Class B operations/month; free egress | month | غير محسوم من المصدر | المجاني Standard فقط؛ Infrequent Access مستبعد. عمليات A/B مختلفة؛ تجاوز الحدود قد يفوتر تلقائيًا على حسابك، فراقب الحصة. |
| [Cloudflare Workers Free](https://developers.cloudflare.com/workers/platform/pricing/) · [الحصول على الوصول](https://dash.cloudflare.com/) | رمز حساب / OAuth | 100000 dynamic requests/day; 10 ms CPU/invocation | day | غير محسوم من المصدر | خطة Workers Free منفصلة عن Paid؛ static assets مجانية دون حصة requests لكن limits الأخرى تبقى؛ التزم وقت CPU. |
| [Cloudflare Workers KV](https://developers.cloudflare.com/kv/platform/pricing/) · [الحصول على الوصول](https://dash.cloudflare.com/) | رمز حساب / OAuth | 100000 reads/day; 1000 writes, deletes and lists/day each | day; 00:00 UTC | غير محسوم من المصدر | Workers Free فقط؛ 1 GB تخزين ثابت؛ تجاوز نوع العملية يوقفه حتى التجديد؛ بعض batch operations تحسب لكل key. |
| [Convex Free](https://www.convex.dev/pricing) · [الحصول على الوصول](https://dashboard.convex.dev/) | رمز حساب / OAuth | 1 million function calls/month; 20 GB-hours action compute included | month | غير محسوم من المصدر | اختر Free لا Starter ذات الدفع حسب الاستخدام؛ حدود تخزين وbandwidth ووظائف متزامنة؛ compute وحدات مختلفة عن calls. |
| [Firebase Cloud Firestore](https://firebase.google.com/docs/firestore/quotas) · [الحصول على الوصول](https://console.firebase.google.com/) | رمز حساب / OAuth | 50000 document reads/day; 20000 writes/day; 20000 deletes/day; 10 GiB transfer/month | day; midnight Pacific / month | غير محسوم من المصدر | Spark بلا billing؛ قاعدة مجانية واحدة لكل project؛ 1 GiB تخزين ثابت؛ TTL/PITR/backups وغيرها قد تتطلب billing وتستبعد. |
| [Firebase Realtime Database](https://firebase.google.com/docs/database/usage/billing) · [الحصول على الوصول](https://console.firebase.google.com/) | رمز حساب / OAuth | 10 GB downloads/month; 1 GB storage | month | غير محسوم من المصدر | Spark دون فاتورة؛ 100 اتصال متزامن وفق جدول الخطة؛ احم البيانات بـRules؛ ترقية Blaze تضيف دفعًا عند التجاوز. |
| [Firebase Remote Config](https://firebase.google.com/pricing) · [الحصول على الوصول](https://console.firebase.google.com/) | رمز حساب / OAuth | 100000 fetch requests/day/project on Spark | day | غير محسوم من المصدر | حسب تسعير بدأ 1 سبتمبر 2026؛ quota للـfetch لا تعني معدل admin REST؛ لا تعتمد وصف unlimited القديم؛ Spark فقط. |
| [JSONStorage Free](https://www.jsonstorage.net/) · [الحصول على الوصول](https://www.jsonstorage.net/) | بلا مفتاح | 1000 API requests/month; 25 items; up to 64KB/item | month | تطوير/تعليم/تقييم فقط | المجاني دون حساب؛ item ID لا يمثل مصادقة مناسبة للأسرار. حد1000 طلب شهريًا؛trial31يومًا للمدفوع مستبعدة؛ تجاوز المجاني قد يسبب throttling. |
| [Neon Data API](https://www.neon.com/pricing) · [الحصول على الوصول](https://console.neon.tech/) | رمز حساب / OAuth | 100 CU-hours/month/project; 1GB database/project; 100 projects; Data API uses database resources | month | غير محسوم من المصدر | Free بلا حد زمني؛ فعّل Data API في مشروعك واستخدم auth وRLS. CU-hours ليست requests، وسعة storage سقف مستمر؛ الاستهلاك الإضافي أوالخدمات المدفوعة خارج المجاني. |
| [Supabase](https://supabase.com/pricing) · [الحصول على الوصول](https://supabase.com/dashboard) | مفتاح شخصي | Unlimited API requests; 50000 monthly active users; 5 GB egress/month | month for egress and MAU; API requests unmetered | غير محسوم من المصدر | 2 مشاريع؛ 500 MB database و1 GB file storage ثابتان؛ pause بعد أسبوع خمول؛ publishable/anon key لا يعطي صلاحية admin ويجب ضبط RLS. |
| [Turso Cloud HTTP API](https://www.turso.tech/pricing) · [الحصول على الوصول](https://app.turso.tech/) | رمز حساب / OAuth | 500 million rows read/month; 10 million rows written/month; 3GB sync/month; 5GB storage; 100 databases | month | غير محسوم من المصدر | الحدود صفوف SQL وليست requests؛ استخدم HTTP pipeline وtoken خاصًا بقاعدتك. التخزين5GB سقف، وSLA والميزات الأعلى مدفوعة. |
| [Upstash Redis REST API](https://www.upstash.com/pricing/redis) · [الحصول على الوصول](https://console.upstash.com/) | رمز حساب / OAuth | 500000 commands/month; 10GB bandwidth/month; 250MB data size | month | غير محسوم من المصدر | commands ليست بالضرورة عدد HTTP requests عند batching. التخزين250MB سقف سعة؛ اختر Free بدل PAYG ولا تفترض أن كل addons مجانية. |
| [Upstash Vector Free](https://upstash.com/pricing/vector) · [الحصول على الوصول](https://console.upstash.com/) | رمز حساب / OAuth | 10000 vector query/update operations/day | day | تطوير/تعليم/تقييم فقط | query/update operations وليست عددvectors التخزينية. embeddings وسعة التخزين لها قواعد مستقلة؛ PAYG وproduction pack خارج المجاني. |
| [Upstash Workflow Free](https://upstash.com/pricing/workflow) · [الحصول على الوصول](https://console.upstash.com/) | رمز حساب / OAuth | 1000 workflow steps/day | day | تطوير/تعليم/تقييم فقط | steps ليست workflow runs. المنتج له حصة مختلفة عنQStash؛ الخدمات والمهام الخارجية قد تكلف؛ HTTPendpoint مشترك وفق طريقة التكامل. |

<a id="biodiversity"></a>

## التنوع الحيوي

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [GBIF public biodiversity APIs](https://www.gbif.org/restricted) · [الحصول على الوصول](https://www.gbif.org/developer/summary) | شخصي أو بلا مفتاح | Free public API access; heavy querying and high offsets may be restricted | continuous | مقيّد بشروط | القراءة العامة دون حساب؛ bulk downloads قد تحتاج حسابًا. البحث ذوoffset مرتفع والجمع المكثف قد يُقيّدان؛ استخدم downloads واحترم ترخيص كل dataset. |

<a id="blockchain"></a>

## البلوكشين

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [Alchemy](https://www.alchemy.com/pricing) · [الحصول على الوصول](https://dashboard.alchemy.com/) | مفتاح شخصي | 30 million compute units/month; 15 requests/second | month/second | غير محسوم من المصدر | الحصة compute units وليست عدد طلبات ثابتًا؛ 5 apps و5 webhooks؛ عمليات الشبكة والمعاملات قد لها gas مستقل غير مجاني. |
| [Blockchain.com Explorer public API](https://www.blockchain.com/explorer/api) · [الحصول على الوصول](https://www.blockchain.com/explorer/api) | بلا مفتاح | Official /public/* explorer endpoints require no payment; fair-use limits apply | continuous | مقيّد بشروط | المجاني للمسارات /public/* في specification؛ mirrors المدفوعة تحت /public/x402/* مستبعدة. قراءةexplorer/charts ليست wallet/transfers مجانية؛ رسومon-chain منفصلة. |
| [BlockCypher free tier](https://www.blockcypher.com/dev/) · [الحصول على الوصول](https://accounts.blockcypher.com/) | شخصي أو بلا مفتاح | 3 requests/second and 100 classic requests/hour; 100 webhook notifications/hour; 10 confidence lookups/hour | hour; top of UTC hour / second | مقيّد بشروط | القراءة الكلاسيكية قد تعمل دون token؛ عمليات POST/DELETE وwebhook/confidence تحتاج token. رسوم الشبكة on-chain منفصلة؛ حدود الجدول لا حدود المثال المدفوع. |
| [Etherscan](https://docs.etherscan.io/resources/rate-limits) · [الحصول على الوصول](https://etherscan.io/register) | مفتاح شخصي | 3 calls/second; 100000 calls/day | second/day | غير محسوم من المصدر | selected chains only؛ PRO endpoints غير مجانية؛ V2 والمفتاح موحد للشبكات المدعومة. |
| [Helius](https://www.helius.dev/pricing) · [الحصول على الوصول](https://dashboard.helius.dev/) | مفتاح شخصي | 1 million credits/month; 10 requests/second; 1 sendTransaction/second | month/second | غير محسوم من المصدر | Solana؛ credits تختلف حسب endpoint؛ لا تفعّل autoscaling مدفوع؛ fees للمعاملات منفصلة. |
| [Infura](https://www.infura.io/pricing) · [الحصول على الوصول](https://app.infura.io/register) | مفتاح شخصي | 3 million credits/day; 500 credits/second on Core | day/second | غير محسوم من المصدر | Core مجانية؛ مفتاح واحد؛ الأرصدة حسب طريقة RPC؛ رسوم blockchain ليست مشمولة بالمجانية. |

<a id="books"></a>

## الكتب

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [Internet Archive public APIs](https://archive.org/developers/) · [الحصول على الوصول](https://archive.org/developers/) | بلا مفتاح | Freely accessible public metadata/search services; no universal numeric quota published | continuous | مقيّد بشروط | القراءة العامة فقط؛ التعديل والرفع يحتاجان حسابًا. كتب الإعارة وحقوق الملفات لا تصبح حرة بمجانية metadata API؛ حدود الخدمات مختلفة. |
| [Open Library](https://openlibrary.org/developers/api) · [الحصول على الوصول](https://openlibrary.org/developers/api) | بلا مفتاح | 1 request/second default; 3/second with identified User-Agent and contact email | second | مقيّد بشروط | للبحث والقراءة البشرية بكمية منخفضة؛ ليست بنية خلفية bulk أو high-traffic تجارية؛ cache وdumps للأعمال الكبيرة. |

<a id="calendar"></a>

## التقاويم والعطلات

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [Abstract Holidays](https://www.abstractapi.com/api/holidays-api) · [الحصول على الوصول](https://app.abstractapi.com/users/signup) | مفتاح شخصي | 1000 requests/month; 1 request/second | month/second | غير محسوم من المصدر | حصةFree مستقلة للعطلات؛ coverage حسب الدولة والمنطقة والسنة. النتائج لا تضمن سياسة العطلات لكل مؤسسة أوولاية؛ تحقق من التحديث. |
| [Abstract Timezone](https://www.abstractapi.com/api/time-date-timezone-api) · [الحصول على الوصول](https://app.abstractapi.com/users/signup) | مفتاح شخصي | 5000 requests/month; 1 request/second | month/second | غير محسوم من المصدر | 5000 طلب شهريًا وسقف1/ثانية؛ المنتج مستقل. حد السرعة لا يلغي الحصة الشهرية؛ راجعDST والمنطقة الزمنية وتاريخ البيانات. |
| [Calendarific](https://calendarific.com/) · [الحصول على الوصول](https://calendarific.com/signup) | مفتاح شخصي | 500 calls/month | month | مقيّد بشروط | attribution مطلوب؛ لغة واحدة وتاريخ/مستقبل محدودان؛ الجدول الحالي 500 وليس 1000 كما في قوائم أقدم. |
| [Google Calendar API](https://developers.google.com/calendar/api/guides/quota) · [الحصول على الوصول](https://console.cloud.google.com/apis/library/calendar-json.googleapis.com) | رمز حساب / OAuth | Sliding per-minute project/user quotas shown in console; threshold 1000000 requests/day/project | minute/day | مقيّد بشروط | الوصول القياسي بلا تكلفة إضافية داخل الحصة؛ الحد الدقيق للدقيقة يتحدد في مشروعك؛ تغيرت سياسة المشاريع الجديدة في1مايو2026؛ invitation/spam limits منفصلة. |
| [Nager.Holiday public holiday API](https://date.nager.at/API) · [الحصول على الوصول](https://date.nager.at/API) | بلا مفتاح | Official page states no rate limits and unlimited queries; no key | no stated rate limit | غير محسوم من المصدر | الموقع الرسمي انتقل إلى API v4 على nagerholidays.com؛ لا تعتمد endpoint v3 من القوائم القديمة؛ تحققت من استجابة مثال عطلات AT/2026. |

<a id="content"></a>

## إدارة المحتوى

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [Contentstack](https://www.contentstack.com/pricing/) · [الحصول على الوصول](https://www.contentstack.com/) | مفتاح شخصي | 100000 API calls/month; 100 GB bandwidth/month | month | غير محسوم من المصدر | Free forever؛ production stack واحد و3 مستخدمين و10 أنواع محتوى؛ عدد entries/assets ثابت؛ ليس كل Agent OS مجانيًا بلا سقف. |
| [DatoCMS Free](https://www.datoCMS.com/pricing) · [الحصول على الوصول](https://dashboard.datocms.com/) | مفتاح شخصي | 100000 API calls/month; 10GB traffic/month; 300 records; 2 editors | month | غير محسوم من المصدر | Free forever بلا overages؛ الخدمة تتوقف عند تجاوز الحدود. management/delivery API يخضعان لحدود المشروع؛ السعة والفرق مختلفة عن المدفوع. |
| [Hygraph Hobby](https://www.hygraph.com/pricing) · [الحصول على الوصول](https://app.hygraph.com/) | شخصي أو بلا مفتاح | 500000 API calls/month; 100GB asset traffic; 1000 entries; uncached rate 5 RPS | month/second | تطوير/تعليم/تقييم فقط | Free forever للهواية والشخصي والتقييم. endpoint من مشروعك؛ auth/permissions تضبط الوصول؛ asset upload50MB؛ الحصص شهرية. |
| [Prismic Free](https://www.prismic.io/pricing) · [الحصول على الوصول](https://prismic.io/dashboard) | شخصي أو بلا مفتاح | 4 million API calls/month; 100GB CDN bandwidth/month; 1 user; 2 locales | month | تطوير/تعليم/تقييم فقط | لموقع شخصي أوPoC؛ no overages. token مطلوب بحسب خصوصية repo؛ الفرق الأكبر والميزات المدفوعة خارج المجاني. |
| [Sanity](https://www.sanity.io/pricing) · [الحصول على الوصول](https://www.sanity.io/get-started) | شخصي أو بلا مفتاح | 1 million CDN API requests/month; 250000 API requests/month; 100 GB bandwidth/month | month | غير محسوم من المصدر | Free forever؛ datasets عامة فقط؛ حصة CDN مستقلة عن API المباشر؛ لا تنشر write token. |
| [Storyblok Starter](https://www.storyblok.com/pricing) · [الحصول على الوصول](https://app.storyblok.com/) | مفتاح شخصي | 100000 API requests/month; 100GB traffic; 1 space; 1 seat, up to 2 | month | تطوير/تعليم/تقييم فقط | Starter مجاني مستمر؛trial45 يومًا لـGrowth Plus منفصل. للخدمات الشخصية والتجريبية؛ لا تنسب مزايا التجربة المؤقتة إلى الخطة المجانية. |

<a id="culture"></a>

## المتاحف والثقافة

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [Art Institute of Chicago](https://api.artic.edu/docs/) · [الحصول على الوصول](https://api.artic.edu/docs/) | بلا مفتاح | 60 requests/minute/IP; scraping at most 1 request/second | minute/second | مقيّد بشروط | بيانات عامة دون auth؛ public-domain artworks فقط للاستعمال الحر للصور؛ استخدم dumps للتحميل الكبير وHTTPS. |
| [Cleveland Museum Open Access](https://openaccess-api.clevelandart.org/) · [الحصول على الوصول](https://www.clevelandart.org/open-access) | بلا مفتاح | Free Open Access collection API; CC0-designated data and images | continuous | مسموح بشروط البيانات | CC0 يخص البيانات والصور الموسومة Open Access فقط. الملفات خارج النطاق قد تحتاج إذنًا؛ استخدم pagination والتخزين المؤقت؛ لا ضمان سعة غير محدودة. |
| [Library of Congress JSON/YAML](https://www.loc.gov/apis/json-and-yaml/working-within-limits/) · [الحصول على الوصول](https://www.loc.gov/apis/json-and-yaml/) | بلا مفتاح | 20 JSON/YAML requests/minute; rate-limit violation may block access for 1 hour | minute | مقيّد بشروط | المجموعات العامة دون حساب؛ limits الصور والنص والصوت مختلفة وتبقى في الصف نفسه. الضغط قد يخفض الحدود؛ حقوق كل عنصر تختلف. |

<a id="development"></a>

## التطوير والاختبار

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [Browserless Free](https://www.browserless.io/pricing) · [الحصول على الوصول](https://www.browserless.io/sign-up) | مفتاح شخصي | 1000 browser units/month; 2 concurrent browsers; max 2-minute sessions | month | غير محسوم من المصدر | units ليست عدد الطلبات؛ البروكسي وزمن الجلسة قد يستهلكان أكثر؛ الوثيقة الحرة محدودة بمناطق ومدة الجلسات. |
| [Cloudflare Browser Run](https://developers.cloudflare.com/browser-rendering/platform/pricing/) · [الحصول على الوصول](https://dash.cloudflare.com/) | رمز حساب / OAuth | Workers Free: 10 browser minutes/day; 3 concurrent browsers for browser sessions | day | غير محسوم من المصدر | الاسم الحالي Browser Run؛10 دقائق يوميًا للمجاني، أما10 ساعات شهريًا فللمدفوع. كل الطرق تشترك في زمن المتصفح. |
| [DummyJSON](https://dummyjson.com/) · [الحصول على الوصول](https://dummyjson.com/docs) | بلا مفتاح | Free fake REST API; no paid usage credit for public sample endpoints | ongoing; fair use | غير محسوم من المصدر | بيانات وهمية؛ auth endpoints للتجريب لا تعني حسابات مستخدمين حقيقية؛ لا تعد خدمة إنتاج خلفية دائمة. |
| [GitHub REST API](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api) · [الحصول على الوصول](https://github.com/settings/tokens) | شخصي أو بلا مفتاح | 60 requests/hour unauthenticated; 5000/hour authenticated | rolling hour | غير محسوم من المصدر | GitHub Free يدعم API؛ search وGraphQL لهما حدود أخرى؛ secondary limits مشتركة؛ لا تشمل الحصة تكاليف Actions أوCopilot؛ لا تنشر PAT. |
| [GitLab.com REST API](https://docs.gitlab.com/user/gitlab_com/rate_limits/) · [الحصول على الوصول](https://gitlab.com/-/user_settings/personal_access_tokens) | شخصي أو بلا مفتاح | Authenticated API up to 2000/minute; anonymous and endpoint-specific limits also apply | minute | غير محسوم من المصدر | خطة Free صفر دولار؛ الصفحة تفصل حدودًا مقترحة غير مفعلة عن الحدود الحالية؛ 100/minute للـFree ضمن proposal لا يعتمد كواقع نافذ؛ تحقق من headers. |
| [JSONPlaceholder](https://jsonplaceholder.typicode.com/) · [الحصول على الوصول](https://jsonplaceholder.typicode.com/guide/) | بلا مفتاح | Free for everyone; no signup or API key; no published recurring billing quota | ongoing; fair use | غير محسوم من المصدر | بيانات وهمية للتجريب؛ POST/PUT لا تحفظ تغييرات فعلية؛ عدم نشر quota لا يعني SLA أو عدم throttling. |
| [Mockfly Starter](https://www.mockfly.dev/pricing) · [الحصول على الوصول](https://www.mockfly.dev/) | رمز حساب / OAuth | 500 mock requests/day; 1 project; 4 endpoints; 2 responses/endpoint | day | تطوير/تعليم/تقييم فقط | APIs اصطناعية للاختبار؛500 طلب يوميًا و4endpoints للمشروع. custom domains وcallbacks والحصص الأعلى مدفوعة؛ URL منلوحة حسابك. |
| [Random User Generator](https://randomuser.me/documentation) · [الحصول على الوصول](https://randomuser.me/) | بلا مفتاح | Free hosted synthetic-user API; up to 5000 generated users/request; no billing quota published | continuous | مقيّد بشروط | بيانات اصطناعية للاختبار؛ الصور لها شروط مصدرها؛ ليست بيانات هوية حقيقية ولا خدمة تحقق من الأفراد. |

<a id="education"></a>

## التعليم

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [Hipo university-directory API](https://github.com/Hipo/university-domains-list) · [الحصول على الوصول](https://github.com/Hipo/university-domains-list) | بلا مفتاح | Free hosted directory API for small projects and exploration; large projects should self-host | continuous | تطوير/تعليم/تقييم فقط | قائمة الجامعات ونطاقاتها عامة؛ المثال الرسمي يستخدمHTTP؛ للاستعمال الكبير يطلب المزود الاستضافة الذاتية، فلا يُعرض كاستضافة إنتاج مجانية غير محدودة. |

<a id="email"></a>

## البريد الإلكتروني

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [Brevo](https://www.brevo.com/pricing/) · [الحصول على الوصول](https://www.brevo.com/) | مفتاح شخصي | 300 emails/day on Free | day | مقيّد بشروط | خطة Free forever بعد اعتماد الحساب للإرسال؛ البريد فقط، SMS وWhatsApp ليست مجانية؛ التزم الموافقة وسياسات الإرسال. |
| [MailerSend](https://www.mailersend.com/pricing) · [الحصول على الوصول](https://www.mailersend.com/) | مفتاح شخصي | 500 emails/month; 100 daily API requests in Free | month/day | مقيّد بشروط | اختر Free، وليس تجربة Professional 14 يومًا ولا Hobby المدفوعة؛ نطاق واحد وقيود تحقق الحساب. |
| [Mailgun Send Free](https://www.mailgun.com/pricing/) · [الحصول على الوصول](https://signup.mailgun.com/new/signup) | مفتاح شخصي | 100 emails/day; 1 custom sending domain; 2 API keys | day | مقيّد بشروط | Free بسعر0 شهريًا منفصل عن تجارب الخطط المدفوعة؛ تحقق النطاق والمرسل مطلوب؛ السجلات يوم واحد؛ لا تشمل خدمات Optimize/Inspect المدفوعة. |
| [Mailjet](https://www.mailjet.com/pricing/) · [الحصول على الوصول](https://app.mailjet.com/signup) | مفتاح شخصي | 6000 emails/month; 200/day | month/day | مقيّد بشروط | خطة Free؛ سقف contacts وخصائص الإحصاء؛ التحقق من المرسل وسياسات البريد مطلوبة. |
| [MailSlurp Free](https://www.mailslurp.com/pricing/) · [الحصول على الوصول](https://app.mailslurp.com/) | مفتاح شخصي | 500 emails received/month; 1000 sandbox sends/month to own account inboxes; 5000 weighted AI tokens/month | month | تطوير/تعليم/تقييم فقط | 0 دولار forever؛ الإرسال المجاني sandbox داخل الحساب وليس إرسال إنتاج مفتوح لأي عنوان؛ inbox/storage وSMS مقيدة. |
| [Mailtrap Email Sending Free](https://www.mailtrap.io/pricing/) · [الحصول على الوصول](https://mailtrap.io/register/signup) | مفتاح شخصي | 4000 emails/month and 150 emails/day; 1 domain; 1 user | month/day | مقيّد بشروط | حصة إرسال واستقبال مشتركة؛ ثلاثة أيام سجلات؛ Email Sandbox منتج مختلف ولا يُخلط بحصة إرسال الإنتاج. |
| [Postmark Free](https://postmarkapp.com/pricing) · [الحصول على الوصول](https://account.postmarkapp.com/sign_up) | مفتاح شخصي | 100 emails/month; no overages | month | تطوير/تعليم/تقييم فقط | الخطة المجانية100 بريد شهريًا لا تنتهي كما يوضح السعر، رغم تسمية الزر Free Trial. no overages؛ مناسب للتقييم والمشروعات الصغيرة. |
| [Resend](https://resend.com/pricing) · [الحصول على الوصول](https://resend.com/signup) | مفتاح شخصي | 3000 emails/month; 100 emails/day | month/day | مقيّد بشروط | المجانية تخص البريد ضمن الحصة؛ يحتاج الإرسال نطاقًا موثقًا وسياسات مكافحة الرسائل المزعجة؛ عدد domains محدود. |
| [SMTP2GO](https://www.smtp2go.com/pricing/) · [الحصول على الوصول](https://www.smtp2go.com/pricing/) | مفتاح شخصي | 1000 emails/month | month | مقيّد بشروط | المجاني مستمر كما ينص المزود. التسجيل يطلب بريد نطاق خاص؛ دعم الهاتف والدردشة محدود بأول14 يومًا، وهذا لا ينهي حصة البريد المجانية. |

<a id="entertainment"></a>

## الترفيه

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [Advice Slip](https://api.adviceslip.com/) · [الحصول على الوصول](https://api.adviceslip.com/) | بلا مفتاح | Free JSON advice API; no billing quota published | continuous | غير محسوم من المصدر | المحتوى ترفيهي؛ نتائجrandom قد تُخزّن مؤقتًا فلا تفترض نصًا جديدًا لكل طلب؛ لا يوجد مفتاح خاص. |
| [Chuck Norris Jokes](https://api.chucknorris.io/) · [الحصول على الوصول](https://api.chucknorris.io/) | بلا مفتاح | Free JSON jokes API; no numeric billing quota published | continuous | غير محسوم من المصدر | محتوى ترفيهي ساخر قد يتضمن ألفاظًا غير ملائمة؛ لا يتطلب مفتاحًا؛ عدم نشر سقف ليس ضمانunlimited. |
| [icanhazdadjoke](https://icanhazdadjoke.com/api) · [الحصول على الوصول](https://icanhazdadjoke.com/api) | بلا مفتاح | Public API requires no authentication and no usage credit | ongoing; fair use | غير محسوم من المصدر | أرسل Accept: application/json وUser-Agent؛ أضف نسبة المصدر عند إعادة عرض المحتوى؛ لا ضمان استضافة. |
| [JokeAPI](https://v2.jokeapi.dev/) · [الحصول على الوصول](https://v2.jokeapi.dev/) | بلا مفتاح | 120 requests/minute | minute | مقيّد بشروط | لاauthorization أوpayment؛ استخدمsafe-mode أوblacklist flags لتصفية المحتوى؛ تجاوز الحد يعيد429. |
| [ZenQuotes public cached API](https://zenquotes.io/) · [الحصول على الوصول](https://zenquotes.io/) | بلا مفتاح | 5 requests per 30 seconds/IP | 30 seconds | مقيّد بشروط | المجاني يحتاجattribution؛ بياناتcached تتحدث كل ساعة؛ CORS والوصولfresh وunlimited بمفتاح مدفوع، فلا تُنسب للمجاني. |

<a id="environment"></a>

## البيئة

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [NOAA Climate Data Online](https://www.ncei.noaa.gov/cdo-web/webservices/v2) · [الحصول على الوصول](https://www.ncei.noaa.gov/cdo-web/token) | مفتاح شخصي | 5 requests/second; 10000 requests/day | second/day | غير محسوم من المصدر | مفتاح خاص بطلب مجاني عبر البريد؛ ليس هو مفتاح NASA؛ البيانات الأمريكية والمناخية فقط. |
| [OpenAQ v3](https://docs.openaq.org/using-the-api/rate-limits) · [الحصول على الوصول](https://explore.openaq.org/register) | مفتاح شخصي | 60 requests/minute and 2000 requests/hour | minute/hour | مقيّد بشروط | General use مجاني؛ زيادة الحدود قد تتطلب الدفع. attribution وشروط مصادر القياسات واجبة؛ v1/v2 القديمة ليست واجهات وصول جديدة. |
| [USGS Earthquake FDSN](https://earthquake.usgs.gov/fdsnws/event/1/) · [الحصول على الوصول](https://www.usgs.gov/information-policies-and-instructions/copyrights-and-credits) | بلا مفتاح | Public earthquake-event query services; no numeric billing ceiling; max query-result sizes apply | continuous | مقيّد بشروط | بيانات حكومية عامة، وحد حجم نتائج للاستعلام في الوثائق. انسب USGS وراجع حقوق الطرف الثالث؛ ليست خدمة إنذار طوارئ ذات توفر مضمون. |
| [WAQI / AQICN](https://aqicn.org/api/) · [الحصول على الوصول](https://aqicn.org/data-platform/token/) | مفتاح شخصي | Default quota 1000 requests/second | second | مقيّد بشروط | يلزم نسبة المصدر؛ لا إعادة توزيع كبيانات مخزنة ولا إعادة بيع؛ راجع acceptable usage قبل الاستخدام التجاري. |

<a id="feature_flags"></a>

## إعدادات التطبيقات وFeature flags

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [ConfigCat Forever Free](https://www.configcat.com/pricing/) · [الحصول على الوصول](https://app.configcat.com/) | رمز حساب / OAuth | 5 million config JSON downloads/month; 20GB network traffic/month; unlimited local flag evaluations | month | غير محسوم من المصدر | عداد الحصة لتحميل config JSON منCDN؛ تقييم flags محليًا غير محدود. limits لعدد products/flags منفصلة؛ management credentials خاصة. |
| [Flagsmith Free](https://www.flagsmith.com/pricing) · [الحصول على الوصول](https://app.flagsmith.com/) | مفتاح شخصي | 50000 requests/month; 1 team member | month | غير محسوم من المصدر | fair use للflags/environments/identities؛ الزيادة تبدأ من50 دولار لكل مليون. أبق الاستهلاك ضمن الحصة وافحص إعداد الفوترة. |

<a id="finance"></a>

## الأسواق والعملات

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [Abstract Exchange Rates](https://www.abstractapi.com/api/exchange-rate-api) · [الحصول على الوصول](https://app.abstractapi.com/users/signup) | مفتاح شخصي | 500 requests/month; 1 request/second | month/second | غير محسوم من المصدر | الخطة Free مستقلة عن منتجات Abstract الأخرى؛ الحصة شهرية والسرعة1 طلب/ثانية. الوصول للتاريخ وتحديث البيانات والحقوق يتبع إعداد الخطة. |
| [Alpha Vantage](https://www.alphavantage.co/support/) · [الحصول على الوصول](https://www.alphavantage.co/support/#api-key) | مفتاح شخصي | 25 API requests/day; higher free access requires verified educational/open-source eligibility | day | مقيّد بشروط | الحصة الأساسية 25 فقط؛ البيانات اللحظية الأمريكية وميزات Premium ليست مجانية؛ لا تفترض قبول الإعفاء التعليمي. |
| [CoinGecko Demo](https://www.coingecko.com/en/api/pricing) · [الحصول على الوصول](https://www.coingecko.com/en/developers/dashboard) | مفتاح شخصي | 10000 call credits/month; 100 calls/minute | month/minute | مقيّد بشروط | خطة Demo صفر دولار متجددة؛ attribution مطلوب؛ البيانات والأسواق ونطاق السجل أقل من الخطط المدفوعة. |
| [coinlayer](https://coinlayer.com/product) · [الحصول على الوصول](https://coinlayer.com/signup/free) | مفتاح شخصي | 100 requests/month | month | غير تجاري فقط | لا انتهاء؛ USD target currency؛ الخطة المجانية وبياناتها أضيق من المدفوع. |
| [CoinLore public market data](https://www.coinlore.com/cryptocurrency-data-api) · [الحصول على الوصول](https://www.coinlore.com/cryptocurrency-data-api) | بلا مفتاح | No strict rate limit; provider recommends approximately 1 request/second | continuous | مسموح بشروط البيانات | المجاني موثق للمطورين والباحثين والشركات؛ واحد في الثانية توصية fair-use وليس حدًا صلبًا أوحصة مالية؛ جودة البيانات لا تضمن صلاحية قرار تداول. |
| [currencyapi Free](https://currencyapi.com/pricing) · [الحصول على الوصول](https://app.currencyapi.com/register) | مفتاح شخصي | 300 requests/month; 10 requests/minute; daily updates | month/minute | غير تجاري فقط | للاستخدام الشخصي والاختبار فقط؛ التجاري يحتاج ترقية. daily updates؛ ليست كل ميزات التاريخ أوالحقول المشمولة في الخطط الأعلى مجانية. |
| [CurrencyBeacon Developer Sandbox](https://currencybeacon.com/pricing) · [الحصول على الوصول](https://currencybeacon.com/register) | مفتاح شخصي | 5000 shared REST/MCP requests/month; hourly rate updates | month | تطوير/تعليم/تقييم فقط | للنماذج الأولية والتقييم؛ REST وMCP وطرق latest/history/conversion تشترك في الحصة. الخطط الإنتاجية الأعلى مدفوعة؛ لا مفتاح مستقل لكل عملة. |
| [CurrencyFreaks Developer](https://currencyfreaks.com/pricing.html) · [الحصول على الوصول](https://currencyfreaks.com/register) | مفتاح شخصي | 1000 API calls/month; 24-hour updates; USD base | month | غير محسوم من المصدر | USD base وتحديث كل24 ساعة؛ قواعد التاريخ وbases المتعددة في خطط أعلى. الحصة شهرية والخدمة مستقلة عن مزودي العملات الآخرين. |
| [currencylayer](https://currencylayer.com/product) · [الحصول على الوصول](https://currencylayer.com/signup/free) | مفتاح شخصي | 100 API calls/month | month | غير تجاري فقط | Free بلا مدة انتهاء؛ لا currency switching والتحويل الموسع؛ صفحة الأسعار أولى من أرقام القوائم القديمة. |
| [DBnomics](https://docs.db.nomics.world/) · [الحصول على الوصول](https://docs.db.nomics.world/) | بلا مفتاح | Free hosted economic-data platform and Web API; fair-use limits apply | continuous | مقيّد بشروط | قاعدة تجميع مجانية لها Web API؛ ترخيص كل provider يظل واجبًا. لا يحول ترخيص دليلنا كل السلاسل الاقتصادية إلى بيانات غير مقيدة. |
| [ExchangeRate-API](https://www.exchangerate-api.com/docs/free) · [الحصول على الوصول](https://www.exchangerate-api.com/) | شخصي أو بلا مفتاح | Registered Free: 1500 requests/month; Open Access: rate-limited, daily data refresh | month; open endpoint rate window unpublished | مقيّد بشروط | المسار المفتوح يتطلب attribution ويمنع إعادة توزيع البيانات؛ المسار ذو المفتاح مختلف؛ لا تختَر تجربة Pro. |
| [exchangerate.host Free](https://exchangerate.host/product) · [الحصول على الوصول](https://exchangerate.host/signup/free) | مفتاح شخصي | 100 requests/month; daily updates | month | غير محسوم من المصدر | الواجهة الحالية تحتاج مفتاحًا؛ وصف keyless القديم غير صالح.100 طلب شهريًا؛ لا تفترض conversion أوتحديثًا لحظيًا مجانيًا. |
| [ExchangeRatesAPI.io](https://exchangeratesapi.io/pricing/) · [الحصول على الوصول](https://exchangeratesapi.io/signup/free) | مفتاح شخصي | 100 requests/month | month | غير تجاري فقط | تحديث يومي وخطة محدودة؛ تبديل العملة الأساسية والتحويل وHTTPS قد يكونان مدفوعين بحسب endpoint والخطة. |
| [Fixer on APILayer](https://apilayer.com/marketplace/fixer-api) · [الحصول على الوصول](https://apilayer.com/marketplace/fixer-api) | مفتاح شخصي | 100 requests/month | month | مقيّد بشروط | Free for Lifetime؛ لا تخلط API السوق مع خطة fixer.io أخرى؛ العملات الأساسية والتحويل قد تختلف حسب الخطة. |
| [Frankfurter](https://frankfurter.dev/) · [الحصول على الوصول](https://frankfurter.dev/) | بلا مفتاح | No daily or monthly quota; abuse rate limits apply | no monthly/daily cap | مسموح بشروط البيانات | أسعار مرجعية وليست live trading؛ ترخيص المصادر المركزية يظل نافذًا؛ self-host للتدفق الكثيف. |
| [Massive Stocks Basic](https://massive.com/pricing) · [الحصول على الوصول](https://massive.com/dashboard/signup) | مفتاح شخصي | 5 API calls/minute; 2 years historical data; end-of-day stock data | minute | غير تجاري فقط | Stocks Basic للاستعمال الفردي؛ بيانات نهاية اليوم وسنتان تاريخ. ليست كل الأسواق أوالبيانات اللحظية أوالتراخيص التجارية مجانية؛ الاسم السابق Polygon. |
| [SEC EDGAR public data APIs](https://www.sec.gov/about/webmaster-frequently-asked-questions) · [الحصول على الوصول](https://www.sec.gov/search-filings/edgar-application-programming-interfaces) | بلا مفتاح | Maximum access rate 10 requests/second; public submissions/XBRL free to access and reuse | second | مسموح بشروط البيانات | User-Agent يعرّف التطبيق ووسيلة الاتصال مطلوب؛ لاCORS؛ يشمل العام فقط وليس تقديمfilings الخاصة؛ للتحميل الكبير استخدمarchives الرسمية. |
| [Twelve Data](https://twelvedata.com/pricing) · [الحصول على الوصول](https://twelvedata.com/register) | مفتاح شخصي | 8 API credits/minute; 800/day on Basic | minute/day | مقيّد بشروط | Basic فقط؛ كل رمز في الطلب قد يستهلك credit؛ اعرض بيانات الأسواق وفق ترخيصها؛ websocket trial غير محسوب. |

<a id="food"></a>

## الأغذية والوصفات

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [Open Food Facts](https://openfoodfacts.github.io/openfoodfacts-server/api/) · [الحصول على الوصول](https://world.openfoodfacts.org/data) | بلا مفتاح | Product reads: 15 requests/minute/IP; search/facet limits are separate | minute | مسموح بشروط البيانات | قاعدة البيانات وAPI مجانيان100%؛ ODbL attribution/share-alike؛ اذكرUser-Agent؛ للتحميل الكبير استخدمdump؛ الكتابة تتطلب حسابًا. |
| [TheCocktailDB development API](https://www.thecocktaildb.com/api.php) · [الحصول على الوصول](https://www.thecocktaildb.com/api.php) | مفتاح اختبار عام رسمي | Official public test key 1 for development/education; no paid trial credits | ongoing; fair use | تطوير/تعليم/تقييم فقط | مفتاح 1 رسمي؛ production/app store يتطلب Premium؛ random selection/popular/recent الموسعة مدفوعة. |
| [TheMealDB development API](https://www.themealdb.com/api.php) · [الحصول على الوصول](https://www.themealdb.com/api.php) | مفتاح اختبار عام رسمي | Official public test key 1 for development/education; no paid trial credits | ongoing; fair use | تطوير/تعليم/تقييم فقط | مفتاح 1 رسمي؛ النشر العام على app store يتطلب supporter؛ multi-ingredient/full database مزايا مدفوعة؛ الاستخدام المجاني هنا تعليمي فقط. |

<a id="games"></a>

## الألعاب

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [DAPI Digimon](https://digi-api.com/) · [الحصول على الوصول](https://digi-api.com/) | بلا مفتاح | Free public Digimon API; no numeric free ceiling published | continuous | مقيّد بشروط | بيانات رسمية ومعجبين؛ المزود غير تابع لـBandai؛ حقوق الشخصية محفوظة؛ لا تُعد حرية الوصول ترخيصًا تجاريًا للصور. |
| [Open Trivia DB](https://opentdb.com/api_config.php) · [الحصول على الوصول](https://opentdb.com/api_config.php) | بلا مفتاح | 1 API request/5 seconds/IP; up to 50 questions/request | 5 seconds | مقيّد بشروط | المجاني كامل؛ CC BY-SA 4.0؛ session token لمنع تكرار الأسئلة لا يمثل مفتاح دفع. |
| [PokeAPI](https://pokeapi.co/docs/v2) · [الحصول على الوصول](https://pokeapi.co/docs/v2) | بلا مفتاح | Rate limiting removed since move to static hosting; all resources open | no request quota documented | مقيّد بشروط | GET فقط؛ التخزين المؤقت وfair use مطلوبان؛ علامة Pokémon والمحتوى ليست ترخيصًا تجاريًا عامًا. |

<a id="geolocation"></a>

## الخرائط والمواقع وIP

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [Abstract IP Geolocation](https://www.abstractapi.com/pricing) · [الحصول على الوصول](https://www.abstractapi.com/api/ip-geolocation-api) | مفتاح شخصي | 1000 requests/month | month | غير محسوم من المصدر | حصة مستقلة لمنتج IP؛ الصفحة تؤكد monthly free tier؛ الميزات المتقدمة تختلف بالخطة. |
| [BigDataCloud client-side free APIs](https://www.bigdatacloud.com/free-api) · [الحصول على الوصول](https://www.bigdatacloud.com/free-api) | بلا مفتاح | No rate limits published for the designated client-side free API package | continuous | مقيّد بشروط | للمتصفح أو تطبيق الهاتف مباشرة فقط؛ استخدام خوادم backend محظور ضمن المجاني؛ لا يشمل حزم IP المدفوعة. |
| [Geoapify](https://www.geoapify.com/pricing/) · [الحصول على الوصول](https://myprojects.geoapify.com/) | مفتاح شخصي | 3000 credits/day; up to 5 requests/second | day/second | مسموح بشروط البيانات | يلزم attribution لـGeoapify ومصادر البيانات؛ بعض endpoints تستهلك عدة credits؛ المجاني يصلح للإنتاج ضمن حدوده. |
| [Geocodio](https://www.geocod.io/pricing/) · [الحصول على الوصول](https://dash.geocod.io/) | مفتاح شخصي | First 2500 credits used/day are free | day | مقيّد بشروط | للولايات المتحدة وكندا والمكسيك والمملكة المتحدة؛ البيانات الإضافية تكلف credits إضافية؛ تجاوز الحصة يدخل الدفع حسب الاستخدام، فتأكد من حدود الحساب. |
| [GeoNames](https://www.geonames.org/export/) · [الحصول على الوصول](https://www.geonames.org/login) | اسم مستخدم مجاني | 10000 credits/day; 1000 credits/hour | day/hour | مسموح بشروط البيانات | أنشئ اسم مستخدمك وفعّل web services؛ لا تستخدم demo username؛ attribution مطلوب؛ معظم الطلبات تستهلك credit واحدًا. |
| [GraphHopper Free](https://www.graphhopper.com/pricing/) · [الحصول على الوصول](https://graphhopper.com/dashboard/) | مفتاح شخصي | 500 credits/day; routing/location restrictions depend on Free package | day | غير تجاري فقط | للعمل غير التجاري مع attribution؛ credits ليست عدد الطرق عند matrix/optimization؛ الحدالأقصى للأماكن والمركبات يختلف بالطلب؛ لا تحمل أرقام paid إلىFree. |
| [ip-api](https://ip-api.com/docs/api:json) · [الحصول على الوصول](https://ip-api.com/docs/legal) | بلا مفتاح | 45 HTTP requests/minute/IP | minute | غير تجاري فقط | المجاني HTTP فقط؛ لا تستخدمه لبيانات حساسة؛ ترخيص تجاري وHTTPS مدفوعان؛ راجع أمثلة الاستخدام المسموح. |
| [IP2Location.io Free package](https://www.ip2location.io/pricing) · [الحصول على الوصول](https://www.ip2location.io/sign-up) | مفتاح شخصي | 50000 IP queries, 500 WHOIS queries and 50 hosted-domain queries/month | month | مقيّد بشروط | حزمة واحدة تشمل منتجات IP وWHOIS وHosted Domain؛ attribution مطلوب؛ لا تشمل خصائص الخطط المدفوعة ولا نعد كل endpoint مفتاحًا مستقلًا. |
| [ipapi.com](https://ipapi.com/product) · [الحصول على الوصول](https://ipapi.com/signup/free) | مفتاح شخصي | 100 IP lookups/month | month | غير تجاري فقط | الخطة Free لغير التجاري؛ HTTPS وLocation Data فقط؛ ليست خدمة ipapi.co المختلفة. |
| [ipapi.is](https://ipapi.is/pricing.html) · [الحصول على الوصول](https://ipapi.is/signup.html) | شخصي أو بلا مفتاح | 1000 requests/day with free account key; 30/day without key | day | مسموح بشروط البيانات | المزود يصرح بأنها ليست تجربة وبأن التجاري مسموح؛ 30 طلبًا دون مفتاح أقل من حصة الحساب المجاني؛ الرصيد المدفوع منفصل. |
| [ipbase Free](https://ipbase.com/pricing) · [الحصول على الوصول](https://app.ipbase.com/register) | مفتاح شخصي | 150 IP lookups/month; 10 requests/minute | month/minute | تطوير/تعليم/تقييم فقط | للاختبار والمشاريع الشخصية؛ بياناتlocation فقط ضمن النطاق؛ security/currency/timezone وبعضASN/reverse-IP ميزات مدفوعة؛ batch لا يزيد الحصة. |
| [ipdata](https://ipdata.co/pricing.html) · [الحصول على الوصول](https://dashboard.ipdata.co/sign-up.html) | مفتاح شخصي | 1500 requests/day | day | غير تجاري فقط | عند نفاد الحصة المجانية تُحجب الطلبات؛ لا تستخدم بيانات الخطة المجانية تجاريًا. |
| [IPGeolocation.io](https://ipgeolocation.io/pricing.html) · [الحصول على الوصول](https://ipgeolocation.io/signup.html) | مفتاح شخصي | 1000 API credits/day for life | day | مقيّد بشروط | للتجريب والمشاريع الصغيرة؛ لا overages بالمجاني؛ APIs المتخصصة قد تختلف في طريقة احتساب credits. |
| [IPinfo Lite](https://ipinfo.io/pricing) · [الحصول على الوصول](https://ipinfo.io/signup) | مفتاح شخصي | Unlimited country-level IP and ASN lookups on Lite | no monthly request cap | مقيّد بشروط | Lite يختلف عن بيانات المدينة وVPN المدفوعة؛ يتطلب مفتاح الحساب وترخيص/attribution الخطة؛ ليس كل endpoint مجانيًا. |
| [IPQuery](https://ipquery.io/) · [الحصول على الوصول](https://ipquery.io/) | بلا مفتاح | Unlimited free tier stated; no API key required | continuous | غير محسوم من المصدر | IP metadata وتحديدIP الخارجي؛ مجانية الوصول لا تضمن دقة جميع مخاطرVPN/Proxy؛ fair use وتوفر الخادم مهمان؛ لا تتطلب أومكتبة SDK. |
| [ipwho.is](https://ipwhois.io/documentation) · [الحصول على الوصول](https://ipwhois.io/documentation) | بلا مفتاح | 1000 requests/day/IP; browser CORS traffic counted per domain | day; access restored after 24h | مسموح بشروط البيانات | المسار Free فقط؛ لا bulk ولا security أو currency data؛ لا SLA؛ لا تفترض أن تبديل مفتاح يجدد حصة IP. |
| [LocationIQ](https://locationiq.com/pricing) · [الحصول على الوصول](https://my.locationiq.com/register) | مفتاح شخصي | 5000 requests/day; 60 requests/minute; 2 requests/second | day/minute/second | مقيّد بشروط | الاستخدام التجاري المجاني يتطلب رابطًا واضحًا للمزود؛ رمز وصول واحد؛ حدود الخرائط والتوجيه تختلف حسب المنتج. |
| [openrouteservice Standard](https://ask.openrouteservice.org/t/pricing-plan-from-the-api/5806) · [الحصول على الوصول](https://account.heigit.org/) | مفتاح شخصي | Standard Directions: 2000/day and 40/minute; geocoding and other endpoints have separate quotas | day/minute | مقيّد بشروط | مصدر الحصة رد رسمي من فريق الدعم؛ نقل API إلىapi.heigit.org في2026؛ api.openrouteservice.org القديم خفضت حصته؛ راجعحدودحسابك والشروط ونسبOSM/HeiGIT. |
| [positionstack](https://positionstack.com/product) · [الحصول على الوصول](https://positionstack.com/signup/free) | مفتاح شخصي | 100 requests/month | month | غير تجاري فقط | للاستخدام الشخصي؛ التوجيه الأمامي والعكسي فقط؛ خصائص batch وGeoJSON الموسعة مدفوعة. |
| [REST Countries API family](https://restcountries.com/docs) · [الحصول على الوصول](https://restcountries.com/) | مفتاح شخصي | 1000 shared requests/month; 20 requests/10 seconds; Free response limit 100 objects | month; account billing anniversary | غير تجاري فقط | حصة ومفتاح مشتركان لجميع APIs العائلة؛ الإصدارات1–4 قديمة وv5 الحالي. الإنتاج لدى الجهات الربحية والحكومية يتطلب خطة مدفوعة؛ بعض nonprofits المؤهلة لها استثناء محدد. لا تنشر dataset كاملًا. |
| [Zippopotam.us](https://api.zippopotam.us/) · [الحصول على الوصول](https://api.zippopotam.us/) | بلا مفتاح | Free postal-code JSON API; no numeric usage ceiling published | continuous | مقيّد بشروط | تغطية أكثر من60 دولة حسب الموقع؛ ليست قاعدة عناوين فردية ولا خدمة geocoding دقيقة؛ راجع شروط مصادر البيانات. |

<a id="government"></a>

## البيانات الحكومية والإحصاءات

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [BLS Public Data API](https://www.bls.gov/developers/api_faqs.htm) · [الحصول على الوصول](https://data.bls.gov/registrationEngine/) | شخصي أو بلا مفتاح | Registered v2: 500 queries/day; unregistered v1: 25/day; 50 requests/10 seconds | day/10 seconds | مقيّد بشروط | تجديد تسجيل المفتاح سنويًا؛ 50 سلسلة و20 سنة/طلب للمسجل مقابل 25 سلسلة و10 سنوات لغير المسجل؛ إحصاءات عامة لا real-time markets. |
| [Census Data API](https://www2.census.gov/data/api-documentation/api-user-guide.pdf) · [الحصول على الوصول](https://api.census.gov/data/key_signup.html) | مفتاح شخصي | Free registered API key required for all data queries; max 50 variables/query; no billing quota published in current guide | continuous | مقيّد بشروط | دليل مايو2026 يطلبkey لكل dataquery؛ لا تستخدم وصف500/day دونkey القديم؛ بيانات إحصائية مجمعة لا أفراد؛ سجل المفتاح وتحقق من email. |
| [GovInfo API](https://www.govinfo.gov/features/api) · [الحصول على الوصول](https://api.data.gov/signup/) | شخصي أو demo رسمي | api.data.gov default 1000 requests/hour shared by key; DEMO_KEY 30/hour and 50/day/IP; service-specific changes possible | hour/day | مقيّد بشروط | مفتاح حكومي مجاني؛1000/ساعة default على مستوى المفتاح عبرagencies، وقد تختلف الخدمة. لا تضاعف الحصة بعددdatasets؛ ترخيص بعض المحتوى الخارجي مختلف. |
| [NASA Open APIs](https://api.nasa.gov/assets/html/authentication.html) · [الحصول على الوصول](https://api.nasa.gov/) | شخصي أو demo رسمي | Registered key: 1000 requests/hour; DEMO_KEY: 30/hour and 50/day/IP | hour rolling/day | مقيّد بشروط | الحصة مشتركة عبر خدمات api.nasa.gov؛ بعض APIs تختلف؛ صور الأطراف الثالثة قد تحمل حقوقًا منفصلة. |
| [National Park Service](https://www.nps.gov/subjects/developer/guides.htm) · [الحصول على الوصول](https://www.nps.gov/subjects/developer/get-started.htm) | مفتاح شخصي | 1000 requests/hour by default | hour rolling | مقيّد بشروط | مفتاح شخصي مجاني؛ يرسل في X-Api-Key؛ احترام Disclaimer وحقوق المحتوى والصور. |
| [ONS public data API](https://developer.ons.gov.uk/) · [الحصول على الوصول](https://www.ons.gov.uk/methodology/geography/licences) | بلا مفتاح | Public datasets and Census APIs under applicable Open Government Licence; rate limiting applies | continuous | مسموح بشروط البيانات | API عامة مع Open Government Licence؛ بعض endpoints قد تقاعدت. راجع datasets الحالية وrate limits؛ البيانات الخاصة والمحكومة مستبعدة. |
| [Socrata public SODA APIs](https://dev.socrata.com/docs/app-tokens.html) · [الحصول على الوصول](https://dev.socrata.com/) | شخصي أو بلا مفتاح | Public open-data reads; optional application tokens increase throttling allowance; no universal numeric quota | continuous | مقيّد بشروط | منصة بوابات Open Data في صف واحد؛ لا تُعد كل مدينة أوdataset خدمة جديدة. token اختياري للقراءة العامة؛ الترخيص حسب الجهة والكتابة/الخاص يحتاجان تفويضًا. |
| [Statistics Canada Web Data Service](https://www.statcan.gc.ca/en/developers/wds) · [الحصول على الوصول](https://www.statcan.gc.ca/en/reference/licence) | بلا مفتاح | Public WDS data/metadata; royalty-free licensed access with service limits | continuous | مسموح بشروط البيانات | تنشر بيانات وإحصاءات كل يوم عمل؛ attribution والدقة مطلوبان. للعمليات الكبيرة استخدم batch/CSV؛ لا سقفbilling موحد منشور. |
| [US EIA Open Data](https://www.eia.gov/opendata/documentation.php) · [الحصول على الوصول](https://www.eia.gov/opendata/register.php) | مفتاح شخصي | Data and keys free; per-second/hour traffic tolerances apply | ongoing; temporary throttle | مقيّد بشروط | يلزم مفتاح عبر البريد؛ الحظر الزائد مؤقت؛ راجع شروط الخدمة وCopyrights and Reuse؛ لم أنسب حدًا رقميًا غير موثق. |
| [US Treasury Fiscal Data](https://fiscaldata.treasury.gov/api-documentation/) · [الحصول على الوصول](https://fiscaldata.treasury.gov/api-documentation/) | بلا مفتاح | Data offered free without restriction for commercial/noncommercial use; no numeric billing quota published | continuous | مسموح بشروط البيانات | البيانات المالية الفدرالية وmetadata؛ endpoint-specific pagination/version1أو2؛ ليست خدمة بيع بيانات أسواق لحظية؛ لا ضمانlatency. |
| [World Bank Indicators API](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation) · [الحصول على الوصول](https://data.worldbank.org/summary-terms-of-use) | بلا مفتاح | Open public indicators with no key or paid request credit | ongoing; no numerical quota stated | مقيّد بشروط | V2؛ ترخيص CC BY 4.0 مع بعض بيانات أطراف ثالثة قد تختلف؛ لا افتراض SLA أو أن عدم نشر quota يلغي throttling. |

<a id="health"></a>

## الصحة والبيانات الطبية

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [openFDA](https://open.fda.gov/apis/authentication/) · [الحصول على الوصول](https://open.fda.gov/apis/authentication/) | شخصي أو بلا مفتاح | 240 requests/minute; 1000/day/IP without key; 120000/day/key with key | minute/day | مقيّد بشروط | المفتاح مجاني ويرفع الحصة اليومية؛ drug/device/food ضمن خدمة واحدة. تقارير الأحداث لا تثبت السببية؛ البيانات ليست إرشادًا طبيًا أووصولًا إلى ملفات مرضى. |

<a id="images"></a>

## الصور والرسوم

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [DiceBear hosted Avatar API](https://www.dicebear.com/how-to-use/http-api/) · [الحصول على الوصول](https://www.dicebear.com/how-to-use/http-api/) | بلا مفتاح | 50 requests/second for SVG; 10/second for raster/JSON | second | غير تجاري فقط | المسار المستضاف لغير التجاري؛ تراخيص styles مختلفة؛ raster حتى 256×256؛ self-host له متطلبات وترخيص منفصلان. |
| [Pixabay](https://pixabay.com/api/docs/) · [الحصول على الوصول](https://pixabay.com/accounts/register/) | مفتاح شخصي | 100 requests/60 seconds by default | 60 seconds | مقيّد بشروط | تخزين نتائج API مؤقتًا 24 ساعة مطلوب؛ لا تحميل جماعي ولا hotlinking دائم؛ التزم Content License ونسبة المصدر. |
| [RoboHash](https://robohash.org/) · [الحصول على الوصول](https://robohash.org/) | بلا مفتاح | Free hosted deterministic avatars; no billing quota published | continuous | مقيّد بشروط | التزم بترخيص مجموعة الرسوم المختارة ونسب الفنان؛ endpoint يأخذ نصًا ولا يحتاج مفتاحًا؛ الطلبات الكثيفة تتطلب مراعاة سعة المزود. |
| [TheCatAPI](https://thecatapi.com/) · [الحصول على الوصول](https://thecatapi.com/) | مفتاح شخصي | 10000 requests/month | month | غير تجاري فقط | خطة التعلم المجانية؛ ترخيص بيانات الاستخدام التجاري في Startup؛ لا تفترض شمول جميع حقول السلالات والمزايا. |
| [UI Avatars](https://ui-avatars.com/) · [الحصول على الوصول](https://ui-avatars.com/) | بلا مفتاح | Hosted avatar API with no limiting or login stated by provider | continuous | غير محسوم من المصدر | أسماء/initials تتحول إلى صور؛ لا تخزين معلومات كما يذكر المزود؛ no limiting ليس ضمانuptime أوسعة إنتاج غير منتهية. |
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
| [Azure AI Language free tier](https://azure.microsoft.com/en-us/pricing/details/cognitive-services/language-service/) · [الحصول على الوصول](https://portal.azure.com/) | مفتاح شخصي | 5000 text records/month for eligible text-analysis features; free-tier overages blocked | month | مقيّد بشروط | record ليست بالضرورةdocument/request كاملًا؛ أنواع CLU/custom/summarization مختلفة؛ عند بلوغ المجاني يتمthrottling بلاoverages كما يوضح المزود. |
| [Azure Translator F0](https://azure.microsoft.com/en-us/pricing/details/cognitive-services/translator/) · [الحصول على الوصول](https://portal.azure.com/) | مفتاح شخصي | 2 million characters/month for eligible standard translation and custom-translation training combined | month | مقيّد بشروط | اختر pricing tier F0؛ لا يشمل كل عمليات document/custom hosting؛ توفر المناطق والحساب يؤثران؛ ليس رصيدAzure الأولي المحدود زمنيًا. |
| [Datamuse](https://www.datamuse.com/api/) · [الحصول على الوصول](https://www.datamuse.com/api/) | بلا مفتاح | 100000 requests/day | day | مقيّد بشروط | لا مفتاح حتى 1 فبراير 2027؛ ابتداءً منه يلزم مفتاح والحصة نفسها يومية؛ نسبة المصدر والتواصل للتطبيقات الواسعة مطلوبان. |
| [Free Dictionary API](https://dictionaryapi.dev/) · [الحصول على الوصول](https://dictionaryapi.dev/) | بلا مفتاح | Always free public word definitions; no billing quota documented | ongoing; fair use | مقيّد بشروط | القاموس الإنجليزي؛ تراخيص المصادر والصوت في الرد؛ عدم نشر حد ليس ضمانًا لطلبات غير محدودة. |
| [Google Cloud Natural Language API](https://cloud.google.com/natural-language/pricing) · [الحصول على الوصول](https://console.cloud.google.com/apis/library/language.googleapis.com) | رمز حساب / OAuth | Feature-specific monthly free units; Entity Analysis first 5000 units at 0 USD; other features differ | month | مقيّد بشروط | وحدات معالجة unicode وليستrequests؛ تختلف moderation/classification/entity/sentiment؛ لا تفترض أن5000 وحدة لكل شيء؛ تحتاج تقييد الفوترة داخل المجاني. |
| [Google Cloud Translation standard models](https://cloud.google.com/translate/pricing) · [الحصول على الوصول](https://console.cloud.google.com/apis/library/translate.googleapis.com) | رمز حساب / OAuth | First 500000 characters/month free as 10 USD monthly credit for eligible standard translation | month | مقيّد بشروط | الرصيد يتجدد شهريًا وليس300دولارtrial؛ فقط أنواع الترجمة القياسية المشمولة؛ document/custom/adaptive تختلف وقد تكون مدفوعة؛ billing account والحدود ضروريان. |
| [LanguageTool Public HTTP API](https://dev.languagetool.org/public-http-api.html) · [الحصول على الوصول](https://dev.languagetool.org/public-http-api.html) | بلا مفتاح | 20 requests/minute/IP; 75 KB text/minute/IP; 20 KB/request | minute | مقيّد بشروط | مسموح للطلبات الفردية فقط؛ automated requests ممنوعة حسب الصفحة؛ لا ضمان خدمة ولا كل ميزات Premium. |

<a id="media"></a>

## الأفلام والتلفاز والموسيقى

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [AniList GraphQL](https://docs.anilist.co/guide/rate-limiting) · [الحصول على الوصول](https://docs.anilist.co/) | شخصي أو بلا مفتاح | Currently 30 requests/minute in degraded mode; normal documented ceiling 90/minute | minute | مقيّد بشروط | قراءة البيانات العامة دون OAuth؛ بيانات المستخدم تحتاج تفويضًا. غير التجاري مجاني، والتجاري دون150 دولار إيراد شهريًا وفق الشروط. الجمع الضخم واستخدامها كخدمة تخزين أومنافس tracking محظوران. |
| [Jikan public REST API](https://jikan.moe/?trk=public_post_reshare-text) · [الحصول على الوصول](https://jikan.moe/) | بلا مفتاح | Free hosted read-only anime/manga API; fair-use throttling applies | continuous | مقيّد بشروط | خدمة غير رسمية لقراءة بيانات MyAnimeList؛ المجانية لا تعني كل عمليات التعديل. احترم rate-limit headers وحقوق المصدر؛ لم ننقل الأرقام غير المحسومة من قوائم GitHub. |
| [MusicBrainz read API](https://musicbrainz.org/doc/MusicBrainz_API) · [الحصول على الوصول](https://musicbrainz.org/doc/MusicBrainz_API) | بلا مفتاح | 1 request/second/application | second | غير تجاري فقط | قراءة البيانات عامة؛ write/user requests تتطلب auth؛ User-Agent واضح؛ خطط تجارية منفصلة. |
| [OMDb](https://www.omdbapi.com/apikey.aspx) · [الحصول على الوصول](https://www.omdbapi.com/apikey.aspx) | مفتاح شخصي | 1000 requests/day on FREE account | day | غير تجاري فقط | بيانات CC BY-NC 4.0؛ Poster API للمشتركين؛ اختر FREE بدل Patreon. |
| [TMDB](https://developer.themoviedb.org/docs/faq) · [الحصول على الوصول](https://www.themoviedb.org/settings/api) | مفتاح شخصي | Free API for non-commercial use; rate limiting applies | ongoing; no paid usage credit in non-commercial API | غير تجاري فقط | attribution مطلوب؛ الترخيص التجاري يحتاج تواصلًا وموافقة منفصلة؛ لا تنشر مفتاح حسابك. |
| [TVmaze Public API](https://www.tvmaze.com/api) · [الحصول على الوصول](https://www.tvmaze.com/api) | بلا مفتاح | At least 20 calls/10 seconds/IP | 10 seconds | مقيّد بشروط | CC BY-SA وترخيص الصور منفصل؛ بيانات cache قد تتأخر ساعة؛ user-level API Premium خارج النطاق. |

<a id="media_processing"></a>

## معالجة الوسائط

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [ApiFlash](https://www.apiflash.com/) · [الحصول على الوصول](https://apiflash.com/accounts/register) | مفتاح شخصي | 100 screenshots/month | month | غير محسوم من المصدر | صيَغ PNG/JPEG/WebP؛ عدد screenshots وليس عدد صفحات متعددة في الطلب؛ لا تفترض ميزات أو SLA خطة Enterprise. |
| [Azure AI Vision F0](https://azure.microsoft.com/en-us/pricing/details/cognitive-services/computer-vision/) · [الحصول على الوصول](https://portal.azure.com/) | مفتاح شخصي | 5000 transactions/month; 20 transactions/minute in eligible regions | month/minute | مقيّد بشروط | حدد F0 ومدى توفره في منطقتك؛ counts تخص transactions للميزات؛ خدمات custom vision/face قد تكون منتجات منفصلة وتحتاج أهلية خاصة؛ المدفوع S1 خارج الدليل. |
| [Cloudinary Image and Video APIs](https://cloudinary.com/pricing) · [الحصول على الوصول](https://cloudinary.com/users/register_free) | مفتاح شخصي | 25 shared credits/month; 3 users / 1 account | month | مقيّد بشروط | Free forever للصور والفيديو؛ 1 credit يعادل 1000 تحويل أو1GB تخزين أوbandwidth ضمن حساب مشترك؛ ليست 25GB لكل بُعد معًا؛ DAM trial مستبعد. |
| [Filestack](https://www.filestack.com/pricing/) · [الحصول على الوصول](https://dev.filestack.com/signup/) | مفتاح شخصي | 500 uploads; 1000 transformations; 1 GB bandwidth in free monthly plan | month | غير محسوم من المصدر | Free forever؛ 1 GB storage ثابت؛ OCR وعمليات premium ليست ضمن المجاني؛ راجع دورة الحساب في لوحة الاشتراك. |
| [Google Cloud Vision API](https://cloud.google.com/vision/pricing) · [الحصول على الوصول](https://console.cloud.google.com/apis/library/vision.googleapis.com) | مفتاح شخصي | First 1000 units/month free per eligible feature; multiple features per image consume multiple units | month | مقيّد بشروط | unit هي معالجة صورة لكل feature؛ لا تعني1000 صورة مع جميع features بلا حدود؛ storage/المنتجات المصاحبة قد تكلف؛ تجاوز المجاني مدفوع تلقائيًا حسب الحساب. |
| [html2pdf.app](https://www.html2pdf.app/pricing) · [الحصول على الوصول](https://html2pdf.app/register) | مفتاح شخصي | 100 credits/month; up to 1MB per PDF; 1 parallel conversion | month; first day | غير محسوم من المصدر | تتجدد credits في أول الشهر؛ سقف 1MB للملف في المجاني؛ credits للتحويل وليست pages. |
| [ImageKit](https://imagekit.io/plans/) · [الحصول على الوصول](https://imagekit.io/registration/) | مفتاح شخصي | 20 GB bandwidth/month; 500 video units/month; 650 extension units/month | month | غير محسوم من المصدر | Forever free؛ 3 GB تخزين ثابت لا يتجدد كرصيد جديد؛ ميزات AI لها حصص منفصلة؛ الخطة Lite المدفوعة مختلفة. |
| [remove.bg preview API](https://www.remove.bg/api) · [الحصول على الوصول](https://www.remove.bg/users/sign_up) | مفتاح شخصي | 50 free API calls/month for preview-size outputs | month | مقيّد بشروط | المجانية للناتج preview منخفض الدقة؛ الصور الكبيرة والمدفوعة تستلزم credits؛ لا يعني حد حجم input أن output الكامل مجاني. |
| [screenshotlayer](https://screenshotlayer.com/product) · [الحصول على الوصول](https://screenshotlayer.com/signup/free) | مفتاح شخصي | 100 snapshots/month; no time limit | month | غير تجاري فقط | الحصة snapshots شهرية؛ الخصائص وتدفق HTTPS تختلف بالخطة؛ لا يشمل المجاني احتياجات معالجة مدفوعة. |

<a id="messaging"></a>

## الرسائل والإشعارات

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [Ably](https://ably.com/pricing) · [الحصول على الوصول](https://ably.com/sign-up) | مفتاح شخصي | 6 million messages/month; 200 concurrent connections; 500 messages/second | month/second | تطوير/تعليم/تقييم فقط | خطة Free لبناء proof of concept؛ الرسائل ومجموع الدقائق قنوات/اتصالات قد يحتسبان بصورة مختلفة في الخطط المدفوعة. |
| [Cloudflare Queues](https://developers.cloudflare.com/queues/platform/pricing/) · [الحصول على الوصول](https://dash.cloudflare.com/) | رمز حساب / OAuth | 10000 operations/day; 24-hour message retention | day | غير محسوم من المصدر | Workers Free؛ رسالة read/write/delete تستهلك غالبًا 3 operations؛ حجم أكثر من 64 KB يزيد الاحتساب؛ مليون operation شهريًا للخطة المدفوعة لا للمجاني. |
| [Courier Developer](https://www.courier.com/pricing) · [الحصول على الوصول](https://app.courier.com/) | مفتاح شخصي | 10000 sends/month for notification orchestration within Developer plan | month | مقيّد بشروط | حصةAPI لتنسيق notifications؛ مزودemail/SMS الخارجي قد يفرض رسومًا، فلا يُدّعى إرسالهما مجانًا. استخدم قنوات/ميزات بتكلفةصفر ضمن الحصة. |
| [Firebase Cloud Messaging](https://firebase.google.com/pricing) · [الحصول على الوصول](https://console.firebase.google.com/) | رمز حساب / OAuth | FCM messaging service is no-cost; request and delivery quotas still apply | ongoing; service-specific quota windows | مقيّد بشروط | الإشعارات push لا SMS؛ تكاليف خادمك أوFunctions منفصلة؛ service account/OAuth لا ينشر؛ limits للإرسال والأجهزة باقية. |
| [Knock Developer](https://www.knock.app/pricing) · [الحصول على الوصول](https://dashboard.knock.app/) | مفتاح شخصي | 10000 messages/month; 500 guide-active users/month; 500 AI-agent credits/month | month | مقيّد بشروط | messages منworkflows/broadcasts في عداد مشترك. الميزات الإضافية والمزودون الخارجيون قد يكلفون؛500 guide users و500 AIcredits شهريًا ضمن المجاني. |
| [Novu Free](https://www.novu.co/pricing) · [الحصول على الوصول](https://dashboard.novu.co/) | مفتاح شخصي | 10000 workflow runs/month; up to 20 workflows; 2 environments; up to 3 team members | month | مقيّد بشروط | workflow runs ليست عدد كلالرسائل. in-app والتنسيق ضمن الحصة؛ all channels لا تعني أن مزوديSMS/email مجانيون. سجلات24 ساعة؛ لا بطاقة. |
| [ntfy.sh public notifications](https://ntfy.sh/docs/publish/) · [الحصول على الوصول](https://ntfy.sh/docs/faq/) | بلا مفتاح | 250 messages/day on hosted ntfy.sh; 5 emails/day; 2MB attachments | day | مقيّد بشروط | المزود يلتزم باستمرار وصول الخادم المجاني دون signup مع منع الإساءة؛ topics العامة يمكن أن يقرأها آخرون؛ الميزات المحجوزة والاتصالات الهاتفية مدفوعة؛ لا تختبر POST على topics الآخرين. |
| [Pusher Channels](https://pusher.com/channels/pricing/) · [الحصول على الوصول](https://dashboard.pusher.com/accounts/sign_up) | مفتاح شخصي | 200000 messages/day; 100 concurrent connections | day | تطوير/تعليم/تقييم فقط | Sandbox المجانية؛ سر التطبيق يستخدم على السيرفر فقط؛ broadcasting قد يستهلك رسائل لكل مستلم. |
| [Upstash QStash Free](https://upstash.com/pricing/qstash) · [الحصول على الوصول](https://console.upstash.com/) | رمز حساب / OAuth | 1000 messages/day | day | تطوير/تعليم/تقييم فقط | تسليم HTTP messages وليس SMS مجانيًا؛ destinations الخارجية قد تكلف. retry وقواعدdelivery تؤثر في الحصة؛ اخترFree بدلPAYG. |

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
| [Finlight Launchpad](https://finlight.me/pricing) · [الحصول على الوصول](https://finlight.me/) | مفتاح شخصي | 5000 requests/month; 12-hour delay | month | غير محسوم من المصدر | الخطة للأفراد والفرق الصغيرة؛ رغم عبارة Real-Time Access يوضح الجدول تأخير12 ساعة. لا webhooks أوsentiment أوtickers أوWebSocket ضمن المجاني. |
| [GDELT public APIs](https://www.gdeltproject.org/data.html) · [الحصول على الوصول](https://www.gdeltproject.org/data.html) | بلا مفتاح | Free and open news/event database with public query APIs; fair use and query-size constraints apply | continuous | مقيّد بشروط | DOC/GEO APIs مجانية لبيانات الأخبار والأحداث؛ محتوى الناشرين وصورهم يحتفظ بحقوقه. BigQuery قد يسبب رسومًا مستقلة، ولا يُعد ضمن المجاني المستضاف المقصود. |
| [GNews](https://gnews.io/pricing) · [الحصول على الوصول](https://gnews.io/register) | مفتاح شخصي | 100 requests/day; up to 10 articles/request | day | غير تجاري فقط | للتطوير والاختبار والمشاريع غير التجارية؛ تأخير 12 ساعة؛ CORS على localhost؛ النص الكامل مدفوع. |
| [Marketaux Free](https://www.marketaux.com/pricing) · [الحصول على الوصول](https://www.marketaux.com/register) | مفتاح شخصي | 100 requests/day; 3 articles/news request | day | غير محسوم من المصدر | ثلاث مقالات لكل news request؛ جدول المجاني يعرض0 entities في stat request. لا تفترض ميزات الإثراء المدفوعة أوترخيص إعادة نشر نصوص الناشرين. |
| [mediastack](https://mediastack.com/product) · [الحصول على الوصول](https://mediastack.com/signup/free) | مفتاح شخصي | 100 calls/month | month | غير تجاري فقط | أخبار مؤخرة؛ لا historical data بالمجاني؛ حقوق المحتوى لا تنتقل بمجرد استعمال API. |
| [The Guardian Open Platform](https://open-platform.theguardian.com/access/) · [الحصول على الوصول](https://open-platform.theguardian.com/access/) | مفتاح شخصي | 500 calls/day and 1 call/second | day/second | غير تجاري فقط | Developer key مجاني لغير التجاري؛ article text متاح وفق شروط العرض والنسب. الاستخدام التجاري له مفتاح وخطة منفصلان. |

<a id="ocr"></a>

## التعرف الضوئي على النص

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [OCR.space](https://ocr.space/ocrapi) · [الحصول على الوصول](https://ocr.space/ocrapi) | شخصي أو demo رسمي | 25000 requests/month and 500 requests/day/IP | month/day | غير محسوم من المصدر | المجاني محدود بحجم ملف 1 MB وثلاث صفحات PDF؛ حد IP مشترك؛ لا ضمان أداء الخطة المدفوعة. |

<a id="productivity"></a>

## المستندات والإنتاجية

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [Google Docs API](https://developers.google.com/docs/api/limits) · [الحصول على الوصول](https://console.cloud.google.com/apis/library/docs.googleapis.com) | رمز حساب / OAuth | Reads: 3000/minute/project and 300/minute/user; writes: 600/minute/project and 60/minute/user | minute | مقيّد بشروط | API القياسية مجانية داخل الحصص؛ OAuth وصلاحيات المستند مطلوبة؛ إنشاء المستندات لا يمنح وصولًا إلى مستندات الآخرين؛ لا تفعّل زيادة مدفوعة لتجاوز المجاني. |
| [Google Drive API](https://developers.google.com/drive/api/guides/limits) · [الحصول على الوصول](https://console.cloud.google.com/apis/library/drive.googleapis.com) | رمز حساب / OAuth | New-project API quotas: 1000000 quota units/minute/project; 325000/user/project; threshold 1TB/day/project | minute/day | مقيّد بشروط | القياسي ضمن الحصص مجاني؛ quota units ليست عدد requests؛ تغيرت الحصص في1مايو2026؛ سعة حساب Drive منفصلة وليست1TB تخزينًا مجانيًا؛ overages خارج النطاق. |
| [Google Forms API](https://developers.google.com/forms/api/limits) · [الحصول على الوصول](https://console.cloud.google.com/apis/library/forms.googleapis.com) | رمز حساب / OAuth | Reads: 975/minute/project, 390/user; responses.list: 450/project, 180/user; writes: 375/project, 150/user | minute | مقيّد بشروط | المصدر ينشر عدم وجود حد يومي ضمن حدود الدقيقة؛ الاستخدام القياسي بلا تكلفة إضافية؛ watches لها حدود منفصلة؛ الاستجابة للنماذج قد تحتوي بيانات خاصة وتتطلب الإذن. |
| [Google Sheets API](https://developers.google.com/sheets/api/limits) · [الحصول على الوصول](https://console.cloud.google.com/apis/library/sheets.googleapis.com) | رمز حساب / OAuth | Read/write separately: 300 requests/minute/project and 60/minute/user/project | minute | مقيّد بشروط | الاستخدام القياسي ضمن الحصة بلا تكلفة إضافية؛ تحتاج OAuth وصلاحية الملفات؛ تجاوز الحصص قد يخضع لفوترة Google المعلنة لاحقًا في2026؛ لا حاجة إلى Workspace مدفوع لملفات حساب شخصي مؤهل. |
| [Google Slides API](https://developers.google.com/slides/api/limits) · [الحصول على الوصول](https://console.cloud.google.com/apis/library/slides.googleapis.com) | رمز حساب / OAuth | Reads: 3000/minute/project and 600/minute/user; writes: 600/minute/project and 60/minute/user; thumbnails lower | minute | مقيّد بشروط | مجانية القياسي ضمن الحصة؛ thumbnail reads300/minute/project و60/user؛ OAuth مطلوب؛ الفوترة فوق الحدود المعلنة خارج النطاق المجاني. |

<a id="science"></a>

## الأبحاث العلمية

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [AlphaFold Protein Structure Database](https://alphafold.ebi.ac.uk/api-docs) · [الحصول على الوصول](https://alphafold.ebi.ac.uk/) | بلا مفتاح | Freely available EMBL-EBI predicted-structure metadata API | continuous | مقيّد بشروط | قاعدة تنبؤات بروتينات وملفات بنية جاهزة؛ ليست خدمة تنفيذ AlphaFold على تسلسل مخصص مجانًا؛ راجع CC-BY ومؤشرات الثقة قبل الاستنتاج العلمي. |
| [arXiv legacy API](https://info.arxiv.org/help/api/tou.html) · [الحصول على الوصول](https://info.arxiv.org/help/api/user-manual.html) | بلا مفتاح | 1 request/3 seconds; one connection at a time | 3 seconds | مقيّد بشروط | metadata تحت CC0؛ المقالات لها تراخيص مستقلة؛ لا parallel requests ولا تجاوز rate limits. |
| [BioModels public read API](https://www.ebi.ac.uk/training/online/courses/biomodels-quick-tour/what-is-biomodels/) · [الحصول على الوصول](https://www.ebi.ac.uk/biomodels/docs/) | بلا مفتاح | Freely available EMBL-EBI public systems-biology model retrieval | continuous | مقيّد بشروط | نماذج علمية منشورة؛ القراءة العامة مجانية والكتابة/الإيداع مختلفة؛ استخدم format=json للمسارات الموثقة؛ ترخيص كل model يجب مراجعته. |
| [BioSamples public read API](https://www.ebi.ac.uk/biosamples/docs/references/api/overview.html) · [الحصول على الوصول](https://www.ebi.ac.uk/biosamples/) | بلا مفتاح | Freely available EMBL-EBI public sample metadata via REST/HAL | continuous | مقيّد بشروط | قراءة metadata العامة؛ كتابة البيانات وتعديلها تحتاجان مصادقة؛ اتبع روابط HAL بدل تخمين جميع المسارات؛ المعلومات ليست بيانات طبية فردية مفتوحة تلقائيًا. |
| [BioStudies public read API](https://www.ebi.ac.uk/biostudies/api/v1/search?query=cancer&pageSize=1) · [الحصول على الوصول](https://www.ebi.ac.uk/biostudies/) | بلا مفتاح | Freely available EMBL-EBI public study metadata and associated-file discovery | continuous | مقيّد بشروط | إثبات الوصول بمثال بحث عام والسياسة الرسمية؛ لا يشمل الدراسات الخاصة أوالمحتوى غير المرخص؛ الرفع يحتاج حسابًا؛ pages ليست طلبات مجانية جديدة. |
| [ChEMBL Web Services](https://www.ebi.ac.uk/training/online/courses/embl-ebi-programmatically/chembl-programmatically/) · [الحصول على الوصول](https://www.ebi.ac.uk/chembl/api/data/docs) | بلا مفتاح | Freely available EMBL-EBI bioactivity REST services; no numeric billing quota published | continuous | مقيّد بشروط | الوصول العام تحت سياسة EMBL-EBI المفتوحة؛ نتائج bioactivity للبحث وليست وصفة علاج؛ اتبع ترخيص البيانات وحمّل النسخ الكاملة عند الحاجة إلى bulk. |
| [Crossref REST API](https://www.crossref.org/documentation/retrieve-metadata/rest-api/) · [الحصول على الوصول](https://api.crossref.org/swagger-ui/index.html) | بلا مفتاح | Free metadata APIs; endpoint and pool rate limits apply | ongoing; response headers expose limits | مقيّد بشروط | استخدم mailto مع User-Agent للاستفادة من polite pool؛ تراخيص abstracts/full text قد تختلف عن metadata. |
| [EMBL-EBI Job Dispatcher and Dbfetch](https://www.ebi.ac.uk/Tools/webservices/) · [الحصول على الوصول](https://www.ebi.ac.uk/Tools/webservices/) | بلا مفتاح | Freely available REST sequence-analysis jobs and data retrieval, subject to fair-use concurrency limits | continuous | مقيّد بشروط | حزمة REST واحدة تشمل أدوات تحليل وتسليم jobs؛ بريد تعريف قد يلزم لتشغيل job؛ لا نعد كل أداة أوقاعدة endpoint خدمة جديدة؛ انتظر اكتمال jobs واحترم fair use. |
| [EMBL-EBI Proteins API](https://www.ebi.ac.uk/proteins/api/doc/) · [الحصول على الوصول](https://www.ebi.ac.uk/proteins/api/doc/) | بلا مفتاح | Freely available EMBL-EBI protein annotations and coordinates REST API | continuous | مقيّد بشروط | يضم annotations وvariation وproteomics في خدمة واحدة؛ لا يتطلب مفتاح قراءة؛ شروط البيانات المصدرية تبقى واجبة؛ استخدم أحجام طلبات معقولة. |
| [EMBL-EBI Search](https://www.ebi.ac.uk/training/online/courses/embl-ebi-programmatically/ebi-search-programmatically/) · [الحصول على الوصول](https://www.ebi.ac.uk/ebisearch/ws/rest/) | بلا مفتاح | Freely available federated biological-resource REST search service | continuous | مقيّد بشروط | البحث عبر موارد EBI المختلفة في صف واحد؛ الحقوق والتراخيص للمصادر الأصلية؛ لا يشمل تنزيل كل محتوى كل قاعدة بحرية غير محدودة؛ سياسة الموارد المفتوحة وfair use تنطبقان. |
| [Ensembl REST API](https://github.com/Ensembl/ensembl-rest/wiki/Rate-Limits) · [الحصول على الوصول](https://rest.ensembl.org/) | بلا مفتاح | Documented 15 requests/second; inspect X-RateLimit and Retry-After headers | second | مقيّد بشروط | بيانات الجينوم عامة ومجانية ضمن مشروع Ensembl/EMBL-EBI؛ الخادم قد يطلب فترة انتظار أطول؛ بيانات الأنواع/releases تختلف؛ لا تتجاوز 429 بتعدد الهويات. |
| [Europe PMC public API](https://www.ebi.ac.uk/training/online/courses/embl-ebi-programmatically/europe-pmc-programmatically/) · [الحصول على الوصول](https://europepmc.org/RestfulWebService) | بلا مفتاح | Freely available EMBL-EBI literature-search REST services | continuous | مقيّد بشروط | بيانات الأبحاث والبحث؛ النص الكامل متاح فقط ضمن ترخيص كل مقالة؛ كون metadata مجانية لا يجعل كل PDF مفتوحًا. |
| [European Nucleotide Archive public API](https://www.ebi.ac.uk/ena/browser/api/xml/ERP000001) · [الحصول على الوصول](https://www.ebi.ac.uk/ena/browser/api) | بلا مفتاح | Freely available EMBL-EBI public sequence/archive metadata APIs | continuous | مقيّد بشروط | قراءة سجلات عامة لا إيداع بيانات؛ تنزيل sequence files الكبيرة له آليات archive/FTP منفصلة؛ التسجيلات المحكومة أوغير المنشورة ليست ضمن المجاني العام. |
| [GWAS Catalog REST v2](https://www.ebi.ac.uk/gwas/docs/api) · [الحصول على الوصول](https://www.ebi.ac.uk/gwas/rest/api/v2/docs) | بلا مفتاح | Freely available EMBL-EBI curated GWAS API; public read access | continuous | مقيّد بشروط | الإصدار v2 هو الحالي؛ بعض full summary statistics لها قيود مصدر منفصلة؛ النتائج ارتباطات بحثية وليست تشخيصًا؛ لا يُعد كل resource خدمة إضافية. |
| [InterPro REST API](https://www.ebi.ac.uk/training/online/courses/embl-ebi-programmatically/interpro-programmatically/) · [الحصول على الوصول](https://www.ebi.ac.uk/interpro/api/) | بلا مفتاح | Freely available EMBL-EBI protein classification API; fair use applies | continuous | مقيّد بشروط | تصنيف البروتينات وdomains؛ استخدم pagination والتخزين المؤقت؛ سياسة المجانية العامة لا تضمن سرعة أوعددًا غير محدود من الاستعلامات. |
| [MGnify API](https://www.ebi.ac.uk/training/online/courses/embl-ebi-programmatically/mgnify-programmatically/) · [الحصول على الوصول](https://www.ebi.ac.uk/metagenomics/api/v1/) | بلا مفتاح | Freely available EMBL-EBI public microbiome-data API | continuous | مقيّد بشروط | القراءة لمجموعات الدراسات العامة فقط؛ البيانات الخاصة/قبل النشر لها شروط مختلفة؛ لا تُقرأ حصة مالية من عدد الدراسات. |
| [Ontology Lookup Service 4](https://www.ebi.ac.uk/ols4/api/) · [الحصول على الوصول](https://www.ebi.ac.uk/ols4/help) | بلا مفتاح | Freely available EMBL-EBI public ontology-search REST API | continuous | مقيّد بشروط | الوصول موثق برد API عام وسياسة الموارد المفتوحة؛ تراخيص الأنطولوجيات المختلفة تبقى واجبة؛ حافظ على pagination وحدود الاستعلام المعقولة. |
| [Open Targets Platform GraphQL](https://www.ebi.ac.uk/training/online/courses/embl-ebi-programmatically/open-targets-programmatically/) · [الحصول على الوصول](https://platform-docs.opentargets.org/data-access/graphql-api) | بلا مفتاح | Freely available hosted target/disease evidence GraphQL API | continuous | مقيّد بشروط | موارد علنية لتحديد أهداف بحثية؛ للاستعلامات المعقدة استخدم downloads؛ بيانات الأدلة ليست توصيات علاج؛ حق كل مصدر وتوثيق إصداره مهمان. |
| [OpenAlex](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication) · [الحصول على الوصول](https://openalex.org/settings/api) | شخصي أو بلا مفتاح | Free daily budget; key gives 10x keyless budget; 10 RPS without key, 30 RPS with free key | day/second | مقيّد بشروط | ميزانية يومية تختلف بتكلفة query؛ الرقم النقدي الحالي لم يثبت من الصفحة لذا لم يُخمن؛ الدفع للتوسع اختياري. |
| [PDBe public APIs](https://www.ebi.ac.uk/pdbe/api/pdb/entry/summary/1cbs) · [الحصول على الوصول](https://www.ebi.ac.uk/pdbe/api/doc/) | بلا مفتاح | Freely available EMBL-EBI structure metadata REST services | continuous | مقيّد بشروط | مزود خدمة مستقل عن RCSB مع قاعدة PDB مشتركة؛ صف واحد لجميع طرق PDBe؛ التراخيص الخاصة بالتعليقات الخارجية ومراعاة السعة واجبة. |
| [PubChem PUG REST](https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest) · [الحصول على الوصول](https://pubchem.ncbi.nlm.nih.gov/) | بلا مفتاح | At most 5 requests/second per user/application/organization; dynamic throttling also applies | second | مقيّد بشروط | معلومات كيميائية عامة مجانية؛ لا API key أوwhitelist لتجاوز الحدود. throttling ديناميكي و503 عند ضغط السعة؛ حقوق المصادر المدمجة قد تختلف. |
| [QuickGO](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0008150) · [الحصول على الوصول](https://www.ebi.ac.uk/QuickGO/api/index.html) | بلا مفتاح | Freely available EMBL-EBI Gene Ontology and annotation REST services | continuous | مقيّد بشروط | Terms/annotations في خدمة واحدة؛ الأدلة البيولوجية بحثية؛ بيانات GO والمصادر لها شروط نسب منفصلة؛ لا نسمي عدد annotations حصة طلبات. |
| [RCSB Protein Data Bank Data API](https://data.rcsb.org/) · [الحصول على الوصول](https://www.rcsb.org/pages/policies) | بلا مفتاح | Public structure-data REST/GraphQL API; PDB archive/API data generally CC0 | continuous | مقيّد بشروط | المصادر الخارجية المدمجة قد تحمل ترخيصًا مختلفًا؛ لا تعمم CC0 على كل annotation؛ استخدم البحث/الأرشيف للعمليات الكبيرة بدل آلاف الاستعلامات الفردية. |
| [Reactome Content Service](https://reactome.org/ContentService/) · [الحصول على الوصول](https://reactome.org/license) | بلا مفتاح | Public pathway-data REST service; CC-BY 4.0-designated content | continuous | مقيّد بشروط | مسارات بيولوجية؛ ترخيص المحتوى CC-BY منفصل عن تراخيص software/dependencies؛ انسب المصدر وأشر إلى التعديلات؛ endpoint العام ليس SLA. |
| [Research Organization Registry](https://ror.org/about/faqs/) · [الحصول على الوصول](https://ror.org/) | بلا مفتاح | Public-domain organization IDs and metadata; access and services carry no charge | continuous | مسموح بشروط البيانات | معرّفات ومعلومات المؤسسات البحثية عامة ولا تتطلب membership. تحقق من حدود API اللحظية واستخدم dump للعمليات الكبيرة؛ ليست بيانات أفراد. |
| [UniChem](https://www.ebi.ac.uk/training/online/courses/embl-ebi-programmatically/chembl-programmatically/) · [الحصول على الوصول](https://www.ebi.ac.uk/unichem/) | بلا مفتاح | Freely available EMBL-EBI chemical cross-reference services; no numeric billing quota published | continuous | مقيّد بشروط | خدمة مطابقة المعرّفات الكيميائية منفصلة عن قاعدة ChEMBL؛ شروط المصادر الخارجية واجبة؛ ليست حصة مستقلة لكل database mapping. |

<a id="search"></a>

## البحث واستخراج المحتوى

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [Abstract Web Scraping](https://www.abstractapi.com/api/web-scraping-api) · [الحصول على الوصول](https://app.abstractapi.com/users/signup) | مفتاح شخصي | 1000 requests/month; 1 request/second | month/second | مقيّد بشروط | جلب المحتوى ضمن حصةFree فقط؛ لا إذن لتجاوز حماية المواقع أوشروطها. rendering والخصائص تعتمد الخطة؛ حقوق إعادة النشر ليست مضمونة. |
| [Algolia Build](https://www.algolia.com/pricing) · [الحصول على الوصول](https://dashboard.algolia.com/users/sign_up) | مفتاح شخصي | 10000 search requests/month; 5000 recommendation requests/month; 50000 records | month | تطوير/تعليم/تقييم فقط | اختر Build المجانية؛ Grow قد يحتسب overages؛ لا تنشر admin key؛ عدد records ثابت وليس رصيدًا يتراكم كل شهر. |
| [Brave Search API](https://www.brave.com/search/api/) · [الحصول على الوصول](https://api-dashboard.search.brave.com/) | مفتاح شخصي | 5 USD credits/month; Search priced at 5 USD/1000 requests within the documented plan | month | مقيّد بشروط | البطاقة مطلوبة للتحقق من الهوية؛ رصيد شهري وليس ضمان كل أنواع البحث مجانًا؛ Search وAnswers يختلفان في التكلفة؛ راقب الفوترة بعد استهلاك الرصيد. |
| [Exa Starter](https://www.exa.ai/pricing) · [الحصول على الوصول](https://dashboard.exa.ai/) | مفتاح شخصي | 10 USD API credits/month; 10 search QPS; 50 agent concurrency | month/second | غير محسوم من المصدر | المقبول هو الرصيد الشهري المتجدد؛ مكافأة onboarding بقيمة 10 دولارات رصيد إضافي لمرة واحدة ولا تدخل الحصة؛ التكلفة تختلف حسب endpoint. |
| [Google Indexing API](https://developers.google.com/search/apis/indexing-api/v3/quota-pricing) · [الحصول على الوصول](https://developers.google.com/search/apis/indexing-api/v3/prereqs) | رمز حساب / OAuth | Default 200 publish requests/day/project for initial onboarding/testing; other request quotas separate | day; midnight Pacific | مقيّد بشروط | الخدمة مجانية؛ مخصصة JobPosting وBroadcastEvent ضمنVideoObject؛ الاستخدام الأوسع والموافقة علىquota يراجعان؛ ليست وسيلة فهرسة أي صفحة عشوائية. |
| [Google Search Console API](https://developers.google.com/webmaster-tools/pricing) · [الحصول على الوصول](https://developers.google.com/webmaster-tools/v1/how-tos/authorizing) | رمز حساب / OAuth | Free API with method-specific QPS/QPM/QPD plus load quotas; URL inspection quotas are separate | second/minute/day | مقيّد بشروط | كل الاستخدام مجاني حسب صفحة السعر؛ إثبات ملكية الموقع مطلوب؛ ليست محرك بحث عام على الإنترنت؛ بيانات Search Analytics وURLInspection تختلف في الحدود. |
| [Jina Reader without API key](https://jina.ai/reader/) · [الحصول على الوصول](https://jina.ai/reader/) | بلا مفتاح | 20 requests/minute for keyless Reader | minute | غير محسوم من المصدر | المسار المجاني هو Reader بلا مفتاح فقط؛ رصيد المفتاح الجديد 10M tokens لمرة واحدة ليس ضمن القائمة؛ خدمة البحث s.jina.ai ليست مشمولة. |
| [Microlink Free](https://microlink.io/pricing) · [الحصول على الوصول](https://microlink.io/) | مفتاح شخصي | 100 requests/month | month | غير محسوم من المصدر | الخطة الحالية100 شهريًا؛ لا تستخدم50 يوميًاالقديمة منالقوائم؛ screenshot/PDF/metadata وطرقأخرى تشتركفيالحصة؛ خصائصالإنتاجالمدفوعةخارجالنطاق. |
| [SerpApi Free](https://serpapi.com/pricing) · [الحصول على الوصول](https://serpapi.com/users/sign_up) | مفتاح شخصي | 250 successful searches/month; 50 successful searches/hour | month/hour | غير محسوم من المصدر | حد الساعة throughput؛ لا يحول الطلب الواحد إلى عدد نتائج غير محدود؛ لا تشمل الحماية والدعم خصائص جميع الخطط الأعلى. |
| [serpstack](https://serpstack.com/product) · [الحصول على الوصول](https://serpstack.com/signup/free) | مفتاح شخصي | 100 searches/month | month | غير تجاري فقط | Free forever؛ JSON فقط؛ لا تفترض أن عدد المواقع المستخرجة يساوي search requests. |
| [Tavily](https://www.tavily.com/pricing) · [الحصول على الوصول](https://app.tavily.com/) | مفتاح شخصي | 1000 API credits/month | month | غير محسوم من المصدر | عدد credits يختلف حسب endpoint ونمط البحث؛ لا تفعّل الدفع حسب الاستخدام للحصول على المزيد. |

<a id="security"></a>

## الأمن

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [AbuseIPDB](https://www.abuseipdb.com/pricing) · [الحصول على الوصول](https://www.abuseipdb.com/register) | مفتاح شخصي | 1000 IP checks/reports/day; 100 block checks/day; 5 bulk reports/day | day | مقيّد بشروط | Individual Free forever؛ blacklist حتى 10000 IP وقيود يومية؛ لا تنسب حدود تجربة الخطة المدفوعة للمجاني. |
| [Cloudflare Turnstile](https://developers.cloudflare.com/turnstile/plans/) · [الحصول على الوصول](https://dash.cloudflare.com/) | مفتاح شخصي | Free plan challenge-validation service; widget/hostname configuration limits apply | continuous | مسموح بشروط البيانات | Sitekey عامة لكنsecretkey خاصة؛ المجاني مناسب للإنتاج أيضًا؛ BotManagement/fingerprintingEnterprise منتجات مدفوعة مختلفة؛ تحقق server-side ولا تنشرsecret. |
| [hCaptcha Basic](https://www.hcaptcha.com/pricing) · [الحصول على الوصول](https://dashboard.hcaptcha.com/signup) | مفتاح شخصي | Basic plan at 0 USD; challenge/siteverify API subject to provider policies | continuous | مقيّد بشروط | المجانيBasic فقط؛100kmonthlyevals المذكورة فيPro المدفوعة ليست حصةBasic؛ Sitekey عامة وsecretkey خاصة؛ لا ننسب passiveEnterprise للمجاني. |
| [MalwareBazaar Community API](https://bazaar.abuse.ch/api/) · [الحصول على الوصول](https://auth.abuse.ch/) | مفتاح شخصي | Free community intelligence queries subject to fair use | continuous | مقيّد بشروط | Auth-Key مجاني مطلوب؛ التجاري قد يحتاج اشتراكًا. تستخدم queries للhash/metadata؛ لم تُنزّل عينات ضارة خلال البحث؛ fair use واجب. |
| [ThreatFox Community API](https://threatfox.abuse.ch/api/) · [الحصول على الوصول](https://auth.abuse.ch/) | مفتاح شخصي | Free community IOC API subject to fair use | continuous | مقيّد بشروط | Auth-Key مجاني مطلوب؛ IOCs القديمة قد تصبح expired. التجاري قد يحتاج enhanced API؛ لا يُعرض الوصول كحصة لا نهائية مضمونة. |
| [URLhaus Community API](https://urlhaus.abuse.ch/api/) · [الحصول على الوصول](https://auth.abuse.ch/) | مفتاح شخصي | Free community API subject to fair use; no unified numeric free ceiling published | continuous | مقيّد بشروط | Auth-Key مجاني مطلوب. الاستخدام التجاري أوfor-profit قد يحتاج enhanced API مدفوعًا؛ نطاق المجتمع يخضع fair use. لا يلزم تحميل عينات malware للاستعلام عن metadata. |
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
| [Abstract Company Enrichment](https://www.abstractapi.com/api/company-enrichment-api) · [الحصول على الوصول](https://app.abstractapi.com/users/signup) | مفتاح شخصي | 100 requests/month; 1 request/second | month/second | غير محسوم من المصدر | منتج إثراء شركات ذو حصة مستقلة. البيانات والحقول تختلف بالخطة؛ راجع الحقوق قبل الاستخدام التجاري؛ المفتاح خاص بحسابك. |
| [Abstract Email Validation](https://www.abstractapi.com/pricing) · [الحصول على الوصول](https://www.abstractapi.com/api/email-verification-validation-api) | مفتاح شخصي | 100 requests/month; 3 requests/second | month/second | غير محسوم من المصدر | حصة مستقلة لمنتج Email؛ اختَر الخطة المجانية؛ نتائج التحقق تقديرية وليست ضمان تسليم. |
| [Abstract IBAN Validation](https://www.abstractapi.com/api/iban-validation-api) · [الحصول على الوصول](https://app.abstractapi.com/users/signup) | مفتاح شخصي | 100 requests/month; 1 request/second | month/second | غير محسوم من المصدر | فحص بنيةIBAN ومعلومات البنك لا يثبت ملكية الحساب أوالرصيد. حصة المنتج ومفتاحه مستقلان؛ حقوق البيانات وشروطFree واجبة. |
| [Abstract Phone Validation](https://www.abstractapi.com/pricing) · [الحصول على الوصول](https://www.abstractapi.com/api/phone-validation-api) | مفتاح شخصي | 100 requests/month | month | غير محسوم من المصدر | حصة مستقلة لمنتج Phone؛ لا يساوي توفر metadata إثبات امتلاك الرقم ولا إرسال SMS مجانيًا. |
| [Abstract VAT Validation and Rates](https://www.abstractapi.com/api/vat-validation-rates-api) · [الحصول على الوصول](https://app.abstractapi.com/users/signup) | مفتاح شخصي | 100 requests/month; 1 request/second | month/second | غير محسوم من المصدر | تحققVAT ضمن حصةFree؛ لا يمثل استشارة ضريبية. حدود الميزات وحقوق الاستخدام التجاري يجب مراجعتها؛ لا نفترض ترخيصًا عامًا. |
| [Demografix name APIs bundle](https://agify.io/pricing) · [الحصول على الوصول](https://agify.io/) | مفتاح شخصي | 1000 names/month shared across Agify, Genderize and Nationalize | month | تطوير/تعليم/تقييم فقط | Agify وGenderize وNationalize في حزمة واحدة ذات حصة مشتركة. تقديرات الاسم احتمالية وليست إثباتًا لهوية أوعمر أوجنسية. المجاني للتقييم والنماذج الأولية؛ لا نعدها ثلاث مفاتيح منفصلة. |
| [Hunter Free](https://www.hunter.io/pricing) · [الحصول على الوصول](https://hunter.io/users/sign_up) | مفتاح شخصي | 50 credits/month; finding an email costs 1 credit; verification costs 0.5 credit | month | مقيّد بشروط | 50 credits تتجدد شهريًا ولا تتراكم. العثور على بريد=1 credit والتحقق=0.5؛ الوصول API داخل الخطة يتقيد بحدود وحقوق البيانات. |
| [mailboxlayer](https://mailboxlayer.com/product) · [الحصول على الوصول](https://mailboxlayer.com/signup/free) | مفتاح شخصي | 100 API requests/month | month | غير تجاري فقط | تقييم جودة البريد فقط؛ لا bulk endpoint بالمجاني؛ راجع تفعيل HTTPS والشروط من لوحة الحساب. |
| [numverify](https://numverify.com/product) · [الحصول على الوصول](https://numverify.com/signup/free) | مفتاح شخصي | 100 requests/month; free without time limit | month | غير تجاري فقط | خطة Free موصوفة trial without time limit لكنها حصة شهرية مستمرة؛ تحقق من دعم HTTPS في الحساب لأن جدول الميزات والFAQ لا يتطابقان دائمًا. |
| [userstack](https://userstack.com/product) · [الحصول على الوصول](https://userstack.com/signup/free) | مفتاح شخصي | 100 lookups/month | month | غير تجاري فقط | جدول Free الحالي 100؛ FAQ أقدم يذكر 10000، استخدمت الرقم الأقل من جدول السعر الحالي؛ لا bulk بالمجاني. |
| [Verifalia Free](https://www.verifalia.com/pricing) · [الحصول على الوصول](https://verifalia.com/sign-up) | رمز حساب / OAuth | 25 daily email-verification credits; 1 standard verification = 1 credit | day | مقيّد بشروط | جودة التحقق الأعلى تستهلك أكثر؛ يستهلك credits اليومية قبل المدفوعة؛ لا تعامل25 كعدد ثابت لكل نوع تحقق. |

<a id="weather"></a>

## الطقس

| الخدمة | الوصول | الحصة المجانية | التجديد | الاستخدام | القيود |
|---|---|---|---|---|---|
| [MET Norway weather APIs](https://sisyphos.api.met.no/) · [الحصول على الوصول](https://api.met.no/doc/GettingStarted) | بلا مفتاح | Free public weather APIs with fair-use, caching and identifying User-Agent requirements | continuous | مقيّد بشروط | بيانات مجانية مع CC-BY ونسب المصدر وUser-Agent والتخزين المؤقت. أكثر من20 طلبًا/ثانية لكل التطبيق يحتاج اتفاقًا خاصًا؛ لا SLA. منتجات الطقس endpoints في صف واحد. |
| [Meteosource Free](https://www.meteosource.com/pricing) · [الحصول على الوصول](https://www.meteosource.com/client/sign-up) | مفتاح شخصي | 400 calls/day | day | مقيّد بشروط | Free منفصل عن trial10 أيام للمدفوع؛ ذكر المصدر وbacklink مطلوبان؛ تغطية forecast/weather variables تختلف حسب الخطة؛ راجع شروط الاستخدام. |
| [National Weather Service](https://www.weather.gov/documentation/services-web-api) · [الحصول على الوصول](https://www.weather.gov/documentation/services-web-api) | بلا مفتاح | Free public data; reasonable unpublished rate limits | ongoing; throttle clears after waiting | مسموح بشروط البيانات | يلزم User-Agent واضح؛ الخدمة تخص الولايات المتحدة؛ عدم نشر حد رقمي لا يعني عدم وجود throttling. |
| [Open-Meteo](https://open-meteo.com/en/pricing) · [الحصول على الوصول](https://open-meteo.com/en/docs) | بلا مفتاح | 600 calls/minute; 5000/hour; 10000/day; 300000/month | minute/hour/day/month | غير تجاري فقط | الاستخدام غير التجاري؛ لا مفتاح للمسار المفتوح؛ الحصة مشتركة مع APIs المفتوحة للمزود؛ الترخيص التجاري مدفوع. |
| [OpenWeather Free APIs](https://openweathermap.org/price) · [الحصول على الوصول](https://home.openweathermap.org/users/sign_up) | مفتاح شخصي | 60 calls/minute; 1000000 calls/month | minute/month | مقيّد بشروط | اختر Free Weather API access؛ يشمل الطقس الحالي وتوقع 5 أيام والتلوث والخرائط والترميز الجغرافي؛ One Call المدفوع منفصل ومستبعد هنا. |
| [Stormglass Free](https://www.stormglass.io/pricing/) · [الحصول على الوصول](https://dashboard.stormglass.io/) | مفتاح شخصي | 10 requests/day | day | غير تجاري فقط | الخطة0يورو شهريًا ومتجددة يوميًا؛ ليست للتجاري؛ جميع weather parameters وفق الجدول لكن قيود المنطقة/الفترة endpoint-specific؛ لا دعم مجاني. |
| [Sunrise-Sunset.org](https://sunrise-sunset.org/api) · [الحصول على الوصول](https://sunrise-sunset.org/api) | بلا مفتاح | Free GET API with no signup/key; no numeric daily/monthly billing ceiling published | continuous | مقيّد بشروط | رابط attribution ظاهر مطلوب. v2 هو المثال الحالي، وv1 قديم مدعوم؛ المنطقة الزمنية وهيكل النتائج يختلفان بالإصدار. لا تحتاج تسجيلًا أومفتاحًا. |
| [Visual Crossing](https://www.visualcrossing.com/weather-api/) · [الحصول على الوصول](https://www.visualcrossing.com/sign-up) | مفتاح شخصي | 1000 weather records/day | day | غير محسوم من المصدر | الحصة records وليست requests؛ الطلب التاريخي متعدد الأيام قد يستهلك أكثر من سجل؛ تجنب تفعيل الاستخدام المدفوع. |
| [WeatherAPI.com](https://www.weatherapi.com/pricing.aspx) · [الحصول على الوصول](https://www.weatherapi.com/signup.aspx) | مفتاح شخصي | 100000 calls/month | month; first day 00:00 UTC | مسموح بشروط البيانات | الخصائص والمدة التاريخية تختلف عن المدفوع؛ عند نفاد الحصة يتوقف الرد حتى التجديد أو الترقية. |
| [Weatherbit](https://www.weatherbit.io/pricing) · [الحصول على الوصول](https://www.weatherbit.io/account/create) | مفتاح شخصي | 50 requests/day; 1 request/second | day/second | غير تجاري فقط | خطة always-free مختلفة عن تجربة Business لمدة 21 يومًا؛ للاستخدام غير التجاري؛ الطقس الحالي وتوقع يومي 7 أيام. |
| [weatherstack](https://www.weatherstack.com/product) · [الحصول على الوصول](https://weatherstack.com/signup/free) | مفتاح شخصي | 100 API calls/month | month | غير تجاري فقط | Free forever مثبت؛ الطقس الحالي فقط؛ forecast/history والميزات التجارية ليست مجانية ضمن هذه الخطة. |

## الصيانة والمساهمة

لتغيير صف، حدّث JSON وCSV والدليل ومصدرًا رسميًا وتاريخ المراجعة. [قواعد المساهمة](CONTRIBUTING.md). فحص CI يراجع التكرار والحقول واتساق النسخ وعدم تسريب أسرار؛ لا يثبت السعر تلقائيًا ولا يسجل حسابات.

توثيق المجانية مختلف عن فحص استجابة endpoint. أمثلة [smoke-test](research/smoke-tests.json) قليلة وخالية من مفاتيح شخصية؛ لم تختبر كل الخدمات ولا الاستحقاق الجغرافي لكل مستخدم.

الكتالوج والكتابة الأصلية تحت [CC0](LICENSE). المحتوى وAPIs وشروط المزودين ليست ضمن هذا الترخيص. قد تتغير الحصص بعد تاريخ المراجعة.
