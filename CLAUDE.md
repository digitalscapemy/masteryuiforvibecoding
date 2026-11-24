# masteryui — peta projek

Folder ni pegang 2 kelas, 1 tutorial dan beberapa video pendek. Setiap projek duduk dalam foldernya sendiri: skrip/slide di atas, projek video dalam `video/` (atau `videos/`). Sebelum edit, pastikan edit **sumber** (bukan salinan / export / `_archive`).

```
index.html, login.html, slides/, Dockerfile, deploy/   deck kelas UI + deploy (kekal di root)
courses/ui-mastery/          kelas Mastering UI for Vibe Coding
courses/github-power-skills/ kelas GitHub Power Skills for Vibe Coders
tutorials/wsl-docker/        tutorial WSL + Docker
short-videos/                stiker-material, skrill-microstock, vibe-fbads, remotion-wow
drafts/                      draf kelas Cloudflare (sedang ditulis)
_archive/                    versi lama (ignored) — jangan edit, rujukan sahaja
OpenMontage/                 repo luar (ignored)
```

Semua VO: ElevenLabs voice "Mikhail" (`6olOdhsgLdwwt9DbIIyp`), model `eleven_v4`.

## 1. Kelas GitHub Power Skills for Vibe Coders (AKTIF) — `courses/github-power-skills/`

| Apa | Sumber (edit sini) | Nota |
|---|---|---|
| Slide | `slides/github-slide-XX.html` | 19 slide, susunan dalam `SLIDES` di `slides/github-deck.html` |
| Deck (tayang) | `slides/github-deck.html` | preview: launch config `drafts` → http://localhost:8765/github-deck.html |
| Shared CSS/JS slide | `slides/assets/` (`base.css`, `base.js`, `dock.css`, `slide-no.js`) | lepas edit: `python tools/inline.py` dari `slides/` |
| VO (skrip) | `github-ecourse-vo.md` | klip c1–c39 (tiada c36); ID ElevenLabs dalam `video/.vo-ids.txt` |
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
| Deck kelas | `index.html` di root (satu file besar) + gambar `slides/01, 02, 21, 22.png` |
| Thumbnail | `courses/ui-mastery/thumbnails/NN-*.png` |
| Skrip video | `courses/ui-mastery/DRAFT-skrip-video.md` (rujukan) dan `videos/NN-*/VO.md` (sumber per video) |
| Video | `courses/ui-mastery/videos/01-welcome` … `20-ui-debugging`, helper `videos/_kit/` (`build.py`, `kit.js`, `index.tpl`, `AGENT-BRIEF.md`) |
| Deploy | `Dockerfile` + `deploy/` (nginx, password `DECK_PASSWORD`), hanya `index.html`, `login.html`, `slides/` |

Video ambil slide terus dari root `index.html`: dalam folder video, `python -I ../_kit/build.py` (video 05: `python -I build.py`). Jangan tukar `data-name` section tanpa kemas `video.json`.
Gaya VO: "Coach" + "Awak"; jangan guna "elemen", "lega", "bekas"; jangan sebut tab "AI Prompt"; nombor ditulis dalam perkataan.

## 3. Tutorial WSL + Docker — `tutorials/wsl-docker/`

| Video | Build (dalam `video/`) | Skrip / VO |
|---|---|---|
| WSL + Docker | `python -I build.py` → `export/WSL-Docker-VO.mp4` (`vo/vNN.mp3`) | `wsl-docker-vo.md` |
| Sambungan Docker | `python -I build.py sambungan_cfg.py` → `export/Sambungan-Docker-VO.mp4` (`vo/sNN.mp3`) | `sambungan-docker-vo.md` |
| Intro WSL | `video/intro/` (HyperFrames, launch config `wsl-intro`), guna `v01b.mp3` | sedang dibuat |

`export/WSL-Docker-Full-VO.mp4` = dua video di atas digabung. Sumber rakaman: `Downloads/WSL Dockers.mp4`.
Versi VO yang dipakai: `v08b`, `v13b` (`v08`, `v13` lama dalam `_archive/`). `v01` dalam video penuh, `v01b` dalam intro.

## 4. Video pendek — `short-videos/`

| Video | Folder | Skrip / VO | Status |
|---|---|---|---|
| Stiker material | `stiker-material/video/` (v2, VO ElevenLabs), `video-asal/` (suara asal) | `stiker-material/stiker-material-v2.md` | siap |
| Skrill microstock | `skrill-microstock/video/` (`scripts/build.py`, satu `assets/vo/vo.wav`) | `skrill-microstock/paypal-skrill-multi-email.md`, logo dalam `plan-assets/` | siap |
| FB ads Vibe Coding Fighter | `vibe-fbads/video/` (render terbaru `v3-60fps`), `video-square/` (belum render) | talking-head, tiada VO ElevenLabs | |
| Remotion test | `remotion-wow/video/` | | eksperimen |

## Jangan edit
- `_archive/`, `renders/`, `export/` (hasil render), `OpenMontage/` (repo luar).
- Folder `video/`, `videos/`, `_archive/`, `OpenMontage/` di-gitignore; skrip, slide dan thumbnail masuk git.

## Isu diketahui
- Nama file export ikut kedudukan dalam `lessons.json` (01, 02…) + `file[3:]`, bukan medan `no`. Jadi lesson `no: "00"` jadi `01-Welcome-...mp4`. Ini normal. Tanpa `--render`, export skip lesson yang file dia dah ada.
- Python `http.server` (preview slide) boleh bagi slide lama dari cache browser; reload dengan `?v=` kalau edit tak nampak.
