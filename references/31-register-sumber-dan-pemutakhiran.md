# Register sumber, mutu bukti, dan batas pemutakhiran

> Tanggal penelusuran: 24 September 2026. Metode: kajian naratif terarah untuk integrasi Website Builder. Ini bukan tinjauan sistematis, meta-analisis baru, atau audit seluruh literatur. Tanggal ini menyatakan waktu pemeriksaan, bukan tanggal terbit sumber.

## Ruang lingkup dan cara membaca

Bahan awal mencakup 25 bidang website, satu indeks, dan enam berkas psikologi milik project. Semua dibaca dan diperbarui dengan penerapan, skenario gagal, serta bukti penerimaan. Enam modul integrasi baru menutup kebutuhan arsitektur modern, arah artistik, protokol sensori, gerbang mutu, alur AI, dan keterlacakan sumber.

Sumber dipilih untuk menjawab ketidakpastian konkret: kriteria aksesibilitas dan levelnya; ambang performa; otorisasi dan konsistensi; batas kemampuan browser; keterterapan studi warna, aroma, musik, dan haptik. Prioritas diberikan kepada badan standar, dokumentasi pemilik teknologi, publikasi peneliti/penerbit, serta sumber resmi hukum. Hasil pencarian umum yang tidak relevan tidak dijadikan dasar.

Kode: **N** standar normatif; **G** panduan resmi/praktik; **P** studi primer; **S** tinjauan/sintesis; **H** hipotesis atau rancangan operasional. Kode adalah jenis bukti, bukan skor kepastian. Nilai juga risiko bias, populasi, konteks, dan kesesuaian terhadap website.

## Standar dan kemampuan web

| Sumber | Jenis dan akses | Klaim/pemakaian yang ditopang | Batas |
| --- | --- | --- | --- |
| [WCAG 2.2](https://www.w3.org/TR/WCAG22/) | N; standar resmi teridentifikasi | Sasaran kriteria A/AA dan lingkup konformansi | Checklist ringkas bukan konformansi penuh |
| [Contrast Minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) | G yang menjelaskan kriteria N; isi dibaca | Rasio teks, pengecualian, definisi teks besar | Tidak membuktikan semua pengguna nyaman |
| [Target Size Minimum](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) | G/N; isi hasil pencarian resmi | 24 × 24 CSS px dan pengecualian spacing | Bukan jarak 24 px di semua sisi |
| [Target Size Enhanced](https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced.html) | G/N; isi hasil pencarian resmi | 44 × 44 CSS px pada AAA | Jangan disebut syarat AA universal |
| [Focus Not Obscured](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html) | G/N; halaman resmi dibuka | Fokus tidak sepenuhnya tertutup menurut SC 2.4.11 | Periksa kondisi dan pengecualian saat audit |
| [Accessible Authentication](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html) | G/N; halaman resmi dibuka | Persyaratan SC 3.3.8 dan mekanisme bantuan | Bukan larangan semua bentuk autentikasi |
| [Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) | G/N; halaman resmi dibuka | Penyesuaian konten pada dimensi rujukan | Ada pengecualian bagian dua dimensi |
| [Audio Control](https://www.w3.org/WAI/WCAG22/Understanding/audio-control.html) | G/N; halaman resmi dibuka | Kontrol audio otomatis yang memenuhi kondisi kriteria | Default senyap skill adalah keputusan desain yang lebih luas |
| [Captions Prerecorded](https://www.w3.org/WAI/WCAG22/Understanding/captions-prerecorded.html) | G/N; halaman resmi dibuka | Padanan tersinkron untuk audio bermakna | Tidak semua kebutuhan media selesai dengan transkrip |
| [W3C COGA](https://www.w3.org/TR/coga-usable/) | G; isi bagian relevan dibaca | Pola untuk kebutuhan kognitif dan jalur tugas | Bukan syarat konformansi WCAG |
| [HTML Living Standard](https://html.spec.whatwg.org/multipage/) | N; dokumen resmi dibuka | Struktur dan perilaku elemen/form | Uji integrasi browser tetap diperlukan |
| [APG Modal Dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/) | G; isi keyboard dibaca | Fokus masuk, urutan tab, penutupan dialog | Contoh pola tidak menjamin implementasi benar |
| [MDN Reduced Motion](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion) | G; halaman resmi dibuka | Membaca preferensi gerak pengguna | Harus diperiksa pada efek CSS dan JS |
| [MDN Vibration API](https://developer.mozilla.org/en-US/docs/Web/API/Vibration_API) | G; dukungan dan kemampuan dibaca | Getaran bergantung hardware dan dukungan terbatas | Bukan haptik universal atau reproduksi tekstur |
| [W3C Language](https://www.w3.org/International/questions/qa-html-language-declarations) | G; halaman resmi dibuka | Deklarasi bahasa HTML | Locale mencakup lebih dari atribut bahasa |
| [WAI alt decision tree](https://www.w3.org/WAI/tutorials/images/decision-tree/) | G; halaman resmi dibuka | Alt sesuai peran gambar | Mutu deskripsi tetap memerlukan penilaian konteks |

## Implementasi, data, operasi, dan konten

| Sumber | Jenis dan akses | Pemakaian | Batas |
| --- | --- | --- | --- |
| [Web Vitals](https://web.dev/articles/vitals) | G; ambang dan persentil dibaca | LCP/INP/CLS, p75, mobile/desktop | Pengukuran lab tidak menggantikan lapangan |
| [OWASP ASVS](https://github.com/OWASP/ASVS) | Standar verifikasi proyek; versi 5.0.0 teridentifikasi | Persyaratan keamanan dengan versi/ID | Pemakaian sebagian bukan klaim konformansi |
| [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) | G; bagian every request dibaca | Izin setiap objek/tindakan dan deny by default | Desain tepat bergantung model ancaman |
| [OWASP Third Party JavaScript](https://cheatsheetseries.owasp.org/cheatsheets/Third_Party_Javascript_Management_Cheat_Sheet.html) | G; risiko dibaca | Kode pihak ketiga, perubahan, kebocoran data | Mitigasi harus sesuai arsitektur |
| [PostgreSQL Transaction Isolation](https://www.postgresql.org/docs/current/transaction-iso.html) | G/spesifikasi implementasi; bagian isolasi dibaca | Snapshot, update bersamaan, retry konflik | URL current bergerak; cek versi database aktual |
| [RFC 9110](https://httpwg.org/specs/rfc9110.html) | N; dokumen resmi dibuka | Semantik metode dan hasil HTTP | Idempotensi bisnis tetap harus dirancang |
| [RFC 9457](https://www.rfc-editor.org/info/rfc9457/) | N; dokumen resmi dibuka | Problem details untuk galat API | Bukan izin membocorkan detail internal |
| [Playwright Best Practices](https://playwright.dev/docs/best-practices) | G; bagian perilaku pengguna dibaca | Tes perilaku dan isolasi | Otomasi bukan uji manusia |
| [Google Search Essentials](https://developers.google.com/search/docs/essentials) | G; halaman resmi dibuka | Kelayakan dan praktik konten pencarian | Tidak menjamin indeks atau ranking |
| [Learn Images](https://web.dev/learn/images) | G; halaman resmi dibuka | Format, responsivitas, pemuatan | Hak aset dan ketepatan foto diperiksa terpisah |
| [W3C Privacy Principles](https://www.w3.org/TR/privacy-principles/) | G; dokumen resmi dibuka | Minimisasi dan rancangan privasi | Bukan pengganti hukum setempat |
| [UU 27/2022, BPK](https://peraturan.bpk.go.id/Details/229798/uu-no-27-tahun-2022) | Hukum resmi; halaman metadata/ringkasan dibaca | Titik awal pemetaan kewajiban Indonesia | Bukan penelaahan semua aturan pelaksana/sektor pada tanggal ini |
| [GOV.UK Discovery](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works) | G; halaman resmi dibuka | Masalah, batas, kebutuhan sebelum solusi | Proses disesuaikan ukuran proyek |
| [GOV.UK Usability Testing](https://www.gov.uk/service-manual/user-research/using-moderated-usability-testing) | G; desain tugas dibaca | Tugas netral, peserta relevan, observasi | Tidak menetapkan sampel universal |
| [Google SRE Monitoring](https://sre.google/sre-book/monitoring-distributed-systems/) | G; bagian sinyal dibaca | Latensi, trafik, galat, saturasi | Target SLO mengikuti layanan |
| [Let's Encrypt](https://letsencrypt.org/how-it-works/) | G; halaman resmi dibuka | Validasi domain dan sertifikat | TLS bukan keamanan aplikasi menyeluruh |
| [Pro Git](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository) | G; halaman resmi dibuka | Pencatatan perubahan secara terarah | Tidak menggantikan backup database |
| [React Effects](https://react.dev/learn/you-might-not-need-an-effect) | G; bagian sinkronisasi dibaca | Menghindari state/Effect yang tidak diperlukan | Berlaku untuk model React |
| [TypeScript Narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html) | G; discriminated union dibaca | Kontrak tipe dan keadaan | Tidak memvalidasi data runtime |
| [Next.js Server/Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components) | G; batas data/rahasia dibaca | Penempatan tugas klien–server | Periksa versi; bukan aturan semua framework |

## Penelitian psikologi yang menopang integrasi

| Sumber | Rancangan/akses | Hasil yang digunakan | Inferensi yang tidak dibenarkan |
| --- | --- | --- | --- |
| [Tuch dkk., 2012](https://research.google/pubs/the-role-of-visual-complexity-and-prototypicality-regarding-first-impression-of-websites-working-towards-understanding-aesthetic-judgments/) | P; abstrak penulis dibaca; dua studi screenshot | Kompleksitas/prototipikalitas terkait penilaian estetika awal dalam eksperimen | Semua situs harus minimalis; peningkatan penjualan tertentu |
| [Jonauskaite dkk., 2020](https://journals.sagepub.com/doi/10.1177/0956797620948810) | P; abstrak penerbit dibaca; asosiasi 4.598 peserta, 30 negara | Pola bersama beserta variasi bahasa/geografi | Palet tertentu menyebabkan emosi yang sama pada semua orang |
| [Herz & von Clef, 2001](https://pubmed.ncbi.nlm.nih.gov/11374206/) | P; abstrak dibaca; label berubah pada bau yang dicium | Konteks verbal memengaruhi penilaian bau dalam kondisi eksperimen | Teks website memancarkan aroma atau memberi terapi |
| [Ernst & Banks, 2002](https://www.nature.com/articles/415429a) | P; abstrak penerbit dibaca; tugas visual–haptik | Penggabungan isyarat sejalan model estimasi dalam tugas tersebut | Semua tambahan modalitas atau getaran memperbaiki UX |
| [de Witte dkk., 2020](https://research.ou.nl/en/publications/effects-of-music-interventions-on-stress-related-outcomes-a-syste/) | S; metadata institusi dan ringkasan pencarian; teks penuh penerbit terhalang | Kajian intervensi musik merupakan konteks yang berbeda dari audio wajib website | Ukuran efek pada materi lama telah diaudit ulang atau autoplay mengurangi stres |

Materi psikologi lama juga memuat Spence, Fondberg, Murray, Brown, Chen, Crane, Hummel, studi termal, dan panduan WHO/EPA. Materi itu dipertahankan dengan batas aslinya; putaran ini tidak mengaudit ulang seluruh naskah kesehatan/ruang fisik. Beberapa halaman PubMed hanya menampilkan halaman kosong dan PMC menampilkan tantangan akses. Angka efek dan rincian metode yang tidak terbaca tidak ditambah atau diklaim baru diverifikasi. Gunakan bagian website yang diperbarui; periksa kembali sumber fisik sebelum menjadikannya dasar intervensi baru.

## Jejak pencarian dan pengecualian

Kueri utama mencakup “WCAG22 target size minimum 24”, “Web Vitals LCP INP CLS thresholds”, “OWASP ASVS 5.0”, judul studi Tuch dan Jonauskaite, judul kajian musik de Witte, serta label verbal dan persepsi bau. Pencarian ditindaklanjuti ke halaman asli yang relevan. Hasil tidak terkait, artikel pemasaran dengan ambang salah, dan ringkasan tanpa sumber tidak digunakan sebagai dasar baru.

Akses halaman bukan audit penuh metodologi. Pada register ini, “halaman dibuka” dibedakan dari “bagian dibaca” dan “abstrak dibaca”. Klaim spesifik yang memerlukan pasal, nomor kontrol, rincian metode, atau API tambahan harus diverifikasi lagi ketika dipakai. Riset skill tidak menjamin bahwa website yang dibangun kemudian sudah memenuhi standar tanpa pengujian implementasinya.

## Protokol pembaruan selanjutnya

Catat pertanyaan, alasan sumber dipilih, URL/DOI, tanggal akses, versi, bagian yang mendukung klaim, cakupan, dan batas. Cari bukti yang dapat menolak hipotesis awal. Ubah keputusan hanya jika relevan; jangan mengganti penelitian lama dengan artikel baru yang lebih lemah.

Periksa ulang API/dukungan browser, versi framework, keamanan, kebijakan pencarian, harga, hukum, dan kemampuan host ketika keputusan implementasi dibuat. Simpan pembaruan dalam berkas domain yang tepat dan pertahankan tautan dari SKILL.md. Jika suatu referensi tidak diperlukan untuk tugas, tidak perlu dimuat seluruhnya.
