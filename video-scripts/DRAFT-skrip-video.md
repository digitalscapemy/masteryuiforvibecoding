# Mastering UI for Vibe Coding — Draft Skrip Video

> **Status:** DRAFT v3 · satu video setiap tajuk slide (slide 03–20)
> **Voice:** ElevenLabs — "Mikhail"
> **Gaya:** santai, ayat pendek, beginner-friendly. "Coach" = saya, "Awak" = student.
> **Format setiap video:** Hook → Konsep → Playground → Prompt AI → Recap. Sasaran 1.5–3 minit.

---

## Nota penting untuk ElevenLabs

- **Nombor & unit ditulis dalam perkataan** dalam VO (contoh: "tiga puluh dua piksel", bukan "32px") supaya sebutan tak jadi pelik / campur English.
- **Bahasa:** VO dalam BM. Slide & playground dalam video kekal **English** (deck mode EN).
- **Term penting disebut dalam English** (padding, margin, button, hover, state, flexbox, grid, breakpoint, responsive, prompt...). Jangan terjemah term tu.
- `...` = jeda pendek. Baris kosong = jeda panjang / tukar scene.
- Teks dalam **[VISUAL]** tak dibaca — itu arahan untuk edit / screen record.
- Kalau sebutan mana-mana perkataan lari, tukar ejaan dalam VO sahaja (contoh: "si-es-es" untuk CSS kalau perlu).

---

## Senarai Video (18) — satu video = satu tajuk slide (konsep + playground)

> Nombor video = nombor slide dalam deck.

| # | Tajuk | Slide | Playground |
|---|---|---|---|
| 03 | Kenapa UI Mastery Penting? | 03 | – |
| 04 | CSS Box Model | 04 | – |
| 05 | Padding vs Margin | 05 | 05A Padding, 05B Margin |
| 06 | Visual Styling Essentials | 06 | 06A, 06B |
| 07 | Button States & Variants | 07 | 07A |
| 08 | Component States & Feedback | 08 | 08A |
| 09 | Navigation Components | 09 | 09A, 09B |
| 10 | Form Components | 10 | 10A |
| 11 | Common UI Components | 11 | 11A, 11B |
| 12 | Modals, Loading & Notifications | 12 | 12A, 12B |
| 13 | Layout Components | 13 | 13A, 13B |
| 14 | Layout Patterns | 14 | 14A |
| 15 | Page Layout Structure | 15 | 15A |
| 16 | Responsive Breakpoint | 16 | 16A |
| 17 | Essential Pages untuk SaaS | 17 | latihan mini |
| 18 | Cara Cari UI Inspiration | 18 | latihan mini |
| 19 | Dari UI Reference ke AI Prompt | 19 | 19A Prompt Builder |
| 20 | UI Debugging & Mini Challenge | 20 | 20A Fix the UI |

---

## VIDEO 03 — Kenapa UI Mastery Penting?
**Slide:** 03 · **Durasi:** ~2 min
**Objektif:** Awak faham kenapa kena faham UI walaupun AI boleh generate.

**[VISUAL]** Slide 03, fokus pada soalan besar.
> AI boleh generate UI. Itu betul. Tapi soalan Coach... Awak boleh kawal dia ke tak?

**[VISUAL]** Tunjuk "Before" (UI berselerak) → "After" (dashboard kemas).
> Tengok dua UI ni. Dua-dua dibuat oleh AI. Bezanya? Yang kanan... orang yang bagi arahan tu tahu apa yang dia nak.
> Kalau Awak cuma cakap "buat dashboard"... AI akan teka. Bila AI teka, hasilnya rawak.

**[VISUAL]** Empat kad manfaat muncul satu-satu.
> Bila Awak faham UI, empat benda jadi lebih baik.
> Satu... prompt lebih baik. Awak tahu nak minta apa, dan cara terangkan.
> Dua... interface lebih kemas dan moden.
> Tiga... kurang debugging. Masalah design berkurang, dan Awak tahu cara betulkan.
> Empat... development lebih laju. Idea terus jadi UI sebenar.

**[VISUAL]** Teks besar: "Awak = Director. AI = Pelukis."
> Senang cerita, Awak director. AI pelukis. Director yang bagus tahu bahasa visual. Dan itulah yang kita akan belajar sepanjang kelas ni.

---

## VIDEO 04 — CSS Box Model
**Slide:** 04 · **Durasi:** ~2 min
**Objektif:** Awak boleh namakan 4 lapisan box model.

**[VISUAL]** Slide 04. Animasi kotak: content muncul dulu, kemudian lapisan demi lapisan.
> Setiap benda dalam website... tulisan, gambar, button... semuanya adalah kotak. Dan setiap kotak ada empat lapisan.

**[VISUAL]** Highlight Content.
> Paling dalam... Content. Ini isi sebenar. Tulisan, gambar, apa sahaja.

**[VISUAL]** Highlight Padding.
> Lepas tu Padding. Ruang di dalam kotak, antara content dengan garisan tepi.

**[VISUAL]** Highlight Border.
> Lepas tu Border. Garisan tepi yang balut padding tadi.

**[VISUAL]** Highlight Margin.
> Dan paling luar... Margin. Ruang di luar kotak, yang jarakkan kotak ni dengan kotak lain.

**[VISUAL]** Analogi: gambar dalam bingkai di dinding.
> Cuba bayangkan gambar dalam bingkai. Gambar tu content. Kertas putih keliling gambar tu padding. Bingkai tu border. Dan jarak antara bingkai dengan bingkai lain di dinding... itu margin.

**[VISUAL]** Recap empat perkataan.
> Content, padding, border, margin. Dari dalam ke luar. Ingat urutan ni, sebab dalam video seterusnya kita akan main dengan padding dan margin.

---

## VIDEO 05 — Padding vs Margin
**Slide:** 05 · **Playground:** 05A Padding, 05B Margin · **Durasi:** ~3 min
**Objektif:** Awak boleh beza padding dan margin, dan guna dalam prompt.

**[VISUAL]** Slide 05, dua sisi.
> Ramai beginner keliru dua benda ni. Jadi Coach ringkaskan dalam satu ayat. Padding dalam. Margin luar.

**[VISUAL]** Sisi Padding.
> Padding tambah ruang di dalam elemen. Dia tolak content jauh dari border. Kotak tu sendiri jadi lebih besar.

**[VISUAL]** Sisi Margin.
> Margin pula tambah ruang di luar. Dia tolak elemen lain supaya jauh. Isi dalam kotak tak berubah langsung.

**[VISUAL]** Buka Playground 05A. Screen record.
> Jom cuba. Ni playground padding. Awak nampak kawalan top, right, bottom dan left.
> Coach naikkan padding atas... tengok. Ruang di dalam card bertambah. Tulisan turun ke bawah.
> Sekarang Coach samakan keempat-empat sisi. Nampak lebih seimbang, kan?

**[VISUAL]** Buka Playground 05B.
> Sekarang margin. Coach naikkan margin... tengok card sebelah. Dia kena tolak jauh. Tapi isi dalam card ni sendiri tak berubah.

**[VISUAL]** Buka tab Prompt dalam playground, tunjuk butang copy.
> Bila Awak dah suka hasilnya, buka tab Prompt. Playground ni dah tukarkan setting Awak jadi ayat untuk AI. Copy, dan paste dalam AI coding tool Awak.

**[VISUAL]** Recap.
> Padding... ruang dalam. Margin... ruang luar. Sekarang giliran Awak. Buka playground, dan cuba buat card yang nampak lega dan kemas.

---

## VIDEO 06 — Visual Styling Essentials
**Slide:** 06 · **Playground:** 06A, 06B · **Durasi:** ~4.5 min
**Objektif:** Satu video untuk seluruh slide 06 — Bahagian A, kemudian Bahagian B.

### Bahagian A — Colors & Typography

**[VISUAL]** Slide 06, highlight kad Colors.
> UI yang nampak profesional biasanya bermula dengan dua benda. Warna... dan tulisan.
> Warna set mood. Kuncinya satu je... konsisten. Pilih palet yang kecil, dan guna benda yang sama berulang kali.

**[VISUAL]** Highlight kad Typography (Aa, Heading 1, Heading 2, Body).
> Typography pula tentang mudah dibaca. Kita guna hierarki. Heading satu paling besar dan tebal. Heading dua lebih kecil. Body text untuk ayat biasa.
> Bila hierarki jelas, mata user tahu nak baca apa dulu.

**[VISUAL]** Playground 06A.
> Jom ke playground. Awak boleh pilih H1 sampai H4, atau P1 dan P2.
> Coach pilih H1... besarkan saiz... tambah weight. Nampak lebih tegas.
> Sekarang P1. Coach naikkan line height sikit. Tengok, perenggan jadi lebih selesa dibaca.

**[VISUAL]** Tab Prompt.
> Macam biasa, tab Prompt dah sediakan ayat untuk AI. Copy je.

**[VISUAL]** Recap.
> Warna... konsisten. Tulisan... ada hierarki. Cuba ubah setiap level tulisan sampai Awak rasa ia jelas, beza, dan senang dibaca.

### Bahagian B — Radius, Shadow & Glow

**[VISUAL]** Slide 06, highlight Border & Radius.
> Tiga benda kecil ni buat UI nampak moden dalam sekelip mata.
> Pertama... border radius. Ini bucu kotak. Radius kecil nampak tegas dan formal. Radius besar nampak lembut dan mesra.

**[VISUAL]** Highlight Shadow.
> Kedua... shadow. Bayang. Dia bagi rasa dalam, macam card tu terapung atas page. Ini bantu pisahkan satu bahagian dengan yang lain.

**[VISUAL]** Highlight Outer Glow.
> Ketiga... outer glow. Cahaya di keliling elemen. Guna untuk tarik perhatian, contohnya pada button utama.

**[VISUAL]** Playground 06B.
> Jom cuba. Coach tukar radius dari kecil ke besar... tengok perubahan rasa dia.
> Sekarang tambah shadow. Card terus nampak timbul.
> Last sekali, glow. Tapi ingat... sikit dah cukup. Kalau terlalu banyak, nampak murah.

**[VISUAL]** Teks: "Kurang itu lebih."
> Tip Coach... guna radius yang sama untuk semua elemen. Shadow yang lembut. Dan glow hanya pada satu benda paling penting.

---

## VIDEO 07 — Button States & Variants
**Slide:** 07 · **Playground:** 07A · **Durasi:** ~3 min
**Objektif:** Awak kenal 5 state dan 6 variant button.

**[VISUAL]** Slide 07, bahagian Button States.
> Button nampak simple. Tapi button yang bagus sentiasa bagitahu user apa yang sedang berlaku. Itu dipanggil state.
> Ada lima. Default... keadaan biasa. Hover... bila mouse di atas. Active... masa sedang ditekan. Focus... bila dipilih guna keyboard. Dan disabled... tak boleh ditekan.

**[VISUAL]** Bahagian Button Variants.
> Lepas tu variant. Gaya berbeza untuk tujuan berbeza.
> Primary untuk tindakan utama, macam Save. Secondary untuk yang kurang penting, macam Cancel. Outline untuk pilihan alternatif. Ghost untuk gaya paling minimal. Danger untuk tindakan bahaya, macam Delete. Dan Success untuk tindakan positif.

**[VISUAL]** Playground 07A.
> Ni button betul. Cuba hover... nampak berubah. Klik... nampak ditekan. Sekarang tekan Tab di keyboard... nampak garisan focus. Ini penting untuk user yang guna keyboard.
> Awak juga boleh paksa satu state, supaya senang tengok setiap satu.

**[VISUAL]** Contoh skrin: satu Primary + satu Secondary sebelah-menyebelah.
> Tip Coach... dalam satu skrin, hanya ada satu Primary button. Kalau semua button nampak penting... tak ada yang penting.

---

## VIDEO 08 — Component States & Feedback
**Slide:** 08 · **Playground:** 08A · **Durasi:** ~2.5 min
**Objektif:** Awak faham setiap tindakan user perlukan feedback.

**[VISUAL]** Slide 08.
> Bayangkan Awak tekan button Save... dan tak ada apa berlaku. Awak tekan lagi. Dan lagi. Itulah masalah UI tanpa feedback.
> Ada lima jenis feedback yang Awak kena tahu.

**[VISUAL]** Highlight setiap kad.
> Loading... bagitahu sesuatu sedang diproses.
> Success... sahkan tindakan berjaya. "Changes have been saved."
> Error... bagitahu ada masalah, dan apa nak buat.
> Empty state... bila tak ada data lagi. Jangan biar skrin kosong. Bagi panduan, macam "tambah item pertama Awak."
> Dan Information... maklumat penting, contohnya session nak tamat.

**[VISUAL]** Playground 08A.
> Jom cuba. Coach tukar ke loading... ke success... ke error... ke empty. Nampak tak? Setiap satu ada warna dan icon sendiri.

**[VISUAL]** Recap.
> Bila Awak minta AI bina apa-apa feature, jangan lupa sebut state ni. Contoh: "tambah loading, success, error dan empty state." Satu ayat je, tapi UI terus jadi lebih matang.

---

## VIDEO 09 — Navigation Components
**Slide:** 09 · **Playground:** 09A, 09B · **Durasi:** ~4.5 min
**Objektif:** Satu video untuk seluruh slide 09 — Bahagian A, kemudian Bahagian B.

### Bahagian A — Desktop Navigation

**[VISUAL]** Slide 09, highlight Header.
> Navigation ialah peta website Awak. Kalau user sesat, dia akan keluar.
> Bermula dengan Header. Bahagian paling atas. Biasanya ada logo, search bar, dan tindakan user macam notification dan profile.

**[VISUAL]** Highlight Navbar.
> Navbar pula senarai link utama. Home, Products, Services, About, Contact. Dan penting... tunjuk page mana user sedang berada. Itu dipanggil active state.

**[VISUAL]** Highlight Breadcrumb.
> Breadcrumb tunjuk lokasi user. Home, Products, Category, Product Name. Macam jejak roti... supaya user tahu jalan balik.

**[VISUAL]** Playground 09A.
> Jom cuba. Coach klik Products... tengok active state berpindah. Klik About... berpindah lagi.

**[VISUAL]** Recap.
> Header untuk identiti. Navbar untuk bergerak. Breadcrumb untuk tahu lokasi. Pastikan semuanya pendek dan jelas.

### Bahagian B — Mobile Menu & Sidebar

**[VISUAL]** Slide 09, highlight Mobile Header.
> Di phone, skrin kecil. Lima link tak muat. Jadi kita guna Mobile Header. Logo lebih kecil, icon search, dan hamburger menu. Icon tiga garis ni.

**[VISUAL]** Highlight Sidebar.
> Untuk dashboard atau web app, kita guna Sidebar. Navigation menegak di kiri. Dikumpul ikut bahagian, ada icon, ada label, dan ada active state.

**[VISUAL]** Playground 09B.
> Tengok ni. Coach tekan hamburger... drawer keluar dari tepi. Tekan lagi... dia tutup.
> Sekarang sidebar. Klik Orders... klik Customers. Active state ikut sama.

**[VISUAL]** Recap.
> Website biasa di phone... hamburger. Web app dan dashboard... sidebar. Bila Awak prompt AI, sebut terus: "guna sidebar di kiri dengan icon dan label."

---

## VIDEO 10 — Form Components
**Slide:** 10 · **Playground:** 10A · **Durasi:** ~3 min
**Objektif:** Awak tahu bila guna setiap jenis input.

**[VISUAL]** Slide 10.
> Form ialah tempat user bercakap dengan aplikasi Awak. Login, register, checkout... semua guna form. Jom kenal lima komponen.

**[VISUAL]** Highlight setiap kad.
> Input field... untuk tulisan pendek. Nama, email, password.
> Select atau dropdown... bila ada senarai pilihan.
> Checkbox dan radio. Checkbox boleh pilih banyak. Radio hanya pilih satu.
> Toggle atau switch... untuk on dan off. Biasa dalam settings.
> Dan textarea... untuk tulisan panjang, macam mesej.

**[VISUAL]** Playground 10A.
> Semua kawalan dalam playground ni berfungsi. Coach taip nama... pilih dropdown... tanda checkbox... pilih radio... on-kan toggle... dan cuba upload fail.

**[VISUAL]** Teks: "Checkbox = banyak · Radio = satu"
> Kesilapan biasa beginner... guna checkbox untuk soalan yang hanya ada satu jawapan. Ingat... satu jawapan, guna radio.

---

## VIDEO 11 — Common UI Components
**Slide:** 11 · **Playground:** 11A, 11B · **Durasi:** ~4.5 min
**Objektif:** Satu video untuk seluruh slide 11 — Bahagian A, kemudian Bahagian B.

### Bahagian A — Card & Badge

**[VISUAL]** Slide 11, highlight Card.
> Card ialah bekas untuk kumpulkan content yang berkaitan. Contoh product card ni. Gambar, tajuk, penerangan, harga... dan button tindakan.

**[VISUAL]** Highlight Badge.
> Badge pula label kecil. New, Popular, Sale. Atau status macam Success, Warning, Danger.
> Peraturannya... pendek. Satu atau dua perkataan. Dan warna mesti konsisten. Merah sentiasa bahaya, hijau sentiasa berjaya.

**[VISUAL]** Playground 11A.
> Jom bina. Coach ubah spacing dalam card... ubah bucu... tambah shadow. Sekarang tambah badge "New" di atas.

**[VISUAL]** Recap.
> Card yang bagus... kemas, ada ruang, dan satu tindakan yang jelas. Badge yang bagus... pendek dan warna bermakna.

### Bahagian B — Alert, Tabs & Tooltip

**[VISUAL]** Slide 11, highlight Alert.
> Alert untuk mesej penting. Info, success, warning dan error. Setiap satu ada warna dan icon sendiri. Mesej pendek, dan bagi user pilihan untuk tutup.

**[VISUAL]** Highlight Tabs.
> Tabs untuk tukar content dalam satu tempat. Overview, Features, Pricing, Reviews. Tab yang aktif mesti nampak jelas.

**[VISUAL]** Highlight Tooltip.
> Tooltip pula bantuan kecil yang keluar bila hover atau focus. Sesuai untuk icon dan form field.

**[VISUAL]** Playground 11B.
> Coach tukar jenis alert... klik tab Features... klik Pricing. Sekarang hover pada icon tanda soal... tooltip keluar.

**[VISUAL]** Recap.
> Alert... untuk mesej. Tabs... untuk susun content. Tooltip... untuk bantuan ringkas.

---

## VIDEO 12 — Modals, Loading & Notifications
**Slide:** 12 · **Playground:** 12A, 12B · **Durasi:** ~4.5 min
**Objektif:** Satu video untuk seluruh slide 12 — Bahagian A, kemudian Bahagian B.

### Bahagian A — Modal & Notification

**[VISUAL]** Slide 12, highlight Modal.
> Modal ialah kotak yang keluar di tengah skrin, tanpa tukar page. Guna untuk pengesahan penting. Contoh... "Delete item? Are you sure?"
> Mesej pendek. Dan dua button yang jelas. Cancel, dan Delete dalam warna merah.

**[VISUAL]** Highlight Notifications.
> Notification, atau toast, pula mesej kecil yang keluar sekejap, kemudian hilang sendiri. Success, error, warning, info.

**[VISUAL]** Playground 12A.
> Coach klik icon tong sampah... modal keluar. Coach tekan Cancel... tak jadi. Klik lagi, tekan Delete... item hilang.
> Sekarang dari panel kiri, Coach tembak toast. Success... error... warning.

**[VISUAL]** Recap.
> Modal... bila user kena buat keputusan. Toast... bila Awak cuma nak bagitahu. Jangan guna modal untuk perkara kecil. Ia ganggu user.

### Bahagian B — Loading, Skeleton & Lazy Load

**[VISUAL]** Slide 12, highlight Loading States.
> Bila data tengah dimuatkan, user perlu tahu sesuatu sedang berlaku. Kalau tak, dia ingat aplikasi rosak.

**[VISUAL]** Playground 12B, tunjuk setiap satu.
> Ada empat cara.
> Spinner... bulatan berpusing. Untuk proses pendek.
> Progress bar... tunjuk peratus. Sesuai untuk upload atau proses panjang.
> Skeleton... bentuk kelabu yang tiru layout sebenar sebelum data sampai. Ini rasa paling laju.
> Dan lazy load... gambar di bawah skrin hanya dimuatkan bila user scroll sampai situ. Page jadi lebih ringan.

**[VISUAL]** Recap.
> Bila prompt AI untuk page yang ada data, cuba tambah: "guna skeleton masa loading, dan lazy load untuk gambar." Page Awak terus nampak lebih profesional.

---

## VIDEO 13 — Layout Components
**Slide:** 13 · **Playground:** 13A, 13B · **Durasi:** ~4.5 min
**Objektif:** Satu video untuk seluruh slide 13 — Bahagian A, kemudian Bahagian B.

### Bahagian A — Flexbox

**[VISUAL]** Slide 13, highlight Flexbox.
> Flexbox ialah cara susun item dalam satu baris... atau satu lajur. Paling sesuai untuk navbar dan toolbar.
> Contoh navbar ni. Logo di kiri, menu di tengah, button Sign In di kanan. Semua tu flexbox.

**[VISUAL]** Playground 13A.
> Jom cuba. Coach tukar arah dari row ke column... item tersusun menegak.
> Balik ke row. Sekarang Coach tukar susunan... kiri... tengah... kanan... dan space between, item tersebar sama rata.
> Last, gap. Ini jarak antara item. Coach besarkan... item jadi lebih lega.

**[VISUAL]** Tab Prompt.
> Playground ni akan tukarkan setting Awak jadi prompt. Copy dan guna.

**[VISUAL]** Recap.
> Satu arah, baris atau lajur... fikir flexbox.

### Bahagian B — Grid & Container

**[VISUAL]** Slide 13, highlight Grid.
> Kalau flexbox untuk satu arah, grid untuk dua arah. Baris dan lajur serentak. Sesuai untuk senarai card, gallery, atau dashboard.

**[VISUAL]** Highlight Container.
> Container pula kotak yang hadkan lebar content. Kenapa perlu? Sebab di skrin besar, kalau tulisan memanjang dari hujung ke hujung... penat nak baca. Container kekalkan content di tengah, dengan lebar maksimum yang selesa.

**[VISUAL]** Playground 13B.
> Coach tukar bilangan lajur... dua... tiga... empat. Tambah item. Ubah gap.
> Sekarang Coach ubah max width container. Tengok... content kekal di tengah.

**[VISUAL]** Teks: "Flexbox = 1 arah · Grid = 2 arah"
> Satu arah... flexbox. Baris dan lajur... grid. Dan sentiasa balut dengan container.

### Bahagian C — Section / Hero & Divider & Spacing

**[VISUAL]** Slide 13, highlight Section / Hero ("Grow Your Business").
> Dua lagi layout component. Pertama... section, atau hero. Ini bahagian besar untuk content utama. Strukturnya jelas... tulisan, gambar, dan satu CTA, macam button Get Started. Dan bagi ruang yang cukup.

**[VISUAL]** Highlight Divider & Spacing.
> Kedua... divider dan spacing. Divider ialah garisan yang pisahkan section. Spacing pula jarak, guna margin dan padding yang Awak dah belajar. Kuncinya... konsisten. Jarak antara section mesti sama.

**[VISUAL]** Recap lima kad slide 13.
> Container, grid, flexbox, section, dan spacing. Lima benda ni... asas setiap layout yang Awak akan bina.

---

## VIDEO 14 — Layout Patterns
**Slide:** 14 · **Playground:** 14A · **Durasi:** ~2.5 min
**Objektif:** Awak kenal pattern layout biasa dan nama dia untuk prompt.

**[VISUAL]** Slide 14.
> Kebanyakan website sebenarnya guna pattern yang sama. Bila Awak tahu nama pattern ni, prompt Awak jadi lebih tepat.

**[VISUAL]** Highlight setiap pattern.
> Grid layout... beberapa lajur dengan jarak sama. Contoh: empat card sebaris.
> Row layout... section disusun menegak, satu atas satu.
> Column layout... content dibahagi sebelah-menyebelah. Contoh: sidebar di kiri, main content di kanan.

**[VISUAL]** Playground 14A.
> Dalam playground ni, Coach pilih satu pattern... dan sekarang tengok versi mobile. Nampak? Lajur jadi satu, tersusun ke bawah.

**[VISUAL]** Recap.
> Daripada cakap "susun cantik-cantik", cakap terus: "sidebar kiri, main content kanan, card dalam grid empat lajur." AI terus faham.

---

## VIDEO 15 — Page Layout Structure
**Slide:** 15 · **Playground:** 15A · **Durasi:** ~2.5 min
**Objektif:** Awak boleh namakan 6 bahagian page.

**[VISUAL]** Slide 15, highlight dari atas ke bawah.
> Hampir semua website moden ada struktur yang sama. Dari atas ke bawah.
> Satu... Top Header. Optional. Untuk pengumuman, macam "free shipping."
> Dua... Header. Logo, menu, search dan tindakan user.
> Tiga... Hero section. Banner utama dengan headline, visual, dan call to action.
> Empat... Main content. Isi page. Features, produk, artikel.
> Lima... Main footer. Link, contact, social media.
> Enam... Footer bottom. Copyright, privacy policy dan terms.

**[VISUAL]** Playground 15A.
> Coach hover setiap bahagian... nama dia keluar. Sekarang Coach tutup top header... tutup hero... tengok macam mana page berubah.

**[VISUAL]** Recap.
> Bila prompt AI untuk landing page, senaraikan bahagian ikut urutan ni. Hasilnya lebih tersusun.

---

## VIDEO 16 — Responsive Breakpoint
**Slide:** 16 · **Playground:** 16A · **Durasi:** ~3 min
**Objektif:** Awak faham 4 breakpoint dan navigation responsive.

**[VISUAL]** Slide 16, bahagian Breakpoint.
> Lebih separuh user buka website guna phone. Jadi UI Awak mesti cantik di semua saiz skrin. Caranya... breakpoint.
> Desktop... seribu dua ratus lapan puluh piksel ke atas. Menu penuh, banyak lajur.
> Laptop... seribu dua puluh empat hingga seribu dua ratus tujuh puluh sembilan. Menu penuh, spacing disesuaikan.
> Tablet... tujuh ratus enam puluh lapan hingga seribu dua puluh tiga. Navigation diringkaskan, section disusun.
> Mobile... tujuh ratus enam puluh tujuh ke bawah. Hamburger menu, satu lajur, dan butang lebih besar untuk jari.

**[VISUAL]** Bahagian Responsive Navigation.
> Navigation pun berubah. Skrin besar... tunjuk semua menu. Tablet dan phone... hamburger, dan simpan icon yang penting sahaja.

**[VISUAL]** Playground 16A.
> Coach tarik handle ni dari besar ke kecil... tengok layout dan navbar berubah. Atau pilih terus device. Desktop... tablet... mobile.

**[VISUAL]** Recap.
> Setiap kali prompt AI, tambah satu ayat: "pastikan responsive untuk mobile, guna hamburger menu." Lepas tu, sentiasa test di saiz phone.

---

## VIDEO 17 — Essential Pages untuk SaaS
**Slide:** 17 · **Latihan mini** · **Durasi:** ~2 min
**Objektif:** Awak tahu page asas SaaS dan boleh rancang page untuk projek sendiri.

**[VISUAL]** Slide 17, enam kad.
> Kalau Awak nak bina SaaS, ini enam page yang paling biasa.
> Landing page... perkenalkan produk dan tarik user.
> Login dan register... untuk daftar dan masuk.
> User dashboard... ringkasan dan aktiviti user.
> Admin panel... urus user, data dan sistem.
> Profile dan settings... user urus akaun sendiri.
> Dan pricing dan subscription... pelan harga dan langganan.

**[VISUAL]** Highlight nota.
> Tapi ingat... bukan semua SaaS perlukan semua page ni. Ikut feature dan target user Awak.

**[VISUAL]** Skrin latihan: senarai semak kosong.
> Latihan untuk Awak. Fikir satu idea SaaS. Tulis page mana yang Awak perlukan, dan satu ayat apa fungsi setiap page. Itulah pelan pertama Awak sebelum minta AI bina.

---

## VIDEO 18 — Cara Cari UI Inspiration
**Slide:** 18 · **Latihan mini** · **Durasi:** ~2 min
**Objektif:** Awak tahu 3 tempat cari rujukan UI.

**[VISUAL]** Slide 18.
> Designer yang hebat pun tak mula dari kosong. Mereka cari rujukan dulu. Coach kongsi tiga tempat.

**[VISUAL]** Highlight Pinterest.
> Pinterest... untuk cari gaya dan buat moodboard. Bagus untuk idea warna dan rasa keseluruhan.

**[VISUAL]** Highlight Dribbble.
> Dribbble... design UI kualiti tinggi. Bagus untuk tengok component dan pattern moden.

**[VISUAL]** Highlight ChatGPT.
> Dan ChatGPT... untuk brainstorm. Contoh, tanya: "bagi idea UI dashboard SaaS untuk project management tool."

**[VISUAL]** Skrin latihan.
> Latihan. Cari tiga UI yang Awak suka untuk idea SaaS tadi. Simpan screenshot. Kita akan guna dalam video seterusnya.

---

## VIDEO 19 — Dari UI Reference ke AI Prompt
**Slide:** 19 · **Playground:** 19A Prompt Builder · **Durasi:** ~3 min
**Objektif:** Awak boleh tukar gambar rujukan jadi prompt yang tepat.

**[VISUAL]** Slide 19, tiga langkah.
> Ni bahagian paling penting. Macam mana nak tukar gambar yang Awak suka... jadi arahan yang AI faham.
> Tiga langkah. Cari rujukan. Terangkan dengan jelas. Dan dapatkan UI.

**[VISUAL]** Zoom pada contoh prompt BM.
> Tengok contoh prompt ni. Dia tak cakap "buat dashboard cantik." Dia senaraikan apa yang perlu ada. Sidebar di kiri dengan icon dan label. Search bar dan avatar. Stat cards. Line chart. Recent activity. Team members.
> Lepas tu dia terangkan gaya. Sidebar gelap, content cerah, card bucu bulat, warna ungu-biru. Dan last... responsive.

**[VISUAL]** Teks formula: "Apa nak buat + Bahagian + Gaya + Responsive"
> Formula dia senang. Apa nak buat... bahagian apa... gaya macam mana... dan responsive.
> Perasan tak? Semua perkataan dalam prompt ni... sidebar, card, radius, responsive... Awak dah belajar dalam video-video sebelum ni.

**[VISUAL]** Playground 19A.
> Kalau Awak masih tak pasti, guna Prompt Builder. Pilih jenis page... pilih bahagian... pilih gaya. Prompt siap. Copy, dan paste dalam AI.

---

## VIDEO 20 — UI Debugging & Mini Challenge
**Slide:** 20 · **Playground:** 20A Fix the UI · **Durasi:** ~3.5 min
**Objektif:** Awak boleh kesan masalah UI dan minta AI betulkan dengan tepat.

**[VISUAL]** Slide 20, empat langkah.
> AI tak sempurna. Kadang-kadang UI yang dia buat ada masalah. Jadi Awak kena tahu debug. Empat langkah.
> Inspect... tengok UI dan guna browser inspect tool.
> Identify... cari masalah tepat. Alignment, spacing, overflow, atau responsive.
> Fix... minta AI betulkan dengan ayat yang spesifik.
> Verify... semak hasil di pelbagai saiz skrin.

**[VISUAL]** Playground 20A.
> Sekarang challenge. Card ni ada lima bug UI. Pause video, dan cuba cari sendiri dulu.

**[VISUAL]** Teks "PAUSE" 3 saat.

**[VISUAL]** Klik setiap bug satu-satu.
> Okay, jom semak.
> Satu... padding tak sama di setiap sisi.
> Dua... tulisan kelabu atas card gelap. Kontras rendah, susah baca.
> Tiga... dua button tak sejajar dan tinggi tak sama.
> Empat... jarak antara senarai feature tak sekata.
> Lima... bucu card, input dan button semua lain-lain.

**[VISUAL]** Prompt yang terhasil dalam playground.
> Bila Awak dah jumpa bug, playground terus bina prompt untuk betulkan. Tengok... setiap bug diterangkan dengan tepat. Itulah cara prompt untuk debug.
> Berapa bug Awak jumpa? Kalau lima... tahniah. Mata UI Awak dah terlatih.

---

## Keputusan yang dah dikunci

1. **Satu video = satu tajuk slide (bukan sub tajuk).** Slide konsep + semua playground slide tu dalam satu video (Bahagian A / B).
2. **Bahasa:** VO BM, slide English, term penting sebut English.
3. **Slide tanpa playground** (Why UI, Box Model, SaaS Pages, Inspiration): tak perlu buat playground baru.
4. **Wajib guna content slide & playground sedia ada** dari `index.html`. Tiada visual baru yang bercanggah dengan deck.
5. **Tiada video** untuk 01 Title, 02 Meet Your Trainer, 00 Agenda, 21 Q&A dan 22 Thank You.
6. **Tool:** HyperFrames, voice ElevenLabs "Mikhail" (ms-malaysian).
