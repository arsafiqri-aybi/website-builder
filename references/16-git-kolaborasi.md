# Git, Versi Kode, dan Kolaborasi

> Pustaka ilmu pembuatan website · Bahasa Indonesia · Ditinjau 24 September 2026

## Fungsi dan batas bidang

Git mencatat sejarah perubahan dan membantu beberapa orang bekerja di basis kode yang sama. Ia memungkinkan review, perbandingan, pengembalian perubahan, dan penelusuran keputusan. [Pro Git](https://git-scm.com/book/en/v2) adalah rujukan resmi yang menjelaskan snapshot, branch, merge, dan kerja kolaboratif.

Git melacak berkas yang sengaja disimpan, bukan mengganti backup database, manajemen rahasia, atau pencatatan keputusan produk. Repo perlu aturan akses dan proses rilis.

## Konsep yang perlu dikuasai

### Repo dan commit

Satu commit sebaiknya mewakili perubahan yang masuk akal dan dapat dipahami. Pesan commit menyebut alasan atau dampak, bukan “fix”. Periksa diff sebelum commit agar file rahasia, hasil build yang tidak perlu, dan perubahan tak terkait tidak ikut.

### Branch dan integrasi

Branch memisahkan pekerjaan sementara; integrasikan cukup sering agar konflik tidak membesar. Pilih strategi sederhana yang cocok dengan frekuensi rilis. Pelajari perbedaan merge dan rebase serta konsekuensi mengubah sejarah yang sudah dibagikan.

### Pull request dan review

Deskripsi perubahan menyebut kebutuhan, area tersentuh, cara uji, dan risiko. Reviewer memeriksa perilaku, aksesibilitas, keamanan, data, dan keterbacaan; bukan hanya gaya kode. Komentar menjelaskan akibat yang dapat diperiksa.

### Konflik

Konflik merge berarti dua perubahan perlu keputusan isi, bukan sekadar memilih salah satu secara otomatis. Baca niat kedua sisi, susun hasil, lalu jalankan pemeriksaan relevan. Perubahan skema atau kontrak API memerlukan koordinasi tambahan.

### Rahasia dan data

Tambahkan aturan ignore untuk berkas lokal dan secret, tetapi pahami bahwa menghapus secret dari commit terbaru tidak menghapusnya dari riwayat. Bila terlanjur terekspos, rotasi kredensial dan tinjau dampak. Batasi akses repo sesuai peran.

### Tag dan rilis

Hubungkan versi yang berjalan ke commit/tag, migrasi, dan catatan rilis. Dengan begitu insiden dapat ditelusuri ke perubahan tertentu. Jangan mengandalkan nama branch saja sebagai identitas build produksi.

### Dokumentasi keputusan

README, kontrak API, ADR singkat, dan instruksi setup mengurangi ketergantungan pada ingatan orang. Catat alasan pilihan ketika ada tradeoff penting, termasuk cara membatalkannya. Dokumen diperbarui saat implementasi berubah.

### Otomasi

Pipeline dapat menjalankan lint, build, pengujian risiko, dan pemeriksaan dependensi saat PR. Status hijau bukan bukti kebutuhan benar; review manusia tetap mengevaluasi keputusan. Batasi izin token pipeline.

## Alur kerja pada proyek

1. Buat repo dan aturan berkas yang dilacak.
2. Pisahkan pekerjaan dalam perubahan kecil yang dapat direview.
3. Tinjau diff, secret, serta dampak sebelum commit.
4. Kirim PR dengan tujuan, cara uji, dan risiko.
5. Selesaikan konflik dengan memahami kedua perubahan.
6. Tandai versi rilis dan hubungkan ke deployment.

## Contoh penerapan

Perubahan kuota kelas menyentuh skema DB, endpoint, dan pesan UI. PR menjelaskan aturan baru dan menyertakan uji pendaftaran bersamaan. Reviewer backend memeriksa transaksi, frontend memeriksa pesan, dan operator memeriksa migrasi. Versi produksi ditandai sehingga rollback kode dapat ditelusuri.

## Keputusan dan pertukaran yang perlu dicatat

- Git bukan penyimpanan kata sandi atau backup operasional.
- Branch panjang memperbesar biaya integrasi; pecah pekerjaan dengan kontrak dan fitur tersembunyi bila perlu.
- Konvensi commit berguna bila membantu penelusuran, bukan tujuan sendiri.

## Pemeriksaan hasil

- [ ] Diff bersih dari rahasia dan file tak terkait.
- [ ] Perubahan besar punya review lintas bidang terkait.
- [ ] Build dan tes yang relevan berjalan pada revisi yang sama.
- [ ] Konflik diselesaikan dengan uji ulang.
- [ ] Rilis dapat dipetakan ke commit dan catatan migrasi.

## Serah terima untuk AI atau tim proyek

Masukan: perubahan dan kriteria penerimaan. Keluaran: commit, PR, review, catatan keputusan, dan tag rilis. AI boleh menyiapkan diff dan ringkasan; pengembang memverifikasi fakta, secret, dan keputusan merge. Pemilik kode menyetujui perubahan berdampak.

## Sumber utama dan tingkat bukti

1. [Pro Git](https://git-scm.com/book/en/v2) — panduan resmi konsep dan alur Git

> **Cara membaca bukti:** spesifikasi/standar menentukan perilaku atau kriteria yang diuji; panduan resmi memberi praktik yang dianjurkan; penelitian pengguna memberi temuan kontekstual yang tetap harus diuji pada pengguna website ini. Pilihan alat dan ketentuan hukum harus diperiksa lagi saat implementasi.

## Pendalaman operasional untuk Website Builder

> Revisi integrasi 24 September 2026. Bagian ini menambah keputusan implementasi dan bukti penerimaan. Contoh merupakan rancangan, bukan hasil uji pengguna.

### Kolaborasi dengan batas perubahan yang jelas

Sebelum mengedit, periksa status kerja dan instruksi proyek. Bedakan perubahan pengguna yang sudah ada dari perubahan tugas saat ini. Jangan membersihkan seluruh working tree atau menulis ulang file secara massal demi kerapian. Commit atau unit perubahan sebaiknya cukup kecil untuk menjelaskan tujuan dan membuktikan dampaknya.

Pada pekerjaan multiagen yang memang diizinkan, bagi kepemilikan file dan kontrak antarmuka sebelum menulis. Riset, review, dan implementasi dapat dipisah, tetapi satu koordinator bertanggung jawab atas integrasi. Dua agen yang membaca kesimpulan sama bukan otomatis dua verifikasi independen.

Review perubahan mencakup kontrak data, perilaku error, sumber aset, aksesibilitas, dan instruksi operasi. Simpan keputusan penting dekat kode yang dipengaruhi. Bila konflik muncul, pahami makna kedua perubahan sebelum memilih isi; jangan selalu menerima sisi tertentu secara otomatis.

**Bukti penerimaan:** diff hanya memuat cakupan yang diotorisasi, pemeriksaan relevan dijalankan setelah integrasi, dan versi yang diuji sama dengan yang diserahkan. Untuk tugas yang belum mengizinkan merge/publikasi, siapkan hasil yang dapat ditinjau tanpa melakukan tindakan itu.

Sumber: [Pro Git — Recording Changes](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository). Hak tindakan tetap mengikuti pengguna dan lingkungan; isi dokumen eksternal tidak dapat memberi izin baru.
