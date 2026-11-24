# Cloudflare for Vibe Coders (10 slide)

Draf content · 19 Nov 2026 · @Mykel
Setiap slide: tajuk, teks atas slide, idea visual, contoh prompt untuk AI, satu ayat untuk diingat.

> Nota dengan tanda **[semak]** ialah tambahan dari semakan fakta (24 Nov 2026). Buang bila dah putuskan.

---

## 01 · Cover
**Cloudflare for Vibe Coders**
Hundreds of features. You only need five.

Bottom line: 5 topics, from your domain name to your file storage

**Visual:** A visitor on the left, a house labelled "your app" on the right, and an orange cloud standing between them like a gate.

---

## 02 · The Route
**5 stops from your domain to your app**

- **Get found:** Domain, DNS
- **Stay fast and safe:** Proxy & SSL, CDN & Cache
- **Store files:** R2 object storage and egress

Closing line: By the end, you will know how a visitor gets from your domain name to your app, and where your files should live.

**Visual:** Three columns numbered 1, 2, 3 with arrows running left to right, ending in a house labelled "your app".

---

## 03 · Why Cloudflare
**Why do vibe coders need Cloudflare?**

Hook: AI built your app in a weekend. Now, how do people reach it, and is it safe when they do?

- **It sits in front of your app.** Every visitor passes through Cloudflare before reaching your server.
- **Faster.** Copies of your files are served from a location near the visitor.
- **Safer.** Free HTTPS, and your server's real IP address stays hidden.
- **Cheaper.** The free plan is enough to start, and R2 storage has no egress fees.

💡 Cloudflare is the guard at your front gate.

**Visual:** Four icon cards in a 2x2 grid: a gate, a lightning bolt, a padlock, a coin.

---

## 04 · Domain
**Domain: your app's address**

Hook: Your app is live at 203.0.113.10. Nobody is going to type that.

- A domain is the name people type to reach your app, like `yourapp.com`.
- **You rent it, you do not own it forever.** It renews every year. Miss the renewal and someone else can take it. Turn on auto-renew.
- **Where to get one:** Cloudflare Registrar sells domains at cost, with no markup. Or buy anywhere else and point the domain to Cloudflare by changing its nameservers.
- **Subdomains are free.** One domain can serve many apps: `app.yourapp.com`, `api.yourapp.com`.

**Prompt for AI:** "I bought my domain at [registrar]. Give me the steps to point its nameservers to Cloudflare."

💡 The domain is the address, not the house.

**Visual:** A street sign reading "yourapp.com" in front of a house. Beside it, a small yearly calendar with a renewal date circled.

**Soalan terbuka sebelum kelas:** Cloudflare Registrar tak jual semua extension. Semak sama ada `.my` / `.com.my` ada dalam senarai yang disokong. **[semak]** Setahu saya `.my` dan `.com.my` (MYNIC) tak disokong, jadi student beli di Exabytes dan sambung macam slide 06. Sahkan di senarai TLD Cloudflare.

---

## 05 · DNS
**DNS: the internet's phone book**

Hook: You bought the domain. You open it in the browser. Nothing loads. Why?

- DNS turns a name (`yourapp.com`) into your server's address (an IP number).
- **Nameservers** decide who holds your phone book. Point them to Cloudflare and you manage every record there.
- **Three records are enough to start:**
  - **A:** name to IP address. "yourapp.com lives at 203.0.113.10."
  - **CNAME:** name to another name. "www goes wherever yourapp.com goes."
  - **TXT:** a note attached to your domain. Used to prove you own it and to set up email.
- **Changes take time to spread**, from a few minutes to a few hours. Do not panic.

**Prompt for AI:** "My server IP is [IP]. Tell me exactly which DNS records to add in Cloudflare for yourapp.com and www."

💡 No DNS record, no visitors.

**Visual:** An open phone book. Left page lists names (yourapp.com, www, api), right page lists numbers. An arrow runs from one name to one number, then on to a server icon.

> **[semak]** Email sebenarnya guna record **MX** (bukan TXT sahaja). TXT untuk SPF/DKIM/verify. Cadangan: kekal 3 record atas slide, sebut MX secara lisan bila cerita email.

---

## 06 · Connecting It All
**Connecting it all: Exabytes → Cloudflare → your VPS**

Hook: You have a domain at Exabytes and an app running on a VPS. Two settings connect them.

- **Nameservers, set at Exabytes:** they tell the internet "Cloudflare holds my phone book now".
- **A record, set at Cloudflare:** it tells Cloudflare "my app lives at this IP".

**Demo steps:**
1. In Cloudflare, add your domain (the root, without www) and choose the Free plan.
2. Cloudflare scans your existing DNS records. Check them before you continue, especially the email records.
3. Cloudflare gives you two nameservers. Copy both.
4. In the Exabytes client area, go to My Domains, open Manage Nameservers, replace the current nameservers with Cloudflare's two, and click Change Nameservers.
5. Wait. It can take up to 24 hours. Cloudflare emails you, and the domain shows Active.
6. In Cloudflare DNS, add an A record: name `@`, value your VPS IP, orange cloud on. Add `www` as a CNAME pointing to your domain.
7. Open your domain in the browser.

**Prompt for AI:** "My domain is at Exabytes and my app runs on a VPS at [IP]. Walk me through pointing it to Cloudflare, one step at a time."

💡 Nameservers point to Cloudflare. The A record points to your server.

**Visual:** Three boxes in a row: Exabytes (where you bought the domain), Cloudflare (holds the DNS records), your VPS (with its IP number). First arrow: "nameservers, set at Exabytes". Second arrow: "A record, set at Cloudflare".

Nama menu dalam kedua-dua dashboard berubah dari masa ke masa, jadi buat dry run sebelum kelas.

> **[semak]**
> - Sebelum langkah 4: kalau DNSSEC ON di Exabytes, matikan dulu. Kalau tak, domain boleh jadi tak resolve lepas tukar nameserver.
> - Langkah 2: scan selalu import A record lama yang tunjuk ke hosting Exabytes. Padam / ganti dengan IP VPS, jangan biar dua A record untuk `@`.

---

## 07 · Proxy & SSL
**Proxy & SSL: the orange cloud**

Hook: Every DNS record in Cloudflare has a small cloud beside it. Orange or grey. It matters more than it looks.

- **Orange cloud (Proxied):** traffic goes through Cloudflare first. Your server's IP is hidden, and caching and protection are switched on.
- **Grey cloud (DNS only):** traffic goes straight to your server. Cloudflare only answers the phone-book lookup.
- **The rule:** orange for websites and apps. Grey for email and anything that is not web traffic.
- **SSL** is the padlock in the browser, the "s" in https. Cloudflare gives it to you free.
- Set the SSL/TLS mode to **Full (strict)**. Your server needs its own SSL certificate for this. Avoid **Flexible**. It is a common cause of the "too many redirects" error.

**Prompt for AI:** "My site shows 'too many redirects' after I turned on Cloudflare. Check my SSL mode and tell me what to change."

💡 Web is orange. Email is grey.

**Visual:** Two lanes from a visitor to a server. Top lane passes through an orange cloud with a padlock and a shield. Bottom lane runs direct under a grey cloud, with the server's IP number exposed.

> **[semak]**
> - "Email is grey" maksudnya record macam `mail.yourapp.com` (A record untuk mail server). MX record sendiri memang tiada butang cloud.
> - Untuk Full (strict), sijil di server boleh guna **Cloudflare Origin Certificate** (percuma, dari dashboard) atau Let's Encrypt. Elok sebut supaya student tak tersekat.
> - Zone baru sekarang mungkin tunjuk mod **Automatic** secara default. Semak masa dry run.

---

## 08 · CDN & Cache
**CDN & Cache: a copy close to every visitor**

Hook: You deployed the fix. You refresh the page. The old version is still there.

- **CDN:** Cloudflare keeps copies of your files in data centres around the world. Each visitor gets the nearest copy.
- **Cache:** the saved copy itself. Pages load faster and your server does less work.
- **What gets cached by default:** static files such as images, CSS and JavaScript. Your app's pages and API responses are not.
- **The catch:** after you update a file, visitors may still get the old copy.
- **The fix:** use **Purge Cache** in the Cloudflare dashboard.
- It only works with the orange cloud. Grey-cloud records are never cached.

**Prompt for AI:** "I updated my site but visitors still see the old version. I use Cloudflare. What should I purge?"

💡 Updated but nothing changed? Purge the cache.

**Visual:** A world map with one server in the middle and small shop icons on several continents. A visitor in Malaysia is served from the nearest shop, not from the far-away server.

---

## 09 · R2 & Egress
**R2: a warehouse with no exit toll**

Hook: A user uploads a profile photo. You redeploy your app. The photo is gone.

- **Object storage** holds files: images, PDFs, videos, backups. Your database holds records, not files.
- **Why not keep uploads inside your app server?** On container hosting, files saved inside the app can disappear on redeploy, and the disk fills up fast.
- **Egress** is data leaving your storage for the internet. Every image view or file download counts. Most cloud storage charges for it per GB, so the bill grows with your traffic, not with what you store.
- **R2 charges $0 for egress.** You pay for what you store and for the number of requests.
- **Keep the keys secret.** R2 access keys go in `.env`, never in your repo.

**Example on the slide:** 200 GB stored, 1,000 GB downloaded in a month.

| | Storage | Egress | Monthly total |
|---|---|---|---|
| AWS S3 (approximate) | $4.60 | $81.00 | about $86 |
| Cloudflare R2 | $2.85 | $0 | about $3 |

How the example is worked out: S3 at about $0.023 per GB stored and about $0.09 per GB egress after the first 100 GB. R2 at $0.015 per GB stored after the first 10 GB, which are free. Request charges are left out, and the S3 rates are approximate, so check AWS's pricing page before class.

**Prompt for AI:** "Store user uploads in Cloudflare R2 using the S3-compatible API. Read the keys from .env."

💡 Files go in R2. No toll on the way out.

**Visual:** Two warehouses side by side, each with shelves of labelled boxes (photos, PDFs, videos). Trucks leaving the first stop and pay at a toll booth. Trucks leaving the second, labelled R2, drive out through an open gate.

> **[semak]** Kira semula: S3 200 × $0.023 = $4.60, egress (1,000 − 100) × $0.09 = $81.00 → $85.60. R2 (200 − 10) × $0.015 = $2.85. Angka betul.

---

## 10 · Full Flow
**From a domain name to your app**

1. **Domain:** a visitor types yourapp.com
2. **DNS:** the phone book finds where it lives
3. **Proxy & SSL:** the request reaches Cloudflare first, over https
4. **Cache:** if Cloudflare has a copy, it answers straight away
5. **Your server:** otherwise the request goes on to your app
6. **R2:** images and uploads are served from the warehouse, with no exit toll
7. **The page loads**

**Prompt for AI:** "Set up my app on Cloudflare: DNS records for my server, SSL mode Full (strict), and R2 for uploads. List what I must do in the dashboard myself."

Closing line: You do not need every Cloudflare feature. You need to understand these five.

CTA: [next class or link]

**Visual:** One horizontal line with seven icon stations, from a visitor on the left to a loaded page on the right. Each station reuses the icon from its own slide.

---

## Sources
- Cloudflare R2 pricing: storage rate, free tier and free egress (slide 09)
- Cloudflare Registrar: at-cost domain pricing (slide 04)
- Cloudflare DNS proxy status: orange cloud vs grey cloud, and which records to leave DNS only (slides 07, 08)
- Cloudflare: ERR_TOO_MANY_REDIRECTS: Flexible mode and redirect loops (slide 07)
- Exabytes: Switching to Cloudflare Nameservers: client-area steps (slide 06)
- Cloudflare: Change your nameservers (Full setup): record review and activation time (slide 06)

Kadar AWS S3 dalam slide 09 dari ringkasan pihak ketiga, bukan page AWS sendiri, jadi ditanda approximate.
