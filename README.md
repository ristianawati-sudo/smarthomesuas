# 🏠 Smart-Temp Predictor: Sistem Prediksi Suhu Ruangan Berbasis AI

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

![Github-Prediksi-Suhu-Ruang](https://github.com/user-attachments/assets/4da6ef52-0315-4057-a923-cc5681d32ba9)

## 📝 Deskripsi Proyek
Proyek ini merupakan implementasi Machine Learning yang bertujuan untuk memprediksi suhu ruangan secara cerdas (Smart-Temp Prediction). Di tengah meningkatnya kebutuhan akan efisiensi energi, sistem ini dirancang untuk memberikan estimasi suhu ruangan yang paling nyaman berdasarkan kondisi lingkungan sekitar.

Proyek ini disusun untuk memenuhi kriteria Ujian Akhir Semester (UAS) mata kuliah Pengantar Kecerdasan Buatan dengan menerapkan standar pengembangan perangkat lunak modern. Seluruh proses kolaborasi tim dikelola melalui platform GitHub, memanfaatkan fitur branching, konsistensi riwayat commit, serta mekanisme pull request untuk memastikan integrasi kode yang bersih dan terdokumentasi dengan baik.

**Tema Machine Learning: Smart Homes**

---

## 👥 Nama Anggota Kelompok & Bukti Kolaborasi
| Nama | NIM | Branch | Jobdesk |
| :--- | :--- | :--- | :--- |
| Ristianawati | M0125025 | **feature-modeling** | Membangun model Machine Learning seperti model-trainer.py, dataset yang digunakan, requirements.txt |
| Devi Aprilia Mulyani | M0125011 | **feature-backend** | Pembuatan API agar model bisa diakses oleh web seperti server.py, index.html, javascript |
| Remalya Rafa | M0125024 | **feature-docs** | Dokumentasi & pembuatan README |

---

## 🚀 Fitur Utama
- **Prediksi Real-time:** Mendapatkan hasil suhu ruangan secara instan.
- **Data Driven:** Menggunakan algoritma Random Forest untuk akurasi tinggi.
- **Responsive UI:** Antarmuka web yang mudah digunakan di perangkat apa pun.
- **REST API:** Backend yang siap diintegrasikan dengan perangkat IoT lainnya.

---

## 📊 Spesifikasi Model & Dataset
- **Algoritma:** Random Forest Regressor
- **Fitur Input:**
  - `Suhu_Luar`: Suhu lingkungan luar ruangan (°C).
  - `Kelembaban`: Persentase kelembaban udara (%).
  - `Jam_Hari`: Waktu dalam format 24 jam.
  - `Status_AC`: Status perangkat (Mati/Menyala).
- **Performa Model:**
  - **MAE (Mean Absolute Error):** 1.27°C
  - **R2 Score:** 0.79

---

## 🛠️ Cara Menjalankan Proyek
Ikuti langkah-langkah berikut untuk menjalankan website Prediksi Suhu Ruangan Berbasis AI pada komputer lokal.
1. **Pastikan Python Terinstal**
   
   Periksa versi Python Anda di terminal:
   ```bash
   python --version
   
2. **Clone Repository Proyek**

   Dapatkan file proyek dari GitHub risti-sudo:
   ```bash
   git clone https://github.com/ristianawati-sudo/smarthomesuas.gitbash
   ```
   Atau klik tombol Code > Download ZIP dan ekstrak filenya ke folder komputer Anda.
   
4. **Install Library yang Dibutuhkan**

   Buka terminal/CMD di dalam folder proyek tersebut, lalu instal menggunakan file requirements.txt:
   ```bash
   pip install -r requirements.txt

6. **Jalankan Server Backend**
   ```bash
   python server.py
   ```
   Pastikan terminal menampilkan pesan: --- SERVER SMART HOME AI AKTIF ---.

   Penting: Jangan tutup jendela terminal ini agar website tetap terhubung dengan AI.

7. **Jalankan Dashboard Website**

   a. Buka File Explorer dan masuk ke folder proyek.
   
   b. Temukan file index.html.
   
   c. Klik Kanan pada file tersebut > Open With > Google Chrome (atau browser modern lainnya).
   
   d. Masukkan data sensor pada form, lalu klik tombol "Prediksi Suhu Ruangan".

📂 **Struktur File Utama**

Agar sistem berjalan lancar, pastikan file berikut berada dalam satu folder:

1. server.py: Script Backend Flask.

2. index.html: Antarmuka Dashboard (Frontend).

3. random_forest_model.pkl: Model AI yang sudah dilatih.

4. scaler.pkl: File normalisasi data.

5. requirements.txt: Daftar library pendukung.
   
