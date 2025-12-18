# Prediksi Suhu Ruangan Menggunakan Machine Learning

Proyek ini bertujuan untuk memprediksi suhu di dalam ruangan berdasarkan parameter lingkungan tertentu (seperti kelembapan, suhu luar ruangan, atau waktu) menggunakan algoritma Regresi.

## 👥 Anggota Kelompok
| No | Nama Lengkap | NIM | Branch | Jobdesk |
|----|--------------|-----|--------|---------|
| 1  | Ristianawati   | M0125025 | `feature-modeling` | Membangun model machine learning seperti model_trainer.py, dataset yang digunakan, requirements.txt, dsb.  |
| 2  | Devi Aprilia Mulyani | M0125011 | `feature-backend`| Pembuatan API agar model bisa diakses oleh web seperti server.py, index.html, javascript  |
| 3  | Remalya Rafa | M0125024 | `feature-docs`     | Dokumentasi & pembuatan README |

## 🛠️ Alur Kolaborasi (Git Flow)
Kami menggunakan metode Git Flow sederhana untuk berkolaborasi:
* **Main Branch**: Kode final yang siap dikumpulkan.
* **Feature Branch**: Setiap anggota membuat cabang (branch) sendiri untuk mengerjakan tugasnya (contoh: `feature-cleaning`, `feature-modeling`).
* **Pull Request**: Setelah tugas selesai, anggota melakukan *request* untuk menggabungkan kodenya ke cabang utama setelah dicek bersama.
  
## 📊 Dataset
Dataset yang digunakan berisi catatan suhu ruangan dalam rentang waktu tertentu. Fitur-fitur utamanya meliputi:
* `Suhu Luar (°C)`: Suhu di luar ruangan sebagai pembanding
* `Kelembapan (%)`: Tingkat kelembapan udara
* `Jam (0-23)`: Waktu saat ingin memprediksi suhu ruang
* `Status AC` : AC mati/hidup
  
## 🛠️ Langkah-Langkah Pengerjaan
1. **Data Cleaning**: Membersihkan data dari nilai yang kosong atau error.
2. **Exploratory Data Analysis (EDA)**: Melihat hubungan antara kelembapan dengan kenaikan suhu.
3. **Feature Engineering**: Mempersiapkan data agar siap diproses oleh komputer.
4. **Model Building**: Melatih model menggunakan algoritma (contoh: Linear Regression).
5. **Evaluation**: Menghitung seberapa akurat prediksi model tersebut.

## 📈 Hasil Prediksi
Model ini dievaluasi menggunakan *Mean Squared Error* (MSE). Semakin kecil nilainya, semakin akurat predisinya.
* **Akurasi Model**: [Masukkan angka akurasi kamu, misal: 92%]

## 🚀 Cara Menggunakan
1. Clone repositori ini atau download file `.ipynb`.
2. Buka melalui **Google Colab**.
3. Pastikan kamu sudah mengunggah file dataset (`.csv`) ke dalam Colab.
4. Klik **Runtime > Run All** untuk melihat hasilnya.
