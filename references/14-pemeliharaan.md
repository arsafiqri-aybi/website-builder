# Pemeliharaan, Observabilitas, dan Respons Insiden

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

Pemeliharaan menjaga website tetap benar, aman, tersedia, dan relevan setelah diluncurkan. Observabilitas menggabungkan metrik, log, dan trace untuk memahami perilaku sistem; [OpenTelemetry](https://opentelemetry.io/docs/concepts/observability-primer/) menjelaskan konsepnya. [Google SRE](https://sre.google/sre-book/monitoring-distributed-systems/) membahas indikator seperti latensi, trafik, error, dan saturasi.

Semakin banyak fitur, pengguna, dan integrasi, semakin besar beban perawatan. Pemeliharaan juga mencakup isi halaman, tautan, lisensi, kontrak vendor, serta perilaku yang berubah saat browser dan dependensi diperbarui.

## Konsep yang perlu dikuasai

### Inventaris dan kepemilikan

Catat sistem, domain, sertifikat, repository, pipeline, database, integrasi, jadwal job, dan kontak pemilik. Satu layanan yang tak diketahui penanggung jawabnya menjadi risiko saat gangguan. Perbarui inventaris setiap perubahan.

### Indikator layanan

Pilih metrik yang mencerminkan pengalaman: keberhasilan pendaftaran, waktu respons, error pengguna, kegagalan pembayaran, dan pengiriman email. Empat sinyal emas membantu diagnosis tetapi target disesuaikan jenis layanan. Hindari alarm atas setiap fluktuasi kecil.

### Log, metrik, trace

Log menjawab kejadian, metrik menunjukkan pola, trace mengikuti alur permintaan. Gunakan correlation ID, waktu konsisten, dan batas retensi; jangan masukkan kata sandi, token, atau data pribadi tanpa alasan sah. Observabilitas harus membantu tindakan, bukan sekadar menumpuk data.

### Alarm dan eskalasi

Tentukan kondisi yang memerlukan tindakan segera dan siapa penerimanya. Alarm harus memiliki runbook dan langkah pemulihan; kebisingan membuat alarm penting terabaikan. Uji alarm secara terkendali sebelum insiden.

### Insiden

Kenali dampak, stabilkan sistem, komunikasikan status yang akurat, lalu perbaiki akar masalah setelah layanan aman. Simpan linimasa tindakan serta keputusan. Tinjauan insiden bertujuan memperbaiki sistem dan proses, bukan mencari kambing hitam.

### Patch dan dependensi

Perbarui runtime, framework, paket, dan image dasar menurut tingkat risiko; uji regresi serta sediakan rollback. Tinjau pemberitahuan kerentanan yang relevan dengan pemakaian nyata. Paket tak dipakai dihapus untuk memperkecil permukaan risiko.

### Backup dan latihan restore

Pantau keberhasilan backup, umur, enkripsi, hak akses, serta proses restore. Uji pemulihan di lingkungan yang sesuai dan catat waktunya. Perencanaan data harus mencakup penghapusan sesuai retensi meski ada backup.

### Kualitas konten

Jadwalkan pemeriksaan tanggal, harga, tautan, informasi legal, dan kontak. Konten yang akurat saat diluncurkan bisa menjadi menyesatkan setelah jadwal berubah. Tetapkan tanggal tinjau dan pemilik untuk setiap jenis halaman.

### Perbaikan berkelanjutan

Gunakan bug, riset pengguna, metrik, serta insiden untuk mengubah prioritas. Bedakan masalah produk, konten, dan infrastruktur agar perbaikan tepat. Catat alasan mengakhiri fitur yang tidak lagi berguna.

## Alur kerja pada proyek

1. Buat daftar aset, penanggung jawab, indikator, dan risiko.
2. Pasang pemantauan bermakna dan kebijakan data log.
3. Siapkan runbook untuk gangguan umum serta latihan restore.
4. Tinjau dependensi, biaya, keamanan, konten, dan akses secara berkala.
5. Saat insiden, stabilkan, komunikasikan, dokumentasikan, dan tindak lanjuti.
6. Ukur kembali hasil setelah setiap perubahan penting.

## Contoh penerapan

Jika formulir kelas gagal pada malam hari, alarm berbasis tingkat kegagalan transaksi memberi tahu operator. Runbook memeriksa status layanan, error aplikasi, koneksi DB, dan provider email. Setelah pemulihan, tim memeriksa apakah ada pendaftaran yang statusnya tak pasti dan memberi kabar kepada pengguna yang terdampak sesuai kebutuhan.

## Keputusan dan pertukaran yang perlu dicatat

- SLO dan SLA berbeda: sasaran internal kualitas layanan tidak otomatis janji kontraktual.
- Lebih banyak log dapat meningkatkan biaya serta risiko privasi; kumpulkan informasi yang membantu diagnosis.
- Frekuensi pembaruan tergantung perubahan dan paparan risiko, bukan kalender semata.

## Pemeriksaan hasil

- [ ] Ada pemilik sistem, domain, dan konten.
- [ ] Alarm prioritas tinggi memiliki langkah tindakan.
- [ ] Log tidak membocorkan rahasia; retensi ditentukan.
- [ ] Restore diuji dan target pemulihan diketahui.
- [ ] Insiden berakhir dengan tindak lanjut yang dapat dilacak.

## Serah terima untuk AI atau tim proyek

Masukan: sistem berjalan, data metrik, kontrak layanan. Keluaran: dashboard, runbook, jadwal tinjau, catatan insiden, dan daftar perbaikan. AI operasi dapat merangkum sinyal dan usulan, tetapi tindakan terhadap produksi perlu diverifikasi oleh pemilik yang berwenang.

## Sumber utama dan tingkat bukti

1. [Google SRE — Monitoring](https://sre.google/sre-book/monitoring-distributed-systems/) — prinsip pemantauan layanan
2. [OpenTelemetry — Observability primer](https://opentelemetry.io/docs/concepts/observability-primer/) — konsep sinyal observabilitas
3. [PostgreSQL — Backup](https://www.postgresql.org/docs/current/backup.html) — dasar pemulihan data

> **Cara membaca bukti:** spesifikasi/standar menentukan perilaku atau kriteria yang diuji; panduan resmi memberi praktik yang dianjurkan; penelitian pengguna memberi temuan kontekstual yang tetap harus diuji pada pengguna website ini. Pilihan alat dan ketentuan hukum harus diperiksa lagi saat implementasi.

## Pendalaman operasional untuk Website Builder

> Revisi integrasi 24 September 2026. Bagian ini menambah keputusan implementasi dan bukti penerimaan. Contoh merupakan rancangan, bukan hasil uji pengguna.

### Pemeliharaan sebagai perjalanan pengguna

Pantau keberhasilan tugas, bukan hanya proses yang hidup. Status HTTP 200 tidak cukup jika pendaftaran tidak tersimpan. Pilih indikator dari titik pandang pengguna dan hubungkan ke metrik latensi, trafik, galat, serta saturasi. Bedakan galat pada permintaan berhasil dan gagal ketika menganalisis durasi.

Sediakan runbook pendek: gejala, dampak, pemeriksaan awal, tindakan pemulihan, verifikasi, dan pemilik. Jangan menaruh token atau data pribadi ke contoh log. Correlation ID membantu menyambungkan peristiwa tanpa menyalin seluruh payload. Retensi log, biaya, dan akses masuk rancangan sejak awal.

Setelah perubahan desain, periksa apakah konten nyata berkembang: judul lebih panjang, harga berubah, aset baru berukuran besar, atau plugin menambah script. Sistem desain bisa tetap konsisten sementara pengalaman memburuk karena isi dan integrasi. Pantau juga hilangnya takarir, tautan kebijakan, serta pengaturan preferensi setelah pembaruan.

**Kasus latihan:** email gagal tetapi transaksi sah. Operator harus membedakan masalah pengiriman dari kehilangan pesanan, melakukan retry yang aman, serta menghindari pemberitahuan keliru. Uji restore dan pemulihan secara terpisah dari keberhasilan backup.

Sumber: [Google SRE Monitoring](https://sre.google/sre-book/monitoring-distributed-systems/). Frekuensi latihan, target ketersediaan, dan alarm disesuaikan dampak layanan; tidak ada target universal yang dipaksakan skill.
