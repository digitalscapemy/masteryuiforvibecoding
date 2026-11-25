# Cloudflare Gatekeeper for Vibe Coders

Draf content v4.1 · 25 Nov 2026 · @Mykel · fakta disemak dengan docs rasmi 25 Nov 2026 (✅ = disahkan, **[semak]** = perlu dry run)

**Fokus kelas:** domain, proxy, keselamatan dan R2 cloud storage.
**Bukan fokus:** host app di Cloudflare (Pages, Workers). App kekal di tempat asal (VPS + EasyPanel, atau mana-mana host). Cloudflare berdiri **di depan** app tu.

**Struktur:** 10 bahagian · 18 skrin. Penomboran ikut gaya Super Stack: **NN** = slide utama, **NNA, NNB…** = slide susulan. Setiap slide susulan tambah satu idea baru.

**Contoh sepanjang kelas** (sama dengan Super Stack):
- Domain `sitiscakes.com` (Siti's Cake Shop)
- IP server `203.0.113.10`
- Domain dibeli di registrar tempatan (syarikat jual domain .my)
- App di VPS + EasyPanel

**Audiens bercampur.** Setiap slide ada 2 lapis:
- **Teks utama**: bahasa mudah dengan analogi
- **Pro note**: 2–3 ayat tepat untuk developer pro. Beginner boleh langkau.

**Hubungan dengan kelas lain:**
- **Super Stack** = peta. 16 ajar Domain, DNS, A/CNAME/MX; 16A ajar SSL dan "Cloudflare = CDN + DDoS + SSL"; 17C ajar "point the domain via Cloudflare". Kelas ini = *setting sebenar, kenapa rosak, macam mana betulkan*.
- **GitHub Power Skills** = code sampai Live. `.env` dan secrets dah diajar (03B), dan Super Stack 14A pun cover. Di sini cukup rujuk satu ayat.

Tanda dalam draf:
- **Hook kelas lain** = rujukan ke kelas sebelum ni
- **Pro note** = ayat untuk developer pro
- **[semak]** = perlu sahkan masa dry run

---

## START HERE

### 01 · Cover
**Cloudflare Gatekeeper for Vibe Coders**
Your domain, your gate, your storage.

**Visual:** Full-screen cover artwork `slides/assets/cover.webp` (glowing "Cloudflare Gatekeeper for Vibe Coders" panel with a shield and lock). Fades in with a slow push-in, same as the GitHub deck cover.

### 02 · Class Agenda
**Hook:** Four stops on the road from sitiscakes.com to your server.

- **Part 1 · Domain & DNS:** 03 Rent it, lock it · 04 Nameservers · 04A Demo
- **Part 2 · Proxy & SSL:** 05 The orange cloud · 05A SSL modes · 05B Cache & purge
- **Part 3 · Security:** 06 Free security guard · 06A WAF & rate limiting · 06B Turnstile · 06C Lock the back door · 06D Secure your account
- **Part 4 · R2 Cloud Storage:** 07 R2 · 07A Public or private files · 07B Backups
- Start with 02A, finish with 08 (checklist). Every lesson is a button that jumps to that slide.

**Visual:** One orange road with 4 numbered stations and a finish flag. Each station drops a card listing its lessons.

### 02A · Cloudflare Stands in Front, Not Instead
**Hook:** Your app stays on your server. Cloudflare guards the road to it.

- **Your app stays where it is:** VPS + EasyPanel (Super Stack), or any host.
- **Cloudflare sits in front:** every visitor passes through it first.
- **Stays on your server:** code, database, EasyPanel, `.env` secrets
- **Moves to Cloudflare:** DNS, SSL / https, cache, security rules
- **New, also on Cloudflare:** R2 cloud storage for uploads and backups

**Visual:** Reuse the Super Stack 03 flow (Frontend → Backend → Database → Server → Domain). An orange cloud slides in between Domain and Server. An R2 warehouse docks beside the server.

**Hook kelas lain:** "Super Stack 16A told you what Cloudflare is. Today you set it up yourself."

**Pro note:** We use Cloudflare as a reverse proxy, DNS and storage, not as a hosting platform. Pages and Workers are out of scope.

---

## PART 1 · Domain & DNS

### 03 · Your Domain: Rent It, Lock It
**Hook:** One morning sitiscakes.com shows someone else's page. The renewal email went to spam.

- **You rent it every year.** Turn on auto-renew, and use an email you actually read.
- **Lock it:**
  - turn on **2FA** on the registrar account
  - turn on **Registrar Lock** (blocks transfers)
- **Where to buy:** Cloudflare Registrar sells at cost, but not every extension. `.my` and `.com.my` are bought at a local registrar, then connected to Cloudflare.
- **Subdomains are free:** `app.sitiscakes.com`, `files.sitiscakes.com`, `admin.sitiscakes.com`.

**Prompt for AI:** "I own sitiscakes.com. Suggest a subdomain plan for my shop, admin panel, API and file storage."

💡 Auto-renew on. 2FA on. Lock on.

**Visual:** A calendar with the renewal date circled and an "auto-renew ON" toggle, then a padlock snapping onto a domain card.

**Pro note:** Most domain hijacks start with a stolen registrar login, not a technical hack. At your registrar, Registrar Lock changes the domain status to `DomainTransferProhibited`; it blocks transfers, not DNS changes. Domains on Cloudflare Registrar must use Cloudflare nameservers, so it suits people who want everything in one place.

> ✅ Disahkan 25 Nov: `.my` / `.com.my` tiada dalam senarai TLD Cloudflare Registrar. Nama setting biasa di registrar: **Registrar Lock**.

### 04 · Nameservers: Who Holds the Phonebook
**Hook:** You added the A record in Cloudflare. Nothing happens. The internet is still reading the phonebook at your registrar.

- **Quick recap (Super Stack 16):** A → IP, CNAME → another name, MX → mail server.
- **Nameservers decide who holds the phonebook.** Only one place is in charge. If they point to your registrar, records you add in Cloudflare are ignored.
- **TXT records:** notes that prove you own the domain and protect your email (SPF, DKIM). Delete them by mistake and email starts going to spam.
- **Changes take time:** from minutes up to 48 hours. Do not keep changing things while you wait.

**Prompt for AI:** "Here are my DNS records [paste]. Which are for my website and which are for email? What must I keep when I move to Cloudflare?"

💡 Records say where. Nameservers say who.

**Visual:** Two phonebooks. The registrar's one is greyed out; Cloudflare is highlighted. One arrow from "the internet" points to Cloudflare. Inside it, two tabs: Web (A, CNAME) and Email (MX, TXT).

**Pro note:** "Propagation" is really caching. Resolvers keep old answers until the TTL runs out, and a nameserver change waits on the TLD's TTL. Check with `dig sitiscakes.com NS +short` or `nslookup`. A CNAME cannot sit on the root in standard DNS; Cloudflare allows it through CNAME flattening.

### 04A · Demo: registrar → Cloudflare
**Hook:** Two settings connect everything.

- **Nameservers, set at your registrar:** "Cloudflare holds my phonebook now."
- **A record, set at Cloudflare:** "My app lives at 203.0.113.10."

**Demo steps:**
1. In Cloudflare, add sitiscakes.com and choose the Free plan.
2. Cloudflare scans your records. Keep MX and TXT. Delete old A records that point to your old hosting.
3. Copy the two Cloudflare nameservers.
4. At your registrar, open the domain. If **DNSSEC/DS Records** has an entry, remove it first.
5. Left menu **Nameservers** → "Use custom nameservers" → paste both → save.
6. Wait (Cloudflare says up to 24 hours). Cloudflare emails you and the domain shows **Active**.
7. Cloudflare DNS: A `@` → 203.0.113.10 (orange cloud). CNAME `www` → sitiscakes.com.
8. Open sitiscakes.com in the browser.

**Prompt for AI:** "My domain is at [registrar] and my app runs on a VPS at [IP]. Walk me through moving it to Cloudflare, one step at a time. Remind me about DNSSEC and email records."

💡 Nameservers point to Cloudflare. The A record points to your server.

**Visual:** registrar → Cloudflare → VPS (203.0.113.10). Arrow 1: "nameservers, set at the registrar". Arrow 2: "A record, set at Cloudflare". Stickers: "DNSSEC off first" and "keep MX & TXT".

**Pro note:** The record scan is a best guess, so compare it with an export of the old zone. After the zone is Active, turn DNSSEC back on from Cloudflare (that comes in 06D).

Nama menu registrar dan Cloudflare berubah dari masa ke masa. Buat dry run sebelum kelas.

> ✅ Disahkan 25 Nov dalam browser (artikel sokongan registrar .MY): laluan Domains → My Domains → ⋯ → Manage Domain, menu Nameservers ("Use custom nameservers (enter below)"), Registrar Lock dan DNSSEC/DS Records. Artikel MY tak suruh matikan Registrar Lock untuk tukar nameserver (sesetengah registrar suruh matikan dulu). **[semak]** Pastikan masa dry run.

---

## PART 2 · Proxy & SSL

### 05 · The Orange Cloud
**Hook:** Every DNS record has a small cloud. Orange or grey. It decides whether Cloudflare protects you at all.

- **Orange (Proxied):** visitors reach Cloudflare first. They see Cloudflare's IP, not yours. SSL, cache and security rules work.
- **Grey (DNS only):** visitors go straight to your server. Your IP is visible, and nothing in Parts 2–3 applies.
- **The rule:**
  - orange for your website, app and API
  - grey for mail servers (e.g. `mail.sitiscakes.com`), SSH and anything that is not web traffic
  - MX records have no cloud at all
- **Hiding your IP only works if you hide it everywhere.** One grey record on the same IP gives it away.

**Prompt for AI:** "Here are my Cloudflare DNS records [paste]. Which should be orange and which grey? Do any of them leak my server's real IP?"

💡 Orange = protected. Grey = exposed.

**Visual:** Two lanes from a visitor to the server. Top lane goes through an orange cloud with a shield; the server IP is blurred. Bottom lane runs straight under a grey cloud; the IP 203.0.113.10 is in big letters.

**Pro note:** Orange cloud only proxies HTTP on ports 80, 8080, 8880, 2052, 2082, 2086, 2095 and HTTPS on 443, 2053, 2083, 2087, 2096, 8443. SSH (22) and other traffic need grey cloud or Spectrum. Old IPs stay findable in DNS history sites, so a server that was public before Cloudflare is not truly hidden until you lock it down (06C).

### 05A · SSL Modes: The Setting That Breaks Sites
**Hook:** You turned on the orange cloud. Now the site says "too many redirects".

- **Flexible:** visitor → Cloudflare uses https, Cloudflare → server uses plain http. If your server also forces https, they keep redirecting each other. Avoid.
- **Full (strict):** https all the way, and Cloudflare checks your server's certificate. Use this.
- **Your server needs a valid certificate:**
  - EasyPanel's Let's Encrypt certificate, or
  - a free **Cloudflare Origin Certificate**
- **Turn on two settings too:**
  - **Always Use HTTPS:** http visitors are sent to https
  - **Minimum TLS Version 1.2:** blocks old, weak connections (the default is 1.0)

**Prompt for AI:** "My site shows 'too many redirects' after I turned on Cloudflare. My app runs on EasyPanel. Check my SSL mode and tell me exactly what to change to use Full (strict)."

💡 SSL mode: Full (strict). Never Flexible.

**Visual:** Two roads. Full (strict): padlock on both halves. Flexible: padlock on the first half only, then a loop arrow labelled "too many redirects".

**Hook kelas lain:** "Super Stack 16A: SSL gives you the padlock. Here is the one setting that decides whether it really protects you."

**Pro note:**
- New zones default to **Automatic SSL/TLS**, which picks the strongest mode your origin supports. Set Full (strict) yourself so you know what is running.
- An Origin CA certificate works only while the record is orange. Pause Cloudflare or switch to grey, and visitors see certificate errors.
- Cloudflare recommends TLS 1.3 as the minimum when all your users have modern browsers; 1.2 is the safe, compatible choice.
- **HSTS** is stronger still, but browsers remember it for the whole max-age. If https breaks during that time, the site cannot be opened. Enable it last, after everything works.

> ✅ Disahkan 25 Nov: docs EasyPanel kata orange cloud boleh, dengan mod SSL "Full" atau "Full (Strict)". **[semak]** Kalau sijil kekal self-signed masa dry run, tukar record ke grey cloud sampai sijil Let's Encrypt keluar, kemudian orange semula. Ini nasihat komuniti, bukan dari docs EasyPanel.

### 05B · Cache & Purge
**Hook:** You pushed the fix. EasyPanel deployed it. Visitors still see the old CSS.

- **CDN:** Cloudflare saves a copy of your files near each visitor. The first visitor there gets it from your server; the next ones get the saved copy.
- **Cached by default:** images, CSS, JavaScript. **Not cached:** HTML pages and API responses.
- **The fix:**
  - **Purge Cache:** purge one URL (safe) or Purge Everything (big changes).
  - Long term: let your build add a hash to file names (`app.3f9a.css`), so every deploy is a new file.

**Prompt for AI:** "My site is behind Cloudflare. After every deploy visitors see old CSS and JS. Make my build change file names on each deploy, and tell me when I still need to purge."

💡 Updated but nothing changed? Purge the cache.

**Visual:** A timeline: Deploy (server shows v2) → Visitor (Cloudflare still shows v1, sad face) → Purge button → visitor gets v2.

**Hook kelas lain:** "Super Stack 08C: you pasted a CDN link and icons appeared. Now the CDN serves your own files."

**Pro note:** Cloudflare caches by file extension and respects `Cache-Control`. Use Cache Rules to bypass `/api/*` or cache HTML deliberately. Check the `cf-cache-status` header in DevTools: HIT (served from cache), MISS (fetched from origin), DYNAMIC (not cacheable by default), BYPASS, EXPIRED. Ports 2052–2096, 8443 and 8880 are proxied but never cached.

---

## PART 3 · Security (free plan)

### 06 · Your Free Security Guard
**Hook:** Your shop went online yesterday. Today, 3,000 bots already tried `/wp-admin` and `/.env`.

- **DDoS protection:** on automatically for orange-cloud records. Nothing to set.
- **Free Managed Ruleset:** blocks the most common, widely exploited attacks. Included free.
- **Bot Fight Mode:** one switch (Security → Settings) that challenges known bad bots.
- **Security Events:** a log of who was blocked and why (Security → Analytics → Events). Open it once a week.
- **Under Attack Mode:** an emergency button on the Overview page. Every visitor gets a check page for a few seconds. Turn it off when the attack stops.

**Prompt for AI:** "Here is a screenshot of my Cloudflare Security Events [attach]. Explain what these requests were trying to do and whether I should block anything."

💡 Orange cloud on = guard on duty.

**Visual:** A guard at the orange gate. A queue of visitors: real customers walk through; robots with labels `/wp-admin`, `/.env`, `/phpmyadmin` are stopped.

**Pro note:**
- On Free, Bot Fight Mode covers the whole domain. WAF Skip rules do not bypass it, so it can challenge API calls, uptime monitors and webhooks (Billplz, GitHub). An IP Access rule for a known sender's IP still lets it through. If a webhook starts failing, check Security Events first.
- On Free, Security Events shows a sample of requests, not every one, for up to 30 days.

> ✅ Disahkan 25 Nov: lokasi menu, Bot Fight Mode tak boleh dikecualikan ikut path pada plan Free, dan Free Managed Ruleset ada untuk semua plan.

### 06A · Your Own Rules: WAF & Rate Limiting
**Hook:** Someone tries 500 passwords a minute on your login page.

- **WAF custom rules:** "if the request matches X, then block, challenge or allow."
  - Block paths you do not use: `/wp-admin`, `/xmlrpc.php`, `/.env`
  - Challenge visitors from countries you do not sell to (only if your shop is local)
- **Rate limiting:** "more than N requests from one IP in 10 seconds → block for 10 seconds."
  - The Free plan gives you one rule. Use it on `/login`.
- **Start with Managed Challenge, not Block.** Watch Security Events for a day, then tighten.

**Prompt for AI:** "Write Cloudflare WAF custom rules for my Laravel app: block WordPress and .env scanners, and rate-limit POST requests to /login. Explain each rule in one line."

💡 Block what you never use. Slow down what gets attacked.

**Visual:** A rule card that reads like a sentence: "IF path = /wp-admin → BLOCK". Below it, a speedometer on `/login` that turns red past a limit.

**Pro note:**
- Free plan limits:
  - **5 custom rules**. Combine conditions with `or` / `and` in one rule.
  - Actions: Block, Managed Challenge, JS Challenge, Interactive Challenge and Skip. **Log is Enterprise-only.**
  - **1 rate-limiting rule**, with a fixed 10-second period and a 10-second block. It counts per IP, and can match only on path.
- Visitors on shared mobile IPs can trip the rate limit together, so set it for real usage, not the minimum.

> ✅ Disahkan 25 Nov (docs WAF custom rules & rate limiting rules).

### 06B · Turnstile: Stop Bots on Your Forms
**Hook:** Your contact form gets 200 spam messages a day.

- **Turnstile** is Cloudflare's free CAPTCHA replacement. Most real users just see a tick; no puzzles.
- **Two parts, both required:**
  1. the widget on the form (frontend)
  2. a check on your server that the token is real (backend)
- Use it on sign-up, login, contact and checkout forms.
- Works even if the site is not on Cloudflare.

**Prompt for AI:** "Add Cloudflare Turnstile to my sign-up and contact forms. Verify the token on the server, and read the secret key from .env."

💡 Widget on the form. Check on the server.

**Visual:** A form with a small Turnstile box ticking green. A bot icon bounces off. Arrow from the form to the server with a "verify token" stamp.

**Pro note:** A widget without server-side verification (the Siteverify API) protects nothing; bots just skip the widget. Tokens are single-use and expire after 300 seconds. The site key is public; the secret key goes in `.env`. The Free plan allows 20 widgets.

### 06C · Lock the Back Door
**Hook:** You set up all the rules. Then an attacker skips Cloudflare and hits 203.0.113.10 directly.

- **The front door** = sitiscakes.com through Cloudflare. **The back door** = your server's IP.
- **Close the back door (pick one):**
  - **Firewall:** your server only accepts web traffic from Cloudflare's IP ranges.
  - **Cloudflare Tunnel:** your server connects out to Cloudflare. No open web ports, and no public IP to find.
- **Protect your admin pages with Cloudflare Access:** `admin.sitiscakes.com` and the EasyPanel dashboard ask for a one-time email code before the page even loads. Free for up to 50 users.

**Prompt for AI:** "My app runs on EasyPanel on a VPS behind Cloudflare. Help me allow web traffic only from Cloudflare's IP ranges, and protect my EasyPanel dashboard with Cloudflare Access."

💡 Guard the front door. Lock the back door.

**Visual:** A house with a guarded front gate (orange cloud). Round the back, a door labelled "203.0.113.10" gets bricked up. A separate "Admin" room has a keypad lock labelled "Access".

**Pro note:**
- Keep SSH reachable another way (your own IP, a VPN, or Access for SSH) before you lock the firewall. Do not lock yourself out.
- Cloudflare publishes its IP ranges at cloudflare.com/ips, and the list has changed before. Tunnel avoids maintaining that list.
- Tunnel connections are outbound-only, so the server needs no open inbound web ports.

> ✅ Disahkan 25 Nov: Zero Trust Free = 50 pengguna, Access dengan one-time PIN, Tunnel tersedia untuk semua plan. **[semak]** Dry run: Tunnel + Access untuk dashboard EasyPanel (port 3000).

### 06D · Secure Your Cloudflare Account
**Hook:** Your setup is perfect. Then someone logs in to your Cloudflare account.

- **2FA on your Cloudflare account.** Everything above is one login away.
- **DNSSEC on** (now that the domain is Active): stops fake answers to "where is sitiscakes.com". Add the DS record at your registrar.
- **API tokens, not the Global API Key:** when the AI or a tool needs access, give it a token for one zone and only the permissions it needs.
- **Members, not shared passwords:** invite your developer as a member, and remove them when the job ends.

**Prompt for AI:** "Create a Cloudflare API token that can only purge cache for sitiscakes.com. Tell me the exact permissions to tick."

💡 Your Cloudflare login is the master key. Protect it first.

**Visual:** A master key on a keyring with 2FA and DNSSEC tags. Next to it, smaller keys labelled "purge only" and "R2 only".

**Hook kelas lain:** "GitHub class 03B: a leaked key means making a new one. Same here: roll the token in the dashboard."

**Pro note:** The Global API Key has full account access and cannot be scoped. Treat it like the account password and never put it in `.env`. Scoped tokens can also be limited by IP and given an expiry date.

---

## PART 4 · R2 Cloud Storage

### 07 · R2: Cloud Storage With No Exit Toll
**Hook:** A customer uploads a cake photo. You redeploy. The photo is gone.

- **R2 is Cloudflare's cloud storage for files** (object storage): images, PDFs, videos, backups. The database holds records, not files.
- **Why not keep uploads on the server?** Files inside a container can disappear on redeploy, and the disk fills up.
- **Egress** = data leaving storage. Every image view counts. Most cloud storage charges per GB, so the bill grows with traffic.
- **R2 charges $0 for egress.** You pay for storage and requests, with a free monthly allowance.

**Example:** 200 GB stored, 1,000 GB downloaded in a month.

| | Storage | Egress | Monthly total |
|---|---|---|---|
| AWS S3 (approximate) | $4.60 | $81.00 | about $86 |
| Cloudflare R2 | $2.85 | $0 | about $3 |

How it is worked out: S3 at about $0.023/GB stored and $0.09/GB egress after the first 100 GB. R2 at $0.015/GB stored after the first 10 GB free. Request charges left out; S3 rates are approximate, so check AWS's pricing page before class.

💡 Files go in R2. No toll on the way out.

**Visual:** Two warehouses with shelves of boxes (photos, PDFs, videos). Trucks leaving the first stop at a toll booth. Trucks leaving the R2 warehouse drive out through an open gate.

**Hook kelas lain:** "Super Stack 11: Supabase and Firebase come with file storage. On your own VPS (Super Stack route), R2 is that storage."

**Pro note:**
- Docker volumes keep files across redeploys, but they tie files to one server, which makes scaling and backups harder.
- Requests: Class A (writes, lists) at $4.50 per million, Class B (reads) at $0.36 per million. Free each month: 10 GB storage, 1 million Class A and 10 million Class B. Deletes are free.
- R2 speaks the S3 API (endpoint `https://<account_id>.r2.cloudflarestorage.com`, region `auto`), so most S3 libraries work as-is.

> ✅ Disahkan 25 Nov: harga dan free tier R2. Kiraan: S3 200 × $0.023 = $4.60, egress (1,000 − 100) × $0.09 = $81.00, total $85.60. R2 (200 − 10) × $0.015 = $2.85. ✅ Kadar AWS us-east-1 disahkan dari data harga rasmi AWS (diterbitkan 21 Nov 2026): S3 Standard first 50 TB = $0.023/GB-month, data transfer out "Next 10 TB" (selepas 100 GB percuma) = $0.09/GB.

### 07A · Public or Private Files?
**Hook:** Cake photos should be public. Customer invoices should not.

- **Public bucket for public files:** product photos, logos. Connect a custom domain like `files.sitiscakes.com`, so Cloudflare caches them too.
- **Private bucket for private files:** invoices, IC copies, receipts. Nobody can open them by URL.
- **Presigned URL:** your app creates a link for one file that works for a set time (from 1 second up to 7 days). Use it to let a customer download their own invoice for the next 5 minutes.
- **Keys:** create an R2 token for **one bucket** only, and keep it in `.env` (same rule as the GitHub class).

**Prompt for AI:** "Set up Cloudflare R2 for my app: a public bucket on files.sitiscakes.com for product photos, and a private bucket for invoices served through presigned URLs that expire in 5 minutes. Keys come from .env."

💡 Public bucket for photos. Private bucket and presigned links for documents.

**Visual:** Two shelves. "Public" has an open window with cake photos and a `files.sitiscakes.com` sign. "Private" is a locked cabinet; a customer receives a single key with a 5-minute timer.

**Pro note:**
- The `r2.dev` URL is rate-limited, has no WAF or cache, and is meant for development only. In production, use a custom domain. That domain must be a zone in the same Cloudflare account.
- For browser uploads, issue a presigned **PUT** URL so the file goes straight to R2, and add a CORS rule on the bucket for your domain. Presigned POST (HTML form upload) is not supported.
- Validate file type and size on the server before you sign the upload.

### 07B · Backups to R2
**Hook:** Your VPS dies. The code is on GitHub. The database is not.

- **Code** is safe on GitHub. **The database and uploads** are only on your server.
- **Back up to R2 every night, from EasyPanel itself:**
  1. Server Settings → Storage Providers → add **Cloudflare R2**
  2. Open your database service → Backups → Create Database Backup → set a schedule
  - Works for PostgreSQL, MySQL, MariaDB and MongoDB.
  - Needs an EasyPanel **Hobby** licence or above (the Free plan has no database backups).
  - On EasyPanel Free: ask the AI for a nightly script that dumps the database and uploads it to R2.
- **Lifecycle rule:** delete backups older than 30 days automatically, so storage stays cheap.
- **Test the restore.** A backup you have never restored is only a hope.

**Prompt for AI:** "My PostgreSQL runs on EasyPanel. Walk me through backing it up every night to a private Cloudflare R2 bucket, adding a 30-day lifecycle rule, and restoring one backup to test it."

💡 No restore test, no backup.

**Visual:** A moon icon and a clock at 3:00 AM. A database box drops into the R2 warehouse every night. A shelf labelled "30 days" pushes the oldest box out the back.

**Hook kelas lain:** "Super Stack 18: Backup is your job. This is how."

**Pro note:**
- R2 tokens have no write-only permission ("Object Read & Write" can also delete). So use a separate bucket and token for backups, never the app's token.
- To stop a hacked server from deleting its own backups, add a **bucket lock** on the backup bucket. It blocks deletes and overwrites for a set number of days. A lock overrides lifecycle rules, so keep the lock shorter than the lifecycle age.
- Encrypt dumps that hold personal data before upload.

> ✅ Disahkan 25 Nov: EasyPanel ada backup database terbina ke R2 (preset Cloudflare R2 dalam Storage Providers). ✅ Disahkan 25 Nov (easypanel.io/pricing): "Database backups" bermula dari plan **Hobby** ($10.9/server/bulan bila bayar tahunan; ada kupon Malaysia 10%). Plan Free tiada. Untuk student plan Free, sediakan alternatif: script `pg_dump` + upload ke R2 (prompt lama).

---

## WRAP-UP

### 08 · Your Cloudflare Checklist
**Hook:** Ten switches. Set them once.

**Domain & DNS**
1. Auto-renew, 2FA and Registrar Lock at the registrar
2. Nameservers on Cloudflare, with MX and TXT kept

**Proxy & SSL**
3. Web records orange, mail and SSH grey
4. SSL Full (strict), Always Use HTTPS, minimum TLS 1.2

**Security**
5. Bot Fight Mode on, and Security Events checked weekly
6. WAF rule for scanners, rate limit on `/login`
7. Turnstile on forms, verified on the server
8. Back door closed (firewall or Tunnel), admin behind Access
9. 2FA on Cloudflare, DNSSEC on, scoped API tokens

**R2 Cloud Storage**
10. Uploads and nightly backups in R2, keys for one bucket only, restore tested

**Prompt for AI:** "Here are screenshots of my Cloudflare dashboard [attach]. Go through this 10-point checklist and tell me what is missing for sitiscakes.com."

Closing line: Your app stays on your server. Cloudflare makes it reachable, safe and cheap to grow.

CTA: [next class or link]

**Visual:** A control panel with 10 switches grouped by the 4 parts, flipping on one by one. The final shot is the gate, guard and warehouse together in front of Siti's Cake Shop.

---

## Senarai semak "kemas" sebelum bina slide
- [ ] Istilah sama di semua slide: "orange cloud" / "grey cloud", "Full (strict)", "nameservers", "bucket", "presigned URL"
- [ ] Contoh sama: `sitiscakes.com`, `203.0.113.10`, registrar tempatan, VPS + EasyPanel
- [ ] Masa DNS sama dengan Super Stack: "minutes up to 48 hours"
- [ ] Setiap slide: 1 hook, maksimum 5 bullet, 1 prompt, 1 💡
- [ ] Pro note pendek, tak lebih besar dari teks utama
- [ ] Dry run penuh: registrar → Cloudflare → SSL → cache → security rules → Access → R2 → backup, dengan screenshot setiap menu
- [ ] Semua item **[semak]** disahkan

## Sources (disemak 25 Nov 2026)
Pautan utama yang dipakai semasa semakan:
- https://www.cloudflare.com/tld-policies/ · https://developers.cloudflare.com/registrar/faq/
- https://developers.cloudflare.com/dns/zone-setups/full-setup/setup/ · https://developers.cloudflare.com/dns/cname-flattening/
- https://developers.cloudflare.com/fundamentals/reference/network-ports/
- https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/ · https://developers.cloudflare.com/ssl/troubleshooting/too-many-redirects/ · https://developers.cloudflare.com/ssl/origin-configuration/origin-ca/ · https://developers.cloudflare.com/ssl/reference/protocols/
- https://easypanel.io/docs/guides/custom-service-domain · https://easypanel.io/docs/backups/database · https://easypanel.io/docs/storage-providers/s3
- https://developers.cloudflare.com/cache/concepts/default-cache-behavior/
- https://developers.cloudflare.com/bots/get-started/bot-fight-mode/ · https://developers.cloudflare.com/waf/analytics/security-events/ · https://developers.cloudflare.com/fundamentals/reference/under-attack-mode/
- https://developers.cloudflare.com/waf/custom-rules/ · https://developers.cloudflare.com/waf/rate-limiting-rules/ · https://developers.cloudflare.com/waf/managed-rules/
- https://developers.cloudflare.com/turnstile/get-started/server-side-validation/
- https://www.cloudflare.com/ips/ · https://developers.cloudflare.com/tunnel/ · https://developers.cloudflare.com/cloudflare-one/identity/one-time-pin/
- https://developers.cloudflare.com/fundamentals/api/get-started/create-token/
- https://developers.cloudflare.com/r2/pricing/ · https://developers.cloudflare.com/r2/buckets/public-buckets/ · https://developers.cloudflare.com/r2/api/s3/presigned-urls/ · https://developers.cloudflare.com/r2/buckets/object-lifecycles/ · https://developers.cloudflare.com/r2/api/tokens/ · https://developers.cloudflare.com/r2/buckets/bucket-locks/
- https://developers.cloudflare.com/email-routing/ · https://developers.cloudflare.com/changelog/post/2026-04-16-email-sending-public-beta/
- https://aws.amazon.com/s3/pricing/

Topik ikut slide:
- Cloudflare Registrar: supported TLDs and at-cost pricing (03)
- Cloudflare: Change your nameservers (Full setup), DNSSEC (04, 04A, 06D)
- Cloudflare: CNAME flattening (04)
- Registrar: switching to Cloudflare nameservers (04A)
- Cloudflare: Proxy status (orange/grey cloud), network ports (05)
- Cloudflare: SSL/TLS encryption modes, ERR_TOO_MANY_REDIRECTS, Origin CA, Always Use HTTPS, Minimum TLS, HSTS (05A)
- Cloudflare Cache: default cached extensions, Cache Rules, Purge, cf-cache-status (05B)
- Cloudflare: DDoS protection, Bot Fight Mode, Security Events, Under Attack Mode (06)
- Cloudflare WAF: custom rules and rate limiting rules, plan limits (06A)
- Cloudflare Turnstile: client widget and server-side validation (06B)
- Cloudflare IP ranges, Cloudflare Tunnel, Cloudflare Access / Zero Trust free plan (06C)
- Cloudflare API tokens vs Global API Key, account members (06D)
- Cloudflare R2: pricing and free tier, public buckets and custom domains, presigned URLs, CORS, lifecycle rules (07, 07A, 07B)

Kadar AWS S3 dalam 07 dari ringkasan pihak ketiga, jadi ditanda approximate.

## Peta topik antara kelas
| Topik | Super Stack | GitHub | Mastery UI | Kelas ini |
|---|---|---|---|---|
| Domain, A/CNAME/MX | Peta (16) | — | — | Recap + nameserver + demo |
| SSL, CDN, DDoS | Peta (16A) | — | — | Mod SSL, cache, purge |
| Hosting, VPS, EasyPanel | Mendalam (15, 15A, 15B) | — | — | Tak diajar, cuma "origin" |
| `.env`, API keys | 12A, 14A | Mendalam (03B) | — | Satu ayat + token Cloudflare |
| Webhook | 12B | 09 | — | Pro note Bot Fight Mode sahaja |
| File storage | Supabase/Firebase (11) | — | Upload UI (10) | R2 public/private, presigned |
| Backup | Senarai semak (18) | Code di GitHub | — | Backup DB ke R2 |
| Keselamatan web (WAF, bot, Turnstile, Access, Tunnel) | — | — | — | **Baru** |
| Keselamatan akaun (2FA, DNSSEC, scoped token) | — | — | — | **Baru** |
