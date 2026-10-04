# Analisis Kebutuhan dan Perumusan Masalah

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

Bidang ini menjawab mengapa website dibuat, siapa yang dilayani, tugas apa yang perlu selesai, dan bagaimana keberhasilannya dibuktikan. Hasilnya adalah ruang lingkup yang dapat diuji, bukan sekadar daftar halaman atau permintaan fitur. Penemuan kebutuhan sebaiknya mendahului keputusan teknologi; pedoman [GOV.UK Discovery](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works) membahas pemahaman pengguna, konteks, batasan, dan nilai masalah.

Berlaku untuk situs statis sampai aplikasi transaksional. Kedalaman proses menyesuaikan risiko: halaman profil usaha dapat memakai wawancara singkat, sedangkan layanan yang memproses uang atau data sensitif memerlukan pemetaan pihak, aturan, dan kegagalan lebih ketat.

## Konsep yang perlu dikuasai

### Masalah, tujuan, dan hasil

Tuliskan masalah sebagai hambatan pengguna, misalnya calon peserta tidak menemukan jadwal yang akurat; jangan langsung menetapkan solusinya berupa aplikasi. Pisahkan tujuan pengguna, tujuan organisasi, dan indikator hasil. Sasaran yang bisa diamati lebih berguna daripada target abstrak seperti “lebih modern”.

### Pemangku kepentingan dan pengguna

Identifikasi pengunjung, pemilik konten, operator, admin, mitra, dan orang yang tidak nyaman memakai layanan digital. Catat kebutuhan, wewenang, kendala perangkat/jaringan, bahasa, serta aksesibilitas masing-masing. Wawancarai pengguna nyata; asumsi internal diberi label hipotesis.

### Riset dan triangulasi

Gunakan wawancara untuk memahami alasan, observasi untuk melihat praktik, analitik untuk pola, serta uji kegunaan untuk hambatan antarmuka. Data perilaku menjelaskan apa yang terjadi, belum tentu mengapa. Catat asal data, jumlah/sampel, bias rekrutmen, dan kesimpulan yang belum teruji.

### Persyaratan fungsional

Nyatakan kemampuan secara konkret: “pengunjung melihat kelas sesuai tanggal”, “admin mengubah kapasitas”, “pembayaran gagal tidak membuat pesanan lunas”. Sertakan keadaan kosong, kesalahan, batas akses, pembatalan, dan pengulangan permintaan. Fitur tanpa kondisi gagal sering belum siap dibangun.

### Persyaratan nonfungsional

Tentukan target aksesibilitas, keamanan, performa, pemulihan, perangkat, volume, bahasa, privasi, dan kesiapan operasional. Nyatakan konteks ukur: misalnya waktu tanggap pada halaman tertentu dan jenis jaringan, bukan janji umum “cepat”. Hubungkan setiap target ke cara memeriksanya.

### Prioritas dan dependensi

Pisahkan kebutuhan wajib untuk tugas inti, kebutuhan penting setelah peluncuran, dan eksperimen. Petakan dependensi: formulir pendaftaran memerlukan kebijakan data, model data, mekanisme kesalahan, dan alur konfirmasi. Nilai tinggi tidak selalu berarti dikerjakan dahulu bila risiko dasar belum ditangani.

### Kriteria penerimaan

Buat contoh kondisi Given–When–Then atau skenario dalam bahasa biasa yang dapat diamati. “Ketika kursi habis, tombol pendaftaran tidak mengirim pesanan dan alternatif ditampilkan” lebih bisa diuji daripada “UI ramah pengguna”. Kriteria mencakup pengguna keyboard dan layar kecil.

### Risiko dan asumsi

Daftar asumsi yang paling dapat menggagalkan proyek: data tersedia, layanan pihak ketiga dapat diandalkan, izin pemrosesan data sesuai, operator punya waktu memperbarui isi. Susun eksperimen atau bukti untuk masing-masing. Jangan menyamakan temuan dari satu responden dengan fakta populasi.

### Pengukuran dan batas data

Definisikan keberhasilan sebagai hasil tugas, seperti persentase pendaftaran selesai, tingkat kesalahan, waktu menemukan informasi, dan umpan balik. Ukur hanya data yang diperlukan; tetapkan pemilik metrik, baseline, dan periode. Penurunan klik dapat berarti pengalaman lebih baik jika pengguna lebih cepat selesai.

## Alur kerja pada proyek

1. Tulis ringkasan masalah, audiens, dan tujuan dengan kata-kata yang bisa diverifikasi.
2. Kumpulkan bukti dari pengguna serta pemilik proses; tandai asumsi, fakta, dan batas penelitian.
3. Peta perjalanan tugas dari sebelum masuk situs hingga sesudah tugas selesai.
4. Ubah temuan menjadi cerita kebutuhan, kondisi gagal, dan persyaratan nonfungsional.
5. Urutkan prioritas menggunakan nilai pengguna, risiko, biaya, dan dependensi.
6. Tulis kriteria penerimaan dan metrik keberhasilan, lalu tinjau bersama pemilik proses.
7. Kelola perubahan: jika temuan baru mengubah prioritas, perbarui keputusan dan alasan.

## Contoh penerapan

Contoh situs kelas: kebutuhan awal “buat aplikasi kelas” diubah menjadi “orang bisa menemukan jadwal dan mendaftar tanpa menghubungi admin”. Temuan wawancara mungkin menunjukkan harga dan kuota tidak jelas. Keluaran fase ini: halaman jadwal publik, rincian biaya, pendaftaran dengan konfirmasi, hak admin memperbarui kuota, serta ukuran keberhasilan penyelesaian pendaftaran. Pemrosesan pembayaran ditunda bila belum ada bukti kebutuhan dan kesiapan operasi.

## Keputusan dan pertukaran yang perlu dicatat

- MVP adalah cakupan awal yang cukup untuk menguji hasil pengguna, bukan alasan mengabaikan keamanan atau aksesibilitas.
- Situs statis sering cukup jika informasi jarang berubah dan tidak ada data transaksi; pilih sistem dinamis bila pengelolaan mandiri dan alur data memang diperlukan.
- Jangan menetapkan target performa, volume, atau konversi angka tertentu tanpa baseline dan konteks bisnis.

## Pemeriksaan hasil

- [ ] Dokumen masalah menyebut pengguna dan tugas utama.
- [ ] Setiap fitur prioritas memiliki kriteria penerimaan dan penanggung jawab.
- [ ] Keadaan gagal dan akses tidak sah ikut terpetakan.
- [ ] Persyaratan privasi, aksesibilitas, dan operasional punya cara uji.
- [ ] Asumsi serta keputusan yang belum pasti diberi pemilik dan tenggat.

## Serah terima untuk AI atau tim proyek

Masukan: tujuan organisasi, wawancara, proses saat ini. Keluaran: brief masalah, persona berbasis bukti (bila berguna), daftar kebutuhan berprioritas, skenario uji, metrik, dan daftar asumsi. AI perencana mengusulkan struktur; peneliti memverifikasi dengan manusia; pemilik proyek menyetujui keputusan ruang lingkup. Jangan biarkan AI mengarang hasil wawancara.

## Sumber utama dan tingkat bukti

1. [GOV.UK — Discovery](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works) — panduan praktik pemerintah untuk membingkai masalah dan batasan
2. [GOV.UK — User research](https://www.gov.uk/service-manual/user-research) — metode pengumpulan dan analisis kebutuhan
3. [GOV.UK — Measuring success](https://www.gov.uk/service-manual/measuring-success) — panduan mengukur hasil layanan

> **Cara membaca bukti:** spesifikasi/standar menentukan perilaku atau kriteria yang diuji; panduan resmi memberi praktik yang dianjurkan; penelitian pengguna memberi temuan kontekstual yang tetap harus diuji pada pengguna website ini. Pilihan alat dan ketentuan hukum harus diperiksa lagi saat implementasi.

## Pendalaman operasional untuk Website Builder

> Revisi integrasi 24 September 2026. Bagian ini menambah keputusan implementasi dan bukti penerimaan. Contoh merupakan rancangan, bukan hasil uji pengguna.

### Dari brief menjadi kontrak hasil

Pisahkan tiga hal: fakta yang diberikan pemilik, asumsi sementara, dan keputusan yang sudah diuji. Brief minimum memuat jenis layanan, pengguna utama, satu perjalanan penting, sumber konten, cara kontak/transaksi, perangkat, pengelola setelah rilis, serta tindakan yang diizinkan. Jangan menunggu riset besar untuk membuat prototipe yang reversibel; jangan pula memakai prototipe sebagai bukti kebutuhan pasar.

Gunakan matriks `kebutuhan → perilaku → komponen/data → kasus gagal → bukti penerimaan`. Contoh toko roti: kebutuhan mengetahui produk yang cocok diturunkan menjadi daftar bahan dan alergen yang berasal dari pemilik, filter yang jujur, foto representatif, serta keadaan informasi belum tersedia. Ukuran keberhasilannya ialah pengguna memahami pilihan; jumlah animasi bukan indikatornya. Jangan mengisi fakta yang belum ada dengan dugaan AI.

Untuk kualitas pengalaman, pilih dua atau tiga kata arah seperti hangat, teliti, dan lapang. Terjemahkan masing-masing menjadi keputusan yang bisa diperiksa: fotografi produk nyata, informasi harga terstruktur, dan ruang antarbagian. Label tersebut adalah sasaran desain, bukan diagnosis psikologis.

**Gerbang keputusan:** sebelum memilih stack, pastikan apakah tugas membutuhkan penyimpanan, akun, pembayaran, pencarian besar, atau penyunting nonteknis. Jawaban ini lebih menentukan daripada tren framework. Catat alasan jika keputusan berubah.

**Uji pembuktian:** minta pembaca menjelaskan apa yang bisa dilakukan, biaya/konsekuensinya, dan langkah berikutnya. Jika penjelasannya berbeda dari tujuan layanan, perbaiki hierarki dan isi sebelum menambah fitur.

Sumber pemutakhiran: [GOV.UK Discovery](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works). Kontrak hasil di atas adalah sintesis operasional untuk project ini.
