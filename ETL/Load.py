def Load(data, nama=""):
    # Validasi input
    if data is None or data.empty:
        raise ValueError("Data tidak boleh kosong.")
    if not nama:
        raise ValueError("Nama file harus diisi.")
    
    # Buat nama file dengan ekstensi .csv
    nama_file = f"{nama}.csv"
    
    # Simpan data ke file CSV
    data.to_csv(nama_file, index=True)