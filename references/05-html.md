# HTML, Semantik, dan Formulir

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

HTML menyatakan struktur serta makna dokumen yang dibaca browser, mesin pencari, dan teknologi bantu. Elemen dipilih berdasarkan fungsinya, bukan rupa awalnya. Rujukan normatifnya adalah [HTML Living Standard](https://html.spec.whatwg.org/multipage/); [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML) memberi panduan penerapan.

HTML tetap perlu dipahami meski memakai framework, CMS, atau pembuat website visual. Kualitas semantik dan formulir tidak otomatis dijamin oleh alat.

## Konsep yang perlu dikuasai

### Kerangka dokumen

Gunakan doctype, `html lang="id"`, `head` berisi judul dan metadata yang sesuai, serta `body`. Judul tab unik membantu orientasi. Deklarasi bahasa membantu teknologi bantu dan pengolahan teks; lihat [W3C Internationalization](https://www.w3.org/International/questions/qa-html-language-declarations).

### Heading dan landmark

Susun `h1` sampai `h6` menurut hierarki isi, bukan ukuran font. Gunakan `header`, `nav`, `main`, `article`, `section`, dan `footer` sesuai peran. Heading dan landmark membantu navigasi halaman panjang; section tidak wajib dipakai untuk setiap pembungkus.

### Semantik konten

Pilih `p`, daftar, `figure`, `blockquote`, `time`, tabel data dengan header, dan tautan sesuai isi. Tabel digunakan untuk hubungan baris-kolom, bukan grid desain. Penanda makna memberi dasar yang lebih tangguh untuk CSS, pembaca layar, dan pengindeksan.

### Tautan dan tombol

`a href` membawa pengguna ke sumber/halaman; `button` menjalankan tindakan. Teks tautan harus menjelaskan tujuan di luar konteks visual. Pastikan tombol dalam form punya `type` yang benar agar tidak mengirim data tanpa sengaja.

### Gambar dan media

Alt menjelaskan fungsi gambar informatif dalam konteks, `alt=""` cocok untuk dekorasi; gambar yang menjadi tautan memerlukan nama tujuan. Sertakan caption atau transkrip/subtitel sesuai media. Dimensi intrinsik membantu mengurangi pergeseran layout.

### Formulir

Hubungkan setiap input dengan `label`, gunakan tipe dan `autocomplete` yang sesuai, kelompokkan radio/checkbox melalui `fieldset`/`legend`, dan beri instruksi sebelum pengguna kesulitan. Validasi native membantu pengalaman tetapi server tetap harus memvalidasi input. Pertahankan isi setelah error bila aman.

### Atribut dan keamanan

Jangan menyimpan rahasia dalam markup atau menganggap atribut `hidden` sebagai kontrol akses. Periksa URL pihak ketiga, unggahan, dan konten HTML dari pengguna agar tidak membuka injeksi. Gunakan `rel` pada tautan sesuai kebutuhan keamanan/kebijakan.

### Progressive enhancement

Buat konten dan tugas utama berfungsi secara wajar dengan HTML sebelum menambah JavaScript bila konteks memungkinkan. Fitur lanjutan boleh membutuhkan script, namun harus memberi status, kesalahan, serta jalur pemulihan yang jelas.

### Validasi dan inspeksi DOM

Periksa struktur aktual di browser, bukan hanya template sumber. Uji heading, nama aksesibel, urutan fokus, kontrol form, dan markup yang dihasilkan framework. Validator membantu menemukan kesalahan sintaks, tetapi tidak menggantikan evaluasi manual.

## Alur kerja pada proyek

1. Tulis struktur halaman dan heading berdasarkan isi nyata.
2. Pilih elemen semantik untuk navigasi, konten, tabel, dan tindakan.
3. Bangun formulir dengan label, bantuan, validasi, dan status.
4. Tambahkan gambar/media dengan alternatif yang sesuai fungsi.
5. Periksa DOM aktual, keyboard, dan pembaca layar pada alur penting.
6. Tinjau ulang setelah styling dan script terpasang.

## Contoh penerapan

Halaman detail kelas dapat memakai `main > article`, `h1` nama kelas, `time datetime` untuk jadwal, daftar rincian, dan `a` untuk kebijakan. Form pendaftaran memakai label “Alamat email”, `type="email"`, dan tombol submit yang jelas. Jika kelas penuh, informasi status tetap berupa teks yang dapat dibaca.

## Keputusan dan pertukaran yang perlu dicatat

- Jangan menambah ARIA untuk mengganti elemen native ketika elemen semantik sudah cocok.
- Heading visual dapat diubah CSS tanpa mengganti urutan semantik.
- `required` dan validasi browser meningkatkan UX tetapi bukan perlindungan server.

## Pemeriksaan hasil

- [ ] Setiap halaman punya judul yang menjelaskan isi dan bahasa dokumen.
- [ ] Heading/landmark sesuai hierarki; satu `main` konten utama.
- [ ] Tautan dan tombol punya nama serta fungsi yang tepat.
- [ ] Input punya label; error dapat dipahami dan terkait kontrol.
- [ ] Konten tetap terbaca ketika CSS atau gambar gagal.

## Serah terima untuk AI atau tim proyek

Masukan: struktur konten, komponen UI, alur. Keluaran: markup semantik, kontrak form, teks alternatif, dan catatan uji aksesibilitas. AI frontend menulis HTML; reviewer memeriksa DOM nyata, bukan hanya cuplikan komponen.

## Sumber utama dan tingkat bukti

1. [WHATWG — HTML Living Standard](https://html.spec.whatwg.org/multipage/) — spesifikasi normatif elemen dan formulir
2. [MDN — HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) — panduan implementasi
3. [W3C WAI — Forms](https://www.w3.org/WAI/tutorials/forms/) — panduan form aksesibel

> **Cara membaca bukti:** spesifikasi/standar menentukan perilaku atau kriteria yang diuji; panduan resmi memberi praktik yang dianjurkan; penelitian pengguna memberi temuan kontekstual yang tetap harus diuji pada pengguna website ini. Pilihan alat dan ketentuan hukum harus diperiksa lagi saat implementasi.

## Pendalaman operasional untuk Website Builder

> Revisi integrasi 24 September 2026. Bagian ini menambah keputusan implementasi dan bukti penerimaan. Contoh merupakan rancangan, bukan hasil uji pengguna.

### Semantik pada aplikasi interaktif

Selesaikan nama, peran, keadaan, dan hubungan sebelum menambah ARIA. Tombol ikon memerlukan nama aksesibel yang sesuai tindakan; ikon dekoratif di dalam tombol berlabel tidak perlu dibaca dua kali. Placeholder tidak menggantikan label. Gunakan teks biasa untuk informasi harga, syarat, bahan, atau kontak agar dapat diperbesar dan disalin.

Pada dialog modal, fokus berpindah ke tempat yang masuk akal saat dibuka; isi latar tidak dapat dioperasikan selama modal aktif; penutupan mengembalikan fokus ke pemicu atau tujuan alur yang logis. `<dialog>` membantu sebagian perilaku tetapi integrasi tetap harus diuji. Jangan membuat semua panel sebagai modal; dialog menambah beban navigasi.

Form yang gagal perlu menjaga masukan yang aman dipertahankan, menandai bidang yang salah, menghubungkan pesan melalui relasi programatis, serta menjelaskan apakah pengiriman terjadi. Pesan hasil proses dapat memakai live region yang sesuai; jangan mengumumkan setiap perubahan dekoratif. Tautan melewati navigasi berulang membantu mencapai konten utama.

**Kasus pembuktian:** buka form dengan keyboard, kirim nilai salah, perbaiki hanya bidang terkait, lalu selesaikan. Ulangi dengan pembaca layar bila alat tersedia. Periksa HTML hasil render karena framework dapat membuat elemen bersarang atau ID ganda yang tidak tampak pada desain.

Rujukan: [HTML Living Standard](https://html.spec.whatwg.org/multipage/), [WAI APG modal dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/), dan [WAI Forms](https://www.w3.org/WAI/tutorials/forms/).
