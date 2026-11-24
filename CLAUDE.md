# masteryui — peta projek

Folder ni pegang 3 kelas (satu masih draf), 1 tutorial dan beberapa video pendek. Setiap projek duduk dalam foldernya sendiri dengan susunan sama: skrip VO `vo.md` (atau `vo-*.md`, `plan.md`), `slides/` atau `deck/`, dan projek video dalam `video/` (atau `videos/`). Sebelum edit, pastikan edit **sumber** (bukan salinan / export / `_archive`).

```
Dockerfile, deploy/          deploy deck kelas UI (kekal di root sebab platform deploy cari Dockerfile di sini)
courses/ui-mastery/          kelas Mastering UI for Vibe Coding (deck dalam deck/)
courses/github-power-skills/ kelas GitHub Power Skills for Vibe Coders
tutorials/wsl-docker/        tutorial WSL + Docker
short-videos/                stiker-material, skrill-microstock, vibe-fbads, remotion-wow
courses/cloudflare/          kelas Cloudflare for Vibe Coders (DRAF, baru content)
courses/hosting-tools/       video hosting tools (Netlify…Dokploy) untuk kelas beginner (DRAF: content + 32 slide)
_archive/                    versi lama (ignored) — jangan edit, rujukan sahaja
OpenMontage/                 repo luar (ignored)
```

Semua VO: ElevenLabs voice "Mikhail" (`6olOdhsgLdwwt9DbIIyp`), model `eleven_v4`.

## 1. Kelas GitHub Power Skills for Vibe Coders (AKTIF) — `courses/github-power-skills/`

| Apa | Sumber (edit sini) | Nota |
|---|---|---|
| Slide | `slides/github-slide-XX.html` | 19 slide, susunan dalam `SLIDES` di `slides/github-deck.html` |
| Deck (tayang) | `slides/github-deck.html` | preview: launch config `github-slides` → http://localhost:8765/github-deck.html |
| Shared CSS/JS slide | `slides/assets/` (`base.css`, `base.js`, `dock.css`, `slide-no.js`) | lepas edit: `python tools/inline.py` dari `slides/` |
| VO (skrip) | `vo.md` | klip c1–c39 (tiada c36); ID ElevenLabs dalam `video/.vo-ids.txt` |
| VO (audio) | `video/assets/vo/cNN.mp3` | lepas tukar: `python -I tools/timing.py` |
| Video | `video/` (HyperFrames) | |

**Video dibina DARI slide.** `video/tools/build.py` baca `../slides` dan tulis `compositions/*.html`. Jadi:
1. Edit slide dalam `slides/` (jangan edit `compositions/` terus, ia akan ditimpa).
2. `cd courses/github-power-skills/video && python -I tools/build.py`
3. `python -I tools/export.py --render <no>` untuk render semula lesson tu sahaja (mis. `09`).

Peta scene → klip VO → masa: `tools/scenes.json`, `tools/layout.txt`. Peta lesson → scene: `tools/lessons.json`.
Timing VO masuk ikut `cues/<scene>.js`. Scene terminal `t1`–`t6` dan `end` dibuat tangan dalam `cues/*.html`.
Export akhir: `video/export/NN-*.mp4` + `.png` + `youtube.txt`.

Gaya VO: BM, istilah teknikal English, "saya" / "Awak", tulis "file" bukan "fail", tiada caption.

## 2. Kelas Mastering UI for Vibe Coding (SIAP, Nov 2–4) — `courses/ui-mastery/`

| Apa | Sumber |
|---|---|
| Deck kelas | `courses/ui-mastery/deck/index.html` (satu file besar) + `deck/login.html` + gambar `deck/slides/01, 02, 21, 22.png` |
| Thumbnail | `courses/ui-mastery/thumbnails/NN-*.png` |
| Skrip video | `courses/ui-mastery/vo-draft.md` (rujukan) dan `videos/NN-*/VO.md` (sumber per video) |
| Video | `courses/ui-mastery/videos/01-welcome` … `20-ui-debugging`, helper `videos/_kit/` (`build.py`, `kit.js`, `index.tpl`, `AGENT-BRIEF.md`) |
| Deploy | `Dockerfile` + `deploy/` (nginx, password `DECK_PASSWORD`). `Dockerfile` di root COPY dari `courses/ui-mastery/deck/`. Kalau alih deck lagi, kemas `Dockerfile` sekali. |

Video ambil slide terus dari `deck/index.html`: dalam folder video, `python -I ../_kit/build.py` (video 05: `python -I build.py`). Jangan tukar `data-name` section tanpa kemas `video.json`.
Gaya VO: "Coach" + "Awak"; jangan guna "elemen", "lega", "bekas"; jangan sebut tab "AI Prompt"; nombor ditulis dalam perkataan.

## 3. Tutorial WSL + Docker — `tutorials/wsl-docker/`

| Video | Build (dalam `video/`) | Skrip / VO |
|---|---|---|
| WSL + Docker | `python -I build.py` → `export/WSL-Docker-VO.mp4` (`vo/vNN.mp3`) | `vo.md` |
| Sambungan Docker | `python -I build.py sambungan_cfg.py` → `export/Sambungan-Docker-VO.mp4` (`vo/sNN.mp3`) | `vo-sambungan.md` |
| Intro WSL | `video/intro/` (HyperFrames, launch config `wsl-intro`), guna `v01b.mp3` | sedang dibuat |

`export/WSL-Docker-Full-VO.mp4` = dua video di atas digabung. Sumber rakaman: `video/src/wsl-docker-original.mp4` (salinan dari `Downloads/WSL Dockers.mp4`), sambungan: `video/src/sambungan-blur.mp4`.
Versi VO yang dipakai: `v08b`, `v13b` (`v08`, `v13` lama dalam `_archive/`). `v01` dalam video penuh, `v01b` dalam intro.

## 4. Kelas Cloudflare for Vibe Coders (DRAF) — `courses/cloudflare/`

Baru ada `slide-content.md` (10 slide: tajuk, teks, idea visual, prompt AI). Bila mula buat slide, ikut susunan kelas GitHub: `slides/`, `vo.md`, `video/`.

## 4b. Hosting Tools for Vibe Coders (DRAF) — `courses/hosting-tools/`

Fakta & harga: `slide-content.md`. Slide **dijana**: edit teks dalam `slides/tools/data.py` (atau susun atur dalam `slides/tools/build.py`), kemudian `python -I tools/build.py` dari `slides/`. Jangan edit `hosting-slide-*.html` terus, ia akan ditimpa. Deck: launch config `hosting-slides` → http://localhost:8766/hosting-deck.html. Setiap tool 4 slide: `N` apa, `NA` pros & cons, `NB` framework + scale, `NC` kos + resources.

## 5. Video pendek — `short-videos/`

| Video | Folder | Skrip / VO | Status |
|---|---|---|---|
| Stiker material | `stiker-material/video/` (v2, VO ElevenLabs), `video-original/` (suara asal) | `stiker-material/vo.md` | siap |
| Skrill microstock | `skrill-microstock/video/` (`scripts/build.py`, satu `assets/vo/vo.wav`) | `skrill-microstock/plan.md`, logo dalam `plan-assets/` | siap |
| FB ads Vibe Coding Fighter | `vibe-fbads/video/` (render terbaru `v3-60fps`), `video-square/` (belum render) | talking-head, tiada VO ElevenLabs | |
| Remotion test | `remotion-wow/video/` | | eksperimen |

## Jangan edit
- `_archive/`, `renders/`, `export/` (hasil render), `OpenMontage/` (repo luar).
- Folder `video/`, `videos/`, `_archive/`, `OpenMontage/` di-gitignore; skrip, slide dan thumbnail masuk git.

## Isu diketahui
- Nama file export ikut kedudukan dalam `lessons.json` (01, 02…) + `file[3:]`, bukan medan `no`. Jadi lesson `no: "00"` jadi `01-Welcome-...mp4`. Ini normal. Tanpa `--render`, export skip lesson yang file dia dah ada.
- Python `http.server` (preview slide) boleh bagi slide lama dari cache browser; reload dengan `?v=` kalau edit tak nampak.
