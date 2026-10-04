# JavaScript dan Interaksi Browser

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

JavaScript menambahkan logika, perubahan DOM, akses Web API, dan interaksi asinkron pada halaman. Ia bekerja bersama HTML/CSS serta batas keamanan browser. [MDN JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide) membahas bahasa, sementara dokumentasi [Web APIs MDN](https://developer.mozilla.org/en-US/docs/Web/API) membahas kemampuan browser.

Tidak semua halaman butuh banyak JavaScript. Pemakaian script harus sepadan dengan kebutuhan interaksi, biaya unduhan, eksekusi, kompleksitas, dan kemungkinan gagal.

## Konsep yang perlu dikuasai

### Fondasi bahasa

Pahami variabel, tipe, scope, fungsi, closure, modul, array/objek, dan penanganan exception. Perhatikan perbedaan `null`, `undefined`, dan nilai falsy agar validasi tidak salah. Pecah fungsi berdasarkan tanggung jawab dan kontrak input/output.

### DOM dan event

Gunakan listener untuk tindakan pengguna; bedakan event bubbling dan perilaku default. Ubah elemen secara aman dan hindari injeksi melalui HTML mentah. Jaga hubungan dengan semantik asli agar keyboard dan pembaca layar tetap mendapat keadaan yang benar.

### State dan alur asinkron

Modelkan keadaan idle, loading, success, empty, dan error. `Promise`, `async/await`, serta pembatalan permintaan membantu menangani respons yang datang terlambat. Hindari race condition saat filter atau pencarian cepat mengganti kueri.

### Fetch dan data

Pahami request, response, status HTTP, parsing JSON, kesalahan jaringan, timeout aplikasi, dan penanganan data tak tepercaya. `fetch` yang berhasil selesai tidak otomatis berarti respons HTTP sukses; periksa `response.ok` sesuai kebutuhan.

### Validasi dan batas kepercayaan

Validasi sisi klien memberi umpan balik cepat, sedangkan server tetap penentu validitas dan otorisasi. Jangan menaruh kunci rahasia atau keputusan hak akses hanya dalam bundel klien. Escape/sanitasi mengikuti konteks output.

### Komponen dan framework

Framework membantu pengelolaan state serta komposisi UI, tetapi komponen harus tetap menghasilkan HTML yang benar. Pelajari lifecycle, event, rendering, hydration bila digunakan, dan aturan serialisasi data. Hindari menambah abstraksi sebelum kebutuhan nyata.

### Performa interaksi

Perhatikan pekerjaan main thread, ukuran bundel, event handler yang berat, serta pengiriman JavaScript yang tidak dibutuhkan. Tunda kode nonkritis, pecah tugas berat, dan uji pada perangkat nyata. [INP](https://web.dev/articles/inp) mengukur responsivitas interaksi di lapangan.

### Penyimpanan browser

Storage, cookie, dan cache memiliki umur, visibilitas, risiko XSS, serta implikasi privasi yang berbeda. Jangan menyimpan data sensitif sekadar karena API penyimpanan tersedia. Rencanakan kedaluwarsa, logout, dan sinkronisasi state.

### Pengujian dan observabilitas

Uji perilaku pada input valid/tidak valid, respons lambat, kegagalan jaringan, klik ganda, dan navigasi kembali. Catat error tanpa membocorkan data pribadi. Uji dengan keyboard setelah script mengubah DOM.

## Alur kerja pada proyek

1. Tentukan interaksi yang benar-benar membutuhkan script.
2. Implementasikan struktur dan keadaan dasar pada HTML.
3. Modelkan state, event, dan kontrak API.
4. Tangani loading, gagal, pembatalan, dan respons usang.
5. Uji keamanan output, keyboard, serta urutan fokus.
6. Ukur bundel dan respons interaksi pada perangkat sasaran.

## Contoh penerapan

Pencarian kelas segera memperbarui hasil ketika tanggal dipilih. Jika pengguna cepat mengubah tanggal dua kali, hasil permintaan pertama tidak boleh menimpa hasil yang terakhir. Tampilan mengumumkan jumlah hasil atau kegagalan yang dapat diperbaiki; kueri dan URL tetap dapat dibagikan bila itu membantu tugas.

## Keputusan dan pertukaran yang perlu dicatat

- Interaksi ringan dapat dibuat tanpa framework; aplikasi kompleks mungkin terbantu oleh pengelolaan state yang terstruktur.
- Optimasi seperti debouncing perlu memastikan tindakan penting tetap terproses.
- Penyimpanan token di browser harus diputuskan bersama model ancaman, bukan mengikuti contoh acak.

## Pemeriksaan hasil

- [ ] Setiap interaksi memiliki keadaan loading, kosong, gagal, dan berhasil.
- [ ] Permintaan lama tidak merusak state terbaru.
- [ ] Tidak ada rahasia tertanam di kode klien.
- [ ] Navigasi keyboard dan pengumuman perubahan penting bekerja.
- [ ] Biaya unduh serta latensi interaksi diperiksa dengan data.

## Serah terima untuk AI atau tim proyek

Masukan: perilaku UI, kontrak API, batas keamanan. Keluaran: modul JS, diagram state bila kompleks, pengujian perilaku, dan ukuran kinerja. AI frontend mengimplementasi; peninjau keamanan memeriksa batas klien/server; QA menguji koneksi buruk dan interaksi cepat.

## Sumber utama dan tingkat bukti

1. [MDN — JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide) — panduan bahasa
2. [MDN — Web APIs](https://developer.mozilla.org/en-US/docs/Web/API) — rujukan API browser
3. [web.dev — INP](https://web.dev/articles/inp) — definisi metrik responsivitas

> **Cara membaca bukti:** spesifikasi/standar menentukan perilaku atau kriteria yang diuji; panduan resmi memberi praktik yang dianjurkan; penelitian pengguna memberi temuan kontekstual yang tetap harus diuji pada pengguna website ini. Pilihan alat dan ketentuan hukum harus diperiksa lagi saat implementasi.

## Pendalaman operasional untuk Website Builder

> Revisi integrasi 24 September 2026. Bagian ini menambah keputusan implementasi dan bukti penerimaan. Contoh merupakan rancangan, bukan hasil uji pengguna.

### State yang jujur dan efek yang terkendali

Gunakan satu representasi keadaan untuk setiap proses: idle, mengirim, berhasil, gagal, atau hasil belum diketahui. Beberapa boolean bebas dapat menghasilkan kombinasi mustahil seperti berhasil sekaligus gagal. Pisahkan state server, input pengguna, URL, serta preferensi; hindari menyimpan salinan nilai yang sebenarnya dapat diturunkan.

Permintaan pencarian dapat dibatalkan atau diberi penanda urutan agar hasil lama tidak menimpa kueri baru. Pembatalan permintaan oleh klien tidak menjamin operasi server dibatalkan. Untuk transaksi, timeout berarti hasil mungkin belum diketahui: cari status otoritatif sebelum mencoba lagi dengan identitas operasi yang sama.

Pada React, pakai Effect untuk sinkronisasi sistem luar; perhitungan turunan dapat dilakukan saat render dan tindakan pengguna ditangani pada event yang sesuai. Ini mengikuti [panduan resmi React](https://react.dev/learn/you-might-not-need-an-effect), bukan kewajiban memakai React. Validasi data runtime tetap diperlukan meskipun TypeScript lulus.

**Kasus uji material:** klik dua kali, ubah kueri cepat, pindah halaman ketika request berjalan, kembali dengan Back, jaringan putus sesudah submit, dan API mengembalikan bentuk data salah. Pilih sesuai fitur yang benar-benar dibuat.

Jangan memainkan bunyi sukses atau getaran hanya karena tombol ditekan. Umpan balik keberhasilan mengikuti hasil yang sudah diketahui; keadaan menunggu diberi pesan tersendiri. Haptik dan audio tidak menentukan keberhasilan transaksi.
