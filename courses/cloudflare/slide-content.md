# Cloudflare for Vibe Coders (10 slide)

Draf content v3 · 24 Nov 2026 · @Mykel

## Cara baca draf ini

**Audiens bercampur:** ramai beginner, ada developer pro. Setiap slide ada 2 lapis:
- **Teks utama**: bahasa mudah dengan analogi. Beginner faham tanpa perlu tanya.
- **Pro note**: kotak kecil di penjuru slide (atau disebut secara lisan). Ayatnya tepat dari segi teknikal, supaya developer pro tak nampak lubang. Beginner boleh langkau.

**Beza dengan kelas lain (boleh sama topik, lain sudut):**
- **Super Stack** = peta. *Apa* kepingan yang wujud (frontend, server, domain, DNS, Cloudflare) dan macam mana ia bersambung.
- **GitHub Power Skills** = bawa code sampai **Live** (Push → CI → CD), termasuk `.env` / secrets.
- **Kelas ini** = tangan di dashboard. *Macam mana* setup, *kenapa* ia rosak, dan *macam mana* nak betulkan.
- Kalau topik sama dengan Super Stack (domain, A/CNAME, SSL, CDN), ulang dengan sudut lain: Super Stack terangkan *apa*, kelas ini terangkan *setting mana* dan *apa jadi kalau salah*.

Tanda dalam draf:
- **Pro note** = ayat untuk developer pro
- **Hook kelas lain** = rujukan ke kelas sebelum ni
- **[semak]** = perlu sahkan masa dry run

---

## 01 · Cover
**Cloudflare for Vibe Coders**
Hundreds of features. You only need these.

Bottom line: from your domain name to your file storage, hands-on

**Visual:** A visitor on the left, a house labelled "your app" on the right, and an orange cloud standing between them like a gate.

---

## 02 · Your App Is Live. Now What?
**Your app is live. Now give it an address, a gate and a warehouse.**

Hook: Last class ended at "Live". But your app lives at 203.0.113.10, anyone can hit your server directly, and user uploads disappear on redeploy.

- **An address:** your domain, pointed the right way (slides 03–05)
- **A gate:** Cloudflare in front of your server, with SSL and cache (slides 06–07)
- **A warehouse:** R2 for files (slide 08)
- **Bonus:** free email on your own domain (slide 09)

**Visual:** Reuse the Super Stack flow (Frontend → Backend → Database → Server → Domain). An orange cloud slides in between Server and Domain. Small "Live ✓" tag on Server from the GitHub class.

**Hook kelas lain:** "In Super Stack you saw the map. In the GitHub class your code reached the server. Today we build the road from the domain to that server."

---

## 03 · Domain: Renting It Right
**Your domain: rent it, protect it, reuse it**

Hook: Your app has been online for a year. One morning the domain shows someone else's page. The renewal email went to spam.

- **You rent it every year.** Turn on auto-renew, and use an email you actually read for the registrar account.
- **Where to buy:** Cloudflare Registrar sells at cost, but **not every extension**. `.my` and `.com.my` are bought locally (e.g. Exabytes), then connected to Cloudflare. That is today's demo.
- **Subdomains are free.** One domain, many apps: `app.yourapp.com`, `api.yourapp.com`, `admin.yourapp.com`.

**Prompt for AI:** "I own yourapp.com. Suggest a subdomain plan for my landing page, web app, API and admin panel."

💡 Auto-renew on. One domain, many subdomains.

**Visual:** A yearly calendar with the renewal date circled and an "auto-renew ON" toggle. Beside it, one tree trunk labelled "yourapp.com" with branches app., api., admin.

**Pro note:** Cloudflare Registrar requires the domain to use Cloudflare nameservers, and it does not support every TLD. Turn on registrar lock and 2FA on the registrar account; most domain hijacks start with a hijacked registrar login.

> **[semak]** Sahkan `.my` / `.com.my` tiada dalam senarai TLD Cloudflare Registrar.

---

## 04 · DNS: Records and Nameservers
**DNS: the phone book, and who holds it**

Hook: You added the right DNS record in Cloudflare. Nothing happens. Because the internet is still reading the phone book at Exabytes.

- **Records** say *where* things live:
  - **A:** name → IP address. `yourapp.com → 203.0.113.10`
  - **CNAME:** name → another name. `www → yourapp.com`
  - **MX:** where email for your domain is delivered.
  - **TXT:** notes for proving ownership and email security (SPF, DKIM).
- **Nameservers** say *who holds the book*. Only one place is in charge. If nameservers point to Exabytes, records you add in Cloudflare are ignored.
- **Break the email records and email stops**, even if the website still works.
- **Changes are not instant.** Record changes usually show in minutes. A nameserver change can take hours (up to 24). Do not keep changing things while you wait.

**Prompt for AI:** "Here are my current DNS records [paste]. Which ones are for my website and which are for email? What must I keep when I move to Cloudflare?"

💡 Records say where. Nameservers say who.

**Visual:** Two phone books. Exabytes is greyed out; Cloudflare is highlighted. One arrow from "the internet" points to the Cloudflare book. Inside it, two tabs: **Web** (A, CNAME) and **Email** (MX, TXT).

**Hook kelas lain:** "Super Stack showed you an A and a CNAME record. Today: where you type them, and why they sometimes do nothing."

**Pro note:** "Propagation" is really caching. Resolvers keep old answers until the TTL runs out, and a nameserver change waits on the TLD's own TTL. Use `dig yourapp.com NS +short` or `nslookup` to see what the internet sees right now. A CNAME cannot sit on the root (`@`) in standard DNS; Cloudflare allows it through CNAME flattening.

---

## 05 · Demo: Exabytes → Cloudflare → Your VPS
**Two settings connect everything**

- **Nameservers, set at Exabytes:** "Cloudflare holds my phone book now."
- **A record, set at Cloudflare:** "My app lives at this IP."

**Demo steps:**
1. In Cloudflare, add your domain (the root, without www) and choose the Free plan.
2. Cloudflare scans your existing records. **Review them:** keep the email records (MX, TXT), and delete old A records that point to Exabytes hosting.
3. Cloudflare gives you two nameservers. Copy both.
4. In Exabytes, if **DNSSEC** is on, turn it off first.
5. In the Exabytes client area: My Domains → Manage Nameservers → replace them with Cloudflare's two → Change Nameservers.
6. Wait. Cloudflare emails you, and the domain shows **Active**.
7. In Cloudflare DNS: A record `@` → your VPS IP, orange cloud on. `www` as a CNAME to your domain.
8. Open your domain in the browser.

**Prompt for AI:** "My domain is at Exabytes and my app runs on a VPS at [IP]. Walk me through pointing it to Cloudflare, one step at a time. Remind me to check DNSSEC and email records."

💡 Nameservers point to Cloudflare. The A record points to your server.

**Visual:** Three boxes in a row: Exabytes → Cloudflare → your VPS (with its IP). First arrow: "nameservers, set at Exabytes". Second arrow: "A record, set at Cloudflare". Two warning stickers: "DNSSEC off first" and "keep MX".

**Pro note:** Once the zone is Active, you can turn DNSSEC back on from Cloudflare (it gives you a new DS record to add at Exabytes). The record scan is a best guess and misses records it cannot see, so compare it with an export of the old zone.

Nama menu dalam kedua-dua dashboard berubah dari masa ke masa, jadi buat dry run sebelum kelas.

---

## 06 · Orange Cloud & SSL Modes
**The orange cloud, and the SSL setting that breaks sites**

Hook: You turned on Cloudflare. Now your site says "too many redirects" and will not load.

- **Orange cloud (Proxied):** traffic goes through Cloudflare first. Visitors see Cloudflare's IP, not yours. Cache and protection are on.
- **Grey cloud (DNS only):** traffic goes straight to your server. Your IP is visible.
- **The rule:** orange for your website and app. Grey for mail servers (e.g. `mail.yourapp.com`) and anything that is not web traffic. MX records have no cloud at all.
- **SSL/TLS mode, the setting that matters:**
  - **Flexible:** visitor → Cloudflare is https, but Cloudflare → server is plain http. If your server also forces https, the two keep redirecting each other: "too many redirects". Avoid.
  - **Full (strict):** https all the way, and Cloudflare checks your server's certificate. Use this.
- **Your server needs a certificate for Full (strict):** a free **Cloudflare Origin Certificate** or Let's Encrypt.

**Prompt for AI:** "My site shows 'too many redirects' after I turned on Cloudflare. My server runs [Nginx / Easypanel / ...]. Check my SSL mode and set up an origin certificate so I can use Full (strict)."

💡 Web is orange. SSL is Full (strict).

**Visual:** Two lanes from a visitor to a server. Top lane: orange cloud with a padlock on both halves of the road (Full strict). Bottom lane: padlock on the first half only, then an open road to the server, with a looping arrow labelled "too many redirects" (Flexible).

**Hook kelas lain:** "Super Stack said 'turn on SSL'. Here is the one setting that decides whether that works."

**Pro note:** "IP hidden" is only true if the origin is not exposed some other way: a grey-cloud record on the same IP, old DNS history, or the server answering direct IP requests. Lock the firewall to Cloudflare's IP ranges, or use Cloudflare Tunnel. An Origin CA certificate is trusted only by Cloudflare, so it works only with the orange cloud on.

> **[semak]** Zone baru mungkin default mod **Automatic**. Tengok apa yang keluar masa dry run.

---

## 07 · Cache & Purge
**Deployed the fix, but visitors still see the old version?**

Hook: CD pushed the fix to your server two minutes ago. You refresh. The old CSS is still there.

- **CDN:** Cloudflare saves a copy of your files in the data centre near each visitor. The first visitor there gets it from your server; everyone after gets the saved copy.
- **Cached by default:** static files such as images, CSS and JavaScript. **Not cached:** your HTML pages and API responses.
- **The catch:** your server has the new file, but Cloudflare still serves the old copy.
- **The fix:**
  - **Purge Cache** in the dashboard: purge a single URL (fast, safe), or Purge Everything (for big changes).
  - Long term: let your build add a hash to file names (`app.3f9a.css`). Every deploy creates a new file name, so nothing needs purging.
- Only orange-cloud records are cached.

**Prompt for AI:** "My site is behind Cloudflare. After every deploy, visitors see old CSS and JS. Set up my build so file names change on each deploy, and tell me when I still need to purge."

💡 Updated but nothing changed? Purge the cache.

**Visual:** A timeline. "Deploy": the server box shows v2. "Visitor": the Cloudflare box still shows v1, with a sad face. Then a "Purge" button, and the visitor gets v2.

**Hook kelas lain:**
- "Remember Bootstrap loading from cdn.jsdelivr.net in Super Stack? You have used a CDN before. Now it is your own files."
- "Lazy load (UI class) sends less data. Cache sends it from closer. They work together."

**Pro note:** Cloudflare caches by file extension by default, and it respects your `Cache-Control` headers. Use Cache Rules to cache HTML or bypass paths such as `/api/*`. Check the `cf-cache-status` response header (HIT, MISS, DYNAMIC) in DevTools to see what is really happening.

---

## 08 · R2: A Warehouse With No Exit Toll
**R2: where user files should live**

Hook: In the UI class you built a file upload box. A user uploads a profile photo. You redeploy. The photo is gone. So where should that file actually go?

- **Object storage** holds files: images, PDFs, videos, backups. Your database holds records, not files.
- **Why not keep uploads on your app server?** On container hosting (Docker, Easypanel), files saved inside the container can disappear on redeploy, and the disk fills up.
- **Egress** = data leaving storage for the internet. Every image view and download counts. Most cloud storage charges per GB, so the bill grows with your traffic.
- **R2 charges $0 for egress.** You pay for what you store and for the number of requests.
- **Keys:** same rule as the GitHub class. R2 keys go in `.env`, never in the repo. Leaked? Delete the token in the Cloudflare dashboard and make a new one.

**Example on the slide:** 200 GB stored, 1,000 GB downloaded in a month.

| | Storage | Egress | Monthly total |
|---|---|---|---|
| AWS S3 (approximate) | $4.60 | $81.00 | about $86 |
| Cloudflare R2 | $2.85 | $0 | about $3 |

How it is worked out: S3 at about $0.023 per GB stored, and about $0.09 per GB egress after the first 100 GB. R2 at $0.015 per GB stored after the first 10 GB, which are free. Request charges are left out, and the S3 rates are approximate, so check AWS's pricing page before class.

**Prompt for AI:** "Store user uploads in Cloudflare R2 using the S3-compatible API. Read the keys from .env. Serve the images from a subdomain like files.yourapp.com."

💡 Files go in R2. No toll on the way out.

**Visual:** Two warehouses side by side, with shelves of boxes (photos, PDFs, videos). Trucks leaving the first stop and pay at a toll booth. Trucks leaving the second, labelled R2, drive out through an open gate.

**Pro note:**
- Docker volumes do keep files across redeploys, but they tie the files to one server. That makes scaling to two servers and backups harder.
- Requests are billed as Class A (writes and lists) and Class B (reads). There is a free monthly allowance.
- The `r2.dev` public URL is rate-limited and meant for testing. In production, connect a custom domain, which also lets Cloudflare cache the files.
- For large uploads, let the browser upload straight to R2 with a presigned URL, so the file does not pass through your server.

> **[semak]** S3: 200 × $0.023 = $4.60. Egress: (1,000 − 100) × $0.09 = $81.00. Total $85.60. R2: (200 − 10) × $0.015 = $2.85. Angka betul.

---

## 09 · Bonus: Email on Your Own Domain, Free
**hello@yourapp.com, without paying for email hosting**

Hook: Your app looks professional. Your contact email is yourapp2024@gmail.com.

- **Cloudflare Email Routing** forwards mail sent to `hello@yourapp.com` into your existing inbox (e.g. Gmail). Free.
- Make as many addresses as you need: `hello@`, `support@`, `billing@`, all landing in one inbox.
- Cloudflare adds the **MX** and **TXT** records for you (the email records from slide 04).
- **Limits to know:**
  - It **receives and forwards only**. It does not give you a mailbox and it does not send email.
  - If you already pay for email hosting at Exabytes, its MX records clash with Email Routing. Pick one.

**Prompt for AI:** "My domain is on Cloudflare. Walk me through setting up Email Routing so hello@yourapp.com forwards to my Gmail. Warn me if my existing MX records will conflict."

💡 Your own email address, forwarded free.

**Visual:** Three envelopes addressed hello@, support@ and billing@ flow into one funnel with an orange cloud, and come out into a single Gmail inbox.

**Pro note:** The destination inbox must be verified first. Sending from your app (sign-up emails, password resets) needs a transactional email service with SPF, DKIM and DMARC set up on the same domain. That is a different job from forwarding.

> **[semak]** Sahkan langkah dalam dashboard Email Routing masa dry run. Alternatif untuk slot ini: **Turnstile** (anti-bot percuma untuk form signup/login) atau **Tunnel** (buka app tanpa dedah IP/port).

---

## 10 · The Full Chain
**From your laptop to a visitor's screen**

The GitHub class chain, extended:

1. **Push → CI → CD:** your new version reaches the server (GitHub class)
2. **Domain:** a visitor types yourapp.com
3. **Nameservers + DNS:** the internet asks Cloudflare's phone book
4. **Orange cloud + SSL:** the request reaches Cloudflare first, over https all the way
5. **Cache:** if Cloudflare has a fresh copy, it answers straight away
6. **Your server:** otherwise the request goes on to your app
7. **R2:** images and uploads come from the warehouse, with no exit toll
8. **The page loads**

**Prompt for AI:** "My app deploys from GitHub to my VPS. Set it up on Cloudflare: DNS records, SSL mode Full (strict) with an origin certificate, and R2 for uploads. List what I must click in the dashboard myself."

Closing line: You do not need every Cloudflare feature. You need to set up these yourself, and now you can.

CTA: [next class or link]

**Visual:** One horizontal line. The left part repeats the GitHub class chain in faded colour (Push → CI → CD). It continues in full colour with this class's icons, ending at a loaded page.

---

## Senarai semak "kemas" sebelum bina slide
- [ ] Istilah sama di semua slide: "orange cloud" / "grey cloud", "Full (strict)", "nameservers" (bukan campur "NS" / "name server")
- [ ] Contoh sama dari awal hingga akhir: `yourapp.com`, IP `203.0.113.10`, Exabytes, VPS
- [ ] Setiap slide: 1 hook, maksimum 5 bullet, 1 prompt, 1 💡
- [ ] Pro note pendek (2–3 ayat), tak lebih besar dari teks utama
- [ ] Dry run penuh: Exabytes → Cloudflare → VPS → SSL → purge → R2 → Email Routing, dan screenshot setiap menu
- [ ] Semua item **[semak]** dah disahkan

## Sources
- Cloudflare R2 pricing: storage rate, free tier, free egress, Class A/B operations (slide 08)
- Cloudflare R2: public buckets, r2.dev vs custom domain, presigned URLs (slide 08)
- Cloudflare Registrar: at-cost pricing and supported TLDs (slide 03)
- Cloudflare: Change your nameservers (Full setup), and DNSSEC before and after moving (slides 04, 05)
- Cloudflare: CNAME flattening (slide 04)
- Exabytes: Switching to Cloudflare Nameservers (slide 05)
- Cloudflare DNS proxy status: orange vs grey cloud (slides 06, 07)
- Cloudflare: ERR_TOO_MANY_REDIRECTS and SSL/TLS modes; Origin CA certificates; Cloudflare IP ranges (slide 06)
- Cloudflare Cache: default cached file extensions, Cache Rules, cf-cache-status, Purge Cache (slide 07)
- Cloudflare Email Routing (slide 09)

Kadar AWS S3 dalam slide 08 dari ringkasan pihak ketiga, bukan page AWS sendiri, jadi ditanda approximate.

## Peta topik antara kelas
| Topik | Super Stack | GitHub | Mastery UI | Kelas ini |
|---|---|---|---|---|
| Apa itu domain / A & CNAME | Peta (slide 14, 16) | — | — | Setting + troubleshoot |
| Manfaat Cloudflare (CDN, DDoS, SSL) | Peta (slide 16) | — | — | Setting sebenar |
| Deploy ke server | Overview (slide 14) | CD + webhook | — | Mula dari "Live" |
| `.env` / secrets | Sebut | Mendalam (03B) | — | Satu ayat + rotate token |
| Upload file | — | — | UI sahaja (10) | Backend R2 (hook) |
| Lazy load | — | — | 12B | Satu ayat (hook) |
| Nameserver, DNSSEC, demo Exabytes | — | — | — | **Baru** |
| Orange/grey, mod SSL, origin cert | — | — | — | **Baru** |
| Cache & purge | — | — | — | **Baru** |
| R2 & egress | — | — | — | **Baru** |
| Email Routing | — | — | — | **Baru** |

**Cadangan untuk Super Stack slide 14 & 16 (belum dibina):** boleh kekal topik sama (domain, DNS, Cloudflare), tapi tahap peta sahaja: apa, kenapa, dan gambarajah. Tiada langkah dashboard, mod SSL atau troubleshoot. Hujung slide 16 letak teaser "setup penuh dalam kelas Cloudflare".
