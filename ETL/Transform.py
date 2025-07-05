from datetime import datetime

def transform(data):
    # Validasi input
    if data is None or data.empty:
        raise ValueError("Data tidak boleh kosong.")
    
    if 'Close' not in data.columns:
        raise ValueError("Kolom 'Close' tidak ditemukan dalam data.")
    
    # Reset indeks untuk menjadikan 'Date' sebagai kolom
    cleanData = data.reset_index()[['Date', 'Close']]
    cleanData['Date'] = cleanData['Date'].dt.date
    
    return cleanData