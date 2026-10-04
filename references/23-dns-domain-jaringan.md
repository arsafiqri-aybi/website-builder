# DNS, Domain, TLS, dan Dasar Jaringan

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

DNS menerjemahkan nama domain ke informasi yang diperlukan klien untuk menemukan layanan. Domain, resolver, record, alamat IP, koneksi, HTTP, dan TLS membentuk jalur akses website. [RFC 1034](https://www.rfc-editor.org/info/rfc1034/) menjelaskan konsep DNS dan sifat cache; [RFC 9110](https://httpwg.org/specs/rfc9110.html) menjelaskan semantik HTTP.

Memahami jalur ini mempermudah diagnosis “situs tidak terbuka”. Domain adalah hak penggunaan yang diperbarui lewat registrar; DNS menyatakan arah layanan; hosting menjalankan konten/aplikasi; sertifikat TLS membuktikan identitas domain untuk koneksi aman sesuai mekanismenya.

## Konsep yang perlu dikuasai

### Nama domain dan kepemilikan

Catat registrar, tanggal perpanjangan, pemilik organisasi, kontak, serta akses pemulihan. Gunakan autentikasi kuat dan catatan perubahan. Risiko kehilangan domain dapat memutus situs serta email sekaligus.

### Resolver dan cache

Browser/OS dan resolver mencari record melalui sistem DNS; hasil disimpan sementara sesuai TTL dan perilaku resolver. Karena cache, perubahan record tidak selalu terlihat serentak di semua lokasi. Diagnosis perlu memeriksa resolver dan record otoritatif.

### Record utama

A/AAAA mengarah ke alamat IP, CNAME alias nama, MX untuk email, TXT untuk data verifikasi/kebijakan, NS untuk delegasi. Nilai record mengikuti petunjuk penyedia dan batas spesifikasi. Jangan mengubah MX ketika hanya memindah hosting web tanpa meninjau dampak email.

### Rantai koneksi

Setelah DNS, klien membangun koneksi jaringan/TLS lalu mengirim HTTP. Kesalahan DNS, TLS, 404, 500, dan timeout berasal dari lapisan berbeda sehingga perlu pemeriksaan berbeda. Gunakan pengamatan dari jaringan luar serta log layanan.

### TLS dan sertifikat

Sertifikat harus cocok dengan domain dan masih berlaku; otomatisasi pembaruan perlu dipantau. [Let’s Encrypt](https://letsencrypt.org/how-it-works/) menjelaskan validasi kepemilikan domain dan penerbitan. TLS mengenkripsi jalur komunikasi yang sesuai tetapi tidak memperbaiki otorisasi aplikasi.

### CDN dan proxy

CDN dapat menyajikan aset dekat pengguna dan melakukan cache; proxy dapat meneruskan permintaan ke server asli. Konfigurasi header, alamat asli klien, cache privat, dan aturan HTTPS harus konsisten. Periksa cache ketika konten berubah atau data tidak boleh dibagikan.

### Subdomain dan lingkungan

Pisahkan `www`, `api`, `staging`, atau subdomain lain bila ada alasan dan kontrol jelas. Lingkungan uji jangan terekspos dengan akun/rahasia lemah. Catat dependensi antara record DNS, sertifikat, dan layanan.

### Migrasi

Sebelum pindah, inventaris record yang ada, turunkan TTL bila strategi memerlukan, buat layanan baru siap, periksa sertifikat, lalu ubah record dan pantau. Simpan jalur kembali selama masa transisi. Perubahan NS bisa memengaruhi seluruh zona, termasuk email dan verifikasi.

### Diagnosis sistematis

Mulai dari gejala dan cakupan: satu pengguna atau semua, satu URL atau semua. Periksa resolusi nama, TLS, status HTTP, konten, dan backend bertahap. Jangan mengubah banyak record sekaligus saat akar masalah belum jelas.

## Alur kerja pada proyek

1. Dokumentasikan registrar, zona DNS, sertifikat, dan pemiliknya.
2. Petakan domain/subdomain ke layanan serta record.
3. Atur HTTPS dan pantau pembaruan sertifikat.
4. Uji akses dari jaringan dan lokasi berbeda sesuai audiens.
5. Sebelum migrasi, catat record serta efek pada email.
6. Jika gangguan, telusuri DNS → koneksi/TLS → HTTP → aplikasi.

## Contoh penerapan

Domain `contoh.id` mengarah ke situs kelas, `api.contoh.id` ke layanan pendaftaran. Saat situs gagal dibuka, operator memeriksa apakah resolver mendapat record, apakah sertifikat valid, dan apakah server mengembalikan HTTP. Bila halaman terbuka tetapi pendaftaran gagal, fokus beralih ke API dan database, bukan langsung mengubah DNS.

## Keputusan dan pertukaran yang perlu dicatat

- TTL mengendalikan salah satu bagian cache DNS; waktu terlihatnya perubahan tidak dapat dijamin persis bagi semua klien.
- CNAME dan A/AAAA punya batas penempatan berbeda; ikuti aturan zona dan penyedia yang digunakan.
- DNSSEC menambah perlindungan autentikasi data DNS bila dioperasikan benar, tetapi bukan pengganti HTTPS.

## Pemeriksaan hasil

- [ ] Domain serta akses registrar dimiliki dan diawasi.
- [ ] Record web dan email tercatat sebelum perubahan.
- [ ] Sertifikat berlaku dan pembaruan terpantau.
- [ ] Lapisan kesalahan dapat dibedakan lewat pemeriksaan.
- [ ] Migrasi memiliki langkah verifikasi dan kembali.

## Serah terima untuk AI atau tim proyek

Masukan: kebutuhan domain, arsitektur layanan, dan penyedia. Keluaran: inventaris record, diagram jalur akses, prosedur perubahan, serta runbook diagnosis. AI infrastruktur dapat memberi rencana, tetapi perubahan DNS produksi memerlukan verifikasi pemilik karena efeknya dapat meluas ke email dan layanan lain.

## Sumber utama dan tingkat bukti

1. [IETF — RFC 1034](https://www.rfc-editor.org/info/rfc1034/) — konsep dan desain DNS
2. [IETF — RFC 9110](https://httpwg.org/specs/rfc9110.html) — semantik HTTP dan URI
3. [Let’s Encrypt — How it works](https://letsencrypt.org/how-it-works/) — sertifikat dan validasi domain

> **Cara membaca bukti:** spesifikasi/standar menentukan perilaku atau kriteria yang diuji; panduan resmi memberi praktik yang dianjurkan; penelitian pengguna memberi temuan kontekstual yang tetap harus diuji pada pengguna website ini. Pilihan alat dan ketentuan hukum harus diperiksa lagi saat implementasi.

## Pendalaman operasional untuk Website Builder

> Revisi integrasi 24 September 2026. Bagian ini menambah keputusan implementasi dan bukti penerimaan. Contoh merupakan rancangan, bukan hasil uji pengguna.

### Perubahan jaringan dengan cakupan yang diketahui

Inventaris seluruh record sebelum migrasi. Satu domain dapat melayani website, email, verifikasi penyedia, dan subdomain lama. Perubahan nameserver memindahkan tanggung jawab zona; memperbarui satu record web tidak sama dengan mengganti seluruh delegasi.

Gunakan urutan diagnosis yang mengisolasi lapisan: resolusi DNS → koneksi → sertifikat/TLS → HTTP → rute aplikasi → API/data. Gejala formulir gagal sesudah halaman termuat tidak otomatis disebabkan DNS. Catat hostname, waktu, jaringan, status, dan langkah reproduksi tanpa menampilkan token sensitif.

Untuk pergantian host, siapkan target serta sertifikat lebih dulu bila mekanisme penyedia memungkinkan; simpan jalur pemulihan dan pantau beberapa lokasi. TTL adalah salah satu kendali cache; jangan menjanjikan propagasi tepat sejumlah menit untuk semua klien. Periksa record IPv4 dan IPv6 bila dipakai agar keduanya mengarah ke layanan yang benar.

**Bukti penerimaan:** domain utama dan subdomain terkait membuka tujuan yang benar, HTTPS valid, redirect tidak berulang, serta layanan email yang sebelumnya ada tetap sesuai. Jangan mengubah domain atau DNS produksi sebagai bagian uji skill; gunakan konfigurasi uji yang terisolasi.

Sumber: [Let's Encrypt — How It Works](https://letsencrypt.org/how-it-works/) dan [RFC 9110](https://httpwg.org/specs/rfc9110.html). Record aktual harus mengikuti penyedia dan kepemilikan yang telah diverifikasi.
