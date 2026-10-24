# -*- coding: utf-8 -*-
import json

levels_data = [
    {
        "id": 1,
        "name": "Level 1 — Penjelajah Demokrasi",
        "shortTitle": "Penjelajah Demokrasi",
        "badgeName": "Penjelajah Demokrasi",
        "badgeImage": "images/badges/badge_1.webp",
        "focus": "Pengertian demokrasi, HAM, dan kebebasan berekspresi",
        "description": "Pengenalan konsep dasar demokrasi, penghormatan hak asasi manusia, dan kebebasan berekspresi secara bertanggung jawab.",
        "difficulty": "Tingkat Dasar",
        "questions": [
            {
                "id": 1,
                "topic": "demokrasi",
                "topicLabel": "Demokrasi & HAM",
                "difficulty": "Mudah",
                "question": "Apa yang ditekankan dalam demokrasi dengan hak asasi manusia?",
                "options": [
                    "Kekuasaan pemerintah tanpa batas",
                    "Penghormatan dan perlindungan HAM",
                    "Pembatasan seluruh pendapat masyarakat",
                    "Kepentingan kelompok mayoritas saja"
                ],
                "correct": 1,
                "explanation": "Demokrasi yang sejati menempatkan penghormatan dan perlindungan hak asasi manusia (HAM) sebagai pilar utama agar tidak terjadi kesewenang-wenangan."
            },
            {
                "id": 2,
                "topic": "ham",
                "topicLabel": "Kebebasan Berekspresi",
                "difficulty": "Mudah",
                "question": "Kebebasan berekspresi berarti warga dapat...",
                "options": [
                    "Menyebarkan fitnah tanpa akibat",
                    "Memaksakan pendapat kepada orang lain",
                    "Menyampaikan pendapat secara bertanggung jawab",
                    "Melanggar privasi orang lain"
                ],
                "correct": 2,
                "explanation": "Kebebasan berekspresi bukan kebebasan mutlak tanpa batas, melainkan kebebasan yang disertai tanggung jawab moral, hukum, dan penghormatan terhadap orang lain."
            },
            {
                "id": 3,
                "topic": "informasi",
                "topicLabel": "Akses Informasi",
                "difficulty": "Mudah",
                "question": "Mengapa akses informasi publik penting dalam demokrasi?",
                "options": [
                    "Agar masyarakat tidak ikut campur",
                    "Agar pemerintah bebas dari pengawasan",
                    "Agar informasi hanya dimiliki pejabat",
                    "Agar warga dapat mengambil keputusan berdasarkan informasi"
                ],
                "correct": 3,
                "explanation": "Keterbukaan informasi publik memungkinkan warga negara berpartisipasi aktif dan membuat keputusan yang tepat berdasarkan fakta terpercaya."
            },
            {
                "id": 4,
                "topic": "privasi",
                "topicLabel": "Privasi Digital",
                "difficulty": "Mudah",
                "question": "Apa yang dimaksud dengan perlindungan privasi digital?",
                "options": [
                    "Melindungi data pribadi dari akses yang tidak sah",
                    "Membagikan seluruh data kepada publik",
                    "Menghapus seluruh informasi pemerintah",
                    "Melarang penggunaan teknologi"
                ],
                "correct": 0,
                "explanation": "Perlindungan privasi digital bertujuan menjaga kerahasiaan data pribadi warga agar tidak disalahgunakan oleh pihak yang tidak berwenang."
            },
            {
                "id": 5,
                "topic": "kesetaraan",
                "topicLabel": "Prinsip Kesetaraan",
                "difficulty": "Mudah",
                "question": "Tindakan diskriminasi bertentangan dengan prinsip...",
                "options": [
                    "Persaingan ekonomi",
                    "Kebebasan berusaha",
                    "Persamaan dan perlindungan HAM",
                    "Pembangunan infrastruktur"
                ],
                "correct": 2,
                "explanation": "Diskriminasi menciderai prinsip persamaan hak dan martabat setiap manusia yang dijamin oleh konstitusi dan deklarasi HAM."
            },
            {
                "id": 6,
                "topic": "ham",
                "topicLabel": "Pendidikan HAM",
                "difficulty": "Mudah",
                "question": "Salah satu cara meningkatkan kesadaran HAM adalah...",
                "options": [
                    "Membatasi pendidikan",
                    "Melaksanakan pendidikan dan advokasi HAM",
                    "Menutup akses informasi",
                    "Mengurangi partisipasi masyarakat"
                ],
                "correct": 1,
                "explanation": "Pendidikan dan advokasi HAM membangun kesadaran kritis serta komitmen masyarakat untuk saling menghormati hak sesama warga."
            },
            {
                "id": 7,
                "topic": "partisipasi",
                "topicLabel": "Partisipasi Publik",
                "difficulty": "Mudah",
                "question": "Partisipasi publik dalam demokrasi dapat dilakukan melalui...",
                "options": [
                    "Pengabaian kebijakan publik",
                    "Penolakan semua keputusan",
                    "Pembatasan kebebasan berpendapat",
                    "Pemilu yang bebas dan adil"
                ],
                "correct": 3,
                "explanation": "Pemilihan umum yang bebas dan jujur adalah instrumen utama partisipasi warga dalam menentukan arah kepemimpinan dan kebijakan publik."
            },
            {
                "id": 8,
                "topic": "teknologi",
                "topicLabel": "Teknologi & HAM",
                "difficulty": "Mudah",
                "question": "Teknologi dalam perlindungan HAM sebaiknya digunakan untuk...",
                "options": [
                    "Mempromosikan dan melindungi hak manusia",
                    "Mengawasi semua orang tanpa batas",
                    "Menyebarkan data pribadi",
                    "Membatasi informasi secara sewenang-wenang"
                ],
                "correct": 0,
                "explanation": "Teknologi harus diarahkan untuk kemaslahatan, edukasi publik, serta perlindungan dan advokasi hak-hak asasi manusia."
            },
            {
                "id": 9,
                "topic": "media",
                "topicLabel": "Kebebasan Media",
                "difficulty": "Mudah",
                "question": "Kebebasan media digital sebaiknya disertai dengan...",
                "options": [
                    "Kebebasan melanggar hukum",
                    "Penghapusan semua kritik",
                    "Tanggung jawab dan penghormatan terhadap hak orang lain",
                    "Larangan berdiskusi"
                ],
                "correct": 2,
                "explanation": "Kebebasan pers dan media digital memerlukan etika jurnalistik, akurasi fakta, serta penghormatan pada martabat orang lain."
            },
            {
                "id": 10,
                "topic": "ham",
                "topicLabel": "Perlindungan Warga",
                "difficulty": "Mudah",
                "question": "Demokrasi yang menghormati HAM memberikan perlindungan kepada...",
                "options": [
                    "Pejabat saja",
                    "Seluruh individu tanpa diskriminasi",
                    "Kelompok mayoritas saja",
                    "Orang yang memiliki kekayaan"
                ],
                "correct": 1,
                "explanation": "Prinsip universal HAM menjamin bahwa setiap individu berhak atas perlindungan yang setara di bawah hukum tanpa pembedaan apa pun."
            }
        ]
    },
    {
        "id": 2,
        "name": "Level 2 — Pelindung Hak Asasi",
        "shortTitle": "Pelindung Hak Asasi",
        "badgeName": "Pelindung Hak Asasi",
        "badgeImage": "images/badges/badge_2.webp",
        "focus": "Akses informasi, privasi, perlindungan HAM, dan partisipasi publik",
        "description": "Fokus pada perlindungan privasi data pribadi, transparansi kebijakan, dan mekanisme penanganan pelanggaran hak asasi.",
        "difficulty": "Tingkat Dasar Lanjutan",
        "questions": [
            {
                "id": 1,
                "topic": "privasi",
                "topicLabel": "Data Pribadi",
                "difficulty": "Mudah",
                "question": "Seseorang menyebarkan data pribadi temannya tanpa izin. Prinsip yang dilanggar adalah...",
                "options": [
                    "Otonomi daerah",
                    "Pembangunan ekonomi",
                    "Perlindungan privasi",
                    "Pemerataan infrastruktur"
                ],
                "correct": 2,
                "explanation": "Menyebarkan data pribadi tanpa izin merupakan pelanggaran serius terhadap hak privasi individu yang dilindungi undang-undang."
            },
            {
                "id": 2,
                "topic": "transparansi",
                "topicLabel": "Transparansi Anggaran",
                "difficulty": "Mudah",
                "question": "Pemerintah menyediakan informasi anggaran yang dapat diakses warga. Hal ini mendukung...",
                "options": [
                    "Transparansi pemerintahan",
                    "Pembatasan partisipasi",
                    "Diskriminasi sosial",
                    "Intervensi peradilan"
                ],
                "correct": 0,
                "explanation": "Keterbukaan informasi anggaran negara merupakan wujud nyata transparansi dan akuntabilitas tata kelola pemerintahan yang baik (good governance)."
            },
            {
                "id": 3,
                "topic": "ham",
                "topicLabel": "Penanganan Diskriminasi",
                "difficulty": "Mudah",
                "question": "Ketika seseorang mengalami diskriminasi, tindakan yang tepat adalah...",
                "options": [
                    "Membalas dengan diskriminasi",
                    "Membiarkan pelanggaran",
                    "Menyebarkan identitas pelaku tanpa pertimbangan",
                    "Melaporkan melalui saluran yang sesuai"
                ],
                "correct": 3,
                "explanation": "Melaporkan tindakan diskriminasi ke lembaga berwenang (seperti Komnas HAM atau penegak hukum) adalah langkah legal dan bermartabat."
            },
            {
                "id": 4,
                "topic": "keadilan",
                "topicLabel": "Penegakan Keadilan",
                "difficulty": "Mudah",
                "question": "Mengapa pelanggaran HAM perlu ditangani secara adil?",
                "options": [
                    "Agar kelompok tertentu selalu menang",
                    "Agar hak korban terlindungi dan pelaku bertanggung jawab",
                    "Agar hukum hanya berlaku bagi warga biasa",
                    "Agar kritik masyarakat dihentikan"
                ],
                "correct": 1,
                "explanation": "Penanganan adil memastikan pemulihan hak korban, mencegah impunitas, dan menuntut pertanggungjawaban hukum bagi pelaku pelanggaran."
            },
            {
                "id": 5,
                "topic": "partisipasi",
                "topicLabel": "Partisipasi Digital",
                "difficulty": "Mudah",
                "question": "Contoh partisipasi publik di era digital adalah...",
                "options": [
                    "Menyebarkan informasi palsu",
                    "Mengakses akun orang lain",
                    "Menyampaikan aspirasi melalui kanal resmi",
                    "Menghapus pendapat berbeda"
                ],
                "correct": 2,
                "explanation": "Menyampaikan aspirasi dan masukan kebijakan lewat kanal resmi (seperti situs pengaduan aspirasi masyarakat) memperkuat demokrasi digital yang sehat."
            },
            {
                "id": 6,
                "topic": "hukum",
                "topicLabel": "UU Perlindungan Data",
                "difficulty": "Mudah",
                "question": "Undang-undang perlindungan data pribadi terutama bertujuan untuk...",
                "options": [
                    "Mengatur perlindungan dan penggunaan data pribadi",
                    "Mewajibkan semua data dipublikasikan",
                    "Melarang semua layanan digital",
                    "Menghapus hak pengguna internet"
                ],
                "correct": 0,
                "explanation": "UU PDP dirancang untuk menjamin hak subjek data atas keamanannya serta mengatur kewajiban pengendali data dalam pemrosesan informasi pribadi."
            },
            {
                "id": 7,
                "topic": "etika",
                "topicLabel": "Batas Berekspresi",
                "difficulty": "Mudah",
                "question": "Kebebasan berpendapat tidak berarti seseorang boleh...",
                "options": [
                    "Memberikan kritik terhadap kebijakan",
                    "Menyampaikan gagasan secara damai",
                    "Mengikuti diskusi publik",
                    "Mengancam dan melanggar hak orang lain"
                ],
                "correct": 3,
                "explanation": "Ujaran ancaman, intimidasi kekerasan, dan pelanggaran hak individu dilarang karena merusak ruang demokrasi dan melanggar hukum."
            },
            {
                "id": 8,
                "topic": "edukasi",
                "topicLabel": "Tujuan Edukasi HAM",
                "difficulty": "Mudah",
                "question": "Pendidikan HAM bagi masyarakat bertujuan untuk...",
                "options": [
                    "Membuat warga takut menyampaikan pendapat",
                    "Meningkatkan pemahaman tentang hak dan cara melindunginya",
                    "Membatasi akses terhadap hukum",
                    "Mengurangi keterlibatan warga"
                ],
                "correct": 1,
                "explanation": "Dengan memahami hak dan kewajibannya, warga negara memiliki kapasitas untuk membela hak diri sendiri dan sesama secara beradab."
            },
            {
                "id": 9,
                "topic": "platform",
                "topicLabel": "Tata Kelola Digital",
                "difficulty": "Sedang",
                "question": "Jika platform digital menghapus kritik yang sah secara sewenang-wenang, aspek yang perlu diperhatikan adalah...",
                "options": [
                    "Pembagian anggaran daerah",
                    "Pembangunan jalan",
                    "Kebebasan berekspresi dan tata kelola platform",
                    "Program pensiun"
                ],
                "correct": 2,
                "explanation": "Penghapusan kritik yang sah menyentuh isu kebebasan berpendapat di ruang digital dan perlunya transparansi tata kelola moderasi konten."
            },
            {
                "id": 10,
                "topic": "pengaduan",
                "topicLabel": "Mekanisme Pengaduan",
                "difficulty": "Mudah",
                "question": "Mekanisme pengaduan pelanggaran HAM yang baik harus...",
                "options": [
                    "Mudah diakses dan memungkinkan penanganan yang adil",
                    "Hanya menerima laporan pejabat",
                    "Menolak seluruh laporan anonim tanpa pemeriksaan",
                    "Tidak memberikan tindak lanjut"
                ],
                "correct": 0,
                "explanation": "Aksesibilitas dan jaminan penanganan yang adil adalah syarat mutlak agar sistem perlindungan HAM dapat dipercaya masyarakat."
            }
        ]
    },
    {
        "id": 3,
        "name": "Level 3 — Penegak Keadilan",
        "shortTitle": "Penegak Keadilan",
        "badgeName": "Penegak Keadilan",
        "badgeImage": "images/badges/badge_3.webp",
        "focus": "Independensi peradilan, proses hukum yang adil, dan akuntabilitas",
        "description": "Memahami konsep pengadilan yang merdeka dari intervensi penguasa, due process of law, dan integritas etika aparat penegak hukum.",
        "difficulty": "Tingkat Menengah",
        "questions": [
            {
                "id": 1,
                "topic": "peradilan",
                "topicLabel": "Independensi Peradilan",
                "difficulty": "Sedang",
                "question": "Apa arti independensi sistem peradilan?",
                "options": [
                    "Hakim mengikuti perintah partai",
                    "Pengadilan bebas dari intervensi yang tidak semestinya",
                    "Putusan ditentukan oleh kekayaan terdakwa",
                    "Pemerintah menentukan seluruh putusan"
                ],
                "correct": 1,
                "explanation": "Independensi peradilan menegaskan bahwa hakim dan pengadilan tidak boleh tunduk pada tekanan eksekutif, legislatif, modal, maupun massa."
            },
            {
                "id": 2,
                "topic": "hakim",
                "topicLabel": "Objektivitas Hakim",
                "difficulty": "Sedang",
                "question": "Mengapa hakim harus bebas dari tekanan politik?",
                "options": [
                    "Agar dapat memutus perkara secara objektif",
                    "Agar dapat mengabaikan hukum",
                    "Agar tidak perlu menjelaskan putusan",
                    "Agar kebal dari pertanggungjawaban"
                ],
                "correct": 0,
                "explanation": "Kemandirian hakim menjamin keputusan diambil murni berdasarkan fakta persidangan, alat bukti sah, dan keyakinan hukum yang objektif."
            },
            {
                "id": 3,
                "topic": "hukum",
                "topicLabel": "Proses Hukum yang Adil",
                "difficulty": "Sedang",
                "question": "Prinsip proses peradilan yang adil menjamin bahwa...",
                "options": [
                    "Semua terdakwa pasti dihukum",
                    "Hanya kelompok tertentu mendapat bantuan hukum",
                    "Perkara diputus berdasarkan tekanan publik",
                    "Setiap individu memperoleh perlakuan hukum yang adil"
                ],
                "correct": 3,
                "explanation": "Prinsip 'fair trial' atau peradilan yang adil memastikan hak setiap orang untuk didengar, dibela, dan diperlakukan secara tidak memihak."
            },
            {
                "id": 4,
                "topic": "pembelaan",
                "topicLabel": "Hak Pembelaan",
                "difficulty": "Sedang",
                "question": "Hak untuk mendapat pembelaan berarti seseorang...",
                "options": [
                    "Tidak perlu mengikuti proses hukum",
                    "Bebas mengabaikan putusan pengadilan",
                    "Berhak memperoleh bantuan atau pembelaan hukum",
                    "Selalu dibebaskan dari tuduhan"
                ],
                "correct": 2,
                "explanation": "Setiap orang yang disangka atau didakwa melakukan tindak pidana berhak didampingi penasihat hukum demi menjamin hak-haknya di hadapan hukum."
            },
            {
                "id": 5,
                "topic": "transparansi",
                "topicLabel": "Prosedur Sidang",
                "difficulty": "Sedang",
                "question": "Mengapa prosedur pengadilan harus jelas dan transparan?",
                "options": [
                    "Agar perkara dapat diatur oleh pihak tertentu",
                    "Agar proses dapat dipahami dan dipantau sesuai aturan",
                    "Agar sidang tidak membutuhkan bukti",
                    "Agar hakim bebas melanggar hukum"
                ],
                "correct": 1,
                "explanation": "Transparansi jalannya persidangan membuka ruang pengawasan publik sehingga keadilan dapat teruji secara terang benderang."
            },
            {
                "id": 6,
                "topic": "etika",
                "topicLabel": "Akuntabilitas Hakim",
                "difficulty": "Sedang",
                "question": "Hakim terbukti melanggar etik profesi. Prinsip yang mengharuskan pertanggungjawaban adalah...",
                "options": [
                    "Otonomi daerah",
                    "Kebebasan media",
                    "Kemakmuran ekonomi",
                    "Akuntabilitas sistem peradilan"
                ],
                "correct": 3,
                "explanation": "Akuntabilitas peradilan (melalui Komisi Yudisial dan Dewan Kehormatan Hakim) menjaga marwah peradilan agar hakim berintegritas tinggi."
            },
            {
                "id": 7,
                "topic": "ham",
                "topicLabel": "Integritas Fisik",
                "difficulty": "Sedang",
                "question": "Larangan penyiksaan dalam proses hukum merupakan bentuk...",
                "options": [
                    "Perlindungan hak asasi manusia",
                    "Peningkatan investasi",
                    "Desentralisasi kekuasaan",
                    "Pemerataan pajak"
                ],
                "correct": 0,
                "explanation": "Hak bebas dari penyiksaan dan perlakuan merendahkan martabat merupakan hak mutlak (non-derogable right) dalam konstitusi."
            },
            {
                "id": 8,
                "topic": "peradilan",
                "topicLabel": "Bukti dan Hukum",
                "difficulty": "Sedang",
                "question": "Jika seorang hakim memutus perkara berdasarkan bukti dan hukum, bukan tekanan pihak luar, ia menerapkan...",
                "options": [
                    "Dominasi mayoritas",
                    "Intervensi politik",
                    "Independensi peradilan",
                    "Pemberdayaan ekonomi"
                ],
                "correct": 2,
                "explanation": "Menolak intervensi luar dan murni bersandar pada bukti persidangan adalah perwujudan tertinggi independensi peradilan."
            },
            {
                "id": 9,
                "topic": "kesetaraan",
                "topicLabel": "Persamaan Hukum",
                "difficulty": "Sedang",
                "question": "Perlakuan diskriminatif dalam pengadilan bertentangan dengan...",
                "options": [
                    "Kemandirian ekonomi",
                    "Persamaan di hadapan hukum",
                    "Pengembangan infrastruktur",
                    "Otonomi fiskal"
                ],
                "correct": 1,
                "explanation": "Asas 'Equality Before the Law' menolak diskriminasi apa pun di ruang sidang pengadilan."
            },
            {
                "id": 10,
                "topic": "konstitusi",
                "topicLabel": "Tujuan Peradilan Merdeka",
                "difficulty": "Sedang",
                "question": "Tujuan utama pengadilan yang merdeka dalam demokrasi adalah...",
                "options": [
                    "Melindungi kepentingan penguasa",
                    "Membatasi akses masyarakat",
                    "Mengutamakan tekanan sosial",
                    "Mewujudkan keadilan dan putusan yang objektif"
                ],
                "correct": 3,
                "explanation": "Pengadilan yang merdeka adalah benteng terakhir bagi pencari keadilan untuk memperoleh kepastian hukum yang objektif dan adil."
            }
        ]
    },
    {
        "id": 4,
        "name": "Level 4 — Ahli Hukum",
        "shortTitle": "Ahli Hukum",
        "badgeName": "Ahli Hukum",
        "badgeImage": "images/badges/badge_4.webp",
        "focus": "Pendidikan hukum, akses keadilan, dan sistem peradilan yang responsif",
        "description": "Pendalaman mengenai bantuan hukum gratis (pro bono), pengawasan integritas, dan transformasi peradilan modern yang responsif.",
        "difficulty": "Tingkat Menengah Lanjutan",
        "questions": [
            {
                "id": 1,
                "topic": "kompetensi",
                "topicLabel": "Pendidikan Hukum Hakim",
                "difficulty": "Sedang",
                "question": "Pendidikan hukum berkelanjutan bagi hakim dibutuhkan untuk...",
                "options": [
                    "Mengurangi pemahaman terhadap aturan baru",
                    "Menghindari evaluasi profesi",
                    "Memperbarui pengetahuan dan keterampilan hukum",
                    "Membatasi kemampuan menangani perkara"
                ],
                "correct": 2,
                "explanation": "Perkembangan hukum dan teknologi menuntut pembaruan kapasitas hakim agar mampu menangani perkara kompleks secara relevan dan tepat."
            },
            {
                "id": 2,
                "topic": "bantuan_hukum",
                "topicLabel": "Akses Keadilan",
                "difficulty": "Sedang",
                "question": "Bantuan hukum gratis bagi masyarakat kurang mampu bertujuan untuk...",
                "options": [
                    "Memperluas akses terhadap keadilan",
                    "Mengistimewakan pejabat",
                    "Menghapus seluruh proses peradilan",
                    "Menggantikan tugas hakim"
                ],
                "correct": 0,
                "explanation": "Bantuan hukum cuma-cuma menjamin bahwa hak mencari keadilan tidak hanya dinikmati oleh mereka yang memiliki uang atau kekuasaan."
            },
            {
                "id": 3,
                "topic": "integritas",
                "topicLabel": "Pengawasan Peradilan",
                "difficulty": "Sedang",
                "question": "Pengawasan terhadap integritas pengadilan berguna untuk...",
                "options": [
                    "Meningkatkan tekanan politik",
                    "Menutup informasi perkara",
                    "Menghindari tanggung jawab hakim",
                    "Memastikan sistem peradilan berjalan secara bertanggung jawab"
                ],
                "correct": 3,
                "explanation": "Sistem peradilan harus memiliki pengawasan internal dan eksternal demi mencegah korupsi yudisial dan menjaga kepercayaan publik."
            },
            {
                "id": 4,
                "topic": "peradilan",
                "topicLabel": "Peradilan Responsif",
                "difficulty": "Menantang",
                "question": "Sistem peradilan yang responsif harus...",
                "options": [
                    "Menolak perkembangan teknologi",
                    "Menyesuaikan penanganan perkara dengan kebutuhan masyarakat dan perubahan sosial",
                    "Hanya menangani perkara lama",
                    "Mengabaikan kebutuhan masyarakat"
                ],
                "correct": 1,
                "explanation": "Peradilan responsif peka terhadap rasa keadilan substantif masyarakat serta dinamis mengikuti transformasi sosial zaman."
            },
            {
                "id": 5,
                "topic": "kebijakan",
                "topicLabel": "Bantuan Hukum Masyarakat",
                "difficulty": "Sedang",
                "question": "Seorang warga miskin kesulitan membayar pengacara. Kebijakan yang paling sesuai adalah...",
                "options": [
                    "Menolak laporan warga",
                    "Membatasi hak pembelaan",
                    "Menyediakan bantuan hukum yang terjangkau atau gratis sesuai ketentuan",
                    "Mewajibkan warga menyelesaikan semua masalah sendiri"
                ],
                "correct": 2,
                "explanation": "Negara berkewajiban menyediakan pos bantuan hukum (Posbakum) dan advokat pro bono bagi warga yang tidak mampu secara finansial."
            },
            {
                "id": 6,
                "topic": "sanksi",
                "topicLabel": "Penegakan Kode Etik",
                "difficulty": "Sedang",
                "question": "Apabila hakim terbukti melakukan pelanggaran hukum, tindakan yang sesuai dengan akuntabilitas adalah...",
                "options": [
                    "Memeriksa dan menjatuhkan sanksi melalui mekanisme yang sah",
                    "Membiarkannya karena berstatus hakim",
                    "Menghapus semua bukti",
                    "Meminta masyarakat mengabaikan kasus"
                ],
                "correct": 0,
                "explanation": "Tidak ada seorang pun yang berada di atas hukum; hakim yang melanggar hukum harus diproses dan disanksi sesuai koridor peraturan."
            },
            {
                "id": 7,
                "topic": "teknologi",
                "topicLabel": "Teknologi Peradilan (E-Court)",
                "difficulty": "Sedang",
                "question": "Teknologi baru dalam sistem peradilan sebaiknya digunakan untuk...",
                "options": [
                    "Menghapus hak terdakwa",
                    "Menghindari transparansi",
                    "Menggantikan semua prinsip hukum",
                    "Meningkatkan layanan dengan tetap menjaga keadilan dan hak warga"
                ],
                "correct": 3,
                "explanation": "Pemanfaatan e-Court dan sidang digital ditujukan mempercepat, mempermudah, dan mengefisienkan layanan peradilan tanpa mengurangi hak terdakwa."
            },
            {
                "id": 8,
                "topic": "akses",
                "topicLabel": "Kesetaraan Akses",
                "difficulty": "Sedang",
                "question": "Kesetaraan akses terhadap peradilan berarti...",
                "options": [
                    "Hanya orang kaya dapat mengajukan perkara",
                    "Setiap orang memiliki kesempatan memperoleh layanan hukum",
                    "Pejabat selalu mendapat putusan lebih ringan",
                    "Warga desa tidak dapat mencari keadilan"
                ],
                "correct": 1,
                "explanation": "Semua warga, baik kaya maupun miskin, di kota maupun pelosok, memiliki hak setara memperoleh perlindungan dan layanan hukum peradilan."
            },
            {
                "id": 9,
                "topic": "profesionalisme",
                "topicLabel": "Pelatihan Aparat Peradilan",
                "difficulty": "Sedang",
                "question": "Pelatihan hukum yang berkualitas membantu aparat peradilan...",
                "options": [
                    "Mengabaikan perkembangan hukum",
                    "Mengurangi akuntabilitas",
                    "Menangani perkara secara kompeten dan profesional",
                    "Menghindari pemeriksaan perkara"
                ],
                "correct": 2,
                "explanation": "Kompetensi teknis dan integritas moral aparat peradilan dibentuk melalui pelatihan profesional yang berkelanjutan."
            },
            {
                "id": 10,
                "topic": "layanan",
                "topicLabel": "Contoh Peradilan Responsif",
                "difficulty": "Sedang",
                "question": "Manakah contoh peradilan yang responsif?",
                "options": [
                    "Menyediakan layanan informasi dan prosedur yang mudah diakses masyarakat",
                    "Menolak semua pengaduan digital",
                    "Memperlambat seluruh proses tanpa alasan",
                    "Mengabaikan kebutuhan kelompok rentan"
                ],
                "correct": 0,
                "explanation": "Layanan informasi yang ramah, cepat, transparan, dan inklusif bagi kaum rentan mencerminkan peradilan modern yang responsif."
            }
        ]
    },
    {
        "id": 5,
        "name": "Level 5 — Penggerak Daerah",
        "shortTitle": "Penggerak Daerah",
        "badgeName": "Penggerak Daerah",
        "badgeImage": "images/badges/badge_5.webp",
        "focus": "Otonomi daerah, desentralisasi, dan pemberdayaan masyarakat lokal",
        "description": "Memahami desentralisasi kekuasaan, otonomi daerah, partisipasi masyarakat dalam musrenbang, dan akuntabilitas pemerintah daerah.",
        "difficulty": "Tingkat Menengah Lanjutan",
        "questions": [
            {
                "id": 1,
                "topic": "otonomi",
                "topicLabel": "Konsep Otonomi Daerah",
                "difficulty": "Sedang",
                "question": "Apa yang dimaksud dengan otonomi daerah?",
                "options": [
                    "Penghapusan pemerintahan daerah",
                    "Penyerahan seluruh kekuasaan kepada perusahaan",
                    "Kewenangan daerah mengurus urusan pemerintahan sesuai ketentuan",
                    "Larangan daerah mengelola sumber daya"
                ],
                "correct": 2,
                "explanation": "Otonomi daerah adalah hak, wewenang, dan kewajiban daerah otonom untuk mengatur dan mengurus sendiri urusan pemerintahan sesuai aspirasi masyarakat dan UU."
            },
            {
                "id": 2,
                "topic": "desentralisasi",
                "topicLabel": "Makna Desentralisasi",
                "difficulty": "Sedang",
                "question": "Desentralisasi kekuasaan berarti...",
                "options": [
                    "Pemindahan sebagian kewenangan dari pusat kepada daerah sesuai aturan",
                    "Semua keputusan harus dibuat presiden",
                    "Daerah tidak boleh membuat kebijakan",
                    "Penghapusan pelayanan publik"
                ],
                "correct": 0,
                "explanation": "Desentralisasi mendelegasikan wewenang urusan publik kepada daerah agar pelayanan lebih cepat, tepat sasaran, dan kontekstual."
            },
            {
                "id": 3,
                "topic": "daerah",
                "topicLabel": "Keunggulan Pemerintah Daerah",
                "difficulty": "Sedang",
                "question": "Mengapa pemerintah daerah dianggap lebih memahami kebutuhan lokal?",
                "options": [
                    "Karena tidak perlu mendengar warga",
                    "Karena tidak terikat aturan",
                    "Karena selalu memiliki dana tak terbatas",
                    "Karena lebih dekat dengan masyarakat setempat"
                ],
                "correct": 3,
                "explanation": "Kedekatan geografis dan kultural membuat pemda lebih peka terhadap dinamika, potensi, dan permasalahan riil warga di daerah."
            },
            {
                "id": 4,
                "topic": "partisipasi",
                "topicLabel": "Musrenbang Daerah",
                "difficulty": "Sedang",
                "question": "Contoh partisipasi masyarakat dalam otonomi daerah adalah...",
                "options": [
                    "Mengabaikan musyawarah",
                    "Mengikuti musyawarah perencanaan pembangunan daerah",
                    "Menolak seluruh layanan publik",
                    "Membatasi akses warga terhadap informasi"
                ],
                "correct": 1,
                "explanation": "Mengikuti Musrenbang (Musyawarah Perencanaan Pembangunan) dari tingkat desa hingga kabupaten/kota adalah wujud partisipasi warga menentukan prioritas pembangunan."
            },
            {
                "id": 5,
                "topic": "ekonomi_lokal",
                "topicLabel": "Potensi Daerah",
                "difficulty": "Sedang",
                "question": "Pemanfaatan potensi ekonomi dan budaya lokal bertujuan untuk...",
                "options": [
                    "Menghilangkan identitas daerah",
                    "Meningkatkan ketergantungan sepenuhnya pada pusat",
                    "Mendorong pembangunan dan kemandirian daerah",
                    "Mengurangi kesempatan kerja"
                ],
                "correct": 2,
                "explanation": "Mengoptimalkan kearifan lokal dan potensi ekonomi daerah mewujudkan kemandirian daerah yang berdaya saing."
            },
            {
                "id": 6,
                "topic": "pelayanan",
                "topicLabel": "Pelayanan Publik Daerah",
                "difficulty": "Sedang",
                "question": "Pelayanan publik daerah yang baik harus...",
                "options": [
                    "Sesuai kebutuhan masyarakat dan mudah diakses",
                    "Hanya tersedia bagi pejabat",
                    "Dibatasi tanpa alasan",
                    "Tidak menerima masukan warga"
                ],
                "correct": 0,
                "explanation": "Standar pelayanan prima di daerah berakar pada kemudahan akses, keramahan, kepastian biaya, dan kecepatan waktu bagi seluruh warga."
            },
            {
                "id": 7,
                "topic": "pemerintahan",
                "topicLabel": "Peran Pemerintah Pusat",
                "difficulty": "Sedang",
                "question": "Dalam otonomi daerah, pemerintah pusat tetap dapat berperan sebagai...",
                "options": [
                    "Penguasa mutlak semua urusan lokal",
                    "Pihak yang tidak boleh berkoordinasi",
                    "Pengganti seluruh pemerintah daerah",
                    "Fasilitator dan pemberi dukungan sesuai kewenangannya"
                ],
                "correct": 3,
                "explanation": "Pemerintah pusat memegang urusan absolut (politik luar negeri, pertahanan, moneter, yustisi, agama) dan membina serta memfasilitasi urusan daerah."
            },
            {
                "id": 8,
                "topic": "pengawasan",
                "topicLabel": "Pengawasan Pemda",
                "difficulty": "Sedang",
                "question": "Mengapa pemerintah daerah perlu diawasi?",
                "options": [
                    "Agar tidak dapat menjalankan tugas",
                    "Agar kewenangan digunakan secara bertanggung jawab",
                    "Agar masyarakat tidak mengetahui anggaran",
                    "Agar seluruh keputusan dirahasiakan"
                ],
                "correct": 1,
                "explanation": "Pengawasan oleh DPRD, inspektorat, BPK, dan warga mencegah terjadinya penyalahgunaan wewenang dan korupsi di tingkat daerah."
            },
            {
                "id": 9,
                "topic": "pariwisata",
                "topicLabel": "Pariwisata Berkelanjutan",
                "difficulty": "Sedang",
                "question": "Jika suatu daerah memiliki potensi wisata alam, langkah yang sesuai adalah...",
                "options": [
                    "Mengabaikan potensi tersebut",
                    "Mengembangkan wisata tanpa memperhatikan lingkungan",
                    "Mengembangkan wisata secara bertanggung jawab dan melibatkan masyarakat",
                    "Melarang warga memperoleh manfaat ekonomi"
                ],
                "correct": 2,
                "explanation": "Pengembangan ekowisata berbasis komunitas menjaga kelestarian alam sekaligus mendongkrak perekonomian warga lokal."
            },
            {
                "id": 10,
                "topic": "pemberdayaan",
                "topicLabel": "Partisipasi Lokal",
                "difficulty": "Sedang",
                "question": "Keputusan pembangunan dibuat melalui konsultasi warga dan mempertimbangkan kondisi setempat. Hal ini menunjukkan...",
                "options": [
                    "Pemberdayaan dan partisipasi masyarakat lokal",
                    "Intervensi terhadap pengadilan",
                    "Pelanggaran privasi",
                    "Pembatasan otonomi"
                ],
                "correct": 0,
                "explanation": "Pembangunan partisipatif (bottom-up) menempatkan masyarakat bukan sekadar objek, melainkan subjek utama pemegang kedaulatan daerah."
            }
        ]
    },
    {
        "id": 6,
        "name": "Level 6 — Arsitek Kemakmuran",
        "shortTitle": "Arsitek Kemakmuran",
        "badgeName": "Arsitek Kemakmuran",
        "badgeImage": "images/badges/badge_6.webp",
        "focus": "Pembangunan berkelanjutan, kesejahteraan, dan pemerataan ekonomi",
        "description": "Membahas demokrasi ekonomi, pembangunan berkelanjutan (SDGs), transparansi anggaran publik, serta pemberdayaan UMKM.",
        "difficulty": "Tingkat Lanjutan",
        "questions": [
            {
                "id": 1,
                "topic": "kemakmuran",
                "topicLabel": "Tujuan Kemakmuran",
                "difficulty": "Sedang",
                "question": "Apa tujuan demokrasi dengan kemakmuran?",
                "options": [
                    "Memusatkan kekayaan pada satu kelompok",
                    "Mendorong kesejahteraan yang merata bagi masyarakat",
                    "Mengurangi layanan kesehatan",
                    "Mengabaikan pembangunan ekonomi"
                ],
                "correct": 1,
                "explanation": "Demokrasi dengan kemakmuran bertujuan memastikan kemajuan ekonomi dirasakan secara adil dan merata oleh seluruh lapisan rakyat Indonesia."
            },
            {
                "id": 2,
                "topic": "keberlanjutan",
                "topicLabel": "Pembangunan Berkelanjutan",
                "difficulty": "Sedang",
                "question": "Pembangunan ekonomi berkelanjutan memperhatikan...",
                "options": [
                    "Keuntungan jangka pendek saja",
                    "Pertumbuhan tanpa batas",
                    "Kepentingan generasi sekarang saja",
                    "Pertumbuhan ekonomi, lingkungan, dan generasi mendatang"
                ],
                "correct": 3,
                "explanation": "Pembangunan berkelanjutan menyeimbangkan tiga pilar: kemakmuran ekonomi, kelestarian ekologis, dan keadilan antargenerasi."
            },
            {
                "id": 3,
                "topic": "kesenjangan",
                "topicLabel": "Pengurangan Kesenjangan",
                "difficulty": "Sedang",
                "question": "Kebijakan yang mengurangi kesenjangan ekonomi dapat dilakukan dengan...",
                "options": [
                    "Memperluas akses pendidikan dan layanan publik",
                    "Membatasi pendidikan bagi warga miskin",
                    "Mengurangi bantuan bagi kelompok rentan",
                    "Memusatkan seluruh kesempatan kerja"
                ],
                "correct": 0,
                "explanation": "Pendidikan berkualitas dan akses merata terhadap fasilitas publik merupakan kunci mobilitas sosial untuk memutus rantai kemiskinan."
            },
            {
                "id": 4,
                "topic": "pemberdayaan",
                "topicLabel": "Pelatihan Kerja",
                "difficulty": "Sedang",
                "question": "Program pelatihan kerja bagi masyarakat merupakan contoh...",
                "options": [
                    "Pembatasan kesempatan ekonomi",
                    "Pengurangan kualitas sumber daya manusia",
                    "Pemberdayaan ekonomi masyarakat",
                    "Intervensi peradilan"
                ],
                "correct": 2,
                "explanation": "Peningkatan keterampilan dan keahlian vokasi memperkuat daya saing tenaga kerja dan kemandirian ekonomi keluarga."
            },
            {
                "id": 5,
                "topic": "infrastruktur",
                "topicLabel": "Peran Infrastruktur",
                "difficulty": "Sedang",
                "question": "Mengapa infrastruktur penting bagi kemakmuran?",
                "options": [
                    "Agar hanya kota besar berkembang",
                    "Untuk mendukung aktivitas ekonomi dan akses pelayanan",
                    "Untuk membatasi mobilitas warga",
                    "Untuk mengurangi perdagangan"
                ],
                "correct": 1,
                "explanation": "Konektivitas jalan, listrik, jembatan, dan internet menurunkan biaya logistik dan mempermudah akses ke fasilitas kesehatan dan pendidikan."
            },
            {
                "id": 6,
                "topic": "anggaran",
                "topicLabel": "Keuangan Publik",
                "difficulty": "Sedang",
                "question": "Transparansi pengelolaan keuangan publik membantu mencegah...",
                "options": [
                    "Partisipasi masyarakat",
                    "Pembangunan daerah",
                    "Peningkatan kualitas layanan",
                    "Korupsi dan penyalahgunaan kekuasaan"
                ],
                "correct": 3,
                "explanation": "Pengelolaan APBN/APBD yang terbuka dan diaudit secara berkala menutup celah kebocoran anggaran dan praktik korupsi."
            },
            {
                "id": 7,
                "topic": "umkm",
                "topicLabel": "Dukungan Usaha Kecil",
                "difficulty": "Sedang",
                "question": "Pemerintah memberikan dukungan kepada usaha kecil agar mampu berkembang. Tujuannya adalah...",
                "options": [
                    "Memperkuat kemampuan ekonomi masyarakat",
                    "Menghapus seluruh usaha lokal",
                    "Membatasi kesempatan kerja",
                    "Mengurangi keterampilan tenaga kerja"
                ],
                "correct": 0,
                "explanation": "UMKM adalah tulang punggung perekonomian nasional yang menyerap tenaga kerja terbesar dan menopang ketahanan ekonomi keluarga."
            },
            {
                "id": 8,
                "topic": "lingkungan",
                "topicLabel": "Etika Lingkungan",
                "difficulty": "Sedang",
                "question": "Pembangunan yang hanya mengejar keuntungan tetapi merusak lingkungan bertentangan dengan...",
                "options": [
                    "Kebebasan media",
                    "Independensi hakim",
                    "Prinsip pembangunan berkelanjutan",
                    "Transparansi peradilan"
                ],
                "correct": 2,
                "explanation": "Eksploitasi berlebihan merusak daya dukung alam dan merugikan generasi mendatang, bertolak belakang dengan prinsip pembangunan berkelanjutan."
            },
            {
                "id": 9,
                "topic": "perencanaan",
                "topicLabel": "Partisipasi Ekonomi",
                "difficulty": "Sedang",
                "question": "Warga dilibatkan dalam perencanaan kebijakan ekonomi daerah. Hal ini mencerminkan...",
                "options": [
                    "Penghapusan tanggung jawab pemerintah",
                    "Partisipasi publik dalam pembangunan ekonomi",
                    "Pembatasan informasi publik",
                    "Dominasi kelompok tertentu"
                ],
                "correct": 1,
                "explanation": "Pelibatan warga memastikan program ekonomi daerah selaras dengan kebutuhan riil pelaku usaha dan warga di lapangan."
            },
            {
                "id": 10,
                "topic": "kesejahteraan",
                "topicLabel": "Indikator Kemakmuran",
                "difficulty": "Sedang",
                "question": "Indikator kemakmuran yang lebih menyeluruh adalah...",
                "options": [
                    "Besarnya keuntungan satu perusahaan saja",
                    "Banyaknya gedung di pusat kota saja",
                    "Tingginya pendapatan kelompok terkaya saja",
                    "Peningkatan kualitas hidup dan akses kebutuhan dasar masyarakat"
                ],
                "correct": 3,
                "explanation": "Kesejahteraan sejati diukur dari Indeks Pembangunan Manusia (IPM), pemenuhan gizi, pendidikan, dan kesehatan bagi seluruh warga."
            }
        ]
    },
    {
        "id": 7,
        "name": "Level 7 — Pejuang Keadilan Sosial",
        "shortTitle": "Pejuang Keadilan Sosial",
        "badgeName": "Pejuang Keadilan Sosial",
        "badgeImage": "images/badges/badge_7.webp",
        "focus": "Kesetaraan kesempatan, distribusi sumber daya, dan pengurangan kesenjangan",
        "description": "Mendalami sila kelima Pancasila: pemerataan kesempatan, perlindungan kaum marginal, inklusi disabilitas, dan pajak progresif.",
        "difficulty": "Tingkat Lanjutan",
        "questions": [
            {
                "id": 1,
                "topic": "keadilan_sosial",
                "topicLabel": "Keadilan Sosial",
                "difficulty": "Sedang",
                "question": "Demokrasi yang berkeadilan sosial menekankan...",
                "options": [
                    "Persaingan tanpa aturan",
                    "Kepentingan kelompok kaya saja",
                    "Kesetaraan dan keadilan dalam distribusi sumber daya dan kesempatan",
                    "Penghapusan seluruh bantuan sosial"
                ],
                "correct": 2,
                "explanation": "Keadilan sosial menjamin distribusi sumber daya alam dan ekonomi dialokasikan untuk sebesar-besarnya kemakmuran rakyat secara adil."
            },
            {
                "id": 2,
                "topic": "kesempatan",
                "topicLabel": "Pemerataan Kesempatan",
                "difficulty": "Sedang",
                "question": "Pemerataan kesempatan berarti...",
                "options": [
                    "Setiap individu memperoleh kesempatan yang adil tanpa diskriminasi",
                    "Semua pekerjaan diberikan kepada satu kelompok",
                    "Pendidikan hanya tersedia di perkotaan",
                    "Kesempatan bergantung pada hubungan pribadi"
                ],
                "correct": 0,
                "explanation": "Setiap anak bangsa berhak atas peluang yang sama untuk menempuh pendidikan, bekerja, dan mengembangkan potensinya tanpa diskriminasi."
            },
            {
                "id": 3,
                "topic": "fiskal",
                "topicLabel": "Pajak Progresif",
                "difficulty": "Sedang",
                "question": "Kebijakan pajak progresif berkaitan dengan gagasan bahwa...",
                "options": [
                    "Semua orang tidak perlu membayar pajak",
                    "Pajak hanya digunakan oleh perusahaan",
                    "Pajak harus dihapuskan",
                    "Masyarakat berpenghasilan lebih tinggi dapat menanggung proporsi pajak lebih besar sesuai aturan"
                ],
                "correct": 3,
                "explanation": "Pajak progresif mendistribusikan kembali kekayaan untuk membiayai fasilitas publik, subsidi pendidikan, dan perlindungan warga miskin."
            },
            {
                "id": 4,
                "topic": "afirmasi",
                "topicLabel": "Kelompok Marginal",
                "difficulty": "Sedang",
                "question": "Bantuan bagi kelompok marginal bertujuan untuk...",
                "options": [
                    "Memperlebar kesenjangan",
                    "Membantu meningkatkan kualitas hidup dan mengurangi ketimpangan",
                    "Membatasi akses terhadap pendidikan",
                    "Menghilangkan partisipasi publik"
                ],
                "correct": 1,
                "explanation": "Tindakan afirmatif dan bantuan sosial memberdayakan kelompok rentan agar mampu mandiri dan keluar dari jurang kemiskinan."
            },
            {
                "id": 5,
                "topic": "distribusi",
                "topicLabel": "Distribusi Sumber Daya",
                "difficulty": "Sedang",
                "question": "Contoh distribusi sumber daya yang adil adalah...",
                "options": [
                    "Semua anggaran diberikan ke satu kota",
                    "Layanan hanya tersedia bagi pejabat",
                    "Anggaran dialokasikan sesuai kebutuhan masyarakat, termasuk kelompok tertinggal",
                    "Daerah terpencil tidak memperoleh fasilitas"
                ],
                "correct": 2,
                "explanation": "Alokasi anggaran yang berkeadilan mengutamakan percepatan fasilitas dasar bagi wilayah dan komunitas yang tertinggal."
            },
            {
                "id": 6,
                "topic": "minoritas",
                "topicLabel": "Hak Kelompok Minoritas",
                "difficulty": "Sedang",
                "question": "Pengakuan hak kelompok minoritas berarti...",
                "options": [
                    "Hak mereka diakui dan dilindungi dari diskriminasi",
                    "Mereka tidak boleh terlibat dalam politik",
                    "Mereka harus mengikuti semua kebiasaan mayoritas",
                    "Mereka tidak berhak mendapatkan layanan publik"
                ],
                "correct": 0,
                "explanation": "Kematangan demokrasi diukur dari seberapa baik negara melindungi hak-hak kelompok minoritas dari diskriminasi dan perlakuan tidak adil."
            },
            {
                "id": 7,
                "topic": "jamsos",
                "topicLabel": "Jaminan Sosial",
                "difficulty": "Sedang",
                "question": "Perlindungan sosial yang kuat dapat mencakup...",
                "options": [
                    "Larangan memperoleh layanan kesehatan",
                    "Penghapusan program pensiun",
                    "Pembatasan pendidikan",
                    "Asuransi pengangguran, bantuan kesehatan, dan program pensiun"
                ],
                "correct": 3,
                "explanation": "Sistem jaminan sosial nasional (SJSN) merupakan jaring pengaman agar warga negara terlindungi dari resiko sakit, kecelakaan, dan hari tua."
            },
            {
                "id": 8,
                "topic": "evaluasi",
                "topicLabel": "Evaluasi Kebijakan Publik",
                "difficulty": "Sedang",
                "question": "Mengapa dampak kebijakan publik perlu dievaluasi?",
                "options": [
                    "Agar kebijakan tidak pernah berubah",
                    "Untuk menilai apakah tujuan keadilan sosial tercapai",
                    "Agar masyarakat tidak dapat memberi masukan",
                    "Untuk menghindari transparansi"
                ],
                "correct": 1,
                "explanation": "Evaluasi berkala memastikan program pemerintah tepat sasaran dan benar-benar menekan ketimpangan sosial di masyarakat."
            },
            {
                "id": 9,
                "topic": "inklusi",
                "topicLabel": "Inklusi Disabilitas",
                "difficulty": "Sedang",
                "question": "Sekolah menyediakan fasilitas yang dapat diakses siswa penyandang disabilitas. Prinsip yang diterapkan adalah...",
                "options": [
                    "Dominasi ekonomi",
                    "Pembatasan akses",
                    "Inklusi dan kesetaraan kesempatan",
                    "Sentralisasi peradilan"
                ],
                "correct": 2,
                "explanation": "Penyediaan fasilitas ramah disabilitas (seperti ramp, lift braille, dan modul khusus) adalah hak asasi atas pendidikan inklusif tanpa hambatan."
            },
            {
                "id": 10,
                "topic": "kesenjangan",
                "topicLabel": "Solusi Kesenjangan",
                "difficulty": "Sedang",
                "question": "Kesenjangan sosial dapat dikurangi melalui...",
                "options": [
                    "Kebijakan yang memperluas akses pendidikan, pekerjaan, dan layanan dasar",
                    "Pembatasan bantuan bagi warga miskin",
                    "Pengurangan kesempatan kerja",
                    "Diskriminasi berdasarkan latar belakang"
                ],
                "correct": 0,
                "explanation": "Peluang kerja yang luas, jaminan kesehatan semesta, dan pendidikan bermutu adalah kunci utama mengatasi ketimpangan sosial."
            }
        ]
    },
    {
        "id": 8,
        "name": "Level 8 — Master Demokrasi",
        "shortTitle": "Master Demokrasi",
        "badgeName": "Master Demokrasi",
        "badgeImage": "images/badges/badge_8.webp",
        "focus": "Soal analisis kasus yang menggabungkan seluruh materi LKS",
        "description": "Tantangan pamungkas berupa studi kasus integratif yang memadukan hukum, HAM, independensi peradilan, otonomi daerah, dan keadilan sosial.",
        "difficulty": "Tingkat Ahli (Master)",
        "questions": [
            {
                "id": 1,
                "topic": "kasus_tata_kelola",
                "topicLabel": "Analisis Tata Kelola",
                "difficulty": "Menantang",
                "question": "Pemerintah daerah membuka data anggaran, melibatkan warga dalam musyawarah, dan mengevaluasi hasil pembangunan. Prinsip yang paling lengkap tercermin adalah...",
                "options": [
                    "Independensi peradilan saja",
                    "Perlindungan privasi saja",
                    "Kebebasan ekonomi tanpa pengawasan",
                    "Transparansi, partisipasi publik, dan akuntabilitas"
                ],
                "correct": 3,
                "explanation": "Membuka data (transparansi), musyawarah (partisipasi), dan evaluasi (akuntabilitas) merangkum prinsip tata kelola demokrasi secara menyeluruh."
            },
            {
                "id": 2,
                "topic": "kasus_peradilan",
                "topicLabel": "Integritas Yudisial",
                "difficulty": "Menantang",
                "question": "Seorang pejabat menekan hakim agar menghukum lawan politiknya. Sikap yang sesuai dengan demokrasi adalah...",
                "options": [
                    "Mengikuti perintah demi stabilitas",
                    "Menegakkan independensi peradilan dan memutus berdasarkan hukum serta bukti",
                    "Mengabaikan seluruh proses hukum",
                    "Memutus perkara berdasarkan popularitas"
                ],
                "correct": 1,
                "explanation": "Hakim wajib menolak segala bentuk intervensi politik kekuasaan dan tegak lurus pada kebenaran materiil berdasarkan hukum pembuktian."
            },
            {
                "id": 3,
                "topic": "kasus_digital",
                "topicLabel": "Keamanan Data Warga",
                "difficulty": "Menantang",
                "question": "Sebuah aplikasi layanan publik mengumpulkan data warga tanpa perlindungan memadai. Perbaikan paling tepat adalah...",
                "options": [
                    "Meningkatkan perlindungan data dan mengatur penggunaan secara aman",
                    "Mempublikasikan semua data",
                    "Menghapus akses warga terhadap layanan",
                    "Membagikan data kepada pihak mana pun"
                ],
                "correct": 0,
                "explanation": "Pengelola sistem elektronik wajib menerapkan enkripsi dan tata kelola keamanan ketat demi melindungi hak privasi warga negara."
            },
            {
                "id": 4,
                "topic": "kasus_daerah",
                "topicLabel": "Pemerataan Wilayah",
                "difficulty": "Menantang",
                "question": "Daerah terpencil tertinggal karena minimnya fasilitas kesehatan dan transportasi. Kebijakan paling sesuai dengan keadilan sosial adalah...",
                "options": [
                    "Memusatkan pembangunan di kota besar",
                    "Mengurangi anggaran pelayanan dasar",
                    "Memperluas infrastruktur dan akses layanan di daerah tertinggal",
                    "Menyerahkan seluruh masalah kepada warga"
                ],
                "correct": 2,
                "explanation": "Negara harus hadir membangun daerah 3T (terdepan, terpencil, tertinggal) demi mewujudkan keadilan sosial bagi seluruh rakyat Indonesia."
            },
            {
                "id": 5,
                "topic": "kasus_amdal",
                "topicLabel": "Evaluasi Pembangunan",
                "difficulty": "Menantang",
                "question": "Sebuah proyek meningkatkan pendapatan daerah, tetapi mencemari lingkungan dan merugikan warga. Evaluasi yang tepat harus...",
                "options": [
                    "Menilai keberhasilan hanya dari pendapatan",
                    "Mengabaikan dampak kepada warga",
                    "Melanjutkan proyek tanpa perubahan",
                    "Mempertimbangkan manfaat ekonomi, dampak lingkungan, dan kesejahteraan masyarakat"
                ],
                "correct": 3,
                "explanation": "Pembangunan berkelanjutan mensyaratkan analisis dampak lingkungan (AMDAL) dan perlindungan ruang hidup masyarakat di atas profit semata."
            },
            {
                "id": 6,
                "topic": "kasus_opini",
                "topicLabel": "Kritik Kebijakan",
                "difficulty": "Menantang",
                "question": "Warga mengkritik kebijakan melalui media sosial dengan damai. Pemerintah seharusnya...",
                "options": [
                    "Menghukum semua pengkritik",
                    "Menghormati kebebasan berekspresi dan menanggapi kritik secara bertanggung jawab",
                    "Menutup seluruh media sosial",
                    "Menghapus hak warga untuk berpendapat"
                ],
                "correct": 1,
                "explanation": "Kritik konstruktif dari warga adalah energi perbaikan kebijakan publik dalam demokrasi yang sehat dan beradab."
            },
            {
                "id": 7,
                "topic": "kasus_keadilan",
                "topicLabel": "Keadilan bagi yang Lemah",
                "difficulty": "Menantang",
                "question": "Seorang warga miskin tidak mampu mengakses pengadilan. Solusi yang paling sesuai dengan prinsip peradilan yang adil adalah...",
                "options": [
                    "Menyediakan bantuan hukum dan layanan peradilan yang terjangkau",
                    "Menolak perkara tersebut",
                    "Meminta warga menyerah",
                    "Memberikan hak hukum hanya kepada pejabat"
                ],
                "correct": 0,
                "explanation": "Fasilitasi bantuan hukum pro bono dan pembebasan biaya perkara (prodeo) menjamin tidak ada warga yang tertolak mencari keadilan."
            },
            {
                "id": 8,
                "topic": "kasus_ekonomi",
                "topicLabel": "Pemberdayaan Terpadu",
                "difficulty": "Menantang",
                "question": "Pemerintah membuat program pelatihan kerja bagi kelompok rentan dan membantu usaha kecil. Program tersebut terutama mendukung...",
                "options": [
                    "Intervensi terhadap hakim",
                    "Pembatasan informasi publik",
                    "Pemberdayaan ekonomi dan pengurangan kesenjangan",
                    "Penghapusan otonomi daerah"
                ],
                "correct": 2,
                "explanation": "Kombinasi peningkatan keahlian SDM dan permodalan UMKM adalah strategi jitu mengentaskan kemiskinan struktural."
            },
            {
                "id": 9,
                "topic": "kasus_otonomi",
                "topicLabel": "Otonomi & Akuntabilitas",
                "difficulty": "Menantang",
                "question": "Pemerintah daerah diberi kewenangan mengatur layanan lokal, tetapi penggunaan anggarannya tetap diawasi. Hal ini menunjukkan...",
                "options": [
                    "Daerah bebas melanggar hukum",
                    "Pusat harus mengurus semua hal lokal",
                    "Tidak adanya kemandirian daerah",
                    "Otonomi daerah yang disertai akuntabilitas"
                ],
                "correct": 3,
                "explanation": "Kewenangan luas dalam otonomi daerah harus senantiasa diimbangi dengan transparansi dan pengawasan akuntabilitas keuangan negara."
            },
            {
                "id": 10,
                "topic": "kasus_holistik",
                "topicLabel": "Esensi Demokrasi Pancasila",
                "difficulty": "Menantang",
                "question": "Manakah kebijakan yang paling mencerminkan demokrasi secara menyeluruh?",
                "options": [
                    "Pemerintah membatasi kritik, menutup data, dan memusatkan kekuasaan",
                    "Pemerintah melindungi HAM, menegakkan hukum secara independen, melibatkan warga, dan mengupayakan kesejahteraan yang adil",
                    "Pemerintah hanya mengejar pertumbuhan ekonomi",
                    "Pemerintah memberi hak istimewa kepada kelompok mayoritas"
                ],
                "correct": 1,
                "explanation": "Demokrasi Pancasila yang paripurna menyatukan perlindungan HAM, supremasi hukum yang independen, partisipasi rakyat, dan keadilan sosial kemakmuran bersama."
            }
        ]
    }
]

badge_templates = [
    {
        "id": lvl["id"],
        "level": lvl["id"],
        "name": lvl["badgeName"],
        "alias": lvl["shortTitle"],
        "image": lvl["badgeImage"],
        "focus": lvl["focus"],
        "desc": lvl["description"],
        "unlockCondition": "Skor >= 80 di " + lvl["name"],
        "unlockLabel": "Minimal 80 Poin"
    }
    for lvl in levels_data
]

# Generate JavaScript content
js_content = f"""// Data Soal, Topik, 8 Level Badge, dan Realtime Manager untuk Demokrasi Challenge
// Materi: LKS Pendidikan Pancasila Kelas XI Hal 50-52 (8 Level x 10 Soal = 80 Soal)
// ALL DATA IS REALTIME — backed by localStorage, starts from zero for new users

const QUIZ_DATA = {{
    title: "Demokrasi Challenge",
    subtitle: "Think Smart, Choose Fair, Build Democracy",
    description: "Selamat datang di Demokrasi Challenge! Uji wawasanmu melalui 8 Level progresif dengan 80 soal berbobot dari materi Pendidikan Pancasila Kelas XI.",
    callToAction: "Mulai perjalanan dan kumpulkan 8 lencana kebanggaan!",
    
    // 8 Levels with 10 questions each (80 questions total)
    levels: {json.dumps(levels_data, ensure_ascii=False, indent=4)},

    // 8 Badges matching each Level
    badgeTemplates: {json.dumps(badge_templates, ensure_ascii=False, indent=4)},

    // Helper: get level by id (1-8)
    getLevel(id) {{
        return this.levels.find(lvl => lvl.id === Number(id)) || this.levels[0];
    }},

    // Helper: fallback flat questions for compatibility (Level 1)
    get questions() {{
        return this.levels[0].questions;
    }}
}};

// =============================================================================
// REALTIME DATA MANAGER — All progress and badges backed by localStorage
// =============================================================================
class RealtimeDataManager {{
    constructor() {{
        this.STORAGE_KEYS = {{
            PLAYER_STATS: 'demokrasi_rt_player_stats',
            LEADERBOARD: 'demokrasi_rt_leaderboard',
            GAME_HISTORY: 'demokrasi_rt_game_history',
            LEVEL_PROGRESS: 'demokrasi_rt_level_progress'
        }};
    }}

    // --- Player Stats ---
    getPlayerStats() {{
        const raw = localStorage.getItem(this.STORAGE_KEYS.PLAYER_STATS);
        if (!raw) {{
            return {{
                coins: 0,
                totalXP: 0,
                totalGames: 0,
                totalCorrect: 0,
                totalWrong: 0,
                bestScore: 0,
                bestStreak: 0,
                perfectGames: 0,
                totalLearningSeconds: 0,
                level: 1,
                lastPlayedDate: null
            }};
        }}
        return JSON.parse(raw);
    }}

    savePlayerStats(stats) {{
        localStorage.setItem(this.STORAGE_KEYS.PLAYER_STATS, JSON.stringify(stats));
    }}

    // --- Level Progress (8 Levels) ---
    getLevelProgress() {{
        const raw = localStorage.getItem(this.STORAGE_KEYS.LEVEL_PROGRESS);
        let progress = {{}};
        if (raw) {{
            try {{
                progress = JSON.parse(raw);
            }} catch (e) {{
                progress = {{}};
            }}
        }}

        // Ensure all 8 levels are defined
        for (let i = 1; i <= 8; i++) {{
            if (!progress[i]) {{
                progress[i] = {{
                    levelId: i,
                    unlocked: i === 1, // Level 1 is always unlocked initially
                    passed: false,     // Passed if score >= 80
                    bestScore: 0,
                    bestCorrect: 0,
                    attempts: 0,
                    lastPlayed: null
                }};
            }}
        }}
        return progress;
    }}

    saveLevelProgress(progress) {{
        localStorage.setItem(this.STORAGE_KEYS.LEVEL_PROGRESS, JSON.stringify(progress));
    }}

    isLevelUnlocked(levelId) {{
        const progress = this.getLevelProgress();
        return !!progress[levelId]?.unlocked;
    }}

    isLevelPassed(levelId) {{
        const progress = this.getLevelProgress();
        return !!progress[levelId]?.passed;
    }}

    // Record game result for a specific level
    recordLevelGameResult(levelId, result) {{
        const numLevel = Number(levelId);
        const stats = this.getPlayerStats();
        const progress = this.getLevelProgress();

        // 1. Update general player stats
        stats.totalGames++;
        stats.totalCorrect += result.correctCount;
        stats.totalWrong += (result.totalQuestions - result.correctCount);
        stats.totalLearningSeconds += (result.learningSeconds || 0);

        const gameScore = result.score;
        const gameXP = gameScore * 10;
        stats.totalXP += gameXP;

        if (gameScore > stats.bestScore) stats.bestScore = gameScore;
        if (result.maxStreak > stats.bestStreak) stats.bestStreak = result.maxStreak;
        if (result.correctCount === result.totalQuestions) stats.perfectGames++;

        // Earn coins (e.g. 1 coin per 2 points)
        const earnedCoins = Math.max(5, Math.round(gameScore / 2));
        stats.coins += earnedCoins;

        // Player level derived from badges earned & games played
        const passedCount = Object.values(progress).filter(p => p.passed).length;
        stats.level = Math.min(10, Math.max(1, passedCount + 1));
        stats.lastPlayedDate = new Date().toISOString();
        this.savePlayerStats(stats);

        // 2. Update level progress
        const lvlData = progress[numLevel] || {{
            levelId: numLevel,
            unlocked: true,
            passed: false,
            bestScore: 0,
            bestCorrect: 0,
            attempts: 0
        }};

        lvlData.attempts = (lvlData.attempts || 0) + 1;
        lvlData.lastPlayed = new Date().toISOString();

        if (gameScore > (lvlData.bestScore || 0)) {{
            lvlData.bestScore = gameScore;
            lvlData.bestCorrect = result.correctCount;
        }}

        // Badge requirement: score >= 80 points
        const isPassedNow = gameScore >= 80;
        let newlyUnlockedNext = false;
        let newlyEarnedBadge = false;

        if (isPassedNow) {{
            if (!lvlData.passed) {{
                lvlData.passed = true;
                newlyEarnedBadge = true;
            }}
            // Unlock next level if available
            if (numLevel < 8) {{
                const nextLvl = progress[numLevel + 1];
                if (nextLvl && !nextLvl.unlocked) {{
                    nextLvl.unlocked = true;
                    newlyUnlockedNext = true;
                }}
            }}
        }}

        progress[numLevel] = lvlData;
        this.saveLevelProgress(progress);

        return {{
            stats,
            levelProgress: progress,
            earnedCoins,
            gameXP,
            passed: isPassedNow,
            newlyEarnedBadge,
            newlyUnlockedNext,
            levelId: numLevel
        }};
    }}

    // Fallback for recordGameResult (default Level 1)
    recordGameResult(result) {{
        return this.recordLevelGameResult(1, result);
    }}

    // --- Leaderboard ---
    getLeaderboard() {{
        const raw = localStorage.getItem(this.STORAGE_KEYS.LEADERBOARD);
        if (!raw) return [];
        try {{
            return JSON.parse(raw);
        }} catch(e) {{
            return [];
        }}
    }}

    saveLeaderboard(entries) {{
        localStorage.setItem(this.STORAGE_KEYS.LEADERBOARD, JSON.stringify(entries));
    }}

    updateLeaderboard(playerName, playerAbsen, score, correctCount, totalQuestions, levelId = 1) {{
        let entries = this.getLeaderboard();
        const pName = (playerName || 'Pemain Baru').trim();
        const pAbsen = playerAbsen || '-';
        const playerKey = `${{pName.toLowerCase()}}_${{pAbsen}}`;

        const existingIdx = entries.findIndex(e => e.key === playerKey);

        if (existingIdx >= 0) {{
            const existing = entries[existingIdx];
            // Cumulative or highest score
            if (score > existing.score) {{
                existing.score = score;
                existing.correctCount = correctCount;
                existing.totalQuestions = totalQuestions;
                existing.lastPlayed = new Date().toISOString();
                existing.highestLevel = Math.max(existing.highestLevel || 1, levelId);
            }}
            existing.gamesPlayed = (existing.gamesPlayed || 0) + 1;
        }} else {{
            entries.push({{
                key: playerKey,
                name: pName,
                absen: pAbsen,
                score: score,
                correctCount: correctCount,
                totalQuestions: totalQuestions,
                highestLevel: levelId,
                gamesPlayed: 1,
                lastPlayed: new Date().toISOString()
            }});
        }}

        // Sort descending by score, then by correctCount
        entries.sort((a, b) => {{
            if (b.score !== a.score) return b.score - a.score;
            return b.correctCount - a.correctCount;
        }});

        entries = entries.slice(0, 50);
        this.saveLeaderboard(entries);
        return entries;
    }}

    // --- Badges (1:1 with 8 Levels) ---
    getBadges() {{
        const progress = this.getLevelProgress();
        return QUIZ_DATA.badgeTemplates.map(template => {{
            const lvl = progress[template.id] || {{ unlocked: template.id === 1, passed: false, bestScore: 0 }};
            const unlocked = !!lvl.passed; // Badge is unlocked when level is passed (score >= 80)
            
            let progressLabel = "Terkunci";
            if (lvl.passed) {{
                progressLabel = `Lulus ⭐ (Skor ${{lvl.bestScore}}/100)`;
            }} else if (lvl.unlocked) {{
                if (lvl.attempts > 0) {{
                    progressLabel = `Coba Lagi (Skor ${{lvl.bestScore}}/100)`;
                }} else {{
                    progressLabel = "Tantangan Terbuka";
                }}
            }} else {{
                progressLabel = `Luluskan Level ${{template.id - 1}}`;
            }}

            return {{
                ...template,
                levelId: template.id,
                isLevelUnlocked: lvl.unlocked,
                unlocked: unlocked,
                bestScore: lvl.bestScore || 0,
                progress: progressLabel
            }};
        }});
    }}

    getUnlockedBadgeCount() {{
        return this.getBadges().filter(b => b.unlocked).length;
    }}

    // --- Game History ---
    getGameHistory() {{
        const raw = localStorage.getItem(this.STORAGE_KEYS.GAME_HISTORY);
        if (!raw) return [];
        try {{
            return JSON.parse(raw);
        }} catch(e) {{
            return [];
        }}
    }}

    addGameToHistory(result) {{
        const history = this.getGameHistory();
        history.push({{
            date: new Date().toISOString(),
            levelId: result.levelId || 1,
            score: result.score,
            correctCount: result.correctCount,
            totalQuestions: result.totalQuestions,
            maxStreak: result.maxStreak,
            learningSeconds: result.learningSeconds
        }});
        const trimmed = history.slice(-100);
        localStorage.setItem(this.STORAGE_KEYS.GAME_HISTORY, JSON.stringify(trimmed));
    }}

    // --- Ranking Percentage ---
    getTopRankingPercent(playerName, playerAbsen) {{
        const entries = this.getLeaderboard();
        if (entries.length === 0) return "—";

        const pName = (playerName || '').toLowerCase().trim();
        const pAbsen = playerAbsen || '-';
        const playerKey = `${{pName}}_${{pAbsen}}`;
        const playerIdx = entries.findIndex(e => e.key === playerKey);

        if (playerIdx < 0) return "—";

        const rank = playerIdx + 1;
        const total = entries.length;

        if (rank === 1) return "🥇 #1";
        if (rank === 2) return "🥈 #2";
        if (rank === 3) return "🥉 #3";

        const percent = ((rank / total) * 100).toFixed(1);
        return `Top ${{percent}}%`;
    }}

    // Clear all data
    clearAllData() {{
        Object.values(this.STORAGE_KEYS).forEach(key => localStorage.removeItem(key));
        localStorage.removeItem('demokrasi_player_name');
        localStorage.removeItem('demokrasi_player_absen');
        localStorage.removeItem('demokrasi_player_coins');
        localStorage.removeItem('demokrasi_seen_onboarding');
    }}
}}

// Global instance
const realtimeData = new RealtimeDataManager();
"""

with open(r"c:\quiziz\js\quiz-data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("Successfully written c:\\quiziz\\js\\quiz-data.js with all 80 questions and 8 badges!")
