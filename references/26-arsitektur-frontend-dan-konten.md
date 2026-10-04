# Arsitektur frontend, TypeScript, rendering, dan sistem konten

> Revisi integrasi · 24 September 2026 · Panduan keputusan engineering; baca bersama kebutuhan, HTML/CSS/JS, API, dan keamanan.

## Memilih bentuk sistem

Mulai dari pekerjaan pengguna, kebutuhan penyuntingan, frekuensi perubahan, data privat, serta kemampuan operasi. Pertahankan stack proyek yang ada sampai ada alasan kuat mengubahnya. Keunggulan suatu framework tidak menghilangkan biaya migrasi, pelatihan, hosting, dan dependensi.

| Bentuk kebutuhan | Kandidat awal | Risiko yang harus diperiksa |
| --- | --- | --- |
| Halaman informasi jarang berubah | HTML/CSS atau generasi statis | Kemudahan pembaruan konten dan formulir eksternal |
| Situs editorial dengan banyak penulis | CMS + rendering yang cocok | Peran editor, preview, revisi, media, konten berbahaya |
| Katalog publik yang diperbarui rutin | Data terstruktur + halaman statis/server sesuai kebutuhan | Stok usang, invalidasi cache, penemuan URL |
| Aplikasi interaktif privat | UI komponen + server/API yang terproteksi | Sesi, otorisasi, state, latensi, dan kebocoran cache |
| Transaksi dan pembayaran | Layanan server + data konsisten + penyedia yang sesuai | Idempotensi, webhook, rekonsiliasi, pemulihan |
| Prototipe untuk keputusan desain | Implementasi minimum dengan simulasi berlabel | Pengguna mengira data atau transaksi sudah nyata |

Tabel ini adalah titik awal desain, bukan rekomendasi membeli produk tertentu. Bandingkan pilihan berdasarkan batas konkret dan dokumentasi versi yang digunakan.

## Render dan batas klien–server

Konten statis dapat disiapkan sebelum permintaan; server rendering menghasilkan respons sesuai permintaan; rendering klien memperbarui antarmuka setelah kode berjalan. Kombinasi dapat tepat. Nilai kebutuhan indeks, waktu konten pertama, personalisasi, cache, interaktivitas, serta dukungan host. Jangan mengirim seluruh aplikasi ke klien hanya untuk satu tombol interaktif.

Pada Next.js App Router, dokumentasi membedakan Server dan Client Components: pekerjaan dekat sumber data dan rahasia dapat ditempatkan di server, sedangkan interaksi browser berada di sisi yang sesuai. Ini perilaku framework tersebut, bukan istilah yang otomatis berlaku sama untuk seluruh ekosistem. Rujukan: [Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components).

Rahasia, pemeriksaan izin, dan keputusan transaksi tetap di batas server yang tepercaya. Menamai file “server” tidak cukup jika proses build atau serialisasi mengirim isinya kepada klien. Periksa network payload dan hasil bundle ketika risiko konkret ada. Personalisasi juga mengubah strategi cache: data pengguna A tidak boleh menjadi respons publik pengguna B.

## State dan tipe

Pisahkan sumber state: data server, URL, form lokal, preferensi pengguna, dan nilai turunan. Pilih satu pemilik untuk tiap fakta. Filter yang harus dapat dibagikan sebaiknya punya representasi URL; masukan sementara tidak selalu perlu global store. Nilai total dari keranjang dapat diturunkan, sedangkan nilai final pembayaran diverifikasi server.

TypeScript membantu kontrak dan cabang keadaan melalui tipe, narrowing, serta discriminated union. Ia tidak memvalidasi respons API pada runtime atau menjamin aturan bisnis. Hindari `any` luas yang menghilangkan manfaat kontrak. Rujukan: [TypeScript Narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html).

React Effect digunakan untuk sinkronisasi sistem luar; jangan menyimpan state turunan lewat Effect tanpa kebutuhan. Tindakan yang disebabkan klik dapat ditangani pada event. Rujukan: [You Might Not Need an Effect](https://react.dev/learn/you-might-not-need-an-effect). Prinsip utamanya menjaga aliran data mudah dijelaskan, bukan menghapus semua Effect.

## CMS dan tata kelola konten

Modelkan objek sebelum halaman: produk, artikel, lokasi, jadwal, penulis, media. Tentukan field wajib, sumber fakta, relasi, status draft/published/archived, slug, waktu berlaku, dan siapa boleh mengubahnya. Editor membutuhkan preview dan riwayat revisi; API publik tidak boleh membocorkan draft atau field internal.

Konten kaya yang dapat diedit merupakan input tak tepercaya. Batasi markup, sanitasi sesuai konteks, dan tinjau unggahan. Gambar perlu alt, dimensi, kredit/lisensi, crop, dan pemilik. Jika fakta seperti harga berubah, periksa semua representasinya: halaman, cache, pencarian, data terstruktur, dan checkout.

## Bahasa, locale, dan format

Tetapkan `lang`, format tanggal/mata uang, zona waktu, dan kemungkinan teks memanjang. Nomor telepon atau kode pos bukan besaran aritmetika. Antarmuka multibahasa membutuhkan struktur URL, proses penerjemahan, konten yang belum tersedia, serta perubahan arah baca bila relevan. Jangan menyamakan menerjemahkan tombol dengan melokalkan seluruh pengalaman. [W3C language declarations](https://www.w3.org/International/questions/qa-html-language-declarations) menjadi rujukan deklarasi bahasa.

## Keluaran dan uji

Hasil arsitektur adalah keputusan singkat yang menjawab: mengapa bentuk ini cukup; data mana publik/privat; siapa pemilik state; bagaimana konten berubah; bagaimana sistem gagal dan dipulihkan; apa yang membuat keputusan perlu ditinjau. Hindari diagram banyak kotak bila daftar kontrak lebih jelas.

Uji halaman masuk langsung, navigasi Back, refresh rute, sesi habis, jaringan lambat, respons invalid, konten panjang, dan API gagal sesuai fitur. Pastikan pola loading tidak menyembunyikan kegagalan dan bahwa cache tidak menyeberangkan identitas. Sebelum memilih framework baru, cek kembali dokumentasi dan batas hosting pada saat implementasi.
