# Analitik Web dan Pengukuran Produk

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

Analitik mengubah kejadian penggunaan website menjadi bukti untuk memperbaiki produk, konten, dan operasi. Metrik harus ditautkan ke tugas serta keputusan, bukan sekadar jumlah klik. [GOV.UK Measuring Success](https://www.gov.uk/service-manual/measuring-success) membahas ukuran layanan; [dokumentasi Analytics tentang event](https://support.google.com/analytics/answer/9322688) adalah contoh implementasi, bukan kewajiban memakai satu produk.

Pengukuran memiliki batas: data dapat hilang karena pemblokiran, persetujuan, salah konfigurasi, atau identitas lintas perangkat; observasi angka tidak otomatis membuktikan sebab. Desain pengukuran harus mengikuti kebijakan privasi.

## Konsep yang perlu dikuasai

### Pertanyaan dan metrik

Mulai dengan keputusan: apakah pengunjung bisa menemukan jadwal? Ukur penemuan jadwal, penyelesaian pendaftaran, alasan kegagalan, dan permintaan bantuan. Metrik kesombongan seperti pageview tinggi dapat menyesatkan bila orang terus kembali karena informasi tidak jelas.

### Pohon hasil

Hubungkan tujuan organisasi ke hasil pengguna, perilaku, dan metrik teknis. Misalnya keberhasilan pendaftaran dipengaruhi penemuan kelas, formulir, ketersediaan kursi, dan sistem email. Pisahkan leading indicator dari hasil akhir.

### Rencana event

Definisikan nama event, kapan dikirim, parameter yang diperbolehkan, dan id anonim bila diperlukan. Jangan menaruh email, nama, atau isi bebas ke properti analitik tanpa dasar sah. Versikan skema event agar perubahan tidak merusak dashboard.

### Funnel dan segmentasi

Funnel menunjukkan tahap yang dilalui, tetapi penurunan di suatu tahap bisa normal bila pengguna menemukan kelas yang tidak sesuai. Segmen berdasarkan perangkat, halaman, atau kelompok yang sah dapat mengungkap masalah; hindari segmentasi yang mengidentifikasi orang tanpa kebutuhan.

### Kualitas data

Periksa duplikasi event, bot, perbedaan zona waktu, perubahan URL, pemblokiran tracking, dan definisi “pengguna” atau “konversi”. Catat tanggal rilis yang mengubah instrumentasi. Bandingkan event penting dengan catatan transaksi backend tanpa menyalin data pribadi sembarangan.

### Riset kualitatif

Analitik menjawab pola apa yang terjadi; wawancara dan uji kegunaan membantu menjelaskan mengapa. Gabungkan dengan tiket dukungan, pencarian tanpa hasil, serta kesalahan sistem. Jangan menyimpulkan motif dari klik semata.

### Eksperimen

Untuk perubahan yang dampaknya sulit diprediksi, tetapkan hipotesis, metrik utama, batas keamanan, ukuran sampel/pengamatan yang layak, serta kriteria berhenti. Hindari melihat hasil sementara berulang lalu mengumumkan kemenangan tanpa rencana analisis.

### Privasi dan retensi

Minimalkan pengumpulan, jelaskan tujuan, tentukan dasar pemrosesan yang berlaku, masa simpan, akses, serta penarikan/penghapusan jika relevan. Penggunaan layanan pihak ketiga membawa perpindahan data yang harus ditinjau. [W3C Privacy Principles](https://www.w3.org/TR/privacy-principles/) mendukung prinsip minimisasi dan transparansi.

### Tindakan dan umpan balik

Setiap dashboard harus punya pemilik dan keputusan yang mungkin diambil. Tinjau perubahan setelah rilis, cari kejadian luar yang memengaruhi angka, dan dokumentasikan keyakinan kesimpulan. Ukur hasil pengguna, bukan hanya aktivitas alat.

## Alur kerja pada proyek

1. Tentukan keputusan dan hasil pengguna yang ingin dinilai.
2. Buat definisi metrik dan skema event minimal.
3. Tinjau privasi, dasar data, retensi, dan akses.
4. Implementasi serta validasi event di staging/produksi.
5. Bandingkan pola dengan riset pengguna dan data operasional.
6. Ubah produk lalu evaluasi dampaknya dengan catatan keterbatasan.

## Contoh penerapan

Tim ingin tahu apakah halaman jadwal membantu. Event “lihat_jadwal”, “pilih_sesi”, dan “pendaftaran_berhasil” didefinisikan tanpa email. Ketika banyak orang keluar setelah memilih sesi, tim memeriksa stok kursi, biaya, error backend, dan wawancara; mereka tidak otomatis menyalahkan warna tombol.

## Keputusan dan pertukaran yang perlu dicatat

- Pengukuran sisi klien dapat meleset dari transaksi yang benar-benar tersimpan; hasil akhir divalidasi dengan sumber otoritatif.
- Eksperimen layak bila lalu lintas, etika, dan dampaknya mendukung; uji kegunaan sering lebih tepat untuk hambatan awal.
- Laporan agregat pun perlu pemeriksaan risiko reidentifikasi pada segmen kecil.

## Pemeriksaan hasil

- [ ] Definisi event dan metrik terdokumentasi.
- [ ] Tidak ada data pribadi tidak perlu dalam payload.
- [ ] Dashboard menunjukkan kualitas sampel dan perubahan instrumentasi.
- [ ] Hasil dibaca bersama data kualitatif.
- [ ] Setiap temuan penting mengarah ke keputusan yang dapat diuji ulang.

## Serah terima untuk AI atau tim proyek

Masukan: tujuan produk, kebijakan privasi, alur. Keluaran: rencana pengukuran, kamus event, dashboard, analisis keterbatasan, serta rekomendasi eksperimen. AI analis dapat mencari pola; pemilik produk memeriksa sebab alternatif dan memutuskan perubahan.

## Sumber utama dan tingkat bukti

1. [GOV.UK — Measuring Success](https://www.gov.uk/service-manual/measuring-success) — metrik keberhasilan layanan
2. [Google Analytics — Events](https://support.google.com/analytics/answer/9322688) — contoh skema pengumpulan event
3. [W3C — Privacy Principles](https://www.w3.org/TR/privacy-principles/) — minimisasi dan transparansi data

> **Cara membaca bukti:** spesifikasi/standar menentukan perilaku atau kriteria yang diuji; panduan resmi memberi praktik yang dianjurkan; penelitian pengguna memberi temuan kontekstual yang tetap harus diuji pada pengguna website ini. Pilihan alat dan ketentuan hukum harus diperiksa lagi saat implementasi.

## Pendalaman operasional untuk Website Builder

> Revisi integrasi 24 September 2026. Bagian ini menambah keputusan implementasi dan bukti penerimaan. Contoh merupakan rancangan, bukan hasil uji pengguna.

### Eksperimen dan analitik yang menjawab keputusan

Susun metrik utama dari hasil nyata: pesanan sah, formulir terkirim, informasi ditemukan. Bedakan indikator niat seperti klik tombol dari hasil otoritatif seperti catatan server. Hindari menganggap waktu kunjungan lebih lama selalu baik; pengguna bisa sedang kebingungan.

Kamus event minimum mencatat nama, pemicu, parameter yang diizinkan, sumber, deduplikasi, retensi, dan pemilik. Audit payload aktual agar URL, pencarian bebas, atau pesan galat tidak membawa data pribadi tanpa kebutuhan. Penolakan pelacakan dan pemblokiran browser membuat sampel tidak lengkap; jelaskan keterbatasannya.

Untuk A/B, tetapkan unit pengacakan, hipotesis, metrik primer, ambang efek yang berguna, rencana durasi/sampel, serta indikator dampak buruk sebelum membaca hasil. Jangan menghentikan eksperimen hanya ketika angka sementara menguntungkan. Trafik rendah sering lebih cocok untuk riset tugas dan perbaikan hambatan yang jelas daripada janji signifikansi cepat.

**Kenyamanan sensori:** catat penggunaan mute/reduced motion secara proporsional jika memang dibutuhkan dan sah; tidak perlu mengumpulkan diagnosis. Peningkatan konversi tidak menutup kenaikan salah beli, pembatalan, atau keluhan akses.

Sumber: [W3C Privacy Principles](https://www.w3.org/TR/privacy-principles/) dan [GOV.UK Measuring Success](https://www.gov.uk/service-manual/measuring-success). Rencana eksperimen di atas adalah praktik analisis yang harus disesuaikan desain studi, bukan rumus jumlah sampel universal.
