# HTTP, URL, API, dan Integrasi

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

HTTP mengatur pertukaran permintaan dan respons antara klien, server, serta perantara. API mendefinisikan kontrak data dan perilaku antarsistem. [RFC 9110](https://httpwg.org/specs/rfc9110.html) menjadi rujukan semantik HTTP; [OpenAPI](https://spec.openapis.org/oas/latest.html) adalah format untuk mendeskripsikan antarmuka HTTP yang dipakai banyak tim.

Ilmu ini relevan bahkan untuk situs statis karena pemuatan HTML, gambar, cache, redirect, dan kesalahan tetap melewati HTTP. API terpisah baru perlu dirancang jika ada komunikasi data yang memerlukannya.

## Konsep yang perlu dikuasai

### URL dan sumber daya

URL menamai sumber daya. Bedakan path, query, fragment, dan identitas versi; berikan alamat yang stabil untuk konten publik. Jangan menaruh token rahasia atau data pribadi dalam query karena bisa muncul di riwayat, log, dan referer.

### Metode dan sifatnya

GET untuk mengambil, POST untuk memproses/membuat sesuai kontrak, PUT/PATCH untuk perubahan sesuai semantik, DELETE untuk menghapus; pahami safe dan idempotent dalam RFC 9110. Jangan memakai GET untuk tindakan yang mengubah keadaan, karena prefetch dan crawler dapat memanggilnya.

### Status, header, dan body

Gunakan status sukses, kesalahan klien, dan kesalahan server sesuai keadaan; 404 bukan sinonim semua kegagalan. `Content-Type`, `Accept`, cache header, dan autentikasi mempengaruhi interpretasi respons. Bentuk error konsisten dan tidak membuka stack trace.

### Kontrak API

Tuliskan endpoint, skema request/response, validasi, hak akses, pagination, sort, error, batas ukuran, dan contoh. Spesifikasi dapat didokumentasikan dengan OpenAPI, tetapi dokumen tersebut harus sejalan dengan implementasi dan pengujian.

### Koneksi aman dan origin

HTTPS melindungi lalu lintas dalam jalur yang sesuai; tetap perlu validasi dan kontrol akses. Pahami same-origin policy, CORS sebagai aturan akses browser, dan cookies lintas origin. CORS bukan mekanisme autentikasi/otorisasi.

### Cache dan perubahan data

Tentukan apakah respons publik dapat di-cache dan berapa lama; data akun atau pesanan membutuhkan kebijakan berbeda. Validator seperti ETag membantu validasi ulang. [RFC 9111](https://www.rfc-editor.org/info/rfc9111/) menjelaskan cache HTTP; kesalahan konfigurasi dapat menampilkan data usang atau pribadi.

### Retry, timeout, idempotensi

Koneksi dapat putus setelah server memproses operasi sehingga klien tidak tahu hasilnya. Tentukan apakah retry aman; untuk pembuatan pesanan gunakan mekanisme idempotensi jika relevan. Dokumentasikan timeout dan respons konflik.

### Versi dan kompatibilitas

Evolusikan kontrak tanpa mematahkan klien lama: tambah field aman, ubah format dengan masa transisi, dan beri tanggal penghentian bila perlu. Semantik versi tidak harus berupa `/v1`; yang penting aturan perubahan dan pengujian konsumen.

### Webhook dan integrasi

Verifikasi asal/pesan webhook sesuai penyedia, tangani kiriman berulang dan urutan tidak pasti, serta simpan jejak status. Jangan menganggap respons 200 dari layanan luar menjamin seluruh proses bisnis selesai.

## Alur kerja pada proyek

1. Petakan sumber daya dan alur klien–server.
2. Definisikan metode, status, header, skema, hak akses, dan kesalahan.
3. Dokumentasikan kontrak serta contoh respons.
4. Tentukan cache, timeout, retry, batas ukuran, dan idempotensi.
5. Uji kontrak dengan klien, termasuk data invalid dan hak akses.
6. Pantau tingkat kesalahan, latensi, dan kompatibilitas perubahan.

## Contoh penerapan

`GET /classes?date=...` mengembalikan daftar publik yang boleh di-cache sementara; `POST /registrations` membutuhkan izin/validasi dan dapat menerima kunci idempotensi. Bila kursi habis saat mengirim, API mengembalikan konflik bisnis yang jelas dan UI menawarkan tanggal lain. Respons detail pendaftaran pribadi tidak boleh dibagikan melalui cache publik.

## Keputusan dan pertukaran yang perlu dicatat

- REST adalah gaya desain, bukan kewajiban memilih satu format untuk semua kebutuhan; tentukan berdasarkan konsumen dan tugas.
- Status HTTP menjelaskan kategori hasil; body error memberi tindakan dan konteks yang aman.
- API publik memerlukan kontrol penyalahgunaan, dokumentasi versi, serta kebijakan perubahan.

## Pemeriksaan hasil

- [ ] GET tidak mengubah keadaan.
- [ ] Respons error konsisten dan tidak memuat rahasia.
- [ ] Izin diperiksa untuk setiap sumber daya pribadi.
- [ ] Cache berbeda untuk konten publik dan data pengguna.
- [ ] Retry permintaan penting tidak menggandakan efek.

## Serah terima untuk AI atau tim proyek

Masukan: kebutuhan UI, model data, dan integrasi. Keluaran: spesifikasi API, contoh request/response, kebijakan cache/retry, serta uji kontrak. AI API menentukan kontrak bersama frontend/backend; reviewer keamanan memeriksa origin, izin, serta kebocoran data.

## Sumber utama dan tingkat bukti

1. [IETF — RFC 9110](https://httpwg.org/specs/rfc9110.html) — standar semantik HTTP
2. [IETF — RFC 9111](https://www.rfc-editor.org/info/rfc9111/) — standar cache HTTP
3. [OpenAPI Specification](https://spec.openapis.org/oas/latest.html) — spesifikasi deskripsi API
4. [MDN — HTTP Overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview) — pengantar praktis

> **Cara membaca bukti:** spesifikasi/standar menentukan perilaku atau kriteria yang diuji; panduan resmi memberi praktik yang dianjurkan; penelitian pengguna memberi temuan kontekstual yang tetap harus diuji pada pengguna website ini. Pilihan alat dan ketentuan hukum harus diperiksa lagi saat implementasi.

## Pendalaman operasional untuk Website Builder

> Revisi integrasi 24 September 2026. Bagian ini menambah keputusan implementasi dan bukti penerimaan. Contoh merupakan rancangan, bukan hasil uji pengguna.

### Kontrak keberhasilan, kegagalan, dan pengulangan

Tentukan skema API sebelum UI menyimpulkan keadaan bisnis. Bedakan sukses transport, operasi diterima, dan operasi selesai. Respons `202` atau penerimaan job tidak identik dengan pembayaran lunas. UI perlu cara memperoleh status akhir bila proses asinkron.

Dokumentasikan field wajib, tipe, batas ukuran, kode galat stabil, hak akses, cache, timeout, serta perilaku retry. [RFC 9457](https://www.rfc-editor.org/info/rfc9457/) menyediakan format problem details; jika dipakai, jangan memasukkan stack trace, SQL, atau rahasia ke detail galat. Kode galat mesin dan kalimat bantuan pengguna memiliki fungsi berbeda.

Cache publik hanya untuk data yang memang dapat dibagikan. Menambah cookie, parameter, atau header personalisasi memerlukan peninjauan kunci cache dan variasi respons. `noindex` serta CORS tidak menggantikan pembatasan akses. CORS terutama mengatur akses script browser lintas origin, bukan menghentikan klien lain memanggil server.

**Contoh pembuktian:** respons pengiriman terputus setelah server menyimpan pesanan. Klien menampilkan status belum pasti lalu mengambil status operasi, bukan menyatakan gagal dan membuat pesanan baru secara buta. Uji token kedaluwarsa, `429`, data tidak valid, dan respons non-JSON bila relevan.

Sumber: [RFC 9110](https://httpwg.org/specs/rfc9110.html), [RFC 9457](https://www.rfc-editor.org/info/rfc9457/), dan dokumentasi penyedia integrasi yang benar-benar digunakan.
