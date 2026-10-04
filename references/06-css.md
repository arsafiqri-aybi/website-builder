# CSS, Tata Letak, dan Desain Responsif

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

CSS mengendalikan penyajian konten HTML: warna, tipografi, ruang, tata letak, dan adaptasi perangkat. CSS bekerja melalui cascade, inheritance, selector, dan aturan kondisi. [W3C CSS Snapshot](https://www.w3.org/TR/css-2025/) memetakan modul standar, sedangkan [MDN CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) menyediakan rujukan praktis.

Sasaran CSS bukan meniru tangkapan layar pada satu perangkat, melainkan menjaga isi terbaca dan kontrol tetap berguna di berbagai lebar, zoom, preferensi, dan isi yang tidak terduga.

## Konsep yang perlu dikuasai

### Cascade dan specificity

Pelajari urutan sumber, origin, layer, specificity, dan inheritance untuk memahami konflik aturan. Susun gaya komponen agar perilakunya terprediksi. Pemakaian `!important` sebagai kebiasaan membuat pemeliharaan sulit dan sering menutupi masalah struktur.

### Box model dan overflow

Setiap elemen memiliki content, padding, border, margin, dan perilaku sizing. Uji teks panjang, URL tak terputus, dan media lebar agar tidak menyebabkan scroll horizontal yang tidak disengaja. Pilih `box-sizing` secara konsisten.

### Layout

Gunakan normal flow terlebih dahulu; flexbox untuk hubungan satu dimensi, grid untuk susunan dua dimensi, positioning bila konteks memerlukan. Hindari posisi absolut untuk komponen konten utama yang tingginya dinamis. Uji urutan visual dan DOM tetap masuk akal.

### Responsif dan container

Gunakan fluid sizing, `min()`, `max()`, `clamp()`, media query, dan bila cocok container query. Breakpoint ditentukan ketika isi rusak, bukan angka perangkat yang dianggap universal. Uji ponsel sempit, layar besar, mode lanskap, serta zoom tinggi.

### Tipografi dan unit

Pilih unit relatif yang memungkinkan perubahan ukuran teks dan gunakan unit viewport dengan hati-hati. `rem` untuk skala umum, `em` untuk hubungan lokal, serta ukuran absolut bila benar-benar diperlukan. `line-height` dan jarak paragraf ikut memengaruhi keterbacaan.

### Token dan tema

Simpan peran desain dalam custom properties, misalnya warna teks dan ruang komponen. Untuk mode gelap, uji kembali semua kombinasi kontras dan aset; menginversi warna secara otomatis tidak cukup. Dokumentasikan nilai default dan variasi komponen.

### Preferensi pengguna

Hormati `prefers-reduced-motion`, serta kondisi kontras atau mode warna yang relevan dan didukung. Hindari transisi gerak yang menghambat akses ke konten. Jangan menghapus outline fokus tanpa memberi pengganti yang jelas.

### Kinerja rendering

Kurangi CSS yang tidak terpakai dan gaya yang menyebabkan layout ulang besar saat interaksi. Animasi properti yang sesuai konteks dan pengurangan pekerjaan main thread lebih penting daripada trik micro-optimisasi. Ukur sebelum dan sesudah perubahan.

### Ketahanan

Pastikan layout bertahan saat font gagal, gambar tidak termuat, konten lebih panjang, dan bahasa berubah. Periksa `:focus-visible`, keadaan disabled, dan batas sentuh. UI harus berguna pada browser yang tidak mendukung efek dekoratif terbaru.

## Alur kerja pada proyek

1. Susun token dan gaya dasar semantik.
2. Bangun layout dari normal flow lalu tambahkan flex/grid seperlunya.
3. Uji data nyata, konten panjang, zoom, dan berbagai ukuran.
4. Implementasikan keadaan fokus, error, loading, dan reduced motion.
5. Periksa kontras dan urutan visual/DOM.
6. Ukur dampak perubahan besar pada render dan interaksi.

## Contoh penerapan

Kartu kelas menggunakan grid responsif yang berubah dari satu ke beberapa kolom ketika konten memberi ruang. Judul panjang tidak menimpa harga; tombol tetap terlihat saat teks diperbesar. Perubahan jadwal tidak memaksa tinggi tetap yang memotong isi.

## Keputusan dan pertukaran yang perlu dicatat

- Grid dapat mengatur daftar kartu; flex cocok untuk kelompok tombol kecil, bukan hukum mutlak.
- Desktop first atau mobile first adalah pendekatan organisasi aturan; pilih yang menjaga kompleksitas dan uji mudah.
- Efek visual berat harus dibenarkan oleh manfaat dan diukur pada perangkat lemah.

## Pemeriksaan hasil

- [ ] Tidak ada pemotongan informasi pada zoom dan layar sempit.
- [ ] Fokus keyboard terlihat di semua tema.
- [ ] Konten panjang, gambar gagal, dan font cadangan diuji.
- [ ] Preferensi gerak ditangani; kontras visual memenuhi kriteria target.
- [ ] CSS tidak mengubah makna atau urutan interaksi secara membingungkan.

## Serah terima untuk AI atau tim proyek

Masukan: desain UI, HTML semantik, aset. Keluaran: aturan CSS, token, perilaku responsif, dan tangkapan pengujian keadaan kritis. AI frontend harus menyebut browser dan kondisi yang diuji; reviewer membandingkan hasil visual dan pengalaman keyboard.

## Sumber utama dan tingkat bukti

1. [W3C — CSS Snapshot 2025](https://www.w3.org/TR/css-2025/) — peta modul spesifikasi CSS
2. [MDN — CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) — rujukan properti dan panduan
3. [W3C — WCAG 2.2](https://www.w3.org/TR/WCAG22/) — kriteria tampilan dan operabilitas

> **Cara membaca bukti:** spesifikasi/standar menentukan perilaku atau kriteria yang diuji; panduan resmi memberi praktik yang dianjurkan; penelitian pengguna memberi temuan kontekstual yang tetap harus diuji pada pengguna website ini. Pilihan alat dan ketentuan hukum harus diperiksa lagi saat implementasi.

## Pendalaman operasional untuk Website Builder

> Revisi integrasi 24 September 2026. Bagian ini menambah keputusan implementasi dan bukti penerimaan. Contoh merupakan rancangan, bukan hasil uji pengguna.

### Ketahanan CSS dan preferensi pengguna

Bangun token berdasarkan peran: `text`, `surface`, `border`, `focus`, `danger`; hindari menjadikan nama warna sebagai aturan bisnis. Evaluasi pasangan token dalam konteks final, termasuk lapisan transparansi. Tema gelap merupakan desain kedua yang perlu audit, bukan filter pembalik warna.

Gunakan layout yang menerima isi dinamis: `min-width: 0` bila item flex/grid perlu menyusut, pembungkusan teks yang sesuai, dan lebar maksimum membaca sebagai keputusan desain yang dapat diuji. Jangan memperbaiki overflow global dengan menyembunyikannya sebelum menemukan elemen penyebab; cara itu bisa menyembunyikan kontrol dan informasi.

Utamakan pengalaman tanpa gerak, lalu aktifkan animasi nonesensial bila preferensi dan konteks memungkinkan. Hindari aturan pengurangan gerak yang mengubah durasi menjadi sangat kecil tetapi meninggalkan logika bergantung pada event animasi. Pisahkan keadaan fungsi dari efek visual. Periksa perubahan preferensi saat halaman sudah terbuka.

**Matriks periksa:** viewport sempit, lebar, zoom; teks panjang; font cadangan; gambar gagal; keyboard; reduced motion; mode kontras paksa jika relevan. Rentang ukuran uji adalah sampel engineering, bukan bukti seluruh perangkat telah diuji.

**Contoh:** kartu dengan harga panjang tetap menampilkan CTA, judul membungkus, dan urutan fokus tidak berubah ketika grid menyusun ulang. Bila animasi mati, hasil aksi tetap muncul segera.

Sumber: [MDN prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion) dan [W3C Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html).
