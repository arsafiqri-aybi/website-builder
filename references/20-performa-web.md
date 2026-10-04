# Performa Web dan Pengukuran Pengalaman

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

Performa web menilai seberapa cepat konten berguna muncul, interaksi direspons, dan tata letak tetap stabil. [web.dev Web Vitals](https://web.dev/articles/vitals) menjelaskan LCP, INP, dan CLS sebagai Core Web Vitals; ukur di lapangan dan laboratorium karena keduanya menjawab pertanyaan berbeda. Target metrik dan ambangnya dapat berubah, sehingga verifikasi ulang sebelum menetapkannya dalam kontrak.

Kecepatan juga memengaruhi biaya data, baterai, dan akses pada jaringan lemah. Optimasi yang benar dipilih berdasarkan bottleneck halaman dan pengguna, bukan mengejar satu nilai alat penguji.

## Konsep yang perlu dikuasai

### Anggaran dan sasaran

Tentukan halaman serta perangkat penting, budget ukuran dan pekerjaan script, serta indikator pengalaman. Tetapkan baseline dan periksa distribusi pengguna, bukan hanya rata-rata; keadaan terburuk yang bermakna dapat tersembunyi di angka agregat.

### Jalur pemuatan

Browser mencari DNS, membangun koneksi, mengambil HTML, lalu sumber CSS/JS/gambar. Ketahui resource yang menghalangi render dan prioritas konten terlihat. Pengukuran waterfall membantu mengidentifikasi hambatan jaringan versus main thread.

### LCP

Elemen konten terbesar yang terlihat menjadi sinyal loading; perbaiki respons server, temukan resource utama lebih awal, kompres gambar tepat, dan hindari render yang menunda elemen tersebut. Jangan mengoptimalkan logo kecil saat gambar utama yang menjadi LCP.

### INP

Responsivitas mencakup penundaan input, eksekusi handler, dan render berikutnya. Kurangi tugas JavaScript panjang dan pekerjaan yang tidak diperlukan; periksa interaksi seperti menu, filter, dan submit. [web.dev INP](https://web.dev/articles/inp) membahas cara menafsirkan metrik.

### CLS

Pergeseran layout tak terduga sering muncul saat gambar tanpa dimensi, iklan, font, atau konten disisipkan. Sediakan ruang yang tepat dan hindari memasukkan elemen di atas konten saat pengguna sedang membaca. Pengukuran lapangan perlu memeriksa penyebab spesifik.

### Aset dan bundel

Sajikan gambar responsif dengan dimensi serta format cocok, batasi font dan variasi, pecah JavaScript nonkritis, serta kurangi CSS tak terpakai. Kompresi tidak boleh mengorbankan keterbacaan atau kualitas informasi penting.

### Cache dan distribusi

Aset berversi dapat di-cache lebih lama, sedangkan HTML dan data pribadi memakai kebijakan berbeda. CDN bisa mengurangi jarak jaringan untuk aset publik. [RFC 9111](https://www.rfc-editor.org/info/rfc9111/) menjadi dasar perilaku cache; audit efek konten usang dan privasi.

### Backend dan database

Time to first byte dipengaruhi query, antrean, layanan luar, dan cache server. Profilkan endpoint lambat, perbaiki query berbiaya tinggi, dan tetapkan timeout. Optimasi frontend tidak dapat menutup permintaan server yang macet.

### RUM dan lab

Lab memberi kondisi berulang untuk membandingkan perubahan; real-user monitoring menunjukkan pengalaman perangkat/jaringan sesungguhnya. Ukur secara agregat dengan privasi dan sampel yang jelas. Korelasikan perbaikan angka dengan keberhasilan tugas.

## Alur kerja pada proyek

1. Tentukan halaman, audiens, dan baseline.
2. Rekam waterfall, LCP, INP, CLS, ukuran aset, dan latensi server.
3. Identifikasi sumber hambatan yang terukur.
4. Perbaiki satu kelompok penyebab dan bandingkan sebelum/sesudah.
5. Periksa regresi pada perangkat lambat serta koneksi terbatas.
6. Pasang anggaran kinerja dan pantau distribusi setelah rilis.

## Contoh penerapan

Halaman kelas menampilkan banner besar. Pengukuran menunjukkan gambar banner terlambat ditemukan sehingga LCP lambat; gambar diberi ukuran responsif dan prioritas sesuai kebutuhan. Filter tanggal memicu script berat sehingga INP buruk; logika dipecah dan DOM yang diperbarui dibatasi. Tim menguji lagi pada ponsel sasaran.

## Keputusan dan pertukaran yang perlu dicatat

- Lazy loading gambar di bawah lipatan membantu, tetapi gambar utama yang terlihat segera tidak boleh ditunda secara keliru.
- Satu skor sintetis tidak menggambarkan semua pengguna atau interaksi.
- Kecepatan tidak boleh dicapai dengan menghapus teks alternatif atau menyembunyikan konten penting.

## Pemeriksaan hasil

- [ ] Metrik awal dan sesudah perubahan tercatat.
- [ ] LCP, INP, CLS ditelusuri sampai penyebab halaman.
- [ ] Aset besar dan cache memiliki aturan.
- [ ] Alur utama tetap berfungsi pada jaringan/perangkat lambat.
- [ ] Data lapangan ditafsirkan dengan sampel dan privasi.

## Serah terima untuk AI atau tim proyek

Masukan: halaman, traffic, dan anggaran. Keluaran: laporan waterfall, metrik lapangan/lab, daftar bottleneck, perubahan, dan hasil uji ulang. AI performa menganalisis profil; frontend/backend memperbaiki penyebab; reviewer UX memeriksa manfaat nyata.

## Sumber utama dan tingkat bukti

1. [web.dev — Web Vitals](https://web.dev/articles/vitals) — definisi metrik dan pengukuran
2. [web.dev — INP](https://web.dev/articles/inp) — responsivitas interaksi
3. [MDN — Performance](https://developer.mozilla.org/en-US/docs/Web/Performance) — panduan performa web
4. [IETF — RFC 9111](https://www.rfc-editor.org/info/rfc9111/) — semantik cache

> **Cara membaca bukti:** spesifikasi/standar menentukan perilaku atau kriteria yang diuji; panduan resmi memberi praktik yang dianjurkan; penelitian pengguna memberi temuan kontekstual yang tetap harus diuji pada pengguna website ini. Pilihan alat dan ketentuan hukum harus diperiksa lagi saat implementasi.

## Pendalaman operasional untuk Website Builder

> Revisi integrasi 24 September 2026. Bagian ini menambah keputusan implementasi dan bukti penerimaan. Contoh merupakan rancangan, bukan hasil uji pengguna.

### Ambang, budget, dan bukti ukur

Pada pemeriksaan sumber 24 September 2026, ambang kategori baik Core Web Vitals adalah LCP ≤2,5 detik, INP ≤200 ms, CLS ≤0,1, dinilai pada persentil ke-75 pengalaman lapangan dan dipisah menurut mobile/desktop. Ketiganya harus memenuhi target. Sumber: [Web Vitals](https://web.dev/articles/vitals). Ini ambang metrik pengalaman, bukan bukti seluruh produk berkualitas.

Lab berguna untuk diagnosis dan perbandingan terkontrol; ia tidak boleh dilaporkan sebagai data pengguna nyata. Halaman baru mungkin belum memiliki data lapangan. Tulis kondisi alat, perangkat, koneksi, build, URL, jumlah pengamatan, dan tanggal. Satu angka Lighthouse tidak membuktikan INP lapangan atau keberhasilan semua interaksi.

Pisahkan budget pengiriman dari budget pengalaman. Ukuran JS, foto, font, dan jumlah request adalah batas engineering yang ditentukan proyek; jangan menyebut satu angka KB sebagai standar universal. Cari sumber dominan dari waterfall dan profil interaksi sebelum memotong aset.

**Contoh keputusan:** video hero dapat memperkaya identitas tetapi menghabiskan data serta menggeser konten. Bandingkan poster statis dengan putar opsional; periksa LCP, CLS, akses ke CTA, serta pemahaman informasi. Jangan lazy-load sumber LCP yang perlu muncul segera tanpa bukti manfaat.

**Bukti selesai:** dokumentasikan baseline, perubahan penyebab, pengukuran sesudah, dan batas data lapangan. Pertahankan aksesibilitas serta kebenaran informasi saat optimasi.
