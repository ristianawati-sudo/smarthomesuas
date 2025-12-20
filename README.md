# 🏠 Smart-Temp Predictor: Sistem Prediksi Suhu Ruangan Berbasis AI

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

## 📝 Deskripsi Proyek
Proyek ini merupakan implementasi Machine Learning yang bertujuan untuk memprediksi suhu ruangan secara cerdas (Smart-Temp Prediction). Di tengah meningkatnya kebutuhan akan efisiensi energi, sistem ini dirancang untuk memberikan estimasi suhu ruangan yang paling nyaman berdasarkan kondisi lingkungan sekitar.
Masalah yang Diselesaikan:
a. Efisiensi Energi: Mengurangi penggunaan AC yang berlebihan dengan memprediksi kebutuhan suhu yang tepat.
b. Kenyamanan Otomatis: Memberikan data dasar bagi sistem Smart Home untuk mengatur suhu ruangan secara otomatis tanpa campur tangan manusia.
Teknologi & Algoritma:
a. Algoritma: Menggunakan Random Forest Regressor, sebuah metode Ensemble Learning yang sangat kuat untuk menangani data yang kompleks dan memberikan hasil prediksi yang stabil.
b. Backend: Menggunakan Flask (Python) sebagai API untuk menjembatani model cerdas dengan antarmuka pengguna.
c. Frontend: Dibangun dengan HTML5, CSS3, dan JavaScript agar sistem dapat diakses melalui browser secara interaktif.

Proyek ini disusun untuk memenuhi kriteria Ujian Akhir Semester (UAS) mata kuliah Pengantar Kecerdasan Buatan dengan menerapkan standar pengembangan perangkat lunak modern. Seluruh proses kolaborasi tim dikelola melalui platform GitHub, memanfaatkan fitur branching, konsistensi riwayat commit, serta mekanisme pull request untuk memastikan integrasi kode yang bersih dan terdokumentasi dengan baik.

**Tema Machine Learning: Smart Homes**

---

## 👥 Nama Anggota Kelompok & Bukti Kolaborasi
| Nama | NIM | Branch | Jobdesk |
| :--- | :--- | :--- | :--- |
| Ristianawati | M0125025 | **feature-modeling** | Membangun model Machine Learning seperti model-trainer.py, dataset yang digunakan, requirements.txt, pembuatan README |
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

### 1. Persyaratan Sistem
Pastikan Python sudah terinstal di komputer Anda. Instal semua library yang dibutuhkan dengan menjalankan perintah berikut di terminal:
pip install flask flask-cors pandas scikit-learn joblib
### 2. Melatih Model (Opsional)
Jika Anda ingin melatih ulang model dengan data terbaru, jalankan script trainer:
python model_trainer.py
Langkah ini akan memperbarui file random_forest_model.pkl dan scaler.pkl.
### 3. Menjalankan Server API (Backend)
Jalankan server Flask agar sistem siap menerima permintaan prediksi:
python app.py
Pastikan terminal menampilkan status Running on http://127.0.0.1:5000.
### 3. Mengakses Antarmuka (Frontend)
Buka file index.html menggunakan browser (Chrome/Edge).
Masukkan data parameter suhu dan klik tombol Prediksi.
