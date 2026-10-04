# Keamanan Web dan Pengembangan Aman

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

Keamanan web melindungi kerahasiaan, integritas, dan ketersediaan layanan dari penyalahgunaan serta kesalahan. Ia perlu diterapkan sepanjang desain, pembangunan, pengujian, dan operasi. [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) memberi tindakan teknis, sedangkan [NIST SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) memberi kerangka proses pengembangan aman.

Ancaman ditentukan oleh aset, pelaku, dan dampaknya. Situs informasi tanpa akun tetap dapat terkena pembajakan konten atau kebocoran konfigurasi; aplikasi pembayaran memerlukan kontrol lebih kuat dan peninjauan khusus.

## Konsep yang perlu dikuasai

### Model ancaman

Petakan data, titik masuk, batas kepercayaan, aktor, skenario penyalahgunaan, dan mitigasi. Prioritaskan risiko menurut dampak serta kemungkinan dalam konteks nyata. Tinjau kembali ketika fitur unggahan, login, atau integrasi baru ditambahkan.

### Autentikasi dan sesi

Gunakan mekanisme tepercaya, proteksi kata sandi yang sesuai panduan, MFA bila sesuai risiko, dan pemulihan akun yang tidak membocorkan keberadaan akun. Cookies sesi memerlukan atribut yang sesuai; masa hidup dan pencabutan sesi harus jelas. [OWASP Authentication](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) membahas kontrolnya.

### Otorisasi

Periksa izin pada server untuk setiap objek dan tindakan; ID yang dapat ditebak bukan alasan pemberian akses. Terapkan prinsip hak minimum pada akun admin, database, dan layanan integrasi. Uji “pengguna A meminta milik B” untuk setiap endpoint privat.

### Injection dan output

Gunakan query berparameter terhadap SQL; jangan menggabungkan input sebagai perintah. Terapkan encoding output sesuai konteks HTML/atribut/URL/JS; sanitasi diperlukan saat konten HTML memang diizinkan. [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) membedakan pertahanan efektif.

### CSRF, XSS, dan batas browser

Pahami cara browser mengirim cookie otomatis dan mengeksekusi script. Untuk tindakan yang mengubah keadaan, terapkan perlindungan CSRF sesuai arsitektur; XSS dapat merusak banyak kontrol, sehingga pencegahan injeksi output tetap dasar. CSP dapat menambah lapisan, bukan menghapus kewajiban encoding.

### Rahasia dan transport

Paksa HTTPS untuk layanan publik yang sesuai, kelola sertifikat, simpan secret di mekanisme aman, rotasi saat bocor. Jangan menaruh key rahasia dalam JavaScript frontend, repo, pesan error, atau log. Hak akses operator dibatasi dan dapat dicabut.

### Unggahan dan dependensi

Batasi ukuran/tipe, validasi konten, simpan file di luar jalur eksekusi, dan tentukan kebijakan scanning bila risiko menuntut. Pantau dependensi, lakukan pembaruan terkendali, serta tinjau perubahan supply chain. Jangan percaya ekstensi filename saja.

### Logging dan respons insiden

Catat kejadian keamanan yang relevan tanpa token atau data sensitif. Tentukan siapa menerima peringatan, cara memutus akses, memulihkan layanan, mengomunikasikan insiden, dan memperbaiki akar penyebab. Latih prosedur sebelum ada insiden.

### Verifikasi

Uji jalur normal, penyalahgunaan, akses tidak sah, input berbahaya, serta konfigurasi rilis. Pemindaian otomatis memberi sinyal awal tetapi perlu peninjauan manual dan pengujian berbasis model ancaman.

## Alur kerja pada proyek

1. Buat inventaris aset dan model ancaman.
2. Tetapkan kontrol izin, autentikasi, sesi, dan perlindungan data.
3. Implementasikan validasi input, query berparameter, output encoding, HTTPS.
4. Periksa konfigurasi dan dependensi dalam pipeline rilis.
5. Uji otorisasi lintas akun dan skenario penyalahgunaan.
6. Siapkan log aman, pemantauan, dan respons insiden.

## Contoh penerapan

Pengguna A mengubah ID pendaftaran pada URL menjadi ID pengguna B. Server harus mengembalikan penolakan yang aman, bahkan jika tombol untuk itu tersembunyi di UI. Pada form pendaftaran, input nama dengan markup HTML ditampilkan sebagai teks biasa. Permintaan jaringan berulang tidak boleh membuat tagihan ganda.

## Keputusan dan pertukaran yang perlu dicatat

- Kontrol yang tepat mengikuti ancaman; checklist umum adalah awal pemeriksaan, bukan bukti sistem aman.
- Jangan mengandalkan CORS, validasi frontend, atau URL acak sebagai satu-satunya perlindungan.
- Audit keamanan perlu diulang saat model data, peran, atau integrasi berubah.

## Pemeriksaan hasil

- [ ] Hak akses per objek teruji untuk semua endpoint privat.
- [ ] Query berparameter dan output encoding sesuai konteks diterapkan.
- [ ] Secret dan data sensitif tidak muncul di repositori/log/response.
- [ ] Dependensi dan konfigurasi rilis ditinjau.
- [ ] Ada pemilik, prosedur, dan latihan untuk insiden.

## Serah terima untuk AI atau tim proyek

Masukan: aset, alur, data, dan arsitektur. Keluaran: model ancaman, daftar kontrol, hasil uji penyalahgunaan, serta runbook insiden. AI keamanan meninjau desain dan implementasi; pengembang memperbaiki; peninjau terpisah memverifikasi kasus yang berdampak tinggi.

## Sumber utama dan tingkat bukti

1. [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) — panduan implementasi keamanan aplikasi
2. [OWASP Top Ten](https://owasp.org/projects/top-ten) — ringkasan kategori risiko, bukan daftar lengkap
3. [NIST SSDF SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final) — kerangka praktik pengembangan aman

> **Cara membaca bukti:** spesifikasi/standar menentukan perilaku atau kriteria yang diuji; panduan resmi memberi praktik yang dianjurkan; penelitian pengguna memberi temuan kontekstual yang tetap harus diuji pada pengguna website ini. Pilihan alat dan ketentuan hukum harus diperiksa lagi saat implementasi.

## Pendalaman operasional untuk Website Builder

> Revisi integrasi 24 September 2026. Bagian ini menambah keputusan implementasi dan bukti penerimaan. Contoh merupakan rancangan, bukan hasil uji pengguna.

### Verifikasi keamanan sebagai daftar tuntutan

Gunakan [OWASP ASVS](https://github.com/OWASP/ASVS) untuk memilih persyaratan verifikasi yang sesuai risiko. Edisi 5.0.0 tersedia pada sumber resmi yang diperiksa; catat versi dan nomor kontrol saat memakainya. Top Ten berguna untuk kategori risiko, tetapi bukan sertifikasi atau daftar pengujian lengkap. Jangan mengaku memenuhi ASVS hanya karena memakai beberapa kontrolnya.

Untuk data privat, uji akses lintas pengguna, peran, dan tenant pada baca/tulis/ekspor. Lindungi sesi dengan mekanisme platform yang matang; jangan merancang kriptografi atau autentikasi sendiri tanpa alasan dan keahlian yang sesuai. Periksa alur reset, logout, perubahan peran, dan invalidasi sesi.

Aset pihak ketiga, widget, tag analytics, dan font eksternal juga menjadi bagian ancaman. Catat domain, hak kode, data yang terlihat, serta dampaknya pada performa dan privasi. Gunakan pembatasan yang sesuai arsitektur seperti CSP atau integritas sumber pada aset yang kompatibel; keberadaannya tidak menggantikan review dependensi.

**Batas bukti:** build berhasil, scanner bersih, atau jawaban AI yang meyakinkan belum membuktikan aplikasi aman. Laporkan ruang lingkup pengujian dan bagian belum diperiksa. Untuk fungsi berisiko, temuan kehilangan data atau akses tidak sah menjadi penghalang rilis meskipun desain visual bagus.

Sumber: [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) dan [Third Party JavaScript](https://cheatsheetseries.owasp.org/cheatsheets/Third_Party_Javascript_Management_Cheat_Sheet.html).
