# Privasi, Perlindungan Data, dan Aspek Hukum

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

Privasi mengatur alasan, cara, lama, dan pihak yang memproses data pengguna. Hukum yang relevan bergantung pada lokasi pengguna/organisasi, jenis data, dan layanan. Untuk konteks Indonesia, [UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi](https://peraturan.bpk.go.id/Details/229798/uu-no-27-tahun-2022) adalah rujukan primer; [W3C Privacy Principles](https://www.w3.org/TR/privacy-principles/) memuat prinsip desain teknis seperti minimisasi dan transparansi.

Dokumen ini adalah panduan desain produk, bukan pendapat hukum. Sebelum memproses data sensitif, pembayaran, data anak, atau transfer lintas batas, tinjau aturan yang berlaku dan kebijakan organisasi dengan ahli yang berwenang.

## Konsep yang perlu dikuasai

### Pemetaan data

Inventaris data yang dikumpulkan langsung maupun oleh pihak ketiga: form, cookie, log, analitik, email, pembayaran, dan backup. Untuk setiap data, catat tujuan, dasar pemrosesan yang berlaku, lokasi penyimpanan, penerima, retensi, dan pemilik. Data yang tidak diperlukan sebaiknya tidak dikumpulkan.

### Transparansi

Beri pemberitahuan yang dapat dipahami mengenai tujuan, pihak, masa simpan, hak pengguna, serta kontak terkait sesuai ketentuan yang berlaku. Jelaskan saat keputusan pengguna diperlukan, bukan hanya menaruh kebijakan panjang di footer. Klaim privasi harus sama dengan perilaku sistem nyata.

### Dasar pemrosesan dan pilihan

Persetujuan hanyalah salah satu kemungkinan dasar yang diatur hukum; jangan menganggap semua pemrosesan selalu memerlukan kotak centang, atau semua cookie bebas dari aturan. Pilihan dan penarikan harus dievaluasi menurut tujuan, lokasi, dan aturan aktual. Jangan menggunakan dark pattern untuk memperoleh persetujuan.

### Hak subjek data

Rancang alur untuk menerima dan memverifikasi permintaan akses, koreksi, penghapusan, atau hak lain yang berlaku. Periksa batas pengecualian sebelum menjanjikan hasil absolut. Log pemenuhan permintaan dengan aman tanpa mengumpulkan identitas lebih banyak daripada perlu.

### Retensi dan penghapusan

Tetapkan kapan data dihapus atau dianonimkan, termasuk salinan ekspor, log, dan backup sesuai mekanisme yang memungkinkan. Retensi “selamanya” tanpa alasan menambah risiko. Pahami kebutuhan akuntansi/kontrak yang mungkin mengharuskan penyimpanan tertentu.

### Keamanan dan akses

Lindungi data saat transit/tersimpan sesuai risiko, batasi akses berdasarkan tugas, dan audit pihak yang melihat data. Kebocoran melalui log, link publik, atau analitik pihak ketiga tetap kebocoran meski database utama aman. Lakukan penilaian risiko terhadap proses baru.

### Pihak ketiga dan transfer

Daftar penyedia hosting, email, analitik, pembayaran, serta subprosesor. Tinjau kontrak, lokasi dan alur transfer, penghapusan, serta tanggung jawab insiden. Jangan menyatakan data “hanya di Indonesia” tanpa memverifikasi semua pemrosesan.

### Cookie dan pelacak

Klasifikasikan berdasarkan fungsi, penerima, umur, serta tujuan. Implementasi kontrol mengikuti aturan yang berlaku di yurisdiksi sasaran; periksa apakah script benar-benar menunggu pilihan yang diperlukan. Uji penolakan dan perubahan pilihan.

### Hak cipta dan ketentuan layanan

Periksa hak penggunaan foto, font, teks, perangkat lunak, dan logo; penuhi atribusi/lisensi. Buat syarat transaksi, kebijakan pembatalan, dan informasi usaha yang akurat bila website menjual layanan. Detail ketentuan mengikuti sektor dan hukum yang berlaku.

## Alur kerja pada proyek

1. Petakan seluruh aliran data termasuk pihak ketiga dan backup.
2. Tentukan tujuan, dasar yang berlaku, retensi, akses, dan pemilik.
3. Susun pemberitahuan serta pilihan pengguna yang sesuai.
4. Implementasikan hak pengguna dan jalur penanganan insiden.
5. Tinjau penyedia serta transfer dan hak aset.
6. Uji perilaku aktual, lalu tinjau ulang ketika aturan/fitur berubah.

## Contoh penerapan

Form kelas meminta nama dan email untuk konfirmasi, bukan tanggal lahir bila tidak diperlukan. Pengelola mencatat penyedia email, lokasi penyimpanan, masa retensi, dan cara peserta meminta koreksi. Script analitik tidak mengirim alamat email; pemberitahuan privasi menjelaskan pengukuran yang dilakukan sesuai aturan relevan.

## Keputusan dan pertukaran yang perlu dicatat

- Jangan menyalin kebijakan privasi situs lain karena alur data setiap produk berbeda.
- Anonimisasi harus benar-benar menghalangi identifikasi ulang dalam konteksnya; mengganti nama dengan ID belum tentu anonim.
- Aturan Indonesia dan negara lain dapat sama-sama relevan; evaluasi hukum berdasarkan pengguna, kegiatan, dan pasar.

## Pemeriksaan hasil

- [ ] Peta data sesuai implementasi nyata.
- [ ] Tujuan, retensi, dan akses terdokumentasi.
- [ ] Pemberitahuan, hak, dan pilihan berfungsi serta dapat ditemukan.
- [ ] Penyedia dan transfer ditinjau.
- [ ] Aset memiliki lisensi dan klaim produk dapat dibuktikan.

## Serah terima untuk AI atau tim proyek

Masukan: alur data, wilayah pengguna, penyedia, kontrak. Keluaran: register data, persyaratan privasi, kebijakan yang ditinjau, uji pilihan/hak pengguna, dan daftar lisensi. AI dapat menyusun inventaris serta draft; pemilik data dan penasihat hukum yang sesuai memverifikasi kewajiban spesifik sebelum publikasi.

## Sumber utama dan tingkat bukti

1. [UU No. 27 Tahun 2022 — BPK](https://peraturan.bpk.go.id/Details/229798/uu-no-27-tahun-2022) — sumber resmi hukum Indonesia
2. [JDIH Komdigi — UU PDP](https://jdih.komdigi.go.id/produk_hukum/view/id/832/t/undangundang%2Bnomor%2B27%2Btahun%2B2022) — teks peraturan pada kanal pemerintah
3. [W3C — Privacy Principles](https://www.w3.org/TR/privacy-principles/) — prinsip teknis privasi

> **Cara membaca bukti:** spesifikasi/standar menentukan perilaku atau kriteria yang diuji; panduan resmi memberi praktik yang dianjurkan; penelitian pengguna memberi temuan kontekstual yang tetap harus diuji pada pengguna website ini. Pilihan alat dan ketentuan hukum harus diperiksa lagi saat implementasi.

## Pendalaman operasional untuk Website Builder

> Revisi integrasi 24 September 2026. Bagian ini menambah keputusan implementasi dan bukti penerimaan. Contoh merupakan rancangan, bukan hasil uji pengguna.

### Privasi yang terhubung ke implementasi

Mulai dari daftar pemrosesan, bukan menyalin halaman kebijakan. Untuk tiap formulir, cookie, log, analitik, unggahan, dan vendor, catat tujuan, dasar yang relevan, data, pihak penerima, lokasi, akses, retensi, serta mekanisme hak pengguna. Mengganti email dengan ID tidak otomatis membuat data anonim.

Sumber resmi [UU 27/2022](https://peraturan.bpk.go.id/Details/229798/uu-no-27-tahun-2022) diperiksa sebagai titik awal Indonesia. Pemeriksaan ini tidak menetapkan seluruh kewajiban sektoral, peraturan pelaksana, atau yurisdiksi lain per September 2026. Verifikasi aturan yang relevan terhadap layanan dan pasar sebelum menyatakan kepatuhan. Hindari menulis masa retensi atau tenggat legal tanpa dasar yang dibaca.

Pemberitahuan harus sesuai perilaku nyata. Jika analitik membutuhkan pilihan pengguna dalam konteks hukum yang berlaku, uji penolakan, penerimaan, dan perubahan pilihan; pastikan script serta permintaan jaringan mengikuti pilihan itu. Jangan menyimpan preferensi sensorik sebagai dugaan diagnosis atau membuat profil kerentanan psikologis untuk pemasaran.

**Bukti penerimaan:** payload jaringan, log, retensi, vendor, dan isi pemberitahuan konsisten; tidak ada data pribadi di URL publik; akun hanya melihat objek yang sah. Klaim “aman”, “anonim”, atau “sesuai semua hukum” membutuhkan ruang lingkup dan bukti, bukan checkbox.

Sumber desain tambahan: [W3C Privacy Principles](https://www.w3.org/TR/privacy-principles/), yang bukan pengganti hukum.
