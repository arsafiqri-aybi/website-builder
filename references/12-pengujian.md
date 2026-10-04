# Pengujian, Quality Assurance, dan Validasi

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

Pengujian memeriksa perilaku website terhadap kebutuhan dan risiko, dari logika kecil hingga perjalanan pengguna penuh. QA juga mencakup pemeriksaan isi, aksesibilitas, keamanan, performa, dan kesiapan operasi. [MDN Testing](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Testing) membahas pengujian lintas browser; [W3C WAI](https://www.w3.org/WAI/test-evaluate/) menekankan kombinasi evaluasi otomatis dan manusia.

Tidak semua perubahan memerlukan rangkaian tes yang sama. Prioritaskan alur yang jika rusak merugikan pengguna, uang, data, keamanan, atau kepercayaan.

## Konsep yang perlu dikuasai

### Strategi berbasis risiko

Petakan tugas utama dan mode kegagalan. Gunakan unit test untuk aturan murni, integration test untuk database/API, dan end-to-end untuk beberapa perjalanan paling penting. Jumlah tes tidak menggantikan kualitas kasus dan pemeliharaannya.

### Kriteria penerimaan

Turunkan kasus dari kebutuhan: input normal, batas, kosong, invalid, hak akses, duplikasi, jaringan lambat, dan pembatalan. Buat hasil yang dapat diamati. Tes yang menyalin implementasi persis sering gagal menemukan kesalahan desain.

### Unit dan integrasi

Uji aturan seperti kuota atau harga secara cepat dan deterministik. Pada integrasi, uji query, transaction, endpoint, dan kontrak layanan luar dengan lingkungan yang terkendali. Hindari mock berlebihan yang membuat tes lulus sementara sistem nyata gagal.

### E2E dan browser

Uji beberapa alur kritis lewat browser nyata: mencari kelas, mendaftar, melihat konfirmasi. Periksa browser/perangkat target berdasarkan audiens; [Playwright](https://playwright.dev/docs/intro) adalah salah satu alat otomasi, bukan syarat tunggal. Gunakan selector yang stabil dan tunggu keadaan, bukan delay tetap.

### Aksesibilitas

Jalankan pemeriksa otomatis untuk masalah yang dapat dideteksi, kemudian lakukan inspeksi keyboard, urutan fokus, zoom, nama aksesibel, dan teknologi bantu pada alur penting. Alat otomatis tidak dapat memutuskan kualitas alt dan keterpahaman pesan.

### Keamanan dan privasi

Uji akses lintas akun, input yang mencoba injeksi, penghapusan data, serta log yang tidak membocorkan rahasia. Pengujian dengan data produksi membutuhkan perlindungan dan izin yang tepat. Tambahkan skenario ancaman ke regresi.

### Kinerja dan ketahanan

Ukur di lab serta data lapangan bila tersedia; uji beban sesuai asumsi lalu lintas. Jalankan kondisi server lambat, API gagal, asset hilang, dan cadangan/restore. Satu skor tunggal tidak mewakili semua pengalaman.

### Data dan lingkungan uji

Gunakan data sintetis yang mencakup kasus batas dan isi panjang. Samakan bagian lingkungan yang relevan dengan produksi tanpa menyalin data pribadi sembarangan. Bersihkan state antar tes agar hasil dapat diulang.

### Pelaporan dan triase

Laporan bug memuat langkah, hasil sebenarnya, hasil yang diharapkan, lingkungan, bukti, dan dampak. Kelompokkan menurut risiko, bukan hanya kemudahan perbaikan. Setelah perbaikan, uji kembali akar masalah serta alur sekitarnya.

## Alur kerja pada proyek

1. Petakan risiko dan kebutuhan ke kasus uji.
2. Bangun tes aturan dan integrasi untuk invariannya.
3. Otomatiskan alur browser yang bernilai tinggi.
4. Tambahkan pemeriksaan manual aksesibilitas, konten, dan keamanan.
5. Uji kondisi gagal serta perangkat sasaran.
6. Catat bukti, perbaiki, dan jalankan regresi sebelum rilis.

## Contoh penerapan

Dalam situs kelas, tes unit memeriksa perhitungan kursi; tes integrasi mengirim dua pendaftaran bersamaan; tes browser memastikan pengguna melihat pesan kelas penuh dan dapat memilih sesi lain. Penguji keyboard memeriksa fokus pada pesan kesalahan. Hasil semuanya ditautkan ke kriteria penerimaan yang sama.

## Keputusan dan pertukaran yang perlu dicatat

- Jangan menulis tes hanya untuk menaikkan angka cakupan; pilih skenario yang mendeteksi kegagalan nyata.
- Tes snapshot visual cocok untuk regresi tampilan, tetapi perlu peninjauan makna dan responsif.
- Pengujian produksi harus menjaga data dan pengalaman pengguna serta punya jalan pemulihan.

## Pemeriksaan hasil

- [ ] Alur inti berhasil pada perangkat/browser sasaran.
- [ ] Kasus gagal, batas, izin, dan concurrency diuji.
- [ ] Aksesibilitas diperiksa manual pada tugas utama.
- [ ] Bug kritis memiliki reproduksi dan bukti perbaikan.
- [ ] Rencana rilis menyebut hasil uji serta risiko tersisa.

## Serah terima untuk AI atau tim proyek

Masukan: kriteria penerimaan, model ancaman, kontrak API. Keluaran: matriks risiko-uji, hasil otomatis/manual, laporan bug, dan keputusan kesiapan rilis. AI QA menyusun kasus; pengembang memperbaiki; reviewer manusia menilai kegunaan dan konten yang tidak dapat diuji otomatis.

## Sumber utama dan tingkat bukti

1. [MDN — Testing](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Testing) — pengujian lintas browser
2. [W3C WAI — Evaluating accessibility](https://www.w3.org/WAI/test-evaluate/) — gabungan alat dan evaluasi manusia
3. [Playwright Documentation](https://playwright.dev/docs/intro) — contoh alat uji browser

> **Cara membaca bukti:** spesifikasi/standar menentukan perilaku atau kriteria yang diuji; panduan resmi memberi praktik yang dianjurkan; penelitian pengguna memberi temuan kontekstual yang tetap harus diuji pada pengguna website ini. Pilihan alat dan ketentuan hukum harus diperiksa lagi saat implementasi.

## Pendalaman operasional untuk Website Builder

> Revisi integrasi 24 September 2026. Bagian ini menambah keputusan implementasi dan bukti penerimaan. Contoh merupakan rancangan, bukan hasil uji pengguna.

### Bukti uji yang tidak melebihkan hasil

Pisahkan pemeriksaan statis, eksekusi fungsi, inspeksi visual, evaluasi aksesibilitas, uji dengan pengguna, dan pengukuran lapangan. Masing-masing menjawab pertanyaan berbeda. Screenshot membuktikan tampilan pada satu kondisi; ia tidak membuktikan tombol bekerja. Uji browser otomatis juga tidak membuktikan pengguna memahami bahasa produk.

Buat tabel `risiko → skenario → alat/kondisi → hasil → bukti → batas`. Gunakan status lulus, gagal, belum diuji, atau tidak berlaku disertai alasan. Jangan mengubah belum diuji menjadi lulus untuk melengkapi laporan. Uji tepat pada versi artefak yang akan diserahkan.

Jalankan satu alur utama lengkap beserta satu kegagalan yang paling berbahaya. Untuk transaksi, tambahkan otorisasi dan pengulangan; untuk halaman informasi, prioritaskan tautan, responsif, keyboard, keterbacaan, dan kebenaran isi. Perubahan kecil yang reversibel cukup diperiksa pada area terdampak; hindari suite yang hanya menyalin implementasi.

**Audit visual:** lihat hasil render pada viewport sempit dan lebar, dengan konten panjang serta keadaan kosong/error. **Audit sensori:** fungsi tetap berjalan dengan gerak dikurangi, audio mati, dan haptik tidak didukung. **Audit jaringan:** uji pemuatan lambat atau gagal jika ada operasi remote.

Sumber: [Playwright Best Practices](https://playwright.dev/docs/best-practices) dan [WAI Evaluating](https://www.w3.org/WAI/test-evaluate/). Status siap rilis memerlukan bukti sesuai cakupan, bukan skor rata-rata tunggal.
