# Penulisan Konten, Mikrocopy, dan Tata Kelola Isi

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

Konten adalah bagian dari fungsi website: judul, instruksi, harga, kebijakan, tombol, pesan kesalahan, dan bantuan menentukan apakah pengguna memahami langkah selanjutnya. [GOV.UK content guidance](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/) menekankan kebutuhan pengguna, perencanaan, organisasi, serta bahasa yang jelas.

Menulis untuk web melibatkan penelitian, penyuntingan, struktur, pengujian, dan perawatan. Teks yang estetis tetapi ambigu dapat menyebabkan kesalahan pendaftaran, pembayaran, atau pemahaman hak.

## Konsep yang perlu dikuasai

### Tujuan dan audiens

Untuk setiap halaman, tentukan keputusan atau tugas yang harus didukung. Jawab pertanyaan pengguna sebelum narasi promosi yang panjang. Istilah teknis dijelaskan ketika diperlukan; pemula dan ahli bisa memerlukan detail bertingkat.

### Hierarki dan pemindaian

Gunakan judul yang menyatakan isi, paragraf satu gagasan, daftar bila tepat, serta informasi penting di tempat yang dicari. Jangan menyembunyikan biaya, syarat, atau batasan dalam catatan kecil. Struktur HTML harus mencerminkan struktur konten.

### Bahasa tindakan

Label tombol menyebut hasil seperti “Daftar kelas”, bukan “Kirim” bila konteks kurang jelas. Tautan harus dapat dipahami di luar kalimat. Hindari klaim yang tidak dapat dibuktikan atau urgensi palsu.

### Mikrocopy dan status

Tulis teks untuk kosong, loading, berhasil, gagal, tidak punya izin, dan kedaluwarsa. Pesan error menerangkan apa yang salah, cara memperbaiki, dan apakah data tersimpan. Perjelas konsekuensi sebelum tindakan yang sulit dibatalkan.

### Keakuratan dan sumber

Informasi harga, tanggal, lokasi, kebijakan, dan persyaratan harus punya sumber dan pemilik. Cantumkan tanggal pembaruan bila membantu keputusan. Proses persetujuan konten penting untuk klaim legal, kesehatan, atau finansial.

### Inklusivitas dan bahasa

Gunakan istilah yang menghormati audiens, format tanggal/mata uang sesuai locale, dan instruksi yang tidak mengandalkan warna atau posisi. Setel `lang` dan tandai bagian berbahasa lain jika relevan. Uji teks pada berbagai tingkat literasi dan perangkat.

### SEO alami

Pakai istilah pencarian yang memang dipakai pengguna pada judul serta isi, tanpa mengulang kata kunci secara mekanis. Konten unik dan bermanfaat memudahkan pemahaman pengguna serta pengindeksan; [Google Search Essentials](https://developers.google.com/search/docs/essentials) memberi panduan resmi.

### Model dan alur persetujuan

CMS memerlukan bidang yang jelas: judul, ringkasan, isi, tanggal berlaku, pemilik, status publikasi. Pisahkan draft dan terbit, atur preview dan revisi. Desain konten tidak berhenti pada halaman awal peluncuran.

### Pengukuran dan revisi

Analisis pertanyaan dukungan, pencarian tanpa hasil, serta uji pemahaman. Ubah satu masalah konten lalu periksa apakah tugas lebih mudah selesai. Angka keterlibatan tinggi tidak selalu berarti isi jelas; bisa jadi pengguna berulang karena bingung.

## Alur kerja pada proyek

1. Daftarkan pertanyaan dan tugas yang harus dijawab halaman.
2. Tulis struktur, fakta, dan tindakan dengan bahasa pengguna.
3. Siapkan teks untuk semua keadaan dan batasan penting.
4. Tinjau akurasi, legalitas, aksesibilitas, serta konsistensi istilah.
5. Uji pemahaman dengan pengguna dan revisi.
6. Tetapkan pemilik serta jadwal tinjau isi.

## Contoh penerapan

Halaman kelas menjawab “kapan, di mana, berapa biaya, siapa yang cocok, apa yang terjadi setelah mendaftar”. Jika pendaftaran gagal karena kelas penuh, pesan menyebut keadaan baru dan tautan ke jadwal lain. Admin memiliki bidang tanggal berlaku agar jadwal lama tidak tampak sebagai pilihan baru.

## Keputusan dan pertukaran yang perlu dicatat

- Konten singkat berguna bila lengkap untuk keputusan; ringkas tidak boleh berarti menyembunyikan syarat.
- Satu istilah untuk satu konsep membantu konsistensi, kecuali pengguna memerlukan sinonim dalam pencarian.
- Bahasa merek tetap harus jelas dan tidak mengaburkan konsekuensi transaksi.

## Pemeriksaan hasil

- [ ] Halaman menjawab pertanyaan pengguna utama.
- [ ] Tombol, tautan, dan pesan error dapat dipahami tanpa tebakan.
- [ ] Fakta kritis punya pemilik dan sumber.
- [ ] Teks tetap masuk pada layar sempit/zoom tinggi.
- [ ] Ada tanggal dan proses peninjauan konten.

## Serah terima untuk AI atau tim proyek

Masukan: kebutuhan pengguna dan fakta yang telah diverifikasi. Keluaran: model konten, teks antarmuka, pedoman istilah, pesan keadaan, serta kalender tinjau. AI penulis membuat draft; pemilik fakta mengecek akurasi; desainer dan reviewer aksesibilitas menguji konteksnya.

## Sumber utama dan tingkat bukti

1. [GOV.UK — Content design](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/) — panduan organisasi dan bahasa konten
2. [W3C WAI — Page structure](https://www.w3.org/WAI/tutorials/page-structure/) — struktur konten aksesibel
3. [Google Search Essentials](https://developers.google.com/search/docs/essentials) — praktik isi yang mudah ditemukan

> **Cara membaca bukti:** spesifikasi/standar menentukan perilaku atau kriteria yang diuji; panduan resmi memberi praktik yang dianjurkan; penelitian pengguna memberi temuan kontekstual yang tetap harus diuji pada pengguna website ini. Pilihan alat dan ketentuan hukum harus diperiksa lagi saat implementasi.

## Pendalaman operasional untuk Website Builder

> Revisi integrasi 24 September 2026. Bagian ini menambah keputusan implementasi dan bukti penerimaan. Contoh merupakan rancangan, bukan hasil uji pengguna.

### Konten sebagai data yang dapat dipercaya

Untuk setiap klaim penting, simpan asal, pemilik, tanggal berlaku, dan status verifikasi. Harga, bahan, alergen, alamat, testimoni, sertifikat, serta angka dampak tidak boleh diciptakan untuk mengisi desain. Gunakan contoh berlabel pada prototipe; sebelum publikasi, ganti atau hilangkan klaim yang belum didukung.

Tulis paket keadaan: default, kosong, loading, berhasil, gagal, izin ditolak, sesi habis, dan hasil belum pasti. Pesan “pesanan tersimpan; email belum terkirim” lebih berguna daripada galat umum bila itu benar. Hindari pesan sukses sebelum status otoritatif diketahui. Pertahankan istilah sama pada UI, email, dan dukungan.

Untuk produk sensori, pisahkan atribut faktual dari bahasa pengalaman. “Bahan: kayu jati” memerlukan sumber; “kesan hangat” merupakan arah desain; “tekstur renyah” sebaiknya berdasarkan produk nyata. Jangan menganggap foto atau kata tertentu memberi aroma fisik melalui layar.

**Uji pemahaman:** minta pengguna menjelaskan apa yang akan terjadi setelah menekan CTA dan informasi apa yang mendasari pilihannya. Uji teks di ponsel, saat zoom, dan dalam bahasa sasaran. Bahasa merek boleh khas selama konsekuensi tindakan tetap jelas.

Sumber: [W3C COGA](https://www.w3.org/TR/coga-usable/) dan [W3C language declarations](https://www.w3.org/International/questions/qa-html-language-declarations). COGA adalah panduan tambahan, bukan seluruh kriteria WCAG.
