# 📈 Prediksi Harga Saham GOTO (LSTM Model)

Proyek ini bertujuan untuk memprediksi harga saham PT GoTo Gojek Tokopedia Tbk (GOTO) menggunakan model Long Short-Term Memory (LSTM) berbasis time series. Proyek ini menggunakan data historis dari Yahoo Finance dan bertujuan membantu pengambilan keputusan investasi secara data-driven.

---

## 📊 Dataset

- Sumber: [Yahoo Finance](https://finance.yahoo.com/quote/GOTO.JK/)
- Periode: 2 Januari 2023 – 22 Mei 2025
- Fitur: `Date`, `Close`, `Open`, `High`, `Low`, `Volume`
- Fokus: Kolom `Close` sebagai target utama

---

## ⚙️ Alur Pemodelan

1. **Preprocessing**:
   - Hapus outlier (IQR)
   - Min-max scaling
   - Transformasi windowing 6-langkah (X: x1–x6, y: target)
   - Reshape untuk input LSTM `(samples, timesteps, features)`

2. **Model LSTM**:
   - 2 LSTM layer (100 & 80 units)
   - Dense layer (50 units)
   - Dropout (10–20%)
   - Optimizer: Adam
   - Loss: MSE
   - Epochs: 100 | Batch size: 16

---

## 🧪 Evaluasi

| Metrik | Nilai  |
|--------|--------|
| MAE    | 2.18   |
| RMSE   | 3.12   |

Model menunjukkan performa akurat dan stabil dalam memprediksi harga saham jangka pendek.
