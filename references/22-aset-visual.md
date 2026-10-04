# Desain Visual, Gambar, Ikon, dan Aset Media

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

Aset visual membantu menjelaskan isi, memberi identitas, dan mendukung orientasi. Prosesnya mencakup pemilihan media, komposisi, ukuran, format, versi, hak pakai, alternatif tekstual, dan kinerja. [web.dev Learn Images](https://web.dev/learn/images) menjelaskan gambar responsif dan pemuatan; [W3C WAI Images](https://www.w3.org/WAI/tutorials/images/) membedakan alt untuk gambar informatif, fungsional, dan dekoratif.

Gambar yang indah tidak otomatis membantu tugas. Gunakan aset ketika membawa informasi, konteks, atau identitas yang diperlukan; sediakan makna setara untuk pengguna yang tidak melihatnya.

## Konsep yang perlu dikuasai

### Fungsi aset

Kategorikan sebagai informatif, fungsional, dekoratif, atau kompleks. Foto lokasi dapat membantu orang mengenali tempat, ikon aksi perlu label, sedangkan ornamen tidak perlu deskripsi berulang. Infografik kompleks membutuhkan penjelasan data atau tabel pendamping.

### Format dan resolusi

Pilih SVG untuk vektor yang sesuai, format raster modern untuk foto/ilustrasi bila didukung, serta fallback saat diperlukan. Sediakan ukuran sesuai tampilan dan kerapatan layar; file sumber besar tidak harus dikirim ke semua ponsel. Uji kualitas setelah kompresi.

### Gambar responsif

Gunakan `srcset`/`sizes` atau mekanisme setara ketika browser perlu memilih ukuran; tetapkan width/height atau rasio untuk mencegah pergeseran layout. Crop yang berbeda dapat dipilih melalui `picture` bila komposisi menuntut. Jangan memotong informasi penting pada layar sempit.

### Prioritas pemuatan

Aset utama di area awal perlu ditemukan cepat; aset jauh di bawah halaman dapat dimuat kemudian. Lazy loading pada gambar utama bisa memperburuk LCP. Optimasi ditentukan oleh waterfall dan konteks, bukan satu aturan untuk semua gambar.

### Ikon dan sistem visual

Buat ukuran, ketebalan garis, warna, serta makna ikon konsisten. Ikon abstrak jangan menjadi satu-satunya penjelasan tindakan penting; label teks meningkatkan pemahaman. Keadaan aktif dan kesalahan tidak hanya dibedakan oleh warna.

### Video dan audio

Pilih durasi/format sesuai tugas, beri kontrol pemutaran, subtitle/transkrip bila dibutuhkan, dan hindari autoplay yang mengganggu. Siapkan poster serta pilihan kualitas agar data pengguna tidak terbuang. Informasi inti jangan hanya ada di video bila bentuk teks lebih mudah dicari.

### Lisensi dan asal

Catat pencipta, sumber, lisensi, perubahan yang diizinkan, kredit yang diwajibkan, serta hak orang yang tergambar. Aset hasil AI pun perlu ditinjau untuk kesesuaian, akurasi, dan syarat penggunaan. Jangan mengambil gambar acak dari pencarian lalu menganggapnya bebas pakai.

### Alur produksi

Simpan master, ekspor web, nama yang dapat dilacak, alt, dan pemilik aset. Buat varian tema bila perlu, periksa kualitas di berbagai perangkat. Ketika foto diperbarui, pastikan cache dan halaman lama diperbarui juga.

### Keamanan file

Unggahan pengguna dan SVG pihak ketiga dapat memuat risiko jika diperlakukan sebagai kode atau HTML; validasi tipe dan cara penyajian. Jangan memasukkan metadata lokasi sensitif tanpa tujuan. Terapkan batas ukuran dan hak akses penyimpanan.

## Alur kerja pada proyek

1. Tentukan fungsi setiap aset pada halaman.
2. Pastikan hak pakai, akurasi, dan kualitas visual.
3. Pilih format, ukuran, crop, dan alternatif tekstual.
4. Implementasikan pemuatan serta dimensi yang tepat.
5. Uji pada layar kecil, zoom, jaringan lemah, dan teknologi bantu.
6. Dokumentasikan sumber, pemilik, serta masa tinjau.

## Contoh penerapan

Foto ruang kelas membantu peserta mengenali lokasi, sehingga alt singkat menyebut ciri lokasi yang relevan. Ikon kalender pada tombol tetap didampingi teks “Lihat jadwal”. Foto hero memakai sumber ukuran responsif dan dimensi tetap; gambar kelas lain yang berada jauh di bawah halaman dapat dimuat kemudian.

## Keputusan dan pertukaran yang perlu dicatat

- Aset bermerek unik memberi identitas, tetapi stock photo tanpa fungsi sering menambah beban dan menurunkan kejelasan.
- SVG tidak otomatis aman atau aksesibel; cara memasukkan, judul, dan asal file harus diperiksa.
- Alt menggambarkan fungsi dalam konteks halaman, bukan daftar setiap detail gambar.

## Pemeriksaan hasil

- [ ] Setiap aset punya tujuan dan status hak pakai.
- [ ] Alternatif tekstual sesuai peran dan konteks.
- [ ] Ukuran, crop, serta rasio diuji pada layar sasaran.
- [ ] Media tidak menghambat tugas atau memaksa pemutaran.
- [ ] Aset pihak ketiga/unggahan melewati kontrol keamanan.

## Serah terima untuk AI atau tim proyek

Masukan: konten, rancangan UI, identitas merek. Keluaran: pustaka aset dengan sumber/lisensi, varian web, alt, serta panduan penggunaan. AI visual dapat mengusulkan/membuat aset; editor fakta menilai kebenaran; reviewer aksesibilitas dan hukum memeriksa penggunaan.

## Sumber utama dan tingkat bukti

1. [web.dev — Learn Images](https://web.dev/learn/images) — format, responsif, dan pemuatan
2. [W3C WAI — Images Tutorial](https://www.w3.org/WAI/tutorials/images/) — alt menurut peran gambar
3. [MDN — Performance](https://developer.mozilla.org/en-US/docs/Web/Performance) — dampak sumber media

> **Cara membaca bukti:** spesifikasi/standar menentukan perilaku atau kriteria yang diuji; panduan resmi memberi praktik yang dianjurkan; penelitian pengguna memberi temuan kontekstual yang tetap harus diuji pada pengguna website ini. Pilihan alat dan ketentuan hukum harus diperiksa lagi saat implementasi.

## Pendalaman operasional untuk Website Builder

> Revisi integrasi 24 September 2026. Bagian ini menambah keputusan implementasi dan bukti penerimaan. Contoh merupakan rancangan, bukan hasil uji pengguna.

### Aset yang khas sekaligus jujur

Tentukan fungsi setiap aset sebelum mencarinya: membuktikan produk, menunjukkan lokasi, menerangkan mekanisme, membangun identitas, atau dekorasi. Foto produk nyata lebih kuat untuk menyatakan bentuk dan kondisi barang; ilustrasi AI dapat membantu suasana tetapi tidak boleh menyamar sebagai bukti fasilitas, hasil pelanggan, atau sertifikasi.

Susun register aset berisi sumber, hak pakai, tanggal, pemilik, alt, crop, dimensi, dan status representasi. Catat bila gambar merupakan ilustrasi. Untuk diagram dan grafik yang harus tepat, gunakan data serta elemen yang terkontrol; jangan menyerahkan teks angka penting kepada gambar generatif.

Optimasi setelah komposisi diputuskan: varian ukuran, crop art direction, kompresi, dimensi intrinsik, dan prioritas pemuatan. Periksa bahwa crop ponsel tidak menghilangkan bagian produk yang menjelaskan ukuran atau fungsi. Alt menyampaikan fungsi kontekstual; dekorasi tidak perlu narasi yang menambah kebisingan pembaca layar.

**Uji dua kanal:** matikan gambar lalu periksa apakah keputusan penting masih dapat dibuat; matikan audio lalu periksa apakah video tetap menyampaikan informasi yang setara. Periksa lisensi font dan fallback saat font tidak tersedia.

Sumber: [web.dev Learn Images](https://web.dev/learn/images) dan [WAI alt decision tree](https://www.w3.org/WAI/tutorials/images/decision-tree/). Kesan material, rasa, atau aroma dari foto adalah representasi dan perlu cocok dengan produk nyata.
