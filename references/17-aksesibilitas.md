# Aksesibilitas Web dan Desain Inklusif

> Pustaka ilmu pembuatan website · Bahasa Indonesia · Ditinjau 24 September 2026

## Daftar isi

- [Fungsi dan batas bidang](#fungsi-dan-batas-bidang)
- [Konsep yang perlu dikuasai](#konsep-yang-perlu-dikuasai)
- [Alur kerja pada proyek](#alur-kerja-pada-proyek)
- [Contoh penerapan](#contoh-penerapan)
- [Keputusan dan pertukaran yang perlu dicatat](#keputusan-dan-pertukaran-yang-perlu-dicatat)
- [Pemeriksaan hasil](#pemeriksaan-hasil)
- [Serah terima untuk AI atau tim proyek](#serah-terima-untuk-ai-atau-tim-proyek)
- [Sumber utama dan tingkat bukti](#sumber-utama-dan-tingkat-bukti)
- [Pendalaman operasional untuk Website Builder](#pendalaman-operasional-untuk-website-builder)

## Fungsi dan batas bidang

Aksesibilitas memastikan orang dengan kebutuhan penglihatan, pendengaran, gerak, kognitif, atau teknologi bantu dapat memahami dan memakai website. [WCAG 2.2](https://www.w3.org/TR/WCAG22/) mengelompokkan kriteria menurut perceivable, operable, understandable, robust. Kesesuaian teknis diperiksa bersama pengalaman pengguna nyata; [WAI Evaluating](https://www.w3.org/WAI/test-evaluate/) mengingatkan keterbatasan otomasi.

Aksesibilitas adalah tanggung jawab konten, desain, frontend, backend, QA, dan operasi. Standar Level AA sering dijadikan sasaran proyek, tetapi kewajiban hukum spesifik perlu diperiksa untuk lokasi dan sektor yang berlaku.

## Konsep yang perlu dikuasai

### Struktur dan nama

HTML semantik, heading yang tertib, landmark, label input, dan nama tautan/tombol yang jelas memungkinkan navigasi teknologi bantu. Teks alt menjelaskan fungsi gambar, bukan sekadar daftar objek. Dekorasi murni dapat memakai alt kosong.

### Keyboard dan fokus

Semua tugas penting harus dapat dijalankan tanpa mouse; urutan tab mengikuti alur logis, fokus terlihat, serta komponen dialog mengelola fokus. Jangan menjebak keyboard atau memasang click handler pada `div` tanpa perilaku setara. Periksa fokus setelah error dan perubahan konten.

### Visual dan pembesaran

Uji kontras teks dan nonteks sesuai kriteria target, pembesaran teks, reflow, jarak, dan target interaksi. Jangan bergantung pada warna saja untuk membedakan keadaan. [WCAG Contrast Minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) menjelaskan rasio teks.

### Media dan gerak

Video bermakna memerlukan subtitel dan alternatif yang sesuai; audio perlu transkrip bila relevan. Gerak berlebihan dapat mengganggu pengguna; beri kontrol serta hormati preferensi reduced motion. Kriteria berbeda menurut jenis media dan tingkat konformansi.

### Form dan kesalahan

Hubungkan label, bantuan, dan error ke kontrol; gunakan pesan yang menerangkan perbaikan. Hindari batas waktu yang tidak perlu; beri kesempatan meninjau transaksi penting. Instruksi tidak hanya didasarkan pada posisi atau warna.

### Konten dinamis

Saat hasil pencarian berubah atau proses selesai, pengguna teknologi bantu memerlukan informasi yang tepat, tetapi live region berlebihan dapat mengganggu. Kelola fokus dan pengumuman seperlunya. Komponen native biasanya lebih andal dibanding widget kustom.

### Bahasa dan pemahaman

Setel bahasa dokumen, jelaskan istilah, gunakan struktur konten konsisten, serta periksa navigasi dan bantuan. Aksesibilitas kognitif mengharuskan alur dapat diprediksi dan pemulihan kesalahan. Bahasa sederhana tidak berarti menghilangkan ketelitian.

### Evaluasi berlapis

Mulai dengan audit otomatis, uji keyboard/zoom, pemeriksaan pembaca layar pada alur penting, lalu libatkan pengguna berkebutuhan akses. Catat kriteria, langkah reproduksi, dampak, dan perbaikan. Jangan mengklaim “100% aksesibel” dari satu alat.

### Pengadaan komponen

Ketika memakai widget/library, uji contoh nyata pada versi yang digunakan. Klaim vendor tidak menghapus kewajiban memeriksa integrasi, konten, dan konfigurasi proyek.

## Alur kerja pada proyek

1. Tentukan sasaran kriteria dan kebutuhan pengguna.
2. Bangun HTML semantik dan interaksi keyboard sejak awal.
3. Periksa teks, kontras, fokus, form, media, dan gerak.
4. Uji otomatis lalu manual pada tugas utama.
5. Libatkan pengguna relevan dan perbaiki temuan.
6. Ulangi evaluasi pada perubahan fitur dan konten.

## Contoh penerapan

Pengguna keyboard mencari kelas lalu membuka formulir. Fokus terlihat pada filter, status hasil diumumkan secara tepat, label “Email” terhubung ke input, dan pesan “Email belum valid; gunakan format nama@domain” dapat dibaca serta ditindaklanjuti. Saat berhasil, fokus dan konfirmasi membawa pengguna ke langkah berikutnya.

## Keputusan dan pertukaran yang perlu dicatat

- WCAG adalah kriteria pengujian, sedangkan temuan pengguna mengungkap masalah yang belum tertangkap checklist.
- Rasio kontras dan ukuran target mengikuti jenis elemen serta pengecualian standar, bukan satu angka universal.
- Integrasi widget pihak ketiga tetap harus diuji dalam konteks halaman.

## Pemeriksaan hasil

- [ ] Semua alur utama dapat dipakai keyboard.
- [ ] Nama, peran, status kontrol dapat dipahami.
- [ ] Kontras/zoom/reflow memenuhi sasaran yang ditetapkan.
- [ ] Form error dan perubahan dinamis dapat diketahui.
- [ ] Temuan manual dan pengguna dicatat, diperbaiki, diuji ulang.

## Serah terima untuk AI atau tim proyek

Masukan: alur, konten, komponen, dan sasaran WCAG. Keluaran: kriteria desain, hasil audit, reproduksi bug, serta bukti uji ulang. AI aksesibilitas memberi rekomendasi; pengembang menerapkan; penguji dengan teknologi bantu dan pengguna sasaran memverifikasi pengalaman nyata.

## Sumber utama dan tingkat bukti

1. [W3C — WCAG 2.2](https://www.w3.org/TR/WCAG22/) — standar kriteria normatif
2. [W3C WAI — Evaluating Accessibility](https://www.w3.org/WAI/test-evaluate/) — metode evaluasi
3. [W3C WAI — Involving Users](https://www.w3.org/WAI/planning/involving-users/) — riset dengan pengguna disabilitas

> **Cara membaca bukti:** spesifikasi/standar menentukan perilaku atau kriteria yang diuji; panduan resmi memberi praktik yang dianjurkan; penelitian pengguna memberi temuan kontekstual yang tetap harus diuji pada pengguna website ini. Pilihan alat dan ketentuan hukum harus diperiksa lagi saat implementasi.

## Pendalaman operasional untuk Website Builder

> Revisi integrasi 24 September 2026. Bagian ini menambah keputusan implementasi dan bukti penerimaan. Contoh merupakan rancangan, bukan hasil uji pengguna.

### Kriteria yang sering tertukar

Gunakan WCAG 2.2 AA sebagai sasaran awal engineering bila brief tidak menetapkan yang lain; ini bukan penetapan kewajiban hukum universal. Konformansi AA mencakup seluruh kriteria A dan AA yang berlaku, termasuk halaman lengkap dan proses lengkap. Daftar singkat di sini bukan audit konformansi menyeluruh.

| Area | Aturan dan batas praktis |
| --- | --- |
| Target pointer | SC 2.5.8 AA: 24 × 24 CSS px, atau memenuhi pengecualian; bukan aturan jarak 24 px di semua sisi. Pada pengecualian spacing, gunakan konstruksi lingkaran berdiameter 24 px yang dijelaskan standar |
| Target lebih lapang | SC 2.5.5 AAA memakai 44 × 44 CSS px dengan pengecualian. Memilih 44 px sebagai default desain tidak berarti syarat AA adalah 44 px |
| Fokus | SC 2.4.11 AA: elemen berfokus tidak sepenuhnya tertutup konten buatan penulis. Uji sticky header, footer, dan banner cookie |
| Autentikasi | SC 3.3.8 AA membatasi tes fungsi kognitif tanpa mekanisme/alternatif yang memenuhi pengecualian; dukung password manager dan paste pada pola yang relevan |
| Pembesaran | Uji resize text 200% dan reflow pada ekuivalen lebar 320 CSS px untuk konten horizontal, dengan pengecualian standar untuk bagian yang memerlukan dua dimensi |

Tabel ini merangkum [Target Size Minimum](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html), [Target Size Enhanced](https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced.html), [Focus Not Obscured](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html), [Accessible Authentication](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html), dan [Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html).

**Gerbang hasil:** gabungkan pemeriksaan otomatis dengan keyboard, fokus, zoom/reflow, nama/peran/status, dan teknologi bantu pada tugas inti. Jika pembaca layar belum diuji, tulis belum diuji; jangan menyebut HTML semantik sebagai bukti pengujian tersebut.
