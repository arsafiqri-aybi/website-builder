# Deployment, Hosting, dan Rilis

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

Deployment memindahkan versi website dari lingkungan pengembangan ke layanan yang dapat dipakai; hosting menyediakan komputasi, penyimpanan, dan jaringan. Perencanaan rilis meliputi domain, TLS, konfigurasi, migrasi, rollback, serta verifikasi. [Twelve-Factor App](https://12factor.net/) memberi prinsip pengemasan dan konfigurasi; [Let’s Encrypt](https://letsencrypt.org/how-it-works/) menjelaskan siklus sertifikat TLS.

Jenis hosting bergantung pada beban: konten statis dapat dilayani dari penyimpanan/CDN; proses dinamis memerlukan runtime dan data. Jangan menganggap platform otomatis mengurus backup database, keamanan aplikasi, atau kepemilikan domain tanpa memeriksa batas tanggung jawabnya.

## Konsep yang perlu dikuasai

### Lingkungan dan build

Pisahkan local, staging, dan produksi sesuai kebutuhan. Build harus dapat diulang dari versi kode dan dependency yang diketahui. Artefak yang diuji idealnya sama dengan artefak yang dirilis agar perbedaan lingkungan tidak menyembunyikan bug.

### Konfigurasi

Simpan alamat layanan, secret, dan flag per lingkungan; jangan hardcode rahasia dalam source atau bundel frontend. Catat siapa memiliki izin mengubah konfigurasi dan cara auditnya. Default harus aman bila suatu variabel tidak tersedia.

### Domain dan TLS

Arahkan DNS ke penyedia yang benar, terbitkan sertifikat, dan uji perpanjangan otomatis. Pastikan nama domain utama, subdomain, serta redirect HTTP ke HTTPS sesuai desain. Status “ikon gembok” tidak berarti aplikasi aman dari semua ancaman.

### Migrasi data

Rencanakan urutan migrasi database relatif terhadap kode; perubahan yang kompatibel dua versi mengurangi risiko rilis bertahap. Cadangkan atau siapkan pemulihan sebelum perubahan yang tidak bisa dibatalkan. Uji migrasi terhadap data realistis tanpa membocorkan data nyata.

### Strategi rilis

Rilis serentak sederhana cukup untuk proyek kecil; rolling, blue-green, atau canary membantu saat trafik/risiko memerlukan. Tetapkan pengamat, indikator sehat, ambang berhenti, dan rollback. Rilis bertahap tanpa metrik yang jelas tidak memberi manfaat penuh.

### CDN dan cache

Aset statis dapat diberi nama berhash dan cache panjang; dokumen HTML dan data dinamis perlu aturan lebih hati-hati. Pastikan invalidasi/versi konten saat rilis. Cache yang salah dapat melayani versi lama atau data pribadi.

### Ketersediaan dan skala

Tentukan target layanan, batas sumber daya, koneksi DB, antrean pekerjaan, dan perilaku saat lonjakan. Skala horizontal tidak mengganti optimasi query dan batas beban. Uji dari titik pandang pengguna, bukan hanya proses server hidup.

### Verifikasi pascarilis

Periksa URL utama, alur penting, sertifikat, izin, asset, error, metrik performa, dan log terstruktur. Pastikan operator tahu siapa yang dihubungi dan bagaimana mengembalikan versi. Dokumentasikan waktu dan hasil rilis.

### Biaya dan kepemilikan

Catat biaya domain, compute, penyimpanan, bandwidth, email, log, backup, dan layanan pihak ketiga. Ketahui pemilik akun, tanggal pembaruan, batas anggaran, dan cara migrasi keluar dari layanan.

## Alur kerja pada proyek

1. Pilih bentuk hosting berdasarkan kebutuhan aktual.
2. Siapkan build reproducible, konfigurasi, secret, domain, dan TLS.
3. Tinjau migrasi dan backup; jalankan uji staging relevan.
4. Tentukan langkah rilis, pengamat, indikator kesehatan, rollback.
5. Rilis lalu periksa alur penting dari luar dan metrik.
6. Dokumentasikan versi, biaya, serta tindak lanjut.

## Contoh penerapan

Situs kelas statis bisa di-host sebagai file/CDN, sedangkan pendaftaran membutuhkan layanan penyimpan data. Setelah rilis, operator mencoba satu pendaftaran uji yang aman, memeriksa email/konfirmasi dan status database, serta membatalkan uji sesuai kebijakan. Bila permintaan gagal meningkat, rilis dihentikan atau dibatalkan sesuai runbook.

## Keputusan dan pertukaran yang perlu dicatat

- Platform serverless, VPS, dan platform terkelola berbeda dalam kontrol, biaya, batas runtime, serta tanggung jawab operasi.
- Rollback kode tidak selalu dapat membalik migrasi data; rancang kompatibilitas dan pemulihan sebelum rilis.
- Domain dan akun penyedia sebaiknya dimiliki organisasi, bukan akun pribadi pengembang.

## Pemeriksaan hasil

- [ ] Sertifikat dan pembaruan diuji.
- [ ] Secret tidak disertakan dalam artefak publik.
- [ ] Migrasi dan rollback atau pemulihan terdokumentasi.
- [ ] Alur utama diverifikasi pascarilis.
- [ ] Pemilik domain, backup, biaya, dan alarm jelas.

## Serah terima untuk AI atau tim proyek

Masukan: build teruji, kontrak data, kebutuhan operasi. Keluaran: pipeline rilis, konfigurasi, catatan migrasi, runbook rollback, dan bukti pemeriksaan pascarilis. AI operasi dapat menyusun prosedur, tetapi pemilik layanan memegang izin produksi dan keputusan rilis.

## Sumber utama dan tingkat bukti

1. [Twelve-Factor App](https://12factor.net/) — praktik konfigurasi dan proses aplikasi
2. [Let’s Encrypt — How it works](https://letsencrypt.org/how-it-works/) — siklus sertifikat TLS
3. [Google SRE — Monitoring](https://sre.google/sre-book/monitoring-distributed-systems/) — pengamatan layanan

> **Cara membaca bukti:** spesifikasi/standar menentukan perilaku atau kriteria yang diuji; panduan resmi memberi praktik yang dianjurkan; penelitian pengguna memberi temuan kontekstual yang tetap harus diuji pada pengguna website ini. Pilihan alat dan ketentuan hukum harus diperiksa lagi saat implementasi.

## Pendalaman operasional untuk Website Builder

> Revisi integrasi 24 September 2026. Bagian ini menambah keputusan implementasi dan bukti penerimaan. Contoh merupakan rancangan, bukan hasil uji pengguna.

### Pisahkan prototipe, preview, dan produksi

Tuliskan status keluaran secara eksplisit. Prototipe dapat memakai data contoh; preview membuktikan versi dapat dijalankan dalam lingkungan tertentu; produksi memerlukan integrasi, data, kepemilikan, dan operasi yang sesuai. Jangan menyebut formulir aktif jika hanya menampilkan pesan sukses tanpa pengiriman atau penyimpanan.

Sebelum rilis, catat artefak yang diuji, konfigurasi yang diperlukan, status migrasi, pemilik domain, pemantauan, dan cara pemulihan. Aksi eksternal mengikuti otorisasi yang sudah diberikan pengguna dan aturan platform; jangan menambah permintaan persetujuan berulang tanpa alasan, jangan pula menganggap permintaan desain saja mengizinkan publikasi.

Jika proyek berada di platform pembangun/hosting tertentu, gunakan alur resminya. Untuk proyek yang sudah ada, pertahankan tooling, runtime, dan kebiasaan rilis kecuali ada alasan terukur untuk mengubahnya. Akses akun dan kredensial tidak muncul hanya karena skill menyebut nama penyedia.

**Pemeriksaan nyata:** buka URL setelah rilis, jalankan tugas utama secara aman, periksa aset dan konfigurasi klien, lalu lihat kesalahan server. Rollback kode tidak otomatis mengembalikan data; rencana migrasi harus mengantisipasi versi lama yang kembali berjalan.

Sumber: [Let's Encrypt](https://letsencrypt.org/how-it-works/) dan [Google SRE Monitoring](https://sre.google/sre-book/monitoring-distributed-systems/). Rincian perintah rilis harus diperiksa pada dokumentasi host aktual.
