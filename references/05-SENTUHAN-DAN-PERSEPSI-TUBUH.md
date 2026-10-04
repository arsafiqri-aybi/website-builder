# Sentuhan dan persepsi tubuh: tekstur, haptik, suhu, dan gerak

**Versi:** 24 September 2026 · **Cakupan:** permukaan dan ruang fisik, interaksi perangkat, serta batas pengalaman tubuh di web. Kode bukti N/G/S/P/H berada di `00-KONSEP-DAN-METODE.md`.

## 1. Sistem yang perlu dibedakan

- **Taktil diskriminatif:** membantu mengenali tekanan, bentuk, tekstur, dan posisi kontak. Berguna untuk pegangan dan tombol fisik.
- **Sentuhan afektif:** pengalaman emosional saat disentuh; [Schirmer, Croy & Ackerley (2023)](https://pubmed.ncbi.nlm.nih.gov/37196923/) mengingatkan bahwa hubungan saraf C-tactile dengan rasa menyenangkan tidak satu-banding-satu. Sentuhan lembut pun tidak harus menyenangkan.
- **Termal:** panas/dingin dari permukaan atau udara. Tinjauan [Wang dkk. (2018)](https://researchportal.hkust.edu.hk/en/publications/individual-difference-in-thermal-comfort-a-literature-review/) serta [Schweiker dkk. (2018)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6298492/) menunjukkan variasi persepsi suhu antarorang dan kondisi.
- **Propriosepsi dan vestibular:** posisi serta gerak tubuh; penting untuk produk yang dipakai, kursi, alat, dan pengalaman bergerak/VR. Isyarat visual yang bergerak dapat memicu keluhan vestibular pada sebagian orang [W3C Animation from Interactions](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html).
- **Interosepsi:** penafsiran sinyal tubuh seperti napas, rasa penuh, atau ketegangan; [Chen dkk. (2021)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7780231/) menguraikan proses yang lebih luas daripada lima indera klasik.

Istilah “nyaman di kulit”, “enak digenggam”, “suhu ruang nyaman”, dan “getaran cukup jelas” merujuk hasil yang berbeda. Jangan mereduksinya ke satu angka atau bahan.

## 2. Temuan dan batas

| Temuan | Jenis | Implikasi yang sah | Batas |
| --- | --- | --- | --- |
| Tinjauan C-tactile menyimpulkan serabut tersebut mendukung sentuhan lembut afektif, tetapi tidak semua pengalaman afektif bergantung padanya atau menyenangkan | S | Jangan mengasumsikan sentuhan manusia menenangkan; minta persetujuan | Rekomendasi terapi sentuhan untuk semua orang |
| Tinjauan kenyamanan termal menunjukkan perbedaan preferensi dan banyak faktor individual | S | Beri kendali setempat atau pilihan lokasi/bahan saat layak | Satu suhu ideal atau “nilai biologis universal” |
| Model kenyamanan termal personal dapat menangkap kebutuhan tertentu lebih baik daripada model populasi dalam studi yang ditinjau | S | Uji pilihan penyesuaian; lindungi data preferensi bila dikumpulkan | Sistem personalisasi otomatis terbukti bekerja untuk semua gedung |
| WCAG 2.5.8 AA menetapkan ukuran target minimum 24 × 24 CSS pixel atau pengecualian jarak dan jenis target tertentu | N | Audit kontrol kecil pada layar sentuh, juga akses keyboard | 24 × 24 adalah ukuran fisik tombol atau selalu paling nyaman |
| Informasi/kendali web harus tetap tersedia ketika satu kanal sensori tidak tersedia | N | Getaran hanya penunjang, bukan satu-satunya notifikasi | Semua pengguna dapat merasakan atau menyalakan haptik |
| Studi VR melaporkan variasi mual, disorientasi, dan gangguan okulomotor dalam setting imersif | S | Uji perangkat dan gerak khusus konteks | Persentasenya berlaku pada web 2D biasa |

Sumber: [Schirmer dkk., 2023](https://pubmed.ncbi.nlm.nih.gov/37196923/), [Wang dkk., 2018](https://researchportal.hkust.edu.hk/en/publications/individual-difference-in-thermal-comfort-a-literature-review/), [Schweiker dkk., 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC6298492/), [Martins dkk., 2022](https://www.sciencedirect.com/science/article/abs/pii/S0360132321008970), [W3C Target Size](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html), [W3C Sensory Characteristics](https://www.w3.org/WAI/WCAG22/Understanding/sensory-characteristics.html), dan [Cossio dkk., 2025](https://pubmed.ncbi.nlm.nih.gov/40267853/).

## 3. Panduan produk fisik

### 3.1 Permukaan, pegangan, dan pakaian/perangkat yang dikenakan

- Spesifikasikan kegunaan: dipegang lama atau sebentar, tangan basah/kering, kulit sensitif, kekuatan genggam, suhu lingkungan, kemudahan membersihkan. Jangan memutuskan bahan hanya dari foto.
- Prototipe beberapa pilihan tekstur, tekanan, bentuk, dan bobot; ukur keberhasilan tindakan, kesalahan, slip, rasa panas/dingin, ketidaknyamanan, serta kemudahan melepas. Ini prosedur desain H yang perlu diuji.
- Hindari tepi tajam, suhu permukaan yang dapat melukai, tekanan terus-menerus tanpa jalan melepaskan, dan bahan yang tidak sesuai penggunaan. Penilaian keamanan material/produk spesifik memerlukan standar serta ahli terkait.
- Jika menyentuh orang, sebut tindakan, minta persetujuan yang dapat ditarik, dan berikan layanan alternatif. Respons afektif terhadap kontak tidak dapat ditebak dari niat pemberi sentuhan.

### 3.2 Ruang dan suhu

- Perhatikan temperatur udara, radiasi permukaan, aliran udara, pakaian, aktivitas, posisi, dan lamanya tinggal; angka termostat sendirian tidak menjelaskan pengalaman.
- Jika memungkinkan, sediakan penyesuaian yang nyata: pilihan duduk, bayangan/naungan, lapisan pakaian, kendali lokal. Untuk sistem HVAC besar, evaluasi profesional diperlukan.
- Jangan menyimpulkan bahwa semua perempuan, orang tua, atau kelompok tertentu pasti memiliki satu suhu ideal. Tinjauan menunjukkan variasi antarkelompok **dan** dalam kelompok.

## 4. Panduan aplikasi/website

- Di browser biasa, “sentuhan” adalah menekan layar/mouse/keyboard. Website tidak mengendalikan tekstur atau suhu layar pengguna. Haptik hanya tersedia melalui perangkat/API tertentu, sehingga harus dianggap peningkatan opsional.
- Pastikan target dapat diaktifkan tanpa presisi ekstrem. Terapkan [WCAG 2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) secara lengkap, termasuk aturan jarak dan pengecualiannya; buat area klik lebih lapang jika hasil uji menunjukkan kebutuhan.
- Hindari interaksi yang hanya bergantung pada gestur rumit atau gerak perangkat. Berikan alternatif tombol atau metode masukan yang didukung kriteria WCAG terkait [Pointer Gestures](https://www.w3.org/WAI/WCAG22/Understanding/pointer-gestures.html) dan [Motion Actuation](https://www.w3.org/WAI/WCAG22/Understanding/motion-actuation.html).
- Getaran notifikasi dapat dimatikan dan didampingi teks/status visual yang jelas; bunyi juga dapat dimatikan sesuai `02-PENDENGARAN.md`. Jangan mengartikan tidak adanya respons haptik sebagai keputusan pengguna.
- Efek parallax/gerak besar dibahas pula pada `01-PENGLIHATAN.md`, sebab sumbernya visual tetapi keluhannya bisa berupa mual/pusing tubuh.

## 5. Metode pengujian

1. **Pisahkan tujuan:** pegangan yang aman, tekstur disukai, suhu nyaman, ketepatan target, dan tingkat gangguan haptik adalah variabel berbeda.
2. **Buat kondisi pembanding:** bahan A/B, getaran mati/aktif bila didukung, area target normal/diperbesar, suhu dan aktivitas tercatat. Variasikan urutan bila masuk akal.
3. **Ukur kinerja dan pengalaman:** tugas berhasil, salah tekan, jatuh/slip, waktu, kenyamanan 0–10, keinginan menyesuaikan, serta keluhan nyeri/mual/iritasi. Catat perangkat dan kondisi ruangan.
4. **Rekrut variasi:** orang dengan kemampuan motorik dan sensorik berbeda, pengguna teknologi bantu, usia dan kebiasaan yang sesuai sasaran; jangan meminta kondisi medis rinci bila tidak diperlukan.
5. **Persetujuan dan stop rule:** peserta dapat menarik tangan, menghentikan getaran, atau meninggalkan ruang; hentikan bila ada nyeri, pusing, atau rasa tidak aman.
6. **Laporkan perbedaan individu:** jangan menyembunyikan kelompok yang sangat tidak nyaman di balik rata-rata tinggi. Keputusan akhir mempertimbangkan alternatif yang setara.

## 6. Antiklaim

- “Bahan lembut pasti menyenangkan semua orang” tidak mengikuti dari riset sentuhan afektif.
- “Suhu X optimal untuk semua tubuh” mengabaikan perbedaan konteks dan individu.
- “Haptik membuat semua pengguna lebih mudah memahami” hanya hipotesis sebelum pengujian perangkat dan kebutuhan akses.
- “Getaran yang terasa di perangkat perancang pasti terasa bagi pengguna” mengabaikan kemampuan sensorik, pengaturan OS, dan dukungan perangkat.

## Daftar sumber kunci

1. Schirmer, Croy & Ackerley (2023), [C-tactile afferents and affective touch](https://pubmed.ncbi.nlm.nih.gov/37196923/) — tinjauan yang menolak penyamaan semua sentuhan dengan rasa nyaman.
2. Wang dkk. (2018), [Individual difference in thermal comfort](https://researchportal.hkust.edu.hk/en/publications/individual-difference-in-thermal-comfort-a-literature-review/) — tinjauan variasi.
3. Schweiker dkk. (2018), [Drivers of diversity in human thermal perception](https://pmc.ncbi.nlm.nih.gov/articles/PMC6298492/) — model kenyamanan lebih holistik.
4. Martins dkk. (2022), [A systematic review of personal thermal comfort models](https://www.sciencedirect.com/science/article/abs/pii/S0360132321008970) — potensi dan batas model personal.
5. Chen dkk. (2021), [The Emerging Science of Interoception](https://pmc.ncbi.nlm.nih.gov/articles/PMC7780231/) — persepsi keadaan internal.
6. W3C, [Target Size Minimum](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html); [Motion Actuation](https://www.w3.org/WAI/WCAG22/Understanding/motion-actuation.html) — kriteria interaksi digital.
7. Cossio dkk. (2025), [systematic review cybersickness in immersive VR](https://pubmed.ncbi.nlm.nih.gov/40267853/) — tidak digeneralisasi ke web biasa.

## Lampiran pendalaman: variasi dan kendali tubuh

**Sentuhan afektif tidak menjamin persetujuan.** Tinjauan [Schirmer dkk.](https://pubmed.ncbi.nlm.nih.gov/37196923/) menyatakan CT mendukung sebagian pengalaman sentuhan lembut, namun tidak setiap pengalaman afektif melibatkan CT dan sentuhan semacam itu tidak mesti menyenangkan. Ini membatasi klaim tentang efek sosial atau terapi dari tekstur/tekanan. Desain interaksi manusia harus selalu berangkat dari persetujuan yang dapat ditarik.

**Suhu ialah pengalaman, bukan sekadar angka.** [Wang dkk.](https://researchportal.hkust.edu.hk/en/publications/individual-difference-in-thermal-comfort-a-literature-review/) merangkum perbedaan preferensi dan pengaruh faktor individu. [Martins dkk.](https://www.sciencedirect.com/science/article/abs/pii/S0360132321008970) meninjau model personal; prediksi yang lebih baik pada suatu set data tetap perlu divalidasi dalam gedung, iklim, dan penghuni baru. Simpan data preferensi hanya bila diperlukan untuk fungsi dan jelaskan penggunaannya.

**Target sentuh bukan haptik.** [WCAG 2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) menangani ukuran/ruang target yang dapat diaktifkan pada antarmuka, sedangkan getaran ialah umpan balik perangkat. Memperbesar tombol dapat mengurangi salah tekan tanpa getaran; menambah getaran tidak memperbaiki tombol yang terlalu kecil. Uji keduanya sebagai variabel terpisah.

**Contoh kegagalan:** prototipe kursi bertekstur tampak premium saat disentuh lima detik, namun panas dan menekan setelah tiga puluh menit. Uji sesuai lama duduk sebenarnya, pakaian, suhu ruangan, kemampuan bangun, dan kemudahan membersihkan. Jangan menggeneralisasi hasil kursi itu ke tekstur pakaian atau antarmuka digital.


## Integrasi operasional Website Builder — revisi 24 September 2026

### Sentuh, umpan balik, dan kemampuan perangkat

Pisahkan tiga lapisan: cara pengguna memberi input; umpan balik visual tentang keadaan; getaran fisik bila tersedia. Memperbesar area sentuh dapat membantu tindakan tanpa menambah getaran. Efek bayangan atau tekstur gambar tidak mengubah suhu dan bahan layar.

[MDN Vibration API](https://developer.mozilla.org/en-US/docs/Web/API/Vibration_API) menandai dukungan terbatas. Periksa kemampuan aktual dan sediakan fallback tanpa haptik; pemanggilan API yang diterima tidak membuktikan pengguna merasakan getaran. Jangan menyalakan getaran pada setiap scroll atau sebagai pengganti konfirmasi tekstual. Preferensi haptik sebaiknya eksplisit dan dapat diubah.

[Ernst & Banks (2002)](https://www.nature.com/articles/415429a) meneliti penggabungan isyarat visual dan haptik pada penilaian properti objek. Temuan ini mendukung pembahasan integrasi persepsi dalam tugas tersebut, bukan klaim bahwa semakin banyak efek web semakin optimal. Hipotesis website perlu diukur pada perangkat, pengguna, dan tindakan yang sesuai.

**Pengujian konkret:** tombol kecil dibanding area lebih lapang; tugas dengan haptik aktif/mati/tidak didukung; pengguna hanya keyboard; gestur drag dengan alternatif tombol; klik ganda ketika jaringan lambat. Keberhasilan berasal dari keadaan aplikasi yang sah. Bunyi/getaran sukses tidak muncul sebelum transaksi terkonfirmasi.

Untuk gerak visual besar, prioritaskan versi statis dan kontrol agar pengguna tetap dapat menyelesaikan tugas. Penelitian sentuhan afektif, suhu, dan kursi pada materi dasar tidak boleh dipindahkan menjadi angka radius, warna, atau durasi animasi CSS tanpa bukti penghubung.
