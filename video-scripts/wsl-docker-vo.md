# Video · Cara Install WSL dan Docker Desktop (Windows 11)

Sumber: `Downloads/WSL Dockers.mp4` (3:02, 1920×1080, screen recording + suara asal).
VO baru: Bahasa Melayu, istilah teknikal dalam English. Penceramah sebut diri "saya", tegur penonton "anda" (ikut video asal). Sebut "file", bukan "fail". Tiada em dash.
Ejaan untuk TTS: tulis **W S L** (bukan "WSL") supaya disebut huruf satu-satu, dan **Docker** (bukan "Dockers").

## Apa yang salah dalam VO asal

| Masa asal | VO asal (transcribe) | Masalah |
|---|---|---|
| 0:00 dan seterusnya | "Lebadu SL", "Dockers" | Sebutan WSL tak jelas, nama betul ialah Docker |
| 0:13 | "search Lebadu SL installed" | Yang ditaip sebenarnya `wsl install windows 11` |
| 0:42 | "pastekan komen line tadi" | Sepatutnya "command" |
| 1:04 | "Mikai Aiman" | Username di skrin ialah `mikhail_aiman` |
| 1:13 | "tekan enter banyak kali untuk skip password" | Skrin keluar error `Authentication token manipulation error`. Ajar orang skip password bukan amalan baik (lihat Nota A) |
| 1:54 | "Untuk Intel dan juga AMD processor" | Butang sebenar ialah **Download for Windows - AMD64** (untuk PC Intel/AMD biasa) |
| 0:51, 2:01, 2:27 | (senyap lama) | Tunggu download/install 8 hingga 25 saat, perlu dipotong atau dipercepat |

## Skrip VO baru

| Klip | Masa asal | Skrin | VO |
|---|---|---|---|
| v1 | 0:00 - 0:08 | Desktop | Assalamualaikum semua. Hari ni saya nak tunjuk cara install W S L dan Docker Desktop dalam Windows. |
| v2 | 0:08 - 0:13 | Desktop, buka Chrome | Sebelum install Docker, anda perlu install W S L dulu. W S L ialah Windows Subsystem for Linux, iaitu Linux yang berjalan terus dalam Windows. Docker perlukan W S L untuk berfungsi. |
| v3 | 0:13 - 0:24 | Google: `wsl install windows 11`, AI Overview, tekan Show more | Mula-mula, buka Chrome dan search, W S L install windows eleven. Kemudian tekan Show more. |
| v4 | 0:24 - 0:30 | Kotak code `wsl --install` | Dekat sini ada command, W S L dash dash install. Tekan copy. |
| v5 | 0:30 - 0:42 | Windows search, taip "power", pilih Windows PowerShell | Lepas tu, pergi ke Windows search dan taip PowerShell. Buka Windows PowerShell sebagai Administrator. |
| v6 | 0:42 - 0:51 | Paste `wsl --install`, tekan Enter, Downloading Ubuntu | Paste command tadi, dan tekan Enter. W S L akan download dan install Ubuntu secara automatik. |
| ✂ | 0:51 - 1:00 | Progress bar download | **Potong / speed up 4x.** Tiada VO. |
| v7 | 1:00 - 1:09 | `Create a default Unix user account: mikhail_aiman` | Tunggu sampai keluar arahan Create a default Unix user account. Taip nama user anda. Contohnya saya guna mikhail underscore aiman. Kemudian tekan Enter. |
| v8 | 1:09 - 1:24 | New password / Retype new password | Seterusnya, ia akan minta password. Tekan Enter sahaja banyak kali untuk skip, sampai keluar macam ni. |
| v9 | 1:24 - 1:31 | Prompt hijau `mikhail_aiman@Mikhail` | Bila nampak baris hijau macam ni, maksudnya Ubuntu dah berjaya dipasang menggunakan W S L. |
| v10 | 1:31 - 1:48 | Tab baru, search `docker desktop`, tekan link docker.com | Seterusnya, kita install Docker Desktop. Buka tab baru, search Docker Desktop, dan tekan link docker dot com. |
| v11 | 1:48 - 2:01 | Menu Download Docker Desktop, pilih Windows - AMD64 | Dekat sini ada butang Download Docker Desktop. Untuk kebanyakan PC Windows yang guna processor Intel atau AMD, pilih Download for Windows, AMD sixty four. |
| ✂ | 2:01 - 2:12 | Tunggu download | **Potong.** Tiada VO. |
| v12 | 2:12 - 2:27 | Download history, buka Docker Desktop Installer, tekan OK | Bila download dah siap, buka file Docker Desktop Installer. Tekan OK, dan biarkan ia install sampai siap. |
| ✂ | 2:27 - 2:51 | Unpacking files, progress bar | **Speed up 6x** (kekalkan sekejap supaya nampak progress). Tiada VO. |
| v13 | 2:51 - 3:02 | Installation succeeded, tekan Close | Okey, Docker Desktop dah berjaya di-install. Tekan Close. Itu sahaja untuk video ni. Terima kasih. |

Anggaran panjang lepas potong: lebih kurang 2:00 hingga 2:15.

## Nota untuk anda putuskan

**A. Password Ubuntu (v8).** Skrin asal tunjuk password di-skip dan keluar `Authentication token manipulation error`. Pilihan 1 kekalkan rakaman dan jujur tentang error tu. Pilihan 2 lebih betul untuk penonton, tapi rakaman skrin tak tunjuk password ditaip, jadi kawasan 1:09 hingga 1:24 perlu dirakam semula atau dikaburkan (blur) supaya error tak nampak.

**B. Restart PC.** Google AI Overview sebut langkah 3, Restart Your Computer. Video tak tunjuk restart. Nak tambah satu ayat ringkas? Cadangan selepas v9: "Kalau Windows minta restart, restart dulu sebelum sambung."

**C. Lepas install Docker.** Video tamat di "Installation succeeded". Docker Desktop selalunya minta restart dan accept terms masa pertama kali dibuka. Nak tambah klip penutup atau biar macam ni?

**D. Run as Administrator (v5).** Tajuk tetingkap PowerShell dalam rakaman ialah "Administrator: Windows PowerShell", jadi VO sebut Administrator. Kalau anda tak sengaja buka sebagai admin, buang perkataan tu.

**E. Captions.** Nak burn-in caption Melayu atau tidak?
