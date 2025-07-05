import yfinance as yf
from datetime import datetime

def scrap_saham(start="", saham="", end=None):
    # Validasi parameter
    if not saham:
        raise ValueError("Kode saham harus diisi.")
    if not start:
        raise ValueError("Tanggal mulai harus diisi (format: 'YYYY-MM-DD').")
    
    try:
        # Ambil data saham
        stock = yf.Ticker(saham)
        # Jika end tidak ditentukan, gunakan tanggal saat ini
        if end is None:
            end = datetime.today().strftime('%Y-%m-%d')
        # Ambil data dari start hingga end
        data = stock.history(start=start, end=end)
        
        # Periksa apakah data kosong
        if data.empty:
            raise ValueError(f"Tidak ada data untuk saham {saham} pada rentang waktu tersebut.")
        
        return data
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")
        return None