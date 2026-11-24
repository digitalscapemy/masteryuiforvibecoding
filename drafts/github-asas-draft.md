# DRAFT — Kelas Asas GitHub untuk Vibe Coder

> Sasaran: vibe coder beginner (guna AI macam Claude Code / Cursor / Lovable untuk buat app).
> Gaya: santai, BM + istilah English, satu idea satu slide. Tak perlu hafal command — AI boleh buat, tapi kena **faham apa yang jadi**.

---

## 01 · Cover
**Asas GitHub untuk Vibe Coder**
Simpan, backup & share projek kau — tanpa takut code hilang.

---

## 02 · Kenapa Kena Tahu GitHub?
Pernah jadi tak?
- App kau dah cantik, lepas tu suruh AI tambah satu benda je… tiba-tiba semua tak jalan. Nak balik macam tadi pun tak ingat 😭
- Simpan fail macam ni: `website_final.zip`, `website_final_v2.zip`, `website_FINAL_betul.zip`
- Laptop hilang atau rosak, semua kerja berminggu-minggu lenyap
- Nak letak website online, tapi semua orang cakap "upload ke GitHub dulu"

**GitHub = butang "undo" + backup online untuk projek kau.**

---

## 03 · Git vs GitHub (Beza Paling Penting)
| | **Git** | **GitHub** |
|---|---|---|
| Apa dia | Tool dalam laptop | Website (cloud) |
| Fungsi | Rekod setiap perubahan code | Simpan & share code online |
| Analogi | **Save game** | **Google Drive** untuk save game |

> Git = rekod. GitHub = tempat simpan rekod tu online.

---

## 04 · Analogi: Save Game 🎮
- Main game → sampai checkpoint → **SAVE**
- Kalah kat boss → **load balik** save tadi
- Sama macam code: sebelum suruh AI buat benda besar → **save dulu (commit)**
- AI rosakkan → **patah balik** ke save lama

---

## 05 · 5 Istilah Wajib Tahu
| Istilah | Maksud mudah |
|---|---|
| **Repository (repo)** | Folder projek kau |
| **Commit** | Save point + nota apa yang berubah |
| **Push** | Upload commit dari laptop → GitHub |
| **Pull** | Download perubahan terbaru dari GitHub → laptop |
| **Branch** | Salinan projek untuk test idea tanpa kacau yang asal |

---

## 06 · Flow Asas (Gambar Ringkas)
```
Edit code  →  Commit (save)  →  Push (upload)  →  GitHub ☁️
                                                     ↓
                                    Deploy (Vercel / Netlify)
```
Ulang benda sama setiap kali siap satu feature.

---

## 07 · Setup (Sekali Je)
1. Daftar akaun di **github.com**
2. Install **Git** (atau **GitHub Desktop** kalau tak suka terminal)
3. Login GitHub dalam tool AI / editor kau (VS Code, Cursor, Claude Code)
4. Siap ✅

---

## 08 · Cara Paling Mudah: Suruh AI Buat
Kau tak perlu taip command. Cukup bagi prompt:
- *"Init git untuk projek ni dan buat first commit"*
- *"Buat repo baru kat GitHub nama `my-app` dan push"*
- *"Commit semua perubahan dengan mesej yang jelas"*
- *"Undo perubahan terakhir, balik ke commit sebelum ni"*

> Tapi baca dulu apa AI nak buat sebelum tekan **Allow**.

---

## 09 · Commit Message yang Bagus
❌ `update`, `fix`, `asdf`
✅ `Tambah butang login`, `Betulkan navbar mobile`, `Tukar warna hero section`

**Tip:** Commit kecil & kerap. Satu feature = satu commit.

---

## 10 · ⚠️ JANGAN Push Benda Ni!
- File **`.env`** (API key, password, secret)
- Folder **`node_modules`**
- Data peribadi customer

Guna fail **`.gitignore`** — senarai fail yang Git kena abaikan.
> API key bocor kat GitHub = boleh kena caj beribu ringgit. Bot scan GitHub 24 jam.

---

## 11 · Branch: Test Tanpa Takut
```
main  ────●────●────────────●──  (versi stabil)
               \           /
feature         ●───●───●     (test idea baru)
```
- `main` = versi yang dah OK / live
- Buat branch baru untuk feature besar
- Jadi? **Merge** masuk main. Gagal? Buang je branch tu.

---

## 12 · Bila AI Rosakkan Code — Macam Mana?
1. Tengok **Changes / Diff** — apa yang berubah
2. Belum commit? → *Discard changes*
3. Dah commit? → suruh AI: *"Revert commit terakhir"*
4. Sebab tu: **commit SEBELUM suruh AI buat perubahan besar**

---

## 13 · Bonus: Deploy dari GitHub
- Sambung repo ke **Vercel / Netlify / GitHub Pages**
- Setiap kali **push** → website auto update 🚀
- Tiada lagi upload fail manual

---

## 14 · Cheat Sheet (Simpan Ni)
| Nak buat apa | Command | Prompt AI |
|---|---|---|
| Mula track projek | `git init` | "Init git" |
| Save | `git add . && git commit -m "..."` | "Commit perubahan ni" |
| Upload | `git push` | "Push ke GitHub" |
| Ambil terbaru | `git pull` | "Pull perubahan terbaru" |
| Tengok status | `git status` | "Apa yang dah berubah?" |
| Branch baru | `git checkout -b nama` | "Buat branch baru untuk X" |

---

## 15 · Mini Challenge 🏆
1. Buat repo baru kat GitHub
2. Suruh AI buat landing page simple
3. Commit + push
4. Ubah warna butang → commit lagi
5. Revert ke versi asal
6. (Bonus) Deploy ke Vercel & share link

---

## 16 · Penutup
**Commit kerap. Push selalu. Jangan push `.env`.**
Dengan GitHub, kau boleh eksperimen dengan AI tanpa takut.
