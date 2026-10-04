# Pendengaran: suara yang informatif, dapat dikendalikan, dan aman

**Versi:** 24 September 2026 · **Cakupan:** web/aplikasi dan lingkungan fisik. Rujuk `00-KONSEP-DAN-METODE.md` untuk klasifikasi N/G/S/P/H.

## 1. Mekanisme dan konteks

Bunyi dapat memberi peringatan, konfirmasi, informasi, dan suasana. Respons dipengaruhi level, durasi, waktu, makna, kebiasaan, kemampuan mendengar, serta tugas yang sedang berlangsung. Kebisingan lingkungan berkaitan dengan gangguan tidur dan kesehatan dalam pedoman WHO; ini berbeda dari kesukaan terhadap suatu efek suara. Audio yang diputar tanpa diminta dapat menutupi suara pembaca layar dan mengganggu konsentrasi [W3C Audio Control](https://www.w3.org/WAI/WCAG22/Understanding/audio-control.html).

## 2. Apa yang didukung penelitian

| Temuan | Jenis | Konsekuensi desain | Batas |
| --- | --- | --- | --- |
| WHO mengeluarkan pedoman kebisingan lingkungan untuk sumber seperti jalan, kereta, pesawat, turbin, dan hiburan | G | Ukur sumber dan paparan lingkungan fisik berdasarkan skenario | Angka paparan jalan raya tidak menjadi target volume notifikasi ponsel |
| WHO safe listening mengaitkan risiko pendengaran dengan level, durasi, dan frekuensi; contoh 80 dB selama 40 jam/minggu untuk mendengar personal | G | Hindari memaksa audio keras; gunakan kendali pengguna dan pertimbangkan durasi | Bukan izin membuat bunyi aplikasi selalu 80 dB; perangkat dan headphone bervariasi |
| WCAG 1.4.2 mensyaratkan kendali jika audio web otomatis berjalan >3 detik | N | Dapat dijeda/dihentikan atau volume diatur secara terpisah dari volume sistem | Putar otomatis <3 detik tidak berarti pengalaman yang baik |
| Takarir untuk media tersinkron yang direkam mencakup ujaran dan bunyi bermakna | N | Pastikan informasi sama dapat dipahami tanpa mendengar | Transkrip teks mentah tidak selalu menggantikan takarir tersinkron untuk video |
| Meta-analisis intervensi musik menemukan efek rata-rata pada ukuran stres di konteks yang diteliti | S | Musik pilihan pengguna dapat diuji sebagai fitur opsional | Musik yang diputar wajib di website tidak sama dengan intervensi terstruktur dan disetujui |
| ISO 12913 mendefinisikan soundscape sebagai persepsi lingkungan akustik dalam konteks | N/kerangka | Evaluasi persepsi penghuni selain mengukur desibel | Satu angka dB tidak mewakili pengalaman akustik secara utuh |

Sumber: [WHO environmental noise guidelines](https://www.who.int/publications/i/item/9789289053563), [WHO safe listening](https://www.who.int/news-room/questions-and-answers/item/deafness-and-hearing-loss-safe-listening), [W3C audio control](https://www.w3.org/WAI/WCAG22/Understanding/audio-control.html), [W3C captions](https://www.w3.org/WAI/WCAG22/Understanding/captions-prerecorded.html), [de Witte dkk., 2020](https://pubmed.ncbi.nlm.nih.gov/31167611/), dan [ISO 12913-1](https://www.iso.org/standard/52161.html).

## 3. Spesifikasi untuk website/aplikasi

### 3.1 Kontrol

- **Awal tanpa audio dekoratif** adalah pilihan desain H yang kuat secara kehati-hatian. Bila audio penting, beri label jelas sebelum diputar dan kendali yang dapat ditemukan serta dioperasikan melalui keyboard dan pembaca layar.
- Jika konten otomatis berbunyi >3 detik, penuhi [WCAG 1.4.2](https://www.w3.org/WAI/WCAG22/Understanding/audio-control.html): jeda/berhenti atau volume independen dari volume sistem. Desain yang lebih baik sering menunggu tindakan pengguna.
- Pengguna dapat mengubah level atau mute, dan pilihan tidak tersembunyi di menu dalam. Jangan memulai lagi suara setelah pengguna mematikannya tanpa alasan yang jelas.
- Konfirmasi singkat bisa memakai tampilan + suara/haptik opsional; keadaan gagal atau bahaya tidak boleh hanya lewat suara.

### 3.2 Padanan informasi

- Sediakan takarir untuk video rekaman yang memuat audio sesuai [WCAG 1.2.2](https://www.w3.org/WAI/WCAG22/Understanding/captions-prerecorded.html), termasuk pembicara dan efek bunyi penting.
- Untuk audio saja, sediakan alternatif teks yang setara sesuai kriteria WCAG yang relevan. Untuk video dengan informasi visual penting, pertimbangkan deskripsi audio atau alternatif media sesuai kebutuhan.
- Uji versi tanpa suara. Pengguna yang tuli, memakai ponsel di ruang publik, atau menonaktifkan audio harus dapat menyelesaikan tugas yang sama.

### 3.3 Bunyi yang tidak mengganggu

- Hindari pengulangan notifikasi tanpa batas; berikan cara membedakan urgensi dan membungkam kategori rendah prioritas. Jangan membuat pengguna bergantung pada frekuensi atau nada tertentu saja.
- Musik latar yang dipilih sendiri dapat diuji berdasarkan tugas; saat membaca, bekerja, atau memakai pembaca layar, preferensi dapat berubah. Meta-analisis stres musik tidak menetapkan genre atau tempo universal.
- Jangan klaim “frekuensi X menyembuhkan” atau “suara alam selalu menenangkan” tanpa uji yang sepadan dengan klaim.

## 4. Bila proyek mencakup ruang fisik

- Identifikasi sumber: percakapan, lalu lintas, HVAC, perangkat, gema, dan musik. Catat kapan, berapa lama, di mana, dan siapa yang terdampak.
- Pahami tiga tujuan yang bisa saling tarik-menarik: keselamatan pendengaran, keterpahaman percakapan/pengumuman, dan kenyamanan. Mengurangi semua suara sampai nol tidak selalu sesuai konteks.
- Evaluasi level paparan dan akustik dengan profesional untuk ruang berisiko; bedakan [WHO kebisingan lingkungan](https://www.who.int/publications/i/item/9789289053563) dari [WHO mendengar personal](https://www.who.int/news-room/questions-and-answers/item/deafness-and-hearing-loss-safe-listening). Keduanya memakai metrik serta durasi berbeda.
- Sediakan zona yang lebih tenang atau pilihan duduk bila ruang bersama membutuhkan musik. Beri isyarat visual dan taktil yang pantas untuk pengumuman penting.

## 5. Protokol pengujian

1. Uji tiga kondisi yang relevan: audio mati, audio opsional, dan kondisi bising nyata. Jangan menguji hanya dengan headphone di ruang laboratorium sepi bila produk dipakai di kendaraan atau kantor.
2. Ukur keberhasilan memahami informasi, kesalahan, waktu, kenyamanan, preferensi volume, frekuensi mute, dan apakah pengguna dapat menemukan kontrol.
3. Libatkan orang dengan gangguan pendengaran, pembaca layar, sensitivitas suara, serta pengguna tanpa kebutuhan khusus. Uji juga takarir dan alternatif teks.
4. Untuk ruang, dokumentasikan level, durasi, lokasi, dan keluhan; bila risiko paparan tinggi, gunakan instrumen serta ahli yang sesuai.
5. Hentikan atau ubah audio yang membuat informasi gagal dipahami, sulit dimatikan, atau menyebabkan keluhan berulang. Jangan menyembunyikan rata-rata ketidaknyamanan kelompok kecil di balik skor keseluruhan.

## 6. Batas dan antiklaim

- **Tidak** ada angka volume antarmuka yang berlaku di semua speaker/headphone karena keluaran fisik berbeda.
- **Tidak** boleh menyimpulkan musik pilihan peserta penelitian mengurangi stres berarti musik otomatis di seluruh situs akan menenangkan pengguna.
- **Tidak** cukup memberi ikon speaker jika video takarirnya hilang atau kontrol tidak bisa diakses.

## Daftar sumber kunci

1. WHO, [Environmental noise guidelines for the European Region](https://www.who.int/publications/i/item/9789289053563) — kesehatan dan paparan lingkungan.
2. WHO, [Deafness and hearing loss: Safe listening](https://www.who.int/news-room/questions-and-answers/item/deafness-and-hearing-loss-safe-listening) — level dan durasi mendengar personal.
3. W3C, [Audio Control](https://www.w3.org/WAI/WCAG22/Understanding/audio-control.html); [Captions prerecorded](https://www.w3.org/WAI/WCAG22/Understanding/captions-prerecorded.html) — kriteria web.
4. de Witte dkk. (2020), [tinjauan sistematis dan dua meta-analisis musik dan stres](https://pubmed.ncbi.nlm.nih.gov/31167611/) — intervensi yang diteliti, tidak langsung UI.
5. ISO, [Soundscape ISO 12913-1](https://www.iso.org/standard/52161.html) — kerangka persepsi suara dalam konteks.

## Lampiran pendalaman: tiga pertanyaan yang sering tertukar

**Apakah aman bagi pendengaran?** [WHO Safe Listening](https://www.who.int/news-room/questions-and-answers/item/deafness-and-hearing-loss-safe-listening) memberi contoh 80 dB selama 40 jam per minggu dan 90 dB selama 4 jam per minggu pada konteks mendengar personal. Durasi mingguan ini menunjukkan mengapa paparan perlu dipandang akumulatif. Angka tersebut tidak bisa diubah langsung menjadi “setel volume media pada 60%” untuk semua perangkat; keluaran nyata perlu diketahui.

**Apakah musik mengurangi stres?** [de Witte dkk.](https://pubmed.ncbi.nlm.nih.gov/31167611/) menghimpun uji terkontrol intervensi musik dan melaporkan rata-rata efek pada ukuran fisiologis (d≈0,38) serta psikologis (d≈0,55). Itu dukungan untuk penelitian musik dalam konteks intervensi yang spesifik, bukan alasan autoplay. Perhatikan peserta memilih musik atau tidak, waktu pemaparan, dan jenis tugas sebelum menerapkan temuan.

**Apakah suara membantu tugas?** Bahkan musik yang disukai bisa tidak cocok ketika tugas memerlukan mendengar ucapan lain. [W3C Audio Control](https://www.w3.org/WAI/WCAG22/Understanding/audio-control.html) menjelaskan gangguan terhadap pembaca layar. Jadi uji pemahaman instruksi, bukan hanya penilaian suasana. Di ruang fisik, sumber, gema dan percakapan bermakna lebih penting daripada label generik “hening”.

**Contoh kegagalan:** sistem mengirim bunyi lembut saat pembayaran berhasil, tetapi tidak ada perubahan visual. Pengguna tanpa suara mengulangi pembayaran. Solusi: status tekstual yang persisten dan semantik, bunyi opsional sebagai penguat. Ukur kesalahan ganda setelah perbaikan.


## Integrasi operasional Website Builder — revisi 24 September 2026

### Rancangan audio sebagai keadaan produk

Tentukan fungsi audio: konten utama, pemberitahuan, demonstrasi bunyi produk, atau dekorasi. Audio dekoratif mulai mati sebagai default rancangan skill. Jika pengguna memilih memutar, sediakan nama kontrol yang jelas, status putar/jeda, mute, dan pengaturan yang sesuai. Kegagalan pemutaran karena kebijakan browser harus menghasilkan keadaan yang dapat dipahami, bukan kontrol yang tampak aktif tanpa suara.

Pada video, transkrip dan takarir berbeda fungsinya. Takarir tersinkron memuat ujaran serta bunyi penting; audio description dibutuhkan pada kondisi yang berlaku bila informasi visual penting tidak tersedia dari audio. Jangan menggunakan label “aksesibel” hanya karena ada tombol CC yang tidak memiliki berkas takarir.

**Pengujian setara:** selesaikan tugas dengan audio mati, keyboard, dan perangkat yang berbeda; periksa bahwa notifikasi tidak memotong pembaca layar. Perpindahan halaman dan tab tersembunyi tidak seharusnya memulai ulang musik yang sudah dihentikan. Pengguna dapat menghentikan bunyi tanpa meninggalkan transaksi.

Meta-analisis de Witte dan rekan tetap merupakan referensi intervensi musik. Pada pembaruan ini, metadata dan cakupan kajian ditemukan; naskah penuh tidak dapat diakses melalui jalur yang tersedia. Angka efek pada materi sebelumnya belum diaudit ulang dan tidak digunakan sebagai ambang desain website. Jangan mengubah manfaat rata-rata intervensi menjadi janji bahwa musik situs akan mengurangi stres.

Rujukan langsung: [Audio Control](https://www.w3.org/WAI/WCAG22/Understanding/audio-control.html), [Captions](https://www.w3.org/WAI/WCAG22/Understanding/captions-prerecorded.html), dan [rekaman publikasi de Witte](https://research.ou.nl/en/publications/effects-of-music-interventions-on-stress-related-outcomes-a-syste/).
