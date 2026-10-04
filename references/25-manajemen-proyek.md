# Manajemen Proyek, Prioritas, dan Koordinasi Tim

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

Manajemen proyek menyelaraskan tujuan, orang, waktu, biaya, risiko, serta keputusan agar website benar-benar selesai dan tetap dapat dioperasikan. [Scrum Guide](https://scrumguides.org/scrum-guide.html) adalah salah satu kerangka empiris untuk pekerjaan kompleks, sedangkan [GOV.UK Discovery](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works) menekankan keputusan berdasarkan pemahaman masalah.

Kerangka kerja dipilih sesuai ukuran dan ketidakpastian proyek. Proyek kecil mungkin cukup dengan daftar kerja yang jelas dan review rutin; proyek berdampak tinggi memerlukan tata kelola rilis, anggaran, audit, serta pemilik keputusan yang lebih formal.

## Konsep yang perlu dikuasai

### Tujuan dan ruang lingkup

Nyatakan hasil yang ingin dicapai, audiens, batas proyek, dan definisi selesai. Perbedaan antara “fitur sudah dikode” dan “pengguna dapat berhasil serta operator siap” harus eksplisit. Tinjau perubahan ruang lingkup saat bukti baru muncul.

### Backlog dan prioritas

Pecah pekerjaan menjadi unit bernilai dan dapat diuji, dengan dependensi serta risiko. Dahulukan hambatan paling berisiko yang dapat dipelajari atau diselesaikan. Hindari menjadikan setiap permintaan pemangku kepentingan setara tanpa analisis.

### Peran dan keputusan

Tetapkan pemilik produk, konten, desain, kode, data, keamanan, pengujian, operasi, dan siapa yang menyetujui rilis. Satu orang boleh memegang beberapa peran, tetapi tanggung jawab tidak boleh hilang. Catat keputusan dan alasan.

### Perkiraan dan kapasitas

Perkirakan kerja dengan ketidakpastian, dependensi, serta waktu untuk riset, aksesibilitas, keamanan, QA, dan operasi. Pisahkan tenggat keras dari harapan. Tinjau perkiraan ketika temuan teknis/riset mengubah cakupan.

### Ritme pemeriksaan

Gunakan demo hasil yang bekerja, review pengguna, dan retrospektif untuk menyesuaikan prioritas. Laporan status menyebut hasil, hambatan, keputusan yang diperlukan, dan risiko, bukan hanya jam kerja. Hindari rapat tanpa tindakan.

### Kualitas dan definition of done

Untuk pekerjaan berisiko, selesai berarti kriteria penerimaan terpenuhi, review terkait dilakukan, tes relevan lulus, konten benar, dapat dipantau, dan dapat dipulihkan. Kriteria dapat berbeda menurut jenis perubahan, tetapi harus dipahami sebelum mengerjakan.

### Risiko dan perubahan

Simpan risk register: kejadian, dampak, kemungkinan, pemilik, mitigasi, dan tanda pemicu. Contoh: vendor email bermasalah, lisensi gambar tidak jelas, migrasi gagal, atau domain milik akun pribadi. Perubahan keputusan perlu jejak dan komunikasi lintas fungsi.

### Biaya dan pengadaan

Hitung biaya pengembangan, hosting, domain, layanan pihak ketiga, dukungan, lisensi, serta pemeliharaan. Penghematan saat build yang meningkatkan beban operasi jangka panjang perlu dipertimbangkan. Tinjau batas pemakaian layanan dan biaya tak terduga.

### Penutupan dan keberlanjutan

Setelah rilis, serahkan akses, dokumentasi, runbook, pemilik konten, backup, metrik, dan jadwal tinjau. Nilai apakah hasil pengguna tercapai; hapus atau revisi fitur yang tidak membantu. Website adalah layanan yang berlanjut, bukan hanya proyek peluncuran.

## Alur kerja pada proyek

1. Tetapkan masalah, hasil, batas, dan pemilik keputusan.
2. Buat backlog berprioritas dengan dependensi serta risiko.
3. Susun target dan kapasitas yang menyertakan riset, QA, serta operasi.
4. Tunjukkan hasil kerja secara berkala kepada pengguna/pemilik proses.
5. Verifikasi definition of done sebelum rilis.
6. Serahkan operasi dan tinjau hasil setelah digunakan.

## Contoh penerapan

Untuk situs kelas, tim menunda kupon promosi setelah mengetahui jadwal sering tidak akurat. Iterasi awal menuntaskan data jadwal, pendaftaran, aksesibilitas form, dan pemberitahuan operator. Review mingguan menunjukkan alur yang bekerja; daftar risiko mencatat ketergantungan pada penyedia email dan kepemilikan domain.

## Keputusan dan pertukaran yang perlu dicatat

- Agile berarti belajar dan menyesuaikan dengan bukti, bukan bekerja tanpa dokumentasi atau mutu.
- Estimasi adalah perkiraan dengan ketidakpastian; jangan menyajikan kepastian palsu.
- Satu metrik pengiriman kode tidak mengganti ukuran hasil pengguna.

## Pemeriksaan hasil

- [ ] Tujuan dan definisi selesai dipahami semua peran.
- [ ] Prioritas memiliki alasan dan dependensi jelas.
- [ ] Risiko, biaya berulang, dan pemilik keputusan tercatat.
- [ ] Review menguji hasil yang berfungsi.
- [ ] Setelah rilis ada pemilik, runbook, dan jadwal evaluasi.

## Serah terima untuk AI atau tim proyek

Masukan: brief masalah, kebutuhan, kapasitas, batas anggaran. Keluaran: backlog, roadmap, keputusan, risiko, definition of done, catatan rilis, serta rencana operasi. AI koordinator dapat mengurai pekerjaan dan mengingatkan dependensi; pemilik proyek memutus prioritas, biaya, dan penerimaan hasil.

## Sumber utama dan tingkat bukti

1. [The Scrum Guide](https://scrumguides.org/scrum-guide.html) — kerangka pengelolaan empiris
2. [GOV.UK — Discovery](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works) — pembingkaian masalah dan keputusan lanjut
3. [DORA — Metrics](https://dora.dev/guides/dora-metrics/) — pengukuran kinerja pengiriman perangkat lunak

> **Cara membaca bukti:** spesifikasi/standar menentukan perilaku atau kriteria yang diuji; panduan resmi memberi praktik yang dianjurkan; penelitian pengguna memberi temuan kontekstual yang tetap harus diuji pada pengguna website ini. Pilihan alat dan ketentuan hukum harus diperiksa lagi saat implementasi.

## Pendalaman operasional untuk Website Builder

> Revisi integrasi 24 September 2026. Bagian ini menambah keputusan implementasi dan bukti penerimaan. Contoh merupakan rancangan, bukan hasil uji pengguna.

### Orkestrasi kerja tanpa memperbesar birokrasi

Bagi tanggung jawab menurut keluaran: brief, konten, desain, implementasi, verifikasi, dan operasi. Satu AI dapat memegang semua tahap secara berurutan. Jika subagen diizinkan, bagikan pekerjaan yang mandiri dengan batas file dan kontrak yang jelas; pekerjaan yang bergantung pada keputusan sebelumnya tetap berurutan.

Serah terima ringkas menyebut tujuan, artefak, sumber fakta, keputusan, asumsi, risiko, dan bukti. Reviewer menerima hasil serta bahan mentah yang cukup; untuk uji independen, hindari membocorkan jawaban yang diharapkan. Penilaian AI melengkapi, bukan menggantikan pengguna nyata atau keahlian khusus.

**Gerbang selesai:** tugas inti berfungsi; tidak ada penghalang akses, kebocoran data, atau fakta bisnis yang menyesatkan; tampilan telah dilihat; status integrasi jelas; hasil uji sesuai versi; pemilik mengetahui batas yang tersisa. Perubahan kosmetik kecil tidak perlu seluruh proses proyek baru.

Ketika alat tidak tersedia, selesaikan bagian yang dapat dibuat, jelaskan bagian belum terverifikasi, dan serahkan pekerjaan yang bisa dilanjutkan. Jangan mengaku mengganti model atau tingkat penalaran hanya lewat instruksi persona. Pilihan model mengikuti pengaturan host dan kemampuan alat yang benar-benar tersedia.

**Pengendalian mutu:** perbaiki kegagalan konkret lalu uji ulang area terkait. Berhenti ketika kriteria terpenuhi dan batas diketahui; jangan mengejar label “sempurna” dengan pengujian berulang tanpa pertanyaan baru.

Sumber proses: [GOV.UK Discovery](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works). Matriks peran dan gerbang di atas adalah rancangan operasional project.
