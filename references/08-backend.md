# Pemrograman Backend dan Arsitektur Aplikasi

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

Backend menjalankan aturan yang tidak dapat dipercayakan kepada browser: autentikasi, otorisasi, transaksi, integrasi, penjadwalan, dan akses data. Ia menerima permintaan, memeriksa kewenangan, menerapkan aturan bisnis, lalu mengembalikan hasil yang terstruktur. [MDN server side](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/First_steps/Introduction) memberi gambaran kerja server.

Backend tidak dibutuhkan pada setiap situs informasi. Bila proses menyimpan data, mengirim email, mengelola akun, atau mengakses layanan rahasia, sebuah komponen server atau layanan terkelola biasanya diperlukan.

## Konsep yang perlu dikuasai

### Batas layanan dan modul

Pisahkan transport HTTP, aturan bisnis, akses data, dan integrasi pihak ketiga. Modul mengikuti kemampuan produk agar logika tidak tercecer di banyak endpoint. Arsitektur sederhana yang bisa diuji sering lebih tepat daripada layanan mikro tanpa kebutuhan skala/tim.

### Siklus permintaan

Permintaan masuk melalui routing, parsing, autentikasi, validasi, otorisasi, operasi, dan respons. Urutan penting: pemeriksaan hak akses dilakukan untuk objek yang diminta, bukan hanya saat membuka halaman. Kesalahan aplikasi ditangani konsisten tanpa membocorkan detail internal.

### Model domain

Tuliskan entitas, identitas, relasi, dan aturan invariannya. Untuk pendaftaran kelas, kuota tidak boleh negatif dan satu pengguna tidak boleh menerima dua tempat untuk permintaan yang sama bila produk melarangnya. Aturan ini diuji di lapisan yang menguasai transaksi.

### Konsistensi dan transaksi

Operasi yang mengubah beberapa baris harus mempertahankan keadaan sah bila sebagian gagal. Pahami transaksi DB, concurrency, retry, dan idempotensi untuk permintaan yang mungkin berulang. Tindakan di luar DB seperti email memerlukan strategi agar tidak dikirim saat transaksi gagal.

### Autentikasi dan otorisasi

Autentikasi menjawab siapa pemanggil; otorisasi menjawab apa yang boleh dilakukan. Terapkan prinsip hak minimum serta cek izin setiap operasi, termasuk akses berdasarkan ID langsung. Simpan sesi dan kata sandi sesuai pedoman keamanan yang mutakhir.

### Konfigurasi dan rahasia

Bedakan konfigurasi per lingkungan dan hindari rahasia dalam repo maupun output log. [Twelve-Factor App](https://12factor.net/) membahas pemisahan kode, konfigurasi, proses, dan ketergantungan sebagai praktik arsitektur aplikasi layanan.

### Pekerjaan latar

Email, impor besar, atau proses yang lama dapat dialihkan ke antrian pekerjaan. Tentukan retry, dead letter, idempotensi, dan penanganan kegagalan agar pekerjaan tidak hilang atau terproses dua kali. Jangan memperkenalkan antrian jika proses sederhana cukup.

### Integrasi pihak ketiga

Anggap layanan eksternal bisa lambat atau gagal; tentukan timeout, retry yang aman, rate limit, validasi webhook, serta batas biaya. Simpan status operasional dan rekonsiliasi bila hasil eksternal tidak pasti. Kontrak integrasi harus diuji.

### Operasional dan observasi

Catat request ID, hasil operasi, error dan durasi yang relevan tanpa data sensitif. Siapkan health check yang benar-benar menilai kesiapan, metrik, serta prosedur pemulihan. Dokumentasikan migrasi dan rollback saat rilis.

## Alur kerja pada proyek

1. Definisikan aturan bisnis, batas data, dan aktor.
2. Rancang modul, endpoint, model data, serta kontrak kegagalan.
3. Implementasikan validasi, izin per objek, transaksi, dan idempotensi.
4. Integrasikan layanan luar dengan timeout dan strategi kegagalan.
5. Uji aturan serta operasi bersamaan yang berisiko.
6. Siapkan konfigurasi, pengamatan, migrasi, dan pemulihan.

## Contoh penerapan

Dua calon peserta mengambil kursi terakhir bersamaan. Backend harus memeriksa kapasitas dan menyimpan pendaftaran secara atomik; membaca kapasitas di browser saja tidak cukup. Bila email konfirmasi gagal, status pendaftaran tetap jelas dan pengiriman dapat dicoba ulang tanpa membuat pendaftaran baru.

## Keputusan dan pertukaran yang perlu dicatat

- Server monolit modular adalah titik awal yang wajar untuk banyak proyek; pemisahan layanan membawa biaya jaringan dan operasi.
- Sesi berbasis cookie atau token memiliki tradeoff ancaman dan arsitektur; jangan memilih berdasarkan tren.
- Performa database, bukan jumlah server semata, sering membatasi kapasitas transaksi.

## Pemeriksaan hasil

- [ ] Aturan bisnis tidak hanya dijaga di klien.
- [ ] Pemeriksaan izin per objek dan per tindakan ada di server.
- [ ] Perubahan bersamaan mempertahankan invariannya.
- [ ] Kegagalan pihak ketiga tidak membingungkan status pengguna.
- [ ] Rahasia, log, migrasi, dan prosedur rollback terdokumentasi.

## Serah terima untuk AI atau tim proyek

Masukan: kebutuhan, data, API, dan model ancaman. Keluaran: modul server, aturan bisnis, kontrak integrasi, migrasi, uji concurrency, serta runbook. AI backend harus menyebut asumsi dan ketidakpastian transaksi; reviewer keamanan/data menguji batas izin dan konsistensi.

## Sumber utama dan tingkat bukti

1. [MDN — Introduction to server side](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/First_steps/Introduction) — pengantar fungsi server
2. [Twelve-Factor App](https://12factor.net/) — panduan arsitektur operasional
3. [PostgreSQL — Transactions](https://www.postgresql.org/docs/current/tutorial-transactions.html) — dasar transaksi data

> **Cara membaca bukti:** spesifikasi/standar menentukan perilaku atau kriteria yang diuji; panduan resmi memberi praktik yang dianjurkan; penelitian pengguna memberi temuan kontekstual yang tetap harus diuji pada pengguna website ini. Pilihan alat dan ketentuan hukum harus diperiksa lagi saat implementasi.

## Pendalaman operasional untuk Website Builder

> Revisi integrasi 24 September 2026. Bagian ini menambah keputusan implementasi dan bukti penerimaan. Contoh merupakan rancangan, bukan hasil uji pengguna.

### Efek samping dan status transaksi

Pisahkan perintah pengguna, hasil commit database, pekerjaan lanjutan, dan konfirmasi dari penyedia luar. Contoh pendaftaran: kursi dialokasikan secara atomik; pekerjaan email dicatat secara tahan gagal; pengiriman ulang email tidak membuat pendaftaran baru. Transaksi database tidak otomatis mencakup email atau layanan pembayaran.

Tetapkan identitas operasi yang dapat digunakan ulang untuk retry. Ikat idempotensi pada aktor, tindakan, dan parameter yang relevan; tolak penggunaan kunci sama dengan isi berbeda. Jangan menganggap menonaktifkan tombol di browser cukup untuk mencegah duplikasi. Verifikasi signature webhook, cegah replay sesuai kontrak penyedia, dan tangani pesan yang datang terlambat atau terbalik.

**Matriks otorisasi:** untuk setiap endpoint tulis aktor, objek, aksi, syarat kepemilikan/tenant, dan hasil penolakan. Lakukan pemeriksaan di server pada semua jalur, termasuk unduhan, ekspor, pencarian, dan proses latar. Status login saja tidak memberi hak pada semua objek.

**Bukti penerimaan:** dua pengguna memperebutkan satu kapasitas menghasilkan paling banyak satu alokasi; webhook berulang tidak menambah efek; pengguna A tidak dapat mengakses milik B; gangguan email tidak menghapus transaksi yang sah. Catat batas simulator apabila penyedia asli belum terhubung.

Sumber: [PostgreSQL isolation](https://www.postgresql.org/docs/current/transaction-iso.html) dan [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html). Rancangan idempotensi harus mengikuti kontrak penyedia dan model domain aktual.
