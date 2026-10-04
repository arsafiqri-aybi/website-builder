# Penglihatan: kejelasan, gerak, warna, dan cahaya

**Versi:** 24 September 2026 · **Cakupan:** antarmuka digital dan, bila ditandai, ruang fisik. Baca kerangka bukti pada `00-KONSEP-DAN-METODE.md`.

## 1. Mekanisme yang relevan

Penglihatan membantu mendeteksi objek, membaca, mengarahkan perhatian, dan membangun ekspektasi. Keterbacaan dipengaruhi kontras, ukuran, penskalaan, susunan, serta kondisi tampilan. Gerak dapat menarik perhatian tetapi juga mengalihkan tugas atau menimbulkan reaksi vestibular. Cahaya fisik turut terlibat dalam tidur dan kewaspadaan melalui waktu, intensitas, dan spektrum paparan. Hubungan **warna–emosi** ialah asosiasi yang bervariasi, bukan tombol biologis untuk menghasilkan satu perasaan.

## 2. Temuan dan batas inferensi

| Klaim yang didukung | Jenis | Apa arti praktisnya | Yang tidak boleh disimpulkan |
| --- | --- | --- | --- |
| WCAG 2.2 AA menetapkan kontras teks biasa ≥4,5:1 dan teks besar ≥3:1, dengan pengecualian terdefinisi | N | Periksa kombinasi warna semua status; jangan mengandalkan penilaian mata | “Lolos kontras” tidak membuktikan seluruh pengalaman nyaman |
| WCAG 2.2 AA menetapkan kontras ≥3:1 untuk bagian visual komponen UI dan objek grafis yang diperlukan, dengan pengecualian | N | Audit batas input, ikon informasi, dan indikator fokus sesuai kriterianya | Semua garis dekoratif harus 3:1 |
| Instruksi tidak boleh hanya mengandalkan ciri sensorik; warna tidak boleh menjadi satu-satunya sarana informasi | N | Tambahkan kata, bentuk, atau pola bermakna | Semua desain harus hitam-putih |
| Animasi dari interaksi dapat menyebabkan gangguan atau mual pada sebagian orang; WCAG 2.3.3 berada di tingkat AAA | N | Bila memungkinkan, sediakan cara menonaktifkan animasi tidak esensial; hormati pengaturan gerak | Semua animasi berbahaya atau kriteria AAA otomatis wajib untuk AA |
| Studi 4.598 peserta di 30 negara menemukan asosiasi warna–emosi lintas budaya **beserta perbedaan lokal** | P | Warna dipilih sesuai semantik, budaya, identitas, dan uji pengguna | Merah/biru tertentu terbukti menyebabkan emosi atau terapi |
| Eksperimen kesan pertama website menghubungkan kompleksitas dan prototipikalitas visual dengan penilaian estetika | P | Susunan lazim dan beban visual patut diuji untuk jenis situs tertentu | Satu jumlah elemen atau gaya minimalis selalu paling baik |
| Konsensus ahli mengenai cahaya dalam ruang mengaitkan pola paparan siang/malam dengan fisiologi, tidur, dan kewaspadaan dewasa sehat | S/konsensus | Pertimbangkan pencahayaan ruangan, silau, dan waktu pakai jika merancang ruang | Warna UI atau mode gelap saja mengobati insomnia |

Rujukan langsung: [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [W3C kontras teks](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html), [kontras nonteks](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html), [karakteristik sensorik](https://www.w3.org/WAI/WCAG22/Understanding/sensory-characteristics.html), [warna](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html), [animasi interaksi](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html), [Jonauskaite dkk., 2020](https://pubmed.ncbi.nlm.nih.gov/32900287/), [Tuch dkk., 2012](https://research.google/pubs/the-role-of-visual-complexity-and-prototypicality-regarding-first-impression-of-websites-working-towards-understanding-aesthetic-judgments/), dan [Brown dkk., 2022](https://pubmed.ncbi.nlm.nih.gov/35298459/).

## 3. Spesifikasi untuk website/aplikasi

### 3.1 Keterbacaan dan hierarki

- Nyatakan satu tujuan utama per layar, judul yang menjelaskan isi, urutan bacaan yang masuk akal, label dekat kendalinya, serta pesan galat yang memberi jalan memperbaiki. Ini hipotesis desain yang ditopang pola [W3C COGA](https://www.w3.org/TR/coga-usable/); uji pada tugas asli.
- Periksa kontras teks **pada warna akhir yang dirender**, termasuk placeholder yang diperlukan, teks di atas foto/gradien, teks saat tombol dinonaktifkan bila informasi penting ada di situ, dan mode terang/gelap. Ikuti pengecualian WCAG secara tepat.
- Sediakan pembesaran teks dan tata letak yang menyesuaikan tanpa kehilangan konten/fungsi sesuai [kriteria reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html). Jangan mengunci ukuran huruf atau mencegah zoom.
- Warna dapat memberi redundansi: “Gagal” + ikon + teks penjelasan lebih jelas daripada titik merah sendiri. Instruksi seperti “klik tombol hijau di kanan” harus dapat diidentifikasi tanpa warna/posisi.

### 3.2 Gerak, kedipan, dan video

- Hindari kilatan. Periksa [WCAG 2.3.1 tentang tiga kilatan atau ambang batas](https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html); jangan memakai angka “maksimal tiga” sebagai izin umum tanpa memahami ambang luminansi/luas. Gerak yang tidak berkedip pun dapat menimbulkan mual pada sebagian orang.
- Gerak esensial dibuat singkat, dapat diprediksi, dan tidak menghalangi pembacaan; untuk gerak dekoratif berikan versi statis. Hormati `prefers-reduced-motion` serta kontrol di produk bila masuk akal. Ini pendekatan desain lebih luas daripada ambang minimal WCAG AA.
- Konten bergerak otomatis yang memenuhi kondisi [WCAG 2.2.2](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html) memerlukan jeda, berhenti, atau sembunyi sesuai kriterianya. Jangan memakai efek parallax atau zoom paksa sebagai cara utama bernavigasi.
- Pada AR/VR, evaluasi risiko mual/pusing secara terpisah. [Tinjauan VR 2025](https://pubmed.ncbi.nlm.nih.gov/40267853/) membahas efek yang bervariasi pada perangkat imersif; jangan mengekstrapolasi angka insidennya langsung ke halaman web biasa.

### 3.3 Pilihan tampilan

- Mode gelap/terang adalah preferensi tampilan, bukan terapi. Pertahankan kontras, ikon/status, grafik, foto, dan formulir pada kedua mode.
- Sediakan alternatif teks untuk gambar bermakna dan teks nyata untuk label penting. Skema warna tidak boleh menyembunyikan informasi ketika perangkat memakai mode kontras tinggi.
- Rancang untuk berbagai ukuran layar, kondisi cahaya, dan ketajaman penglihatan. Asumsi tentang “warna tenang” diperlakukan sebagai hipotesis dan dinilai bersama kelompok target.

## 4. Bila proyek mencakup ruang fisik

- Evaluasi silau, bayangan, distribusi dan kendali pencahayaan untuk aktivitas yang benar-benar dilakukan; pencahayaan saat membaca berbeda dari saat beristirahat.
- Tinjauan konsensus [Brown dkk.](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3001571) membahas paparan terang di siang hari dan gelap di malam hari pada dewasa sehat. Rekomendasi fisik spesifik memerlukan ahli pencahayaan, pengukuran di lokasi, dan konteks usia/jam kerja. Jangan menerjemahkan melanopic illuminance ke hex warna CSS.

## 5. Protokol pengujian

1. Audit setiap halaman dan status UI untuk WCAG 2.2 yang relevan; sertakan keyboard, pembaca layar, zoom, dan gerak berkurang. Audit otomatis tidak cukup.
2. Jalankan tugas “temukan, pahami, selesaikan” pada ponsel dan desktop dengan orang dari profil visual/kognitif berbeda; kumpulkan keberhasilan, kesalahan, waktu, dan kenyamanan 0–10.
3. Bandingkan dua susunan atau palet dengan isi dan fungsi yang sama. Tanya alasan pilihan, jangan hanya “mana lebih cantik”.
4. Catat pusing/mual, kesulitan membaca, dan berapa orang memilih mematikan gerak. Jika peserta menghentikan sesi, prioritaskan perbaikan.
5. Jika ruang fisik, dokumentasikan pencahayaan pada waktu dan posisi nyata, termasuk silau yang dilaporkan; jangan bergantung pada foto promosi.

## 6. Kesalahan interpretasi yang harus dihindari

- “Biru menenangkan semua orang” mengubah temuan asosiasi menjadi sebab akibat tanpa uji.
- “Warna hangat pasti lebih nyaman” mengabaikan kebutuhan kontras, konteks, budaya, dan kemampuan visual.
- “Lolos WCAG = nyaman untuk semua” mengabaikan pengujian penggunaan nyata.
- “Mode gelap selalu sehat untuk mata” melampaui bukti dan tidak membahas fungsi atau preferensi.

## Daftar sumber kunci

1. W3C, [WCAG 2.2](https://www.w3.org/TR/WCAG22/) dan [panduan evaluasi](https://www.w3.org/WAI/test-evaluate/).
2. W3C, [Understanding Contrast Minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html); [Non-text Contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html); [Animation from Interactions](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html); [Three Flashes](https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html).
3. Jonauskaite dkk. (2020), [asosiasi warna–emosi lintas 30 negara](https://pubmed.ncbi.nlm.nih.gov/32900287/) — survei asosiasi, bukan uji intervensi suasana hati.
4. Tuch dkk. (2012), [kompleksitas dan prototipikalitas website](https://research.google/pubs/the-role-of-visual-complexity-and-prototypicality-regarding-first-impression-of-websites-working-towards-understanding-aesthetic-judgments/) — studi kesan pertama, bukan resep semua situs.
5. Brown dkk. (2022), [konsensus pola cahaya dalam ruang](https://pubmed.ncbi.nlm.nih.gov/35298459/) — dewasa sehat dan pencahayaan fisik.
6. W3C, [COGA](https://www.w3.org/TR/coga-usable/) — panduan tambahan, bukan kriteria konformansi WCAG.

## Lampiran pendalaman: penilaian tiga jenis bukti

**Asosiasi warna–emosi.** [Jonauskaite dkk.](https://pubmed.ncbi.nlm.nih.gov/32900287/) meminta peserta memilih asosiasi antara istilah warna dan emosi. Besar sampel lintas negara berguna untuk mengetahui pola asosiasi dan variasi budaya. Namun “orang mengasosiasikan biru dengan X” berbeda dari “mengganti tombol menjadi biru menyebabkan X”. Pada website, warna diapit merek, konten, luminositas, kontras, bahasa, dan pengalaman sebelumnya. Jika ingin menguji efek mood, ukur mood sebelum dan sesudah dengan pembanding yang menjaga aspek visual lain setara; bila hanya menguji kesukaan, jangan menyebut mood atau terapi.

**Kesan pertama vs penggunaan lama.** [Tuch dkk.](https://research.google/pubs/the-role-of-visual-complexity-and-prototypicality-regarding-first-impression-of-websites-working-towards-understanding-aesthetic-judgments/) meneliti penilaian estetika awal. Dalam produk nyata, pengguna juga perlu membaca, menavigasi, menunggu, dan menyelesaikan galat. Maka pengujian sebaiknya mencakup kesan awal **dan** tugas yang cukup lama; tampilan yang disukai saat sekilas bisa menimbulkan kesulitan saat dibaca berulang.

**Fisik vs layar.** [Brown dkk.](https://pubmed.ncbi.nlm.nih.gov/35298459/) memberikan rekomendasi pencahayaan dalam ruang bagi dewasa sehat, menggunakan ukuran paparan cahaya yang tidak setara dengan warna piksel. Klaim bahwa CSS tertentu mengatur ritme biologis seseorang memerlukan informasi luminansi layar, jarak, durasi, pencahayaan sekeliling, waktu, dan subjek. Karena itu, untuk website cukup rancang tampilan yang dapat dibaca dan dikendalikan; untuk ruang lakukan penilaian pencahayaan yang benar.


## Integrasi operasional Website Builder — revisi 24 September 2026

### Dari kesan visual ke keputusan halaman

Pisahkan estetika awal, keterbacaan, pemahaman, penyelesaian tugas, dan kenyamanan penggunaan lama. Satu studi screenshot tidak membuktikan semua hasil tersebut. Tentukan terlebih dahulu apakah masalahnya kepadatan, label, kontras, gerak, atau isi; jangan mengubah semuanya bersamaan lalu menisbatkan hasil ke warna.

[Jonauskaite dkk.](https://journals.sagepub.com/doi/10.1177/0956797620948810) mengukur asosiasi istilah warna dan emosi; ia bukan uji bahwa palet tertentu menyebabkan suasana hati. Penerapan pada website adalah hipotesis desain: pilih warna sesuai merek dan semantik, periksa kontras, lalu uji pemahaman serta preferensi pada audiens. Budaya dan konteks tidak boleh direduksi menjadi stereotip warna untuk satu negara.

**Spesifikasi nyata:** tetapkan pasangan warna teks/latar per keadaan, gaya fokus, lebar kolom membaca, hierarki judul, perlakuan gambar, dan versi tanpa gerak. Saat warna merek gagal kontras, cari pasangan permukaan/teks yang memenuhi kebutuhan sambil mempertahankan identitas. Jangan memaksa teks kecil di atas foto yang berubah-ubah.

**Kasus uji:** peserta menemukan harga, memahami status ketersediaan, dan mencapai tindakan utama pada ponsel; ulangi dengan pembesaran dan gerak berkurang. Catat kesalahan memahami ikon/warna, bukan hanya skor suka. Untuk foto produk, periksa kesesuaian crop dan informasi yang hilang.

**Catatan pengukuran kontras:** gunakan warna foreground/background komputasi yang benar termasuk komposit transparansi; antialiasing screenshot bukan dasar tunggal rumus kontras. Efek latar variabel perlu kondisi terburuk yang relevan. Rujukan: [W3C Contrast Minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).
