from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app) # PENTING: Mengizinkan akses dari browser

# Load model & scaler
try:
    model = joblib.load('random_forest_model.pkl')
    scaler = joblib.load('scaler.pkl')
    print("✅ AI Model Siap!")
except Exception as e:
    print(f"❌ Error Load Model: {e}")

@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        # Ambil data dari JSON yang dikirim website
        input_df = pd.DataFrame([{
            'Suhu_Luar': float(data['suhu_luar']),
            'Kelembaban': float(data['kelembaban']),
            'Jam_Hari': int(data['jam']),
            'Status_AC': int(data['status_ac'])
        }])
        
        # Prediksi
        input_scaled = scaler.transform(input_df)
        prediksi = model.predict(input_scaled)
        
        return jsonify({
            'status': 'success',
            'hasil': round(float(prediksi[0]), 2)
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

if __name__ == '__main__':
    print("🚀 Server Jalan di http://127.0.0.1:5000")
    app.run(debug=True, port=5000)