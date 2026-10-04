# Arsitektur Informasi dan Navigasi

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

Arsitektur informasi (IA) mengatur apa saja yang ada di website, bagaimana konten dikelompokkan, dinamai, dan ditemukan. IA menjembatani kebutuhan pengguna dengan menu, pencarian, jalur halaman, URL, dan hubungan konten. Struktur yang terlihat rapi bagi tim belum tentu cocok dengan cara pengguna mengelompokkan informasi; [card sorting NN/g](https://www.nngroup.com/articles/card-sorting-definition/) membantu memeriksa model mental.

Berlaku untuk semua situs. Situs satu halaman pun memiliki hierarki judul dan jalur tindakan; katalog besar membutuhkan taksonomi, filter, metadata, dan tata kelola konten.

## Konsep yang perlu dikuasai

### Inventaris dan audit konten

Daftarkan halaman, aset, pemilik, tujuan, frekuensi pembaruan, serta status akurasi. Temukan duplikasi, halaman mati, dan informasi yang belum ada. Inventaris menjadi dasar sebelum membuat menu baru atau memindahkan URL lama.

### Model tugas dan objek

Identifikasi objek yang dicari pengguna seperti kelas, jadwal, lokasi, harga, dan kebijakan. Bedakan objek dari halaman presentasinya; satu kelas bisa muncul dalam daftar, hasil pencarian, dan detail. Tentukan relasi serta metadata yang diperlukan.

### Taksonomi dan pelabelan

Pilih kategori yang saling masuk akal dan istilah dari bahasa pengguna. Label “Program” mungkin terlalu umum bila pengguna mencari “Jadwal kelas”. Catat sinonim untuk pencarian, hindari kategori yang hanya mencerminkan bagan internal organisasi.

### Struktur situs dan kedalaman

Susun peta situs dengan jalur utama untuk setiap tugas, lalu periksa apakah konten kritis terjangkau melalui navigasi dan tautan kontekstual. Tidak ada angka kedalaman menu yang universal; ukur keberhasilan menemukan tugas, bukan menghitung klik semata.

### Navigasi dan orientasi

Bedakan navigasi global, lokal, breadcrumb, tautan terkait, dan langkah proses. Tunjukkan lokasi saat ini dengan teks/status yang jelas. Menu tetap harus dapat dipakai dengan keyboard dan sesuai pola HTML; [tutorial WAI](https://www.w3.org/WAI/tutorials/menus/) memuat contoh.

### Pencarian, filter, urut

Pencarian menjawab kebutuhan berbasis kata; filter mempersempit himpunan; urutan mengubah prioritas hasil. Definisikan perilaku saat kosong, salah ejaan, kombinasi filter, serta status filter setelah kembali. Jangan membangun pencarian sebelum memeriksa apakah struktur dasarnya sudah cukup.

### URL dan perubahan struktur

Gunakan URL stabil, dapat dibaca, dan mewakili sumber daya; tentukan canonical dan redirect ketika memindah halaman publik. Tautan lama dari mesin pencari atau situs lain adalah bagian dari pengalaman pengguna. Perubahan URL perlu inventaris dan rencana migrasi.

### Validasi struktur

Uji card sorting untuk kelompok konsep dan tree testing untuk menemukan tugas pada struktur tanpa pengaruh desain visual. Uji pengguna yang mewakili audiens berbeda. Catat tingkat keberhasilan, jalur keliru, dan alasan salah paham.

### Tata kelola

Tetapkan pemilik kategori, aturan penamaan, kapan item diarsipkan, dan bagaimana halaman baru masuk struktur. IA menurun kualitasnya ketika setiap tim menambah menu tanpa aturan.

## Alur kerja pada proyek

1. Audit halaman dan tugas pengunjung.
2. Definisikan objek, atribut, relasi, dan istilah yang digunakan pengguna.
3. Rancang hierarki awal, jalur navigasi, dan URL.
4. Validasi istilah dengan card sorting atau wawancara; validasi penemuan lewat tree testing.
5. Prototipe navigasi dengan keyboard, layar kecil, dan keadaan pencarian kosong.
6. Tentukan aturan pengarsipan, redirect, serta pemilik kategori.

## Contoh penerapan

Pada katalog kelas, menu “Kelas”, “Jadwal”, “Biaya”, dan “Bantuan” bisa lebih mudah dipahami daripada nama departemen. Halaman kelas menyertakan jadwal, lokasi, harga, dan cara mendaftar. Filter “Tanggal” dan “Lokasi” bekerja pada objek kelas yang sama; URL detail tetap stabil meski kartu ditampilkan di beberapa halaman.

## Keputusan dan pertukaran yang perlu dicatat

- Pilih kategori berdasarkan tugas dominan dan hasil uji; jangan memaksakan hierarki organisasi.
- Pertimbangkan halaman gabungan bila konten tipis dan tugas berdekatan; pisahkan bila audiens atau keputusan berbeda.
- Pencarian internal memerlukan relevansi, ejaan, privasi log kueri, dan perawatan indeks.

## Pemeriksaan hasil

- [ ] Tugas utama punya jalur yang bisa ditemukan tanpa menebak istilah internal.
- [ ] Heading dan navigasi mendukung orientasi serta dapat dipakai dengan keyboard.
- [ ] Halaman duplikat, kosong, dan konten tanpa pemilik teridentifikasi.
- [ ] URL lama memiliki rencana redirect saat perubahan.
- [ ] Struktur diuji dengan pengguna dan hasilnya dicatat.

## Serah terima untuk AI atau tim proyek

Masukan: inventaris konten dan tugas pengguna. Keluaran: peta situs, taksonomi, aturan label, daftar URL, alur menemukan informasi, dan temuan uji. AI IA boleh mengusulkan kelompok dan sinonim; hasil akhir diverifikasi lewat riset pengguna. Serahkan model konten ke penulis, desainer, backend, dan SEO.

## Sumber utama dan tingkat bukti

1. [NN/g — Card sorting](https://www.nngroup.com/articles/card-sorting-definition/) — metode riset dan batas interpretasinya
2. [W3C WAI — Menus](https://www.w3.org/WAI/tutorials/menus/) — contoh navigasi yang aksesibel
3. [GOV.UK — Content design](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/) — organisasi dan perencanaan konten

> **Cara membaca bukti:** spesifikasi/standar menentukan perilaku atau kriteria yang diuji; panduan resmi memberi praktik yang dianjurkan; penelitian pengguna memberi temuan kontekstual yang tetap harus diuji pada pengguna website ini. Pilihan alat dan ketentuan hukum harus diperiksa lagi saat implementasi.

## Pendalaman operasional untuk Website Builder

> Revisi integrasi 24 September 2026. Bagian ini menambah keputusan implementasi dan bukti penerimaan. Contoh merupakan rancangan, bukan hasil uji pengguna.

### Navigasi sebagai kontrak lintas keadaan

Buat peta setiap tugas dari halaman masuk yang mungkin, bukan hanya beranda. Pengunjung dapat datang langsung dari pencarian, tautan produk, atau halaman kesalahan. Setiap rute membutuhkan judul, orientasi, tindakan berikut, dan jalan kembali yang masuk akal. Pertahankan identitas sumber daya walau tampilan berubah.

Untuk katalog, definisikan hubungan antara URL, filter, sortir, dan pagination. Tentukan apakah tombol Back mengembalikan posisi serta filter; pastikan hasil kosong membedakan katalog kosong dari kombinasi filter yang terlalu sempit. Label aktif harus terbaca tanpa mengandalkan warna. Sediakan cara menghapus satu filter dan seluruh filter bila benar-benar diperlukan.

Pada situs kecil, navigasi biasa dengan tautan dan tombol buka/tutup sering lebih tepat daripada widget menu aplikasi. Jangan memberi `role="menu"` hanya karena elemen itu disebut menu secara visual; pola ARIA membawa kontrak keyboard tertentu. Pada layar kecil, uji buka, aktivasi tautan, Escape bila berupa dialog, dan pemulihan fokus sesuai pola yang dipilih.

**Contoh tugas:** pengguna masuk ke halaman produk yang sudah diarsipkan. Pertahankan penjelasan status dan arahkan ke alternatif yang relevan; jangan mengalihkannya tanpa penjelasan ke beranda sehingga konteks hilang.

**Bukti penerimaan:** telusuri minimal satu tugas dari beranda, deep link, dan Back/Forward; catat URL dan keadaan akhir. Tree test dapat menguji istilah, sedangkan uji browser membuktikan implementasinya.

Sumber: [WAI struktur halaman](https://www.w3.org/WAI/tutorials/page-structure/) dan [APG dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/). Pilih pola sesuai perilaku, bukan kemiripan tampilan.
