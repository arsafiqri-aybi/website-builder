# Basis Data, Pemodelan, dan Konsistensi

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

Basis data menyimpan keadaan yang perlu tetap benar setelah halaman ditutup atau server dimulai ulang. Ilmunya mencakup pemodelan entitas, relasi, query, kendala integritas, transaksi, indeks, migrasi, serta pemulihan. Dokumentasi [PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) digunakan sebagai contoh basis data relasional; prinsip desainnya dapat dipakai lintas produk, sedangkan detail sintaks berbeda.

Situs statis mungkin tidak memerlukan DB. Situs dengan akun, pesanan, stok, dan konten yang dikelola biasanya membutuhkan penyimpanan terstruktur dan kebijakan siklus data.

## Konsep yang perlu dikuasai

### Model konseptual

Uraikan benda dan kejadian: pengguna, kelas, sesi, pendaftaran, pembayaran. Tentukan identitas unik, kepemilikan, relasi satu-ke-banyak dan banyak-ke-banyak, serta data yang bersifat historis. Bedakan fakta yang disimpan dari nilai turunan yang dapat dihitung.

### Skema dan tipe

Pilih tipe data sesuai makna: tanggal/waktu dan zona, uang dengan representasi yang tepat, teks, bilangan, boolean, identitas. Hindari menyimpan status berbeda dalam satu kolom ambigu. Aturan `NOT NULL`, `UNIQUE`, `CHECK`, primary key, dan foreign key membantu menjaga integritas; lihat [PostgreSQL Constraints](https://www.postgresql.org/docs/current/ddl-constraints.html).

### Normalisasi dan denormalisasi

Pisahkan fakta yang berulang agar satu perubahan tidak memerlukan banyak pembaruan. Denormalisasi dapat membantu pola baca tertentu, namun menciptakan kewajiban sinkronisasi. Ukur kebutuhan sebelum menyimpan salinan data yang mudah kedaluwarsa.

### Query dan akses

Pahami SELECT, JOIN, agregasi, filter, urutan, paginasi, dan biaya query. Hindari pola N+1 pada daftar; periksa rencana eksekusi untuk kueri lambat. Gunakan query berparameter dari aplikasi untuk memisahkan data dan perintah.

### Indeks

Indeks dapat mempercepat pencarian dan sortir pada pola akses nyata, tetapi menambah biaya tulis serta ruang; [PostgreSQL Indexes](https://www.postgresql.org/docs/current/indexes.html) menjelaskan tradeoff ini. Buat indeks berdasarkan query penting dan verifikasi lewat metrik, bukan mengindeks setiap kolom.

### Transaksi dan isolasi

Transaksi membungkus perubahan yang harus berhasil bersama atau gagal bersama. Pahami pembacaan bersamaan, penguncian, konflik, dan retry sesuai tingkat isolasi. Untuk kuota kelas, strategi pengurangan kuota harus mencegah dua pendaftaran pada kursi terakhir.

### Migrasi skema

Setiap perubahan tabel perlu urutan penerapan, kompatibilitas dengan versi aplikasi yang masih berjalan, pemeriksaan data lama, serta rencana kembali. Migrasi besar dapat dilakukan bertahap: tambah kolom, tulis dua format bila perlu, alihkan pembacaan, lalu hapus format lama setelah aman.

### Backup dan pemulihan

Cadangkan data dan uji restore secara berkala; keberadaan file backup tidak menjamin bisa dipulihkan. Tentukan kebutuhan RPO (berapa banyak data boleh hilang) dan RTO (berapa lama layanan boleh berhenti). [PostgreSQL Backup](https://www.postgresql.org/docs/current/backup.html) menjelaskan beberapa strategi.

### Retensi dan privasi

Tentukan masa simpan, penghapusan, pseudonimisasi bila sesuai, serta siapa yang berhak melihat tabel. Audit akses yang sensitif tanpa menyimpan rahasia di log. Sediakan mekanisme pemenuhan permintaan data sesuai kebijakan dan hukum.

## Alur kerja pada proyek

1. Gambar model entitas dan aturan bisnis yang tidak boleh dilanggar.
2. Pilih tipe, kunci, relasi, serta constraint.
3. Tulis query untuk tugas utama dan teliti rencana eksekusi.
4. Tambahkan indeks berdasarkan bukti beban dan biaya tulis.
5. Uji transaksi dan skenario dua permintaan bersamaan.
6. Rancang migrasi, backup, restore, dan retensi.

## Contoh penerapan

Tabel `classes`, `sessions`, `users`, dan `registrations` dipisahkan sehingga satu kelas dapat memiliki beberapa jadwal. Kendala unik pada `(user_id, session_id)` mencegah pendaftaran ganda jika aturan melarangnya. Transaksi memeriksa kuota dan menulis pendaftaran; pengujian konkurensi memastikan kursi terakhir tidak terjual dua kali.

## Keputusan dan pertukaran yang perlu dicatat

- SQL relasional cocok saat hubungan dan integritas kuat; penyimpanan dokumen cocok pada bentuk data lain, tetapi tidak menghapus kebutuhan konsistensi.
- Paginasi offset sederhana namun dapat berubah ketika data baru masuk; cursor berguna pada daftar besar dan urutan stabil.
- Backup harus disertai latihan restore, penanggung jawab, serta target pemulihan.

## Pemeriksaan hasil

- [ ] Constraint mencerminkan invariannya dan query kritis teruji.
- [ ] Kueri pengguna tidak dapat membaca data milik orang lain.
- [ ] Operasi bersamaan tidak membuat keadaan invalid.
- [ ] Migrasi menjaga kompatibilitas rilis.
- [ ] Backup berhasil dipulihkan dalam target yang ditetapkan.

## Serah terima untuk AI atau tim proyek

Masukan: aturan domain dan pola akses. Keluaran: model data, skema, migrasi, query, indeks, retensi, serta hasil uji restore. AI data menjelaskan alasan constraint dan indeks; backend mematuhi kontraknya; QA menguji concurrency dan pemulihan.

## Sumber utama dan tingkat bukti

1. [PostgreSQL — Constraints](https://www.postgresql.org/docs/current/ddl-constraints.html) — aturan integritas
2. [PostgreSQL — Transactions](https://www.postgresql.org/docs/current/tutorial-transactions.html) — atomicity transaksi
3. [PostgreSQL — Indexes](https://www.postgresql.org/docs/current/indexes.html) — manfaat dan biaya indeks
4. [PostgreSQL — Backup](https://www.postgresql.org/docs/current/backup.html) — pilihan backup/restore

> **Cara membaca bukti:** spesifikasi/standar menentukan perilaku atau kriteria yang diuji; panduan resmi memberi praktik yang dianjurkan; penelitian pengguna memberi temuan kontekstual yang tetap harus diuji pada pengguna website ini. Pilihan alat dan ketentuan hukum harus diperiksa lagi saat implementasi.

## Pendalaman operasional untuk Website Builder

> Revisi integrasi 24 September 2026. Bagian ini menambah keputusan implementasi dan bukti penerimaan. Contoh merupakan rancangan, bukan hasil uji pengguna.

### Konsistensi yang dapat dibuktikan

`BEGIN` dan `COMMIT` saja tidak mencegah seluruh race condition. Pilih operasi atomik, constraint, penguncian, atau tingkat isolasi sesuai invariant. Misalnya, pengurangan stok bersyarat `stok > 0` harus diperiksa jumlah baris yang benar-benar berubah; seluruh perubahan pesanan terkait tetap berada dalam transaksi yang konsisten. Sintaks serta jaminan harus ditinjau pada mesin database yang dipakai.

Simpan uang sebagai nilai presisi yang sesuai beserta mata uang; jangan mengasumsikan semua mata uang memakai jumlah digit pecahan yang sama. Pisahkan waktu kejadian dari zona waktu tampilan. Nomor telepon, kode pos, dan identitas berformat angka biasanya bukan besaran untuk perhitungan.

Rancang migrasi dengan kompatibilitas versi aplikasi: tambah struktur → isi data dengan kontrol laju → validasi → alihkan penggunaan → hapus struktur lama saat aman. Perintah rollback yang menghilangkan data baru bukan pemulihan yang lengkap. Uji juga durasi lock pada data realistis.

**Uji operasional:** pulihkan backup ke lingkungan terpisah, verifikasi hitungan serta relasi kritis, dan jalankan perjalanan utama. Nilai RPO/RTO dari kebutuhan layanan; jangan mengarang target universal. Catat siapa dapat mengakses backup dan bagaimana penghapusan data berinteraksi dengan retensinya.

Sumber: [PostgreSQL Transaction Isolation](https://www.postgresql.org/docs/current/transaction-iso.html) dan [Backup](https://www.postgresql.org/docs/current/backup.html). Panduan transaksi PostgreSQL tidak boleh diasumsikan identik pada semua database.
