# Laporan Proyek Machine Learning - Rivaldy Arrayan Yuwono

## Domain Proyek

PT GoTo Gojek Tokopedia Tbk (GOTO) merupakan hasil merger antara dua perusahaan teknologi besar di Indonesia, yaitu Gojek dan Tokopedia. Sebagai salah satu unicorn terbesar di Asia Tenggara, GOTO memiliki peran strategis dalam ekosistem digital Indonesia melalui layanan transportasi, e-commerce, dan keuangan digital. Sejak melantai di Bursa Efek Indonesia (BEI) pada tahun 2022, harga saham GOTO menunjukkan volatilitas yang cukup tinggi, mencerminkan ketidakpastian pasar terhadap kinerja fundamental dan prospek bisnis perusahaan.

Pergerakan harga saham GOTO dipengaruhi oleh berbagai faktor, termasuk kondisi keuangan perusahaan, sentimen investor, arah strategi bisnis, serta dinamika makroekonomi global dan domestik. Situasi tersebut menimbulkan tantangan bagi para pemangku kepentingan—baik investor, manajemen perusahaan, maupun analis pasar—dalam membuat keputusan yang tepat dan berdasarkan data. Salah satu pendekatan yang dapat digunakan untuk mengantisipasi ketidakpastian ini adalah melalui forecasting atau peramalan harga saham berbasis data historis.

Metode forecasting menggunakan pendekatan statistik dan machine learning terbukti mampu mengidentifikasi pola pergerakan harga saham secara lebih objektif. Dengan memanfaatkan data historis harga saham GOTO dan algoritma prediktif, analisis ini dapat memberikan wawasan yang berguna bagi investor dalam menentukan strategi beli atau jual, bagi manajemen dalam menyusun kebijakan perusahaan, serta bagi analis dalam menilai dampak faktor eksternal terhadap kinerja saham.

Kebutuhan terhadap forecasting semakin relevan mengingat adanya kejadian tertentu, seperti unjuk rasa pengemudi ojek online (ojol) pada 20 Mei 2025, yang berpotensi memengaruhi persepsi pasar terhadap GOTO. Peristiwa semacam ini dapat meningkatkan kehati-hatian investor dan memperkuat urgensi penggunaan model prediksi untuk mendukung pengambilan keputusan yang lebih terukur. Data yang digunakan dalam analisis ini diperoleh dari situs keuangan terpercaya, yaitu Yahoo Finance.

## Business Understanding
### Problem Statements
Menjelaskan pernyataan masalah latar belakang:
1. Bagaimana pola historis pergerakan harga saham PT GoTo Gojek Tokopedia Tbk (GOTO) dalam periode tertentu?
2. Seberapa akurat hasil prediksi harga saham GOTO dibandingkan dengan data aktualnya?
3. Bagaimana hasil forecasting dapat digunakan sebagai dasar pengambilan keputusan oleh investor atau manajemen perusahaan?

### Goals
Menjelaskan tujuan dari pernyataan masalah:
1. Menganalisis pola dan tren historis harga saham GOTO berdasarkan data pasar yang tersedia.
2. Membangun model forecasting yang mampu memprediksi harga saham GOTO dengan akurasi yang baik menggunakan pendekatan statistik atau machine learning.
3. Memberikan rekomendasi berbasis data yang dapat dimanfaatkan oleh investor dan manajemen perusahaan dalam pengambilan keputusan strategis.

### Solution statements
- Penelitian ini memanfaatkan algoritma LSTM (Long-Short Term Memory) yang mampu mengenali pola jangka panjang pada data time series. Kemudian untuk meningkatkan akurasi prediksi, digunakan optimalisasi dengan Adam.
- Hasil forecasting diukur dengan RMSE (Root Mean Square Error) dan MAE (Mean Abolute Error) agar dapat dibandingkan secara kuantitatif dan terukur.

## Data Understanding
Dataset yang digunakan pada penelitian ini adalah data historis harga saham PT GOTO mulai dari tanggal 2 Januari 2023 sampai 22 Mei 2025 dan hanya selama jam perdagangan setiap hari bursa (senin, selasa, rabu, kamis, jumat) dikarenakan pada hari sabtu dan minggu tidak ada transaksi saham yang dilakukan. Dataset ini diperoleh melalui proses ETL sederhana dari sumber pasar modal yahoo finance (source : "https://finance.yahoo.com/quote/GOTO.JK/"). Kemudian, dataset disimpan dalam file `goto_stock.csv`. Dataset yang telah didapatkan terdiri dari 562 baris dengan 2 kolom, yaitu "Close" dan "Date" dengan kondisi awal tidak terdapat missing value atau duplikasi. Namun, terdapat satu oulier. 

### Variabel-variabel pada dataset harga saham GOTO adalah sebagai berikut:
- Date: Merujuk pada tanggal atau waktu spesifik ketika data harga saham direkam.
- Close: Menunjukkan harga penutupan saham pada akhir sesi perdagangan di hari tersebut.
- Open: Menunjukkan harga pembukaan saham di awal sesi perdagangan pada hari tersebut.
- High: Merujuk pada harga tertinggi yang dicapai oleh saham selama sesi perdagangan pada hari tersebut.
- Low: Menunjukkan harga terendah yang dicapai saham selama sesi perdagangan pada hari tersebut.
- Volume: Menunjukkan jumlah saham yang diperdagangkan selama sesi perdagangan pada hari tersebut.
Dalam penelitian ini, peneliti menggunakan analisis deskriptif, seperti mean, modus, dan median, untuk memahami data.

## Data Preparation
Dalam penelitian ini, proses persiapan data dilakukan dengan beberapa langkah strategis untuk mendukung akurasi prediksi harga saham dalam konteks analisis time series sebagai berikut: 
1. Peneliti memilih untuk mempertahankan hanya variabel "Close" dan "Date" sambil membuang variabel lainnya, karena kedua variabel ini diidentifikasi memiliki pengaruh paling signifikan terhadap prediksi harga saham berdasarkan analisis awal atau korelasi data. Variabel "Close" mencerminkan harga penutupan saham yang merupakan indikator utama dalam forecasting, sedangkan "Date" yang telah dikonversi datetime menyediakan konteks temporal yang esensial untuk analisis deret waktu.
2. Karena pada kondisi awal terdapat satu outlier pada data yang dibuktikan dengan menggunakan metode interquartile range (IQR). Peneliti mengatasi outlier ini dengan menggantinya dengan nilai median, karena ini merupakan pendekatan yang sangat umum dan efektif, terutama dalam situasi untuk menjaga stabilitas data tanpa menghapus baris.
3. Mengambil nilai dari kolom "Close" dan melakukan reshaping guna memastikan bahwa dimensi data yang akan digunakan untuk peramalan sudah sesuai, yaitu 1 kolom dan 562 baris. 
4. Normalisasi min-max diterapkan pada kolom "Close" untuk mengubah rentang nilai ke skala [0,1], sehingga meminimalkan bias akibat skala data yang berbeda, mempercepat proses komputasi, dan meningkatkan stabilitas serta performa model prediksi, terutama pada algoritma yang sensitif terhadap skala data seperti jaringan saraf tiruan atau regresi.
5. Kolom "Close" diubah menjadi enam kolom fitur (x1, x2, x3, x4, x5, x6) dan satu kolom target (y) berdasarkan teori time series, dengan tujuan menangkap pola historis dan ketergantungan temporal dalam data, yang penting untuk membangun model prediksi yang robust. Langkah ini memungkinkan model untuk mempelajari tren dan pola dari data sebelumnya secara efektif.
6. Membuat variabel "X" yang merupakan kolom fitur (x1, x2, x3, x4, x5, x6), kemudian dilakukan pemisahan antara fitur (X) dan target (y) dari data setelah proses windowing. Kolom target yang berisi nilai yang ingin diprediksi, yaitu 'y', dipisahkan dari data, sementara kolom-kolom lainnya digunakan sebagai fitur input (x1, x2, x3, x4, x5, x6). Kedua bagian data ini kemudian dikonversi ke dalam bentuk array NumPy agar dapat digunakan sebagai input pada algoritma pembelajaran mesin yang umumnya membutuhkan format array numerik sebagai input dan output.
7. Melakukan proses reshape terhadap kolom fitur (X) ke dalam bentuk tiga dimensi menggunakan format (samples, timesteps, features). Transformasi ini diperlukan karena model berbasis Recurrent Neural Network (seperti LSTM) mengharuskan input memiliki dimensi tiga untuk dapat mengenali struktur sekuensial dari data. Dimensi pertama merepresentasikan jumlah sampel, dimensi kedua menunjukkan jumlah langkah waktu (timestep) dalam setiap sampel, dan dimensi ketiga menyatakan jumlah fitur yang tersedia di setiap langkah waktu. Jika reshape tidak dilakukan, model tidak akan mengenali pola berurutan dalam data, sehingga proses pelatihan tidak dapat berjalan sebagaimana mestinya.
8. Data dibagi menjadi data pelatihan dan data pengujian dengan rasio 80:20 terhadap kolom fitur dan target. Dimana 80% indeks data pertama merupakan data latih dan 20% menjadi data tes.

## Modeling
**Arsitektur Model**
Model yang digunakan peneliti adalah jaringan saraf tiruan berbasis Long Short-Term Memory (LSTM), yang dirancang untuk menangani data sekuensial dengan mempertahankan informasi jangka panjang dan mengatasi peluruhan gradien. LSTM memiliki mekanisme cell state sebagai memori utama dan tiga gerbang utama—forget gate, input gate, dan output gate—yang bekerja secara dinamis dalam mengelola informasi sepanjang urutan waktu. Forget gate bertanggung jawab untuk menentukan apakah informasi lama harus dipertahankan atau dihapus berdasarkan fungsi aktivasi sigmoid, sementara input gate mengontrol pembaruan cell state dengan kombinasi sigmoid dan tanh, menghasilkan kandidat nilai baru yang dapat ditambahkan ke dalam memori utama. Setelah cell state diperbarui, output gate menentukan bagian informasi yang akan digunakan sebagai hidden state untuk pemrosesan lebih lanjut. Arsitektur model ini terdiri dari dua lapisan LSTM, di mana lapisan pertama memiliki 100 unit dengan return_sequences=True, sehingga outputnya tetap berupa urutan yang bisa diproses oleh lapisan LSTM berikutnya, sementara lapisan kedua memiliki 80 unit tanpa return_sequences, yang hanya menghasilkan satu output pada langkah terakhir. Kedua lapisan menggunakan fungsi aktivasi tanh untuk menangkap pola non-linear dan menjaga stabilitas gradien, sementara lapisan Dense dengan 50 unit menggunakan fungsi aktivasi ReLU untuk meningkatkan kemampuan model dalam menangkap fitur yang lebih kompleks. Selain itu, beberapa lapisan dropout dengan tingkat 20% dan 10% diterapkan untuk meningkatkan generalisasi dan mengurangi risiko overfitting. Model dikompilasi dengan fungsi loss Mean Squared Error (MSE) dan menggunakan Adam optimizer untuk pembelajaran yang lebih efisien berbasis gradien. Selama pelatihan, model dilatih dengan 100 epoch dan batch size 16, menggunakan data validasi untuk memonitor kinerjanya. Evaluasi akhir dilakukan dengan menghitung Mean Absolute Error (MAE) guna mengukur seberapa baik prediksi model dibandingkan dengan data aktual. Dengan arsitektur ini, model memiliki kapabilitas yang baik untuk menangani tugas regresi dalam data deret waktu, mempertahankan hubungan temporal dalam data, serta menghasilkan hasil prediksi yang lebih akurat.

**Kelebihan Model**
- Menangani Ketergantungan Jangka Panjang: Mampu mempelajari dan mempertahankan informasi dari urutan data yang panjang, ideal untuk data time series.
- Cocok untuk Data Time Series: Efektif dalam menangkap pola temporal dan hubungan antar-data berurutan.
- Mengatasi Vanishing Gradient: Struktur gerbang LSTM meminimalkan masalah vanishing gradient, memungkinkan pelatihan yang lebih stabil dibandingkan RNN standar.

**Kekurangan Model**
- Komputasi Intensif: Memerlukan sumber daya komputasi besar dan waktu pelatihan yang lama, terutama pada dataset besar.
Penyesuaian Hyperparameter: Banyaknya hyperparameter memerlukan tuning yang cermat untuk mencapai performa optimal.
- Risiko Overfitting: Model dapat overfit jika data terbatas atau arsitektur terlalu kompleks tanpa regularisasi yang memadai.

**Penyesuaian Hyperparameter**
- Optimizer: Adam, dipilih karena memiliki keunggulan dalam menangani data sekuensial dan memastikan pembaruan bobot yang efisien selama proses pelatihan.

## Evaluation
Dalam penelitian ini, metrik evaluasi Mean Absolute Error (MAE) dan Root Mean Square Error (RMSE) digunakan untuk mengukur tingkat akurasi model prediksi. Kedua metrik ini dipilih karena kesesuaiannya dengan kasus peramalan (forecasting), yang memerlukan pengukuran error yang andal dan mudah diinterpretasikan.

- Mean Absolute Error (MAE): Metrik ini menghitung rata-rata absolut dari selisih antara nilai prediksi dan nilai aktual, memberikan gambaran yang jelas tentang besarnya kesalahan prediksi tanpa mempertimbangkan arah kesalahan. MAE intuitif dan robust terhadap data dengan distribusi yang bervariasi.
- Root Mean Square Error (RMSE): Metrik ini menghitung akar kuadrat dari rata-rata kuadrat selisih antara nilai prediksi dan nilai aktual, memberikan bobot lebih besar pada kesalahan yang lebih signifikan. RMSE sangat berguna untuk mengevaluasi performa model pada data time series karena sensitivitasnya terhadap outlier.

Pemilihan MAE dan RMSE memungkinkan evaluasi menyeluruh terhadap performa model, dengan MAE memberikan ukuran error yang linear dan RMSE menyoroti dampak kesalahan besar, sehingga mendukung analisis yang komprehensif dalam konteks peramalan.

Hasil dari metrik evaluasi pada penelitian ini adalah nilai MAE sebesar 2.18 dan nilai RMSE sebesar 3.12 artinya nilai RMSE dan MAE yang cukup kecil ini menunjukkan bahwa model LSTM mampu memberikan hasil prediksi yang akurat dan layak untuk digunakan sebagai dasar analisis pergerakan harga saham GOTO.