# Dasar Pemrograman, Algoritma, dan Logika

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

Logika pemrograman membantu mengubah kebutuhan menjadi aturan yang dapat dijalankan dan diuji. Ini mencakup tipe data, percabangan, perulangan, fungsi, struktur data, pemecahan masalah, dan penanganan kegagalan. [MDN JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide) dapat menjadi media belajar karena bahasa yang sama dipakai di browser; konsepnya berlaku lebih luas.

Penguasaan dasar lebih bernilai daripada menghafal sintaks satu framework. Ilmu ini dipakai oleh frontend, backend, pengujian, otomasi, dan analisis data.

## Konsep yang perlu dikuasai

### Variabel dan tipe

Kenali nilai teks, angka, boolean, tanggal, daftar, objek, serta nilai kosong. Pilih representasi yang sesuai: uang sebaiknya tidak diolah sembarangan dengan floating point, waktu perlu zona, dan status harus dibatasi ke nilai yang sah. Validasi saat data masuk dari luar.

### Percabangan dan aturan

Tulis aturan sebagai kondisi yang mudah dibaca. Pisahkan keputusan bisnis dari tampilan agar satu aturan tidak berbeda antarhalaman. Untuk setiap cabang, cari kasus batas, input tidak valid, dan kemungkinan kondisi bertentangan.

### Perulangan dan koleksi

Gunakan iterasi untuk mengolah daftar; pahami filter, map, reduce, pengurutan, dan kompleksitas dasar. Pada data besar, pertimbangkan apakah proses dilakukan di browser, server, atau database. Jangan mengambil seluruh data jika hanya halaman pertama yang diperlukan.

### Fungsi dan modularitas

Fungsi memiliki tujuan, input, output, dan efek samping yang jelas. Fungsi murni mudah diuji; operasi yang menulis DB atau mengirim email sebaiknya tampak jelas dalam antarmuka kode. Nama yang menyatakan maksud mengurangi salah tafsir.

### Struktur data

Array sesuai urutan, map untuk akses kunci, set untuk keunikan, objek untuk atribut bernama; DB untuk penyimpanan jangka panjang. Pilih bentuk berdasarkan operasi dominan dan invariannya. Skema data memengaruhi kemudahan perubahan.

### Kompleksitas dan biaya

Big O membantu mengenali pertumbuhan kerja, namun ukur kasus nyata. Query DB, jaringan, dan parsing file sering lebih mahal daripada operasi kecil pada array. Optimasi dimulai dari bottleneck terukur.

### Error dan batas

Bedakan kesalahan yang bisa diperbaiki pengguna, kegagalan sementara, dan bug internal. Pesan untuk pengguna menerangkan langkah berikutnya, sedangkan log teknis aman membantu diagnosis. Jangan menelan exception tanpa catatan atau status yang jelas.

### Debugging dan penalaran

Reproduksi masalah, perkecil contoh, periksa asumsi, lalu uji hipotesis satu per satu. Logging sementara, debugger, dan tes regresi memperjelas sebab. Hindari memperbaiki gejala pada UI ketika aturan server salah.

### Kontrak dan invarian

Nyatakan hal yang harus selalu benar, misalnya kuota tidak negatif dan tanggal selesai sesudah tanggal mulai. Tempatkan pemeriksaan di batas yang dapat dipercaya dan tambah constraint DB jika sesuai. Tes berharga ketika memastikan aturan dari beberapa jalur tetap sama.

## Alur kerja pada proyek

1. Terjemahkan kebutuhan menjadi input, proses, output, dan kegagalan.
2. Tulis contoh kasus normal serta batas sebelum implementasi.
3. Pecah logika menjadi fungsi kecil dengan kontrak jelas.
4. Pilih struktur data berdasarkan operasi dan skala.
5. Jalankan contoh, debug asumsi, dan buat tes untuk aturan berisiko.
6. Tinjau keterbacaan serta biaya saat volume bertambah.

## Contoh penerapan

Aturan diskon kelas: harga akhir tidak boleh negatif, diskon berlaku hanya pada periode tertentu, dan kupon yang sama tidak boleh dipakai dua kali jika kebijakannya begitu. Tulis fungsi perhitungan terpisah dari tombol UI, uji batas tanggal dan angka, lalu lakukan validasi ulang di server sebelum transaksi disimpan.

## Keputusan dan pertukaran yang perlu dicatat

- Kode tersingkat bukan selalu kode yang paling mudah ditinjau.
- Abstraksi dibuat ketika duplikasi benar-benar mencerminkan aturan yang sama.
- Tipe statis membantu sebagian kelas kesalahan, tetapi tidak mengganti validasi data runtime.

## Pemeriksaan hasil

- [ ] Kasus batas dan nilai kosong ditangani.
- [ ] Aturan bisnis punya satu sumber kebenaran di lapisan tepercaya.
- [ ] Efek samping dan kesalahan terlihat jelas.
- [ ] Kode dapat dijelaskan lewat input/output dan invariant.
- [ ] Performa diukur jika menjadi masalah.

## Serah terima untuk AI atau tim proyek

Masukan: aturan kebutuhan. Keluaran: pseudocode, fungsi, kasus batas, uji, dan catatan asumsi. AI pengembang menjelaskan contoh kontra; reviewer memeriksa logika dengan data nyata dan mengecek apakah aturan yang sama ada di server serta database.

## Sumber utama dan tingkat bukti

1. [MDN — JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide) — dasar bahasa dan kontrol alur
2. [MDN — Learn web development](https://developer.mozilla.org/en-US/docs/Learn_web_development) — kurikulum penerapan dasar di web

> **Cara membaca bukti:** spesifikasi/standar menentukan perilaku atau kriteria yang diuji; panduan resmi memberi praktik yang dianjurkan; penelitian pengguna memberi temuan kontekstual yang tetap harus diuji pada pengguna website ini. Pilihan alat dan ketentuan hukum harus diperiksa lagi saat implementasi.

## Pendalaman operasional untuk Website Builder

> Revisi integrasi 24 September 2026. Bagian ini menambah keputusan implementasi dan bukti penerimaan. Contoh merupakan rancangan, bukan hasil uji pengguna.

### Representasi data menentukan keandalan

Modelkan keadaan yang sah secara eksplisit. Contoh status pesanan: draft, diajukan, menunggu pembayaran, dibayar, dibatalkan; daftar transisi mengikuti bisnis. Hindari campuran boolean yang membuka keadaan mustahil. Untuk TypeScript, discriminated union dapat membantu pemilihan cabang dan pemeriksaan kelengkapan, tetapi input JSON tetap perlu validasi runtime.

Pisahkan logika domain dari efek jaringan dan tampilan. Fungsi harga menerima data yang terverifikasi, menghasilkan nilai presisi, dan tidak sekaligus mengubah DOM atau mengirim transaksi. Keputusan bisnis di browser disalin untuk bantuan UX hanya bila server tetap sumber kebenaran.

**Telusuri contoh kontra:** nilai kosong, nol, negatif, jumlah besar, pembulatan, Unicode, tanggal berubah zona, dan respons yang datang terbalik. Pilih kasus yang sesuai domain, bukan daftar ritual pada perubahan kosmetik. Bug yang telah ditemukan menjadi kandidat tes regresi karena mempunyai dampak nyata.

Tipe statis, lint, dan format menjawab kelas masalah berbeda. Lulus compiler tidak membuktikan harga benar, akses sah, atau formulir mudah digunakan. Jika AI menyatakan aturan benar, minta contoh input-output dan telusuri invariant pada batas tepercaya.

Sumber: [TypeScript Narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html). Teknik ini opsional sesuai bahasa proyek; kontrak dan contoh kontra berlaku lebih luas.
