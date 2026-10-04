# Desain Antarmuka Pengguna (UI)

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

UI menerjemahkan struktur dan tugas menjadi komponen yang terlihat dan dapat dioperasikan: tipografi, tata letak, warna, kontrol, status, dan pola responsif. Penilaian visual harus mempertimbangkan kejelasan dan aksesibilitas, bukan selera pribadi saja. [GOV.UK Design System](https://design-system.service.gov.uk/) menyediakan contoh komponen dan pola berbasis pengalaman layanan; [WCAG 2.2](https://www.w3.org/TR/WCAG22/) memberi kriteria terukur.

UI adalah rancangan sistem perilaku pada berbagai layar dan keadaan, bukan satu gambar halaman desktop. Pengukuran keberhasilan ada pada pemahaman dan penyelesaian tugas oleh pengguna.

## Konsep yang perlu dikuasai

### Hierarki visual

Utamakan judul, informasi untuk keputusan, dan tindakan utama dengan ukuran, ruang, urutan, serta kontras. Jangan mengandalkan warna sebagai satu-satunya pembeda. Konten terpenting harus terlihat sesuai konteks layar kecil dan pembesaran teks.

### Tipografi

Tentukan skala judul dan isi, panjang baris yang nyaman, tinggi baris, dan variasi berat huruf secukupnya. Pastikan font cadangan tersedia dan tulisan tetap terbaca ketika font web gagal. Uji bahasa Indonesia dengan kata panjang dan kombinasi angka.

### Warna dan kontras

Definisikan peran warna: teks, latar, fokus, tautan, sukses, peringatan, kesalahan. Uji kombinasi nyata, termasuk teks pada hover dan tombol nonaktif. [WCAG 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) menyebut rasio 4,5:1 untuk teks biasa dan 3:1 untuk teks besar pada Level AA, dengan pengecualian khusus.

### Tata letak responsif

Rancang konten yang dapat mengalir, bukan hanya beberapa ukuran layar tetap. Gunakan batas lebar yang masuk akal, grid atau flex sesuai hubungan elemen, dan periksa ketika teks diperbesar. Urutan visual sebaiknya selaras dengan urutan DOM/keyboard.

### Komponen dan status

Spesifikasikan tombol, tautan, input, kartu, dialog, dan tabel beserta normal, hover, fokus, aktif, loading, kosong, sukses, serta gagal. Komponen yang hanya didesain dalam keadaan ideal akan menimbulkan kebingungan saat data tidak tersedia.

### Formulir dan umpan balik

Label tetap terlihat, bantuan ditempatkan dekat input, kesalahan menyebut cara memperbaiki, dan data pengguna dipertahankan bila pengiriman gagal. Gunakan kontrol HTML bawaan bila cocok. [WAI Forms](https://www.w3.org/WAI/tutorials/forms/) membahas pelabelan dan pemberitahuan.

### Interaksi gerak

Animasi dapat membantu menjelaskan perubahan keadaan, tetapi hindari gerak dekoratif yang mengganggu. Hormati `prefers-reduced-motion`, sediakan kendali untuk gerak nonesensial, dan pastikan fungsi tetap berjalan tanpa animasi.

### Sistem desain

Dokumentasikan token seperti warna, spasi, tipografi, serta komponen dan aturan pemakaian. Komponen bersama mengurangi inkonsistensi, tetapi setiap penggunaan tetap harus sesuai konteks. Catat perubahan agar tim tidak membuat salinan yang menyimpang.

### Dokumentasi untuk implementasi

Serahkan ukuran yang fleksibel, perilaku di breakpoint, interaksi keyboard, isi alt bila relevan, pesan kesalahan, dan data contoh panjang. Satu tangkapan layar tidak cukup untuk pengembang membangun perilaku yang benar.

## Alur kerja pada proyek

1. Mulai dari konten dan tugas prioritas, buat sketsa tata letak kecil dan besar.
2. Bangun hierarki tipografi, warna semantik, grid, dan aturan spasi.
3. Rancang komponen dasar beserta seluruh status interaksinya.
4. Uji kontras, fokus, zoom, gerak, bahasa, dan navigasi keyboard.
5. Prototipe alur, amati pengguna menyelesaikan tugas, revisi rancangan.
6. Dokumentasikan spesifikasi responsif dan handoff ke frontend.

## Contoh penerapan

Halaman kelas menampilkan judul, waktu, biaya, kapasitas, dan tombol “Daftar kelas” dalam urutan yang sama pada ponsel serta desktop. Saat kuota habis, status dan alternatif muncul dalam teks, bukan hanya warna merah. Setelah tombol ditekan, sistem memberi status memproses dan mencegah pengiriman ganda tanpa menyembunyikan informasi penting.

## Keputusan dan pertukaran yang perlu dicatat

- Jangan memakai tombol untuk navigasi atau tautan untuk aksi tanpa alasan; semantik mempengaruhi keyboard dan teknologi bantu.
- Tema gelap dan transisi visual hanya ditambah bila mempertahankan kontras, kontrol, dan keterbacaan.
- Desain sistem kecil dan konsisten lebih berguna daripada perpustakaan komponen luas yang tidak dipakai.

## Pemeriksaan hasil

- [ ] Semua komponen punya keadaan fokus yang terlihat.
- [ ] Teks, kontrol, dan status kritis lolos pemeriksaan kontras yang relevan.
- [ ] Desain bertahan pada layar sempit, pembesaran, dan isi panjang.
- [ ] Status kosong, loading, gagal, dan berhasil tersedia.
- [ ] Perilaku keyboard dan gerak tertera dalam handoff.

## Serah terima untuk AI atau tim proyek

Masukan: alur UX, konten, IA, dan identitas merek. Keluaran: sistem komponen, prototipe, spesifikasi keadaan/responsif, serta hasil uji. AI desainer membuat opsi; reviewer aksesibilitas memeriksa; frontend menerapkan sambil mempertahankan semantik dan perilaku.

## Sumber utama dan tingkat bukti

1. [GOV.UK Design System](https://design-system.service.gov.uk/) — contoh pola antarmuka dan komponen
2. [W3C — WCAG 2.2](https://www.w3.org/TR/WCAG22/) — standar kriteria aksesibilitas
3. [W3C WAI — Forms](https://www.w3.org/WAI/tutorials/forms/) — panduan formulir yang dapat dioperasikan

> **Cara membaca bukti:** spesifikasi/standar menentukan perilaku atau kriteria yang diuji; panduan resmi memberi praktik yang dianjurkan; penelitian pengguna memberi temuan kontekstual yang tetap harus diuji pada pengguna website ini. Pilihan alat dan ketentuan hukum harus diperiksa lagi saat implementasi.

## Pendalaman operasional untuk Website Builder

> Revisi integrasi 24 September 2026. Bagian ini menambah keputusan implementasi dan bukti penerimaan. Contoh merupakan rancangan, bukan hasil uji pengguna.

### Arah artistik yang bisa diterapkan

Mulai dengan kalimat konsep: siapa mereknya, kesan yang ingin dibangun, dan bukti visualnya. Tentukan sistem tipografi, komposisi, palet semantik, perlakuan foto, bentuk, serta ritme ruang. Hindari menempelkan efek populer tanpa hubungan dengan merek atau tugas. Gaya editorial, katalog padat, dan antarmuka operasional boleh sama-sama berkualitas dalam konteks berbeda.

Buat satu halaman representatif dengan konten nyata, kemudian turunkan komponen bersama darinya. Jangan mengunci sistem desain besar sebelum mengetahui variasi konten. Untuk setiap komponen, definisikan struktur, keadaan, keyboard, kontras, panjang teks, dan responsivitas. Polesan mencakup garis dasar teks, alignment angka, crop foto, jarak optis ikon, serta konsistensi label; ini pemeriksaan desain, bukan hukum psikologi universal.

Studi [Tuch dkk.](https://research.google/pubs/the-role-of-visual-complexity-and-prototypicality-regarding-first-impression-of-websites-working-towards-understanding-aesthetic-judgments/) menilai kesan estetika awal pada screenshot. Gunakan sebagai alasan memeriksa kepadatan dan keterkenalan struktur, tanpa menyimpulkan semua website harus minimalis atau gaya tertentu pasti meningkatkan penjualan.

**Alur perbaikan:** render halaman → lihat ponsel dan desktop → temukan satu masalah dominan → ubah → periksa ulang keadaan terkait. Jangan menyamakan CSS berhasil dikompilasi dengan tampilan yang sudah ditinjau.

**Bukti penerimaan:** dokumentasikan alasan tiga keputusan visual utama, gambar halaman pada ukuran sasaran, dan temuan yang diperbaiki. Klaim kenyamanan atau keunggulan konversi menunggu bukti pengguna yang sesuai.
