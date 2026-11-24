# masteryui — peta projek

Folder ni pegang 2 kelas + beberapa video sampingan. Sebelum edit, pastikan edit **sumber** (bukan salinan / export / folder `old`).

## 1. Kelas GitHub Power Skills for Vibe Coders (AKTIF)

| Apa | Sumber (edit sini) | Nota |
|---|---|---|
| Slide | `drafts/github-slide-XX.html` | 19 slide, susunan dalam `SLIDES` di `drafts/github-deck.html` |
| Deck (tayang) | `drafts/github-deck.html` | preview: launch config `drafts` → http://localhost:8765/github-deck.html |
| Shared CSS/JS slide | `drafts/assets/` (`base.css`, `base.js`, `dock.css`, `slide-no.js`) | |
| Content asal | `drafts/github-slide-content.md`, `drafts/github-asas-draft.md` | rujukan, bukan sumber terkini |
| VO (skrip) | `video-scripts/github-ecourse-vo.md` | klip c1–c39; ID ElevenLabs dalam `videos/github-power-skills/.vo-ids.txt` |
| VO (audio) | `videos/github-power-skills/assets/vo/cNN.mp3` | |
| Video | `videos/github-power-skills/` (HyperFrames) | |

**Video dibina DARI slide drafts.** `tools/build.py` baca `../../drafts` dan tulis `compositions/*.html`. Jadi:
1. Edit slide dalam `drafts/` (jangan edit `compositions/` terus, ia akan ditimpa).
2. `cd videos/github-power-skills && python -I tools/build.py`
3. `python -I tools/export.py <no>` untuk render semula lesson tu sahaja (mis. `09`).

Peta scene → klip VO → masa: `tools/scenes.json`, `tools/layout.txt`. Peta lesson → scene: `tools/lessons.json`.
Timing VO masuk ikut `cues/<scene>.js`. Scene terminal `t1`–`t6` dan `end` dibuat tangan dalam `cues/*.html`.
Export akhir: `export/NN-*.mp4` + `.png` + `youtube.txt`. `export-old/` = versi lama, jangan guna.

Gaya VO: BM, istilah teknikal English, "saya" / "Awak", tulis "file" bukan "fail", tiada caption.

## 2. Kelas Mastering UI for Vibe Coding (SIAP, Nov 2–4)

| Apa | Sumber |
|---|---|
| Deck kelas | `index.html` (satu file besar) + gambar `slides/01–22.png` |
| Thumbnail | `thumbnails/NN-*.png` |
| Skrip video | `video-scripts/DRAFT-skrip-video.md` (rujukan) dan `videos/NN-*/VO.md` (sumber per video) |
| Video | `videos/01-welcome` … `videos/20-ui-debugging`, guna helper `videos/_kit/` (`build.py`, `kit.js`, `index.tpl`) |
| Deploy | `Dockerfile` + `deploy/` (nginx, password `DECK_PASSWORD`), hanya `index.html`, `login.html`, `slides/` |

## 3. Video sampingan

| Video | Folder | Skrip / VO | Status |
|---|---|---|---|
| WSL + Docker | `videos/wsl-docker/` (`build.py`, `vo/vNN.mp3`) | `video-scripts/wsl-docker-vo.md` | export ada |
| Sambungan Docker | `videos/wsl-docker/` (`python -I build.py sambungan_cfg.py`, `vo/sNN.mp3`) | `video-scripts/sambungan-docker-vo.md` | export ada |
| Intro WSL | `videos/wsl-docker/intro/` (HyperFrames, launch config `wsl-intro`) | guna `v01b.mp3` | sedang dibuat |
| Stiker material | `videos/stiker-material/` (v2), `stiker-material-asal/` (asal) | `video-scripts/stiker-material-v2.md` | siap |
| Skrill microstock | `videos/skrill-microstock/` | `video-scripts/paypal-skrill-multi-email.md` | |
| FB ads Vibe Coding Fighter | `videos/vibe-fbads/`, `vibe-fbads-square/` | | |
| Remotion test | `videos/remotion-wow/` | | eksperimen |

Versi VO yang dipakai dalam build WSL: `v08b`, `v13b` (bukan `v08`, `v13`). `v01` dalam video penuh, `v01b` dalam intro.

## Jangan edit
- `drafts/old/`, `export-old/`, `renders/`, `export/` (hasil render), `OpenMontage/` (repo luar, ignored).
- `videos/` dan `OpenMontage/` di-gitignore; `drafts/` dan kebanyakan `video-scripts/` belum di-commit.

## Isu diketahui
- Nama file export ikut kedudukan dalam `lessons.json` (01, 02…), bukan medan `no`. Jadi lesson `no: "00"` jadi `01-Welcome-...mp4`. Ini normal. Untuk render semula satu lesson: `python -I tools/export.py --render 09` (tanpa `--render` dia skip kalau file dah ada).
- `videos/_kit/AGENT-BRIEF.md` masih rujuk folder lama `C:\Projects\Landing Page\vbui\` (sekarang `masteryui`).
- Python `http.server` (preview drafts) boleh bagi slide lama dari cache browser; reload dengan `?v=` kalau edit tak nampak.
