# Where Should My App Live? Hosting Tools for Vibe Coders

Draf content v2 · 25 Nov 2026 · @Mykel
Kelas vibe coding untuk beginner · bahagian "server management tools"

## Cara baca draf ini

**Penomboran:** setiap tool = satu nombor. Slide pertama tool tu ialah nombor sahaja (`1`), slide seterusnya `1A`, `1B`, `1C`… Susunan subtopik **sama untuk semua tool**, supaya penonton boleh banding terus:

| Kod | Subtopik |
|---|---|
| `N` | Apa tool ni (analogi + untuk siapa) |
| `NA` | Kelebihan |
| `NB` | Kekurangan |
| `NC` | Scalable jangka panjang? |
| `ND` | Framework PHP & JS: support / tak support |
| `NE` | Kos langganan (plan bulanan) |
| `NF` | Kos penggunaan (apa yang buat bil naik) |
| `NG` | Penggunaan resources (RAM, CPU, kuota) |

**Dalam slide sebenar (v2, 32 slide), subtopik digabung jadi 4 slide setiap tool:** `N` = apa · `NA` = kelebihan + kekurangan · `NB` = framework + scale · `NC` = kos langganan + kos penggunaan + resources. Pembuka `00`–`00A`, penutup `08`–`08A`. Teks slide dalam `slides/tools/data.py`; draf ini kekal sebagai rujukan fakta.

**Teks slide dalam English** (ikut kelas Cloudflare). Kotak **Pro note** = ayat tepat untuk developer pro, beginner boleh langkau.

**Harga:** semua dalam USD, disemak dengan laman rasmi pada 25 Nov 2026. Harga platform ni kerap bertukar (Netlify tukar 3 kali dalam 2026). Tulis "harga setakat Nov 2026" di penjuru setiap slide kos. Tanda **(pihak ketiga)** = angka dari blog / review, bukan laman rasmi.

**Tiga keluarga tool** (guna warna sama dalam semua slide):
- 🟦 **Managed platform**: Netlify, Vercel, Cloudflare. *Sewa kondo siap perabot.* Tak urus server langsung.
- 🟧 **Control panel klasik**: cPanel. *Sewa bilik dalam rumah sewa.* Server dikongsi, panel siap.
- 🟩 **Self-hosted PaaS (atas VPS awak)**: Easypanel, Coolify, Dokploy. *Beli tanah sendiri, ada kontraktor bina rumah.* Awak sewa VPS, tool ni jadi "Vercel peribadi" atas VPS tu.

---

## 0 · Cover
**Where Should My App Live?**
Netlify, Vercel, Cloudflare, cPanel, Easypanel, Coolify, Dokploy. Same question, seven answers.

**Visual:** Seven house icons in a row, grouped by colour: three blue condos, one orange rented room, three green plots of land with cranes.

---

## 0A · Three Families of Hosting
**Before you compare tools, know which family they belong to**

- 🟦 **Managed platform** (Netlify, Vercel, Cloudflare): push code, it goes live. No server to manage. You pay for usage.
- 🟧 **Control panel** (cPanel): classic shared hosting. Upload PHP files, get email and a database. Cheap, familiar, old-school.
- 🟩 **Self-hosted PaaS** (Easypanel, Coolify, Dokploy): you rent a VPS, install the panel, and get a "Vercel" on your own server. Cheapest at scale, but you are the admin.

**Visual:** Three columns: condo / rented room / land with crane. Under each: "They manage" vs "You manage" bar.

**Pro note:** Managed = serverless/edge (no persistent process). cPanel = shared LAMP, usually CloudLinux LVE limits. Self-hosted PaaS = Docker on your VM with a reverse proxy (Traefik/Caddy) in front.

---

## 0B · What We Check for Every Tool
**Same 8 questions, every tool**

What is it · Pros · Cons · Long-term scale · PHP & JS support · Subscription cost · Usage cost · Resources

**Visual:** Checklist card with 8 rows. This card reappears small in the corner of every tool slide, with the current row highlighted.

---

# 🟦 1 · NETLIFY

## 1 · Netlify: What Is It?
**Drag, drop, live. The original "push to deploy" for frontends.**

- Connect GitHub, every push becomes a new version of your site.
- Best for: landing pages, portfolios, static sites, Astro / Vite / React frontends.
- Built-in extras: Forms, Functions (small backend), Deploy Previews.

**Visual:** GitHub logo → arrow → Netlify teal logo → globe "yoursite.netlify.app".

---

## 1A · Netlify: Pros
- **Easiest start.** Drag a folder into the browser, site is live in seconds.
- **Deploy Previews:** every branch gets its own link to test before going live. Preview deploys don't use credits.
- **Forms without a backend:** add one attribute to your HTML form, submissions show in the dashboard (unlimited since Apr 2026).
- **Unlimited team seats on Pro** (since Apr 2026).

---

## 1B · Netlify: Cons
- **Credit system can pause your site.** On Free, when credits run out, the site shows "Site not available" until next month.
- **No PHP.** WordPress and Laravel can't run here.
- **No long-running server.** Functions wake up, answer, sleep. No WebSocket server, no background worker that runs all day.
- **Pricing changes often** (3 changes in 2026). Re-check before you commit.

**Pro note:** Many Free users on the community forum reported sites staying paused even after credits reset (Jul–Aug 2026). Netlify hasn't confirmed it as a bug. If it happens, open a support ticket.

---

## 1C · Netlify: Scalable Long-Term?
**Traffic: yes. Complex backend: no.**

- Static pages are served from a global CDN, so traffic spikes are fine.
- Bills grow with traffic (bandwidth, requests, compute all use credits).
- When your app needs a real backend, queue or database server, you move that part elsewhere and keep Netlify for the frontend.

**Verdict:** ✅ landing page / frontend forever · ⚠️ full SaaS backend

---

## 1D · Netlify: Framework Support

| | Support |
|---|---|
| Static HTML, Vite React/Vue, Astro | ✅ best fit |
| Next.js, Nuxt, SvelteKit, Remix / React Router | ✅ via adapter (auto-detected) |
| Express / Node API | ⚠️ only as Functions, not a full server |
| WebSocket, cron worker 24/7 | ❌ |
| **PHP**: WordPress, Laravel, CodeIgniter | ❌ not supported |

**Pro note:** Functions support JS/TS and Go. Time limits: normal function 10 s, scheduled 30 s, background 15 min, edge function 50 ms CPU.

---

## 1E · Netlify: Subscription Cost

| Plan | Price | Credits / month |
|---|---|---|
| Free | $0 | 300 |
| Personal | $9 / month | 1,000 |
| Pro | from $20 / month (unlimited seats) | 3,000 |

**Pro credit tiers** (you choose, change anytime):

| Credits | 3,000 | 5,000 | 10,000 | 15,000 | 20,000 |
|---|---|---|---|---|---|
| Price / month | $20 | $33 | $63 | $95 | $126 |

- Unused credits expire monthly. Pro 5,000 and above: leftover credits roll over one extra month.

---

## 1F · Netlify: Usage Cost
**Everything costs credits**

- Each **production deploy = 15 credits.** Free plan (300) ≈ 20 deploys a month if you use nothing else.
- Bandwidth, web requests and function compute also take credits.
- Top-up (auto-recharge): Personal 500 credits / $5, Pro 1,500 credits / $10.

**Tip for vibe coders:** don't push to `main` 30 times a day. Work on a branch (preview = free), merge once.

**Visual:** A fuel gauge labelled "300 credits" draining with each "deploy" icon.

---

## 1G · Netlify: Resources
**You don't manage RAM or CPU. You manage credits.**

- No server, no RAM to choose.
- Watch in dashboard: credits used, bandwidth, function invocations.
- Build runs on Netlify's machines, not yours.

---

# 🟦 2 · VERCEL

## 2 · Vercel: What Is It?
**The home of Next.js.**

- Made by the same company that builds Next.js, so Next.js features work first here.
- Push to GitHub → live, with Preview links per branch (same idea as Netlify).
- Best for: Next.js apps, React frontends, AI apps with streaming.

**Visual:** Black triangle logo with a "Next.js" badge glued to it.

---

## 2A · Vercel: Pros
- **Next.js zero config.** Server components, image optimization, ISR just work.
- **Preview deployments** with comments for every pull request.
- **Fast global edge**, good analytics and logs out of the box.
- **AI-friendly:** AI SDK, streaming responses, v0 deploys straight here.

---

## 2B · Vercel: Cons
- **Hobby (free) is non-commercial only.** If you charge users or run a business, you must be on Pro.
- **Bills can jump** with traffic: bandwidth and compute over the included credit are charged on demand. Turn on Spend Management.
- **No PHP officially.**
- **Lock-in risk:** some Next.js features behave best only on Vercel.

**Pro note:** No persistent process: no WebSocket server, functions have max duration. Use an external DB (Neon, Supabase) via Marketplace.

---

## 2C · Vercel: Scalable Long-Term?
**Scales automatically, and so does the bill.**

- Auto-scales functions with traffic, no setup.
- Big companies run on it, so the tech scales. The question is cost.
- Common path: start on Vercel, move heavy backend or high-bandwidth parts to a VPS when the bill gets big.

**Verdict:** ✅ Next.js app from day 1 to medium scale · ⚠️ watch costs at high traffic

---

## 2D · Vercel: Framework Support

| | Support |
|---|---|
| Next.js | ✅ best in class |
| Nuxt, SvelteKit, Astro, Remix / React Router, Vite | ✅ |
| Express / Hono / Node API | ✅ as functions (Express: zero config; static files must go in `public/`) |
| Python, Go functions | ✅ |
| WebSocket server, 24/7 worker | ❌ |
| **PHP** | ⚠️ community runtime only (`vercel-php`), not official |
| WordPress, Laravel (full) | ❌ not practical (no persistent disk, no queue worker) |

---

## 2E · Vercel: Subscription Cost

| Plan | Price | What's included |
|---|---|---|
| Hobby | $0 | Fixed quota, personal use only, can't buy more |
| Pro | $20 / user / month | $20 usage credit included, extra billed on demand |
| Enterprise | custom | |

**Visual:** Price tag "$20" with a small coupon "$20 credit inside".

---

## 2F · Vercel: Usage Cost
**Pro pays per use after the $20 credit**

- **Active CPU:** from $0.128 per hour (only when your code is actually running, not waiting).
- Also metered: provisioned memory, function invocations, data transfer, image optimization.
- Hobby: if you hit the limit, things stop. You cannot pay for more.

**Tip:** set a spend limit in Settings → Billing before launching.

---

## 2G · Vercel: Resources
**Hobby quota (monthly)**

- Active CPU: 4 hours
- Provisioned memory: 360 GB-hours
- Function invocations: 1 million
- Fast Data Transfer (bandwidth): 100 GB (Pro: 1 TB, then $0.15 / GB)

You don't pick a server size. You can pick function memory and region in settings.

---

# 🟦 3 · CLOUDFLARE

## 3 · Cloudflare: What Is It?
**Not just hosting. The gate, the road, and the warehouse.**

- Famous for DNS, SSL and protecting sites. Also hosts apps with **Workers** (and the older **Pages**).
- Your code runs in 300+ cities, close to every visitor.
- Extras in one account: R2 (file storage), D1 (database), KV, email routing.

**Visual:** Orange cloud over a world map with many small dots.

**Hook kelas lain:** "Kelas Cloudflare terangkan setting dashboard. Di sini kita tengok Cloudflare sebagai tempat app tinggal."

---

## 3A · Cloudflare: Pros
- **Most generous free tier.** Static assets are free with no bandwidth bill.
- **Very cheap paid plan:** $5 / month covers millions of requests.
- **R2 has no egress fees:** users download your files, you don't pay per GB out.
- **All-in-one:** domain, DNS, SSL, hosting, storage, database in one dashboard.

---

## 3B · Cloudflare: Cons
- **Workers is not a normal Node.js server.** Some npm packages don't work (better with `nodejs_compat` flag, but not 100%).
- **Free plan CPU limit: 10 ms per request.** Heavy work (big PDF, image processing) fails.
- **No PHP.**
- **Learning curve:** many products and names (Workers, Pages, D1, KV, R2, Durable Objects). Beginners get lost.

**Pro note:** Cloudflare Containers (GA since Apr 2026, needs Workers Paid) can run any Docker image, including PHP. Billed by active CPU, memory and disk. Beyond beginner scope.

---

## 3C · Cloudflare: Scalable Long-Term?
**The most scalable and cheapest of the three managed platforms.**

- Runs on Cloudflare's global network, scaling is automatic.
- Cost grows slowly: $0.30 per extra million requests.
- Limits are about *code style* (edge runtime), not traffic.

**Verdict:** ✅ static + API + storage, very long term · ⚠️ apps that need full Node.js or PHP

---

## 3D · Cloudflare: Framework Support

| | Support |
|---|---|
| Static HTML, Vite React/Vue, Astro | ✅ |
| Hono | ✅ best fit (built for Workers) |
| Next.js | ✅ via OpenNext adapter (`@opennextjs/cloudflare`) |
| Nuxt, SvelteKit, Remix / React Router | ✅ |
| Express | ⚠️ partial, with `nodejs_compat` |
| Python Workers | ✅ supported (some Python packages won't run) |
| **PHP**: WordPress, Laravel | ❌ (only via Containers) |

---

## 3E · Cloudflare: Subscription Cost

| Plan | Price | What's included |
|---|---|---|
| Workers Free | $0 | 100,000 requests / day, 10 ms CPU / request |
| Workers Paid | $5 / month minimum | 10M requests + 30M CPU ms / month |

- One $5 covers Workers, Pages Functions, KV, Hyperdrive and Durable Objects usage on the account.

---

## 3F · Cloudflare: Usage Cost
**Pay only above the included amount**

- Extra requests: $0.30 per million
- Extra CPU: $0.02 per million CPU ms
- Static assets: free
- R2 storage: free 10 GB per month, then pay per GB stored. **Downloads (egress) are always free.**

**Visual:** Calculator: "1 million visitors × 3 requests = still around $5".

---

## 3G · Cloudflare: Resources
- Free: **10 ms CPU** per request (waiting for a database doesn't count, only real computing).
- Paid: default 30 s CPU per request, max 5 minutes.
- Memory per Worker is fixed at 128 MB (Free and Paid). You don't pick a server.

---

# 🟧 4 · CPANEL

## 4 · cPanel: What Is It?
**The classic hosting dashboard since the 2000s.**

- What you get when you buy cheap "web hosting" from a local hosting company.
- Icons for everything: File Manager, MySQL, Email, SSL, WordPress installer.
- Best for: WordPress, PHP sites, business email on your domain.

**Visual:** Old-school grid of blue icons, a "Upload ZIP" button highlighted.

---

## 4A · cPanel: Pros
- **PHP and WordPress feel native.** Install WordPress in one click (Softaculous / WP Toolkit).
- **Email included:** `info@yourbusiness.com` in the same plan.
- **Cheap and familiar in Malaysia:** many local hosts, local support, pay in RM.
- **No server knowledge needed:** the hosting company maintains the server.

---

## 4B · cPanel: Cons
- **Shared server:** a noisy neighbour can slow your site.
- **Modern JS apps are awkward:** Next.js / Node.js needs "Setup Node.js App" and often doesn't run well, or the host doesn't enable it.
- **No auto deploy from GitHub by default** (there's Git Version Control, but setup is manual).
- **License got expensive** if you run cPanel on your own VPS (price up 7 years in a row).

---

## 4C · cPanel: Scalable Long-Term?
**Scale by upgrading the plan, not automatically.**

- Shared hosting → bigger plan → VPS with cPanel → dedicated server.
- Each step is a manual upgrade or migration.
- Fine for business sites and WordPress for years. Not built for a SaaS with sudden traffic spikes.

**Verdict:** ✅ WordPress / company site / email · ⚠️ modern JS SaaS

---

## 4D · cPanel: Framework Support

| | Support |
|---|---|
| **Plain PHP, WordPress** | ✅ best fit |
| **Laravel, CodeIgniter** | ✅ (need SSH + Composer, point domain to `public/`) |
| Static build (Vite React/Vue, Astro) | ✅ upload the `dist/` folder |
| Express / Node API | ⚠️ only if host enables "Setup Node.js App" |
| Next.js (SSR), Nuxt (SSR) | ⚠️ possible but heavy, often blocked by RAM limit |
| WebSocket, queue worker 24/7 | ❌ usually not allowed on shared hosting |

---

## 4E · cPanel: Subscription Cost
**Two ways to pay**

1. **Shared hosting** (cPanel included): local hosts start around RM10–RM27 / month (e.g. Exabytes). Promo price; **renewal is higher**, check before you buy.
2. **cPanel license on your own VPS:**

| Tier | Accounts | Until 15 Dec 2026 | From 16 Dec 2026 |
|---|---|---|---|
| Solo | 1 | $29.99 | $32.99 |
| Admin | up to 5 | $35.99 | $38.99 |
| Pro | up to 30 | $53.99 | $58.99 |
| Premier | 100 | $69.99 | $76.99 |
| Extra account (Premier) | each above 100 | $0.49 | $0.55 |

Nota: harga 16 Dec 2026 dari beberapa laman hosting & berita (pihak ketiga, announcement Okt 2026). Kalau video keluar selepas 16 Dec, tunjuk lajur baru sahaja.

**Visual:** "The license costs more than the server": small VPS tag $6 beside a big license tag $33.

---

## 4F · cPanel: Usage Cost
- Shared hosting: **fixed price**, no surprise bill. Over the limit = site slows or gets suspended, not charged more.
- Own VPS: VPS price + license. License rises if you add accounts (Premier: $0.55 per account above 100 from 16 Dec 2026).
- Extras that add cost: domain renewal, paid SSL (free AutoSSL is enough for most), backups.

---

## 4G · cPanel: Resources
- Shared plan limits (CloudLinux): CPU %, RAM (often 1–2 GB), entry processes, inodes (file count).
- Hit the limit → "508 Resource Limit Reached".
- cPanel on own VPS (official): RAM 2 GB minimum, 4 GB recommended. Disk 20 GB minimum, 40 GB recommended.

---

# 🟩 5 · EASYPANEL

## 5 · Easypanel: What Is It?
**A modern, pretty panel for your own VPS.**

- Rent a VPS, run one command, get a clean dashboard.
- Deploy from GitHub, Docker image, or one-click templates (n8n, WordPress, Postgres…).
- Best for: beginners who want their own server with the least terminal work.

**Visual:** Bare VPS box → install command → shiny dashboard with app cards.

---

## 5A · Easypanel: Pros
- **Nicest UI** of the three self-hosted tools. Feels like Vercel.
- **One-click templates:** n8n, WordPress, databases, Redis in a few clicks.
- **Free plan per server** (up to 3 projects).
- **Run anything in Docker:** PHP and JS in one server.
- Many VPS providers offer an Easypanel image ready-installed.

---

## 5B · Easypanel: Cons
- **Not open source.** If the company stops, the panel stops updating.
- **Free = 3 projects only.** More projects or DB backups need a paid plan.
- **Paid per server:** 2 VPS = 2 licenses.
- **You are the admin:** server updates, disk full, security are your job.
- Multi-server (cluster) is still alpha.

---

## 5C · Easypanel: Scalable Long-Term?
**Scale up the VPS. Scaling out is still early.**

- Easy path: upgrade VPS (2 GB → 4 GB → 8 GB).
- Each app runs in its own container, so one crash doesn't kill others.
- Cluster support only on Business plan and still alpha.

**Verdict:** ✅ small business, side projects, n8n · ⚠️ apps needing many servers

---

## 5D · Easypanel: Framework Support
**If it runs in Docker, it runs here.**

| | Support |
|---|---|
| **Laravel, WordPress, plain PHP** | ✅ (template or Dockerfile / buildpack) |
| Next.js, Nuxt, SvelteKit, Astro, Remix | ✅ |
| Express, NestJS, Hono | ✅ full long-running server |
| WebSocket, cron, queue worker | ✅ |
| MySQL, Postgres, Redis, Mongo | ✅ one-click |

---

## 5E · Easypanel: Subscription Cost
**Per server, per month**

| Plan | Monthly billing | Annual billing (per month) | Adds |
|---|---|---|---|
| Free | $0 | $0 | up to 3 projects, unlimited services & deploys |
| Hobby | $14.90 | $10.90 | unlimited projects, DB backups, advanced monitoring |
| Growth | $23.90 | $16.90 | multiple users, access control |
| Business | $37.90 | $29.90 | cluster (alpha), white-label, priority support |

- Every paid plan is **per server**. 30-day money-back guarantee.
- Nota: senarai "Adds" dari review pihak ketiga; harga dari laman rasmi.

---

## 5F · Easypanel: Usage Cost
**The bill = VPS + (optional) Easypanel plan**

- VPS with 4 GB RAM: about $5–$12 / month (e.g. Hetzner, OVHcloud, Hostinger). Watch for cheap promo prices that renew higher.
- No per-request or bandwidth charge from Easypanel. Traffic cost comes from the VPS provider (most include several TB).
- Fixed, predictable bill.

---

## 5G · Easypanel: Resources
- Minimum: Linux (Ubuntu), **2 GB RAM**.
- Recommended for real use: 4 GB (builds eat RAM).
- Every app and database you add uses RAM on the same VPS. Watch the Monitor page.

---

# 🟩 6 · COOLIFY

## 6 · Coolify: What Is It?
**Open-source "Vercel / Heroku" you install on your own server.**

- Free forever if you self-host. Also has a paid Cloud version (they host the dashboard, you bring servers).
- 280+ one-click services, auto deploy from GitHub, preview per pull request.
- Best for: vibe coders who want many apps on one cheap VPS and full control.

**Visual:** Purple Coolify logo on top of a VPS, with many little app cards stacked.

---

## 6A · Coolify: Pros
- **Open source and free self-hosted.** No license, no project limit.
- **Huge one-click catalog:** Supabase, n8n, Plausible, WordPress, databases.
- **Multi-server:** one dashboard can manage many VPS.
- **Preview deploys per pull request**, automatic SSL, scheduled DB backups to S3/R2.
- Big community, very active development.

---

## 6B · Coolify: Cons
- **You are the sysadmin:** updates, security, disk space, backups.
- **UI is busier** than Easypanel, more options = more confusing for beginners.
- **Updates sometimes break things.** Test before updating production.
- **Dashboard itself uses RAM** on your server.

---

## 6C · Coolify: Scalable Long-Term?
**Good: add more servers when one is not enough.**

- Start: one VPS for dashboard + apps.
- Grow: move dashboard to its own small VPS, add servers for apps and databases.
- Scaling = **more servers, each app on one server.** Docker Swarm (one app across many servers) is deprecated and will be removed in Coolify v5.

**Verdict:** ✅ many apps, long term, low cost · ⚠️ needs someone comfortable with servers

---

## 6D · Coolify: Framework Support

| | Support |
|---|---|
| **Laravel, WordPress, plain PHP** | ✅ (Nixpacks auto-detect, Dockerfile, or template) |
| Next.js, Nuxt, SvelteKit, Astro, Remix | ✅ |
| Static sites | ✅ |
| Express, NestJS, Hono, Python, Go | ✅ |
| WebSocket, cron, queue worker | ✅ (scheduled tasks built in) |
| Docker Compose | ✅ |

---

## 6E · Coolify: Subscription Cost

| Option | Price |
|---|---|
| Self-hosted | **$0** forever |
| Coolify Cloud | $5 / month, includes 2 servers; +$3 per extra server (annual billing: 20% off) |

**Note:** Cloud only hosts the dashboard. Your apps still run on servers you rent.

---

## 6F · Coolify: Usage Cost
**The bill = VPS (+ $5 if Cloud)**

- One 4 GB VPS can host many small apps: about $5–$12 / month.
- No usage-based charges from Coolify.
- Backup storage (S3 / Cloudflare R2) is a small extra cost.

**Visual:** Side by side: "Vercel Pro: $20 + usage" vs "Coolify: $8 VPS, 10 apps".

---

## 6G · Coolify: Resources
- Minimum (official): **2 CPU cores, 2 GB RAM, 10 GB free disk** (amd64 or arm64).
- Recommended: 4 GB if builds run on the same server.
- Tip: build big apps on GitHub Actions, then let Coolify only run the image.

---

# 🟩 7 · DOKPLOY

## 7 · Dokploy: What Is It?
**The newer, lighter open-source alternative to Coolify.**

- Same idea: install on your VPS, deploy from GitHub, one-click templates.
- Strong on Docker Compose and multi-server with Docker Swarm.
- Best for: vibe coders who like Coolify's idea but want a simpler UI and real clustering.

**Visual:** Dokploy logo with a small chain of 3 servers linked together.

---

## 7A · Dokploy: Pros
- **Open source, free self-hosted.**
- **Clean, simple UI**, easier than Coolify for beginners.
- **Docker Swarm built in:** add worker servers and scale an app across them.
- **Built-in monitoring** (CPU, RAM, disk per app), backups, templates.
- Lightweight: the panel idles around 350–450 MB RAM (pihak ketiga).

---

## 7B · Dokploy: Cons
- **Younger project:** smaller community, fewer tutorials than Coolify.
- **Fewer one-click templates** than Coolify.
- **You are still the sysadmin** (updates, security, backups).
- Swarm sounds easy, but clustering brings new problems (shared storage, networking).

---

## 7C · Dokploy: Scalable Long-Term?
**The most "scale-out ready" of the three self-hosted tools.**

- Start on one VPS.
- Add servers → Docker Swarm spreads replicas of your app.
- Databases still need care (Swarm doesn't magically make DB clustered).

**Verdict:** ✅ growing apps that may need several servers · ⚠️ beginners who want many ready templates

---

## 7D · Dokploy: Framework Support

| | Support |
|---|---|
| **Laravel, WordPress, plain PHP** | ✅ (Nixpacks / Railpack / Dockerfile / template) |
| Next.js, Nuxt, SvelteKit, Astro, Remix | ✅ |
| Static sites | ✅ |
| Express, NestJS, Hono, Python, Go | ✅ |
| WebSocket, cron, queue worker | ✅ |
| Docker Compose | ✅ first-class |

---

## 7E · Dokploy: Subscription Cost

| Option | Price |
|---|---|
| Self-hosted | **$0** forever |
| Cloud Hobby | $4.50 / server / month (1 user) |
| Cloud Startup | $15 / month, 3 servers included, unlimited users |
| Extra server (both plans) | $4.50 / month |
| Annual | save 20% |

---

## 7F · Dokploy: Usage Cost
**The bill = VPS (+ Cloud fee if used)**

- No usage-based charges.
- Same VPS math as Coolify: one 4 GB VPS ≈ $5–$12 / month.
- Cost grows only when *you* add servers.

---

## 7G · Dokploy: Resources
- Minimum (official): **2 GB RAM, 30 GB disk**.
- Realistic: 4 GB for development, 8 GB for small production.
- Monitor tab shows which app eats RAM.

---

# 8 · PERBANDINGAN & CARA PILIH

## 8 · All Seven Side by Side

| | Netlify | Vercel | Cloudflare | cPanel | Easypanel | Coolify | Dokploy |
|---|---|---|---|---|---|---|---|
| Family | 🟦 | 🟦 | 🟦 | 🟧 | 🟩 | 🟩 | 🟩 |
| Free start | ✅ | ✅ (non-commercial) | ✅ best | ❌ | ✅ 3 projects | ✅ | ✅ |
| PHP / WordPress | ❌ | ❌ | ❌ | ✅ best | ✅ | ✅ | ✅ |
| Next.js | ✅ | ✅ best | ✅ | ⚠️ | ✅ | ✅ | ✅ |
| 24/7 backend, WebSocket | ❌ | ❌ | ⚠️ | ⚠️ | ✅ | ✅ | ✅ |
| Bill type | credits | seat + usage | usage (cheap) | fixed | VPS + plan | VPS | VPS |
| You manage server | No | No | No | No | Yes | Yes | Yes |
| Long-term scale | frontend ✅ | ✅ $$ | ✅ $ | ⚠️ manual | ⚠️ up only | ✅ multi-server | ✅ Swarm |

---

## 8A · Which One Should I Choose?
**Answer three questions**

1. **Is it PHP / WordPress?** → cPanel (simplest) or Easypanel / Coolify / Dokploy (modern).
2. **Is it frontend or Next.js, and you don't want to touch servers?** → Cloudflare (cheapest), Vercel (best Next.js), Netlify (easiest static).
3. **Many apps, n8n, database, backend that runs all day, fixed bill?** → VPS + Easypanel (easiest) / Coolify (most features) / Dokploy (best multi-server).

**Visual:** Decision tree with three branches, each ending in tool logos.

---

## 8B · My Recommended Path for Beginners
**Start free, move only when you have a reason**

1. **Learn:** Cloudflare or Netlify (free, static / frontend).
2. **First real app with users:** Vercel Pro or Cloudflare Paid ($5).
3. **Bills growing or need backend 24/7:** one VPS + Coolify / Dokploy / Easypanel.
4. **Client wants WordPress + email:** cPanel hosting.

**Prompt for AI:** "My app is [describe: framework, database, users per month, need email?]. Compare Cloudflare, Vercel, Netlify, cPanel and a VPS with Coolify for this app: monthly cost, setup steps, and what breaks first when traffic grows."

---

## Sumber (disemak 25 Nov 2026)
- Netlify Pro tiers: netlify.com/changelog/2026-07-14-pro-plan-credit-tiers; function limits: docs.netlify.com/build/functions
- Vercel Express: vercel.com/docs/frameworks/backend/express
- Cloudflare: workers/platform/limits, r2/pricing, containers GA changelog 2026-04-13
- cPanel 16 Dec 2026: webhosting.today (8 Okt 2026), seahawkmedia.com, monstermegs.com; keperluan: docs.cpanel.net/installation-guide/system-requirements
- Coolify: coolify.io/docs/get-started/installation, coolify.io/docs/knowledge-base/docker/swarm
- Dokploy: dokploy.com/pricing
- Netlify: netlify.com/pricing, docs.netlify.com (credit-based plans, paused projects), changelog Apr & Jul 2026
- Vercel: vercel.com/pricing, vercel.com/docs/plans/hobby, fair use policy
- Cloudflare: developers.cloudflare.com/workers/platform/pricing
- cPanel: support.cpanel.net "2026 cPanel Store License Pricing" & "License Tiers"
- Easypanel: easypanel.io/pricing, easypanel.io/docs
- Coolify: coolify.io/pricing, coolify.io/docs/get-started/cloud
- Dokploy: docs.dokploy.com/docs/core/cloud, docs.dokploy.com/docs/core/installation
