# Protokol multisensori untuk website

> Revisi integrasi · 24 September 2026 · Gunakan untuk mengubah pengetahuan pancaindra menjadi pilihan antarmuka yang realistis, terukur, dan dapat dikendalikan.

## Prinsip dasar

Tujuannya membantu manusia memahami, bertindak, dan merasa memiliki kendali. Jangan memaksimalkan intensitas atau jumlah rangsangan. Website standar menyediakan tampilan dan audio, serta input sentuh/keyboard/pointer; getaran bergantung kemampuan perangkat. Aroma, rasa, suhu, dan tekstur material tidak dipancarkan oleh halaman biasa.

Baca materi tiap indra jika proyek memerlukannya. Pengetahuan fisik berfungsi sebagai konteks dan batas representasi, bukan alasan membuat fitur perangkat yang tidak tersedia. Tidak setiap website membutuhkan audio, haptik, atau narasi aroma.

## Matriks kanal dan keputusan

| Kanal | Yang dapat diterapkan | Default rancangan | Yang diuji |
| --- | --- | --- | --- |
| Visual | Hierarki, teks, warna, gambar, gerak | Isi terbaca; pola jelas; gerak nonesensial dapat dikurangi | Kontras, pemahaman, responsif, fokus, gangguan |
| Audio | Konten, demonstrasi, pemberitahuan | Dekorasi senyap sampai dipilih; kendali mudah | Informasi setara, keyboard, gangguan pembaca layar |
| Sentuhan/input | Target, gestur, umpan balik perangkat | Kontrol mudah diaktifkan; tidak bergantung gestur rumit | Salah tekan, alternatif keyboard/tombol |
| Haptik | Getaran jika perangkat/API mendukung | Opsional; fallback penuh | Tidak didukung, mati, gagal, kenyamanan |
| Aroma | Bahasa, foto, kategori, sampel fisik jika tersedia | Deskripsi bersumber dan tidak berlebihan | Akurasi ekspektasi, bukan aroma digital |
| Rasa/flavor | Profil produk, bahan, tekstur, foto | Fakta produk jelas; tidak mengarang atribut diet | Pemahaman dan kecocokan ekspektasi |
| Tubuh/gerak | Respons visual terhadap scroll/aksi | Hindari gerak paksa yang menghambat tugas | Reduced motion, kontrol, keluhan penggunaan |

Kolom default adalah keputusan desain skill. Sebagian didukung pedoman aksesibilitas, tetapi seluruh tabel bukan satu standar normatif.

## Kartu keputusan sensori

Sebelum menambah fitur sensori, tulis ringkas:

1. Tugas dan hambatan yang ingin diperbaiki.
2. Kanal yang dipakai, fungsi, serta keadaan pemicunya.
3. Sumber bukti: standar, panduan, review, studi primer, atau hipotesis.
4. Kesesuaian bukti terhadap pengguna, perangkat, tugas, stimulus, dan durasi.
5. Alternatif tanpa fitur tersebut; kontrol dan cara berhenti.
6. Beban jaringan/render, implikasi data, dan potensi konflik kanal.
7. Luaran utama, dampak buruk, serta kondisi revisi.

Contoh: bunyi singkat untuk hasil proses bukan dipicu klik submit, melainkan status server yang sah. Status teks tetap hadir. Jika bunyi menutupi pembaca layar atau pengguna tidak menemukan mute, revisi atau hilangkan fitur. Kartu dapat berupa beberapa kalimat; jangan mengubah perubahan kecil menjadi dokumentasi panjang.

## Membedakan jenis bukti

Standar normatif seperti WCAG menetapkan kriteria konformansi dalam lingkupnya. Panduan resmi seperti W3C COGA memberi saran tambahan. Studi primer menunjukkan hasil pada kondisi eksperimen; tinjauan sistematis merangkum studi tetapi masih memiliki batas mutu dan keterterapan. Hipotesis desain adalah penerapan yang diusulkan tim.

Nilai jenis dan keterterapan secara terpisah. Bukti kuat tentang intervensi musik tidak otomatis menjadi bukti musik wajib di website. Asosiasi warna–emosi tidak membuktikan perubahan mood ketika tombol diubah. Eksperimen visual–haptik tidak menentukan manfaat getaran pada ponsel. Daftar bukti terperinci ada pada [register sumber](31-register-sumber-dan-pemutakhiran.md).

Jika hanya abstrak yang dapat dibaca, tandai dan jangan mengarang ukuran efek, rincian sampel, atau penilaian risiko bias. Tidak adanya akses bukan bukti tidak adanya efek. Hasil negatif pada protokol tertentu juga bukan pembuktian bahwa seluruh mekanisme tidak pernah terjadi.

## Konflik dan penyelesaian

| Konflik | Penyelesaian yang layak diuji |
| --- | --- |
| Warna merek terlalu samar | Cari pasangan teks/latar atau peran warna alternatif yang mempertahankan identitas |
| Audio menutupi pembaca layar | Awal senyap, putar opsional, kontrol independen, padanan teks |
| Hero video berat | Poster yang kuat, putar opsional, optimasi format, informasi utama dalam HTML |
| Haptik tidak tersedia | Konfirmasi tekstual/visual tetap berfungsi; jangan memblokir alur |
| Parallax menambah keluhan | Versi statis dan navigasi normal; uji tanpa animasi |
| Foto menggugah tetapi tidak cocok produk | Perbaiki representasi dan deskripsi sebelum menguji persuasi |
| Konversi meningkat bersama salah beli | Gunakan metrik pemahaman, pembatalan, dan keluhan sebagai pembatas |

Hindari manipulasi seperti urgensi palsu, pilihan penolakan disembunyikan, testimoni fiktif, dan profil kerentanan psikologis. Desain mendukung keputusan yang dipahami pengguna.

## Protokol uji lokal

Tentukan satu pertanyaan dan pembanding yang masuk akal, misalnya foto + deskripsi dibanding video opsional + deskripsi. Pertahankan fakta produk dan alur lain setara sejauh mungkin. Pilih peserta dari audiens sebenarnya, termasuk kebutuhan akses yang relevan; partisipasi dan rekaman mengikuti persetujuan yang sesuai.

Ukur keberhasilan tugas, kesalahan, bantuan, waktu jika relevan, pemahaman, kenyamanan yang dilaporkan, dan gangguan. Tentukan skala sebelum dipakai; skor 0–10 internal bukan instrumen klinis. Beri hak menghentikan sesi. Catat preferensi individu dan jangan menutupi kegagalan akses dengan rerata yang baik.

Jika pengguna nyata belum tersedia, lakukan review dan tes teknis, lalu laporkan batas itu. Simulasi AI tidak menjadi bukti bahwa manusia merasa nyaman. Keputusan yang dipengaruhi studi harus ditulis bersama ketidakpastiannya.

## Sumber langsung

- [W3C COGA](https://www.w3.org/TR/coga-usable/) — panduan tambahan kebutuhan kognitif.
- [W3C Audio Control](https://www.w3.org/WAI/WCAG22/Understanding/audio-control.html) — kendali audio dalam kriteria yang berlaku.
- [MDN Vibration API](https://developer.mozilla.org/en-US/docs/Web/API/Vibration_API) — kemampuan dan dukungan terbatas.
- [Jonauskaite dkk.](https://journals.sagepub.com/doi/10.1177/0956797620948810) — asosiasi warna lintas konteks budaya.
- [Ernst & Banks](https://www.nature.com/articles/415429a) — integrasi isyarat visual/haptik pada tugas eksperimen.
- [Herz & von Clef](https://pubmed.ncbi.nlm.nih.gov/11374206/) — label verbal dan penilaian bau nyata.
