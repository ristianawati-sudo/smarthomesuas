# model_trainer.py (Orang 1 - Data Scientist)
# Tujuan: Melatih model prediksi dan menyimpannya.

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

print("--- FASE 2: PELATIHAN MODEL DIMULAI ---")

# --- 1. GENERASI DATA SIMULASI ---
np.random.seed(42)
N = 1000
data = pd.DataFrame({
    'Suhu_Luar': np.random.uniform(20, 40, N),
    'Kelembaban': np.random.uniform(40, 80, N),
    'Jam_Hari': np.random.randint(0, 24, N),
    'Status_AC': np.random.randint(0, 2, N), # 0=Mati, 1=Menyala
})

# Logika Sederhana untuk Suhu Ruangan:
data['Suhu_Ruangan'] = (
    10 + 0.5 * data['Suhu_Luar'] + 
    0.1 * data['Kelembaban'] - 
    3 * data['Status_AC'] + 
    np.random.normal(0, 1.5, N) 
)
data['Suhu_Ruangan'] = np.clip(data['Suhu_Ruangan'], 22, 35)

print(f"Dataset berhasil dibuat. Jumlah baris: {len(data)}")

# --- 2. PERSIAPAN DATA ---
X = data[['Suhu_Luar', 'Kelembaban', 'Jam_Hari', 'Status_AC']]
y = data['Suhu_Ruangan']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalisasi/Scaling Data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# --- 3. PELATIHAN MODEL ---
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)
print("Model Random Forest berhasil dilatih.")

# --- 4. EVALUASI MODEL ---
y_pred = model.predict(X_test_scaled)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("-" * 40)
print(f"MAE (Mean Absolute Error) pada Data Uji: {mae:.2f}°C")
print(f"R-squared Score: {r2:.2f}")

# --- 5. PENYIMPANAN MODEL DAN SCALER ---
try:
    joblib.dump(model, 'random_forest_model.pkl')
    joblib.dump(scaler, 'scaler.pkl')
    print("\nSUCCESS: Model dan Scaler berhasil disimpan sebagai 'random_forest_model.pkl' dan 'scaler.pkl'")
except Exception as e:
    print(f"\nERROR: Gagal menyimpan file. Pastikan Anda memiliki hak akses folder. Detail: {e}")

print("--- FASE 2 SELESAI ---")