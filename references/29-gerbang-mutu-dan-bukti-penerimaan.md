# Gerbang mutu dan bukti penerimaan website

> Revisi integrasi · 24 September 2026 · Gunakan sebelum menyatakan hasil selesai, siap ditinjau, atau siap dirilis. Kedalaman pemeriksaan mengikuti perubahan dan risiko.

## Cara menyatakan hasil

Gunakan empat status: **lulus**, **gagal**, **belum diuji**, atau **tidak berlaku** dengan alasan. Kriteria yang belum diperiksa tidak mendapat nilai lulus. Catat artefak/versi, kondisi, hasil, bukti, dan batas. Sebuah prototipe tetap dapat selesai sesuai brief walaupun belum siap produksi, asalkan statusnya jujur.

Jangan merata-ratakan kegagalan kritis. Kebocoran data, kehilangan transaksi, kendala yang menutup tugas inti, dan fakta produk palsu tidak ditebus oleh skor estetika. Perbaiki penghalang dalam cakupan; bila di luar akses atau otorisasi, selesaikan bagian lain dan jelaskan batas konkret.

## Matriks gerbang

| Area | Bukti minimum yang sesuai konteks | Contoh penghalang |
| --- | --- | --- |
| Tujuan dan isi | Tugas utama jelas; fakta kritis punya sumber; asumsi berlabel | Harga, alamat, testimoni, atau klaim manfaat dikarang |
| Fungsi | Alur utama dijalankan; kegagalan utama ditangani | CTA tidak bekerja atau form menyatakan tersimpan padahal tidak |
| Visual | Hasil render dilihat pada layar sempit/lebar dan keadaan relevan | Teks terpotong, overlay menutup tindakan, foto salah produk |
| Aksesibilitas | Semantik, keyboard, fokus, kontras, zoom/reflow, media; alat bantu bila tersedia | Pengguna tidak dapat menyelesaikan tugas melalui kanal yang setara |
| Sensori | Fungsi berjalan tanpa efek opsional; kontrol bekerja | Musik/getaran dipaksa, status hanya melalui suara, gerak menghalangi |
| Data dan keamanan | Izin server, input/output, rahasia, integrasi diuji sesuai ancaman | Akses milik pengguna lain atau rahasia di klien |
| Performa | Kondisi pengukuran dan bottleneck dicatat; target sesuai konteks | Tugas terhenti pada perangkat/jaringan sasaran |
| Privasi | Payload dan alur data sesuai pemberitahuan serta pilihan | Data pribadi masuk URL/log/analitik tanpa kebutuhan yang benar |
| Operasi | Cara menjalankan, konfigurasi, rilis/pemulihan sesuai cakupan | Tidak ada cara mengetahui transaksi gagal atau memulihkan data |

## Aksesibilitas: contoh yang mudah disalahartikan

Kontras AA untuk teks biasa ialah 4,5:1 dan teks besar 3:1 dengan definisi serta pengecualian standar. Target pointer minimum 24 × 24 CSS px memiliki pengecualian; target 44 × 44 pada kriteria enhanced adalah AAA. Preferensi mengurangi gerak adalah bagian rancangan kenyamanan yang lebih luas; kriteria animasi interaksi 2.3.3 berada pada AAA. Jangan mengganti nama level untuk menyederhanakan laporan.

Audit sampel atau alat otomatis tidak membuktikan konformansi seluruh situs. Penilaian konformansi memerlukan semua kriteria yang berlaku pada cakupan halaman dan proses. Gunakan [WCAG 2.2](https://www.w3.org/TR/WCAG22/) bersama dokumen Understanding dan [panduan evaluasi WAI](https://www.w3.org/WAI/test-evaluate/). Laporkan batas jika pembaca layar atau pengguna nyata belum dilibatkan.

## Performa: lab dan lapangan

Catat URL, build, alat, viewport, perangkat, koneksi, dan waktu. Gunakan lab untuk diagnosis dan perbandingan; gunakan data lapangan ketika tersedia untuk pengalaman nyata. Core Web Vitals menilai LCP, INP, dan CLS; ambang dan persentil dirujuk pada [Web Vitals](https://web.dev/articles/vitals). Halaman baru tanpa sampel cukup dilaporkan belum memiliki bukti lapangan.

Jangan menulis “100/100, berarti terbaik” sebagai kesimpulan umum. Anggaran aset adalah keputusan proyek. Optimasi tidak boleh menghapus informasi aksesibel atau memalsukan indikator loading.

## Uji berdasarkan risiko

Untuk halaman profil, periksa tautan, konten, responsif, keyboard, fokus, kontras, dan pemuatan. Untuk katalog, tambahkan filter, URL, kembali/refresh, kosong, dan data panjang. Untuk akun/transaksi, tambahkan izin, sesi, input invalid, pengulangan, concurrency, serta integrasi dan pemulihan. Pilih pengujian yang dapat mengungkap kegagalan nyata.

Gunakan tes unit untuk aturan murni yang berisiko; integrasi untuk kontrak data dan server; browser untuk perjalanan utama; inspeksi visual untuk kualitas render. [Playwright](https://playwright.dev/docs/best-practices) menekankan perilaku yang terlihat pengguna dan isolasi tes. Hindari menulis tes yang sekadar mengulang detail implementasi.

## Format temuan dan serah terima

Satu temuan memuat dampak, lokasi, langkah reproduksi, hasil aktual, hasil diharapkan, bukti, serta usulan perbaikan. Prioritaskan berdasarkan dampak dan kemungkinan, bukan jumlah baris kode. Setelah memperbaiki, jalankan ulang kasus terkait serta bagian yang dipengaruhi.

Penyerahan kepada pengguna cukup menyebut hasil, cara membuka/memakai, pemeriksaan yang benar-benar dijalankan, dan batas penting. Jangan membebani alur website dengan istilah internal build, test, atau skor audit yang tidak membantu pengunjung. Simpan catatan teknis untuk pemilik dan pengembang.
