from ETL.Extract import scrap_saham
from ETL.Transform import transform
from ETL.Load import Load

def main():
    try:
        # Parameter
        saham = "GOTO.JK"
        start_date = "2023-01-01"
        nama_file = "goto_stock"

        # Proses pengambilan, transformasi, dan penyimpanan data
        print("Mengambil data saham...")
        raw_data = scrap_saham(start=start_date, saham=saham)
        
        if raw_data is not None:
            print("Membersihkan data...")
            clean_data = transform(raw_data)
            
            print("Menyimpan data...")
            result = Load(clean_data, nama=nama_file)
            print(result)
        else:
            print("Proses dihentikan karena data gagal diambil.")
    
    except ValueError as ve:
        print(f"Kesalahan input: {str(ve)}")
    except Exception as e:
        print(f"Kesalahan tak terduga: {str(e)}")

# Jalankan fungsi utama
if __name__ == "__main__":
    main()