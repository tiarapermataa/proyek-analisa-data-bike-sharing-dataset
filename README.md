# Proyek Analisis Data: Tren Penyewaan Sepeda: Mengkaji Pengaruh Suhu dan Hari Libur pada Pengguna Kasual 🚴‍♂️

Proyek bertujuan untuk mengeksplorasi faktor-faktor yang memengaruhi penyewaan sepeda, termasuk musim dengan jumlah penyewaan tertinggi, pengaruh suhu terhadap penyewaan harian dan per jam, serta dampak kondisi cuaca terhadap total penyewaan sepeda, melalui visualisasi bar plot, scatter plot, dan line plot untuk mengidentifikasi pola dan hubungan signifikan.

## Fitur Utama 🚀

- **Pertanyaan Bisnis**: Proyek ini fokus pada dua pertanyaan utama:
  - Bagaimana pengaruh musim terhadap jumlah total pengguna (cnt) yang menggunakan sepeda?
  - Apa pola penggunaan sepeda berdasarkan jam dalam sehari, dan bagaimana faktor cuaca mempengaruhi jumlah pengguna pada jam-jam tertentu?
    
- **Import Data & Wrangling**: Proses memuat, menilai, dan membersihkan data dilakukan secara bertahap, termasuk penghapusan kolom yang tidak diperlukan seperti `instant`.
  
- **Exploratory Data Analysis (EDA)**: Bertujuan untuk mengeksplorasi faktor-faktor yang memengaruhi penyewaan sepeda, termasuk musim dengan jumlah penyewaan tertinggi, pengaruh suhu terhadap penyewaan harian dan per jam, serta dampak kondisi cuaca terhadap total penyewaan sepeda, melalui visualisasi bar plot, scatter plot, dan line plot untuk mengidentifikasi pola dan hubungan signifikan.

- **Regresi Linear**: Proyek ini melakukan analisis regresi linear untuk memodelkan hubungan antara suhu dan jumlah penyewa sepeda harian.

- **Visualisasi Interaktif**: Menggunakan **Streamlit** untuk menghasilkan visualisasi dan analisis interaktif.

## Struktur Proyek 📂

Proyek ini terdiri dari beberapa file dan direktori:

- `notebook.ipynb`: Jupyter Notebook yang berisi analisis mendalam terkait tren penyewaan sepeda.
- `data/`: Direktori yang berisi dataset penyewaan sepeda.
  - `day.csv`: Dataset penyewaan sepeda harian.
  - `hour.csv`: Dataset penyewaan sepeda per jam.
- `dashboard.py`: Script Python untuk menjalankan dashboard interaktif menggunakan **Streamlit**.
- `README.md`: Dokumentasi proyek ini.
- `requirements.txt`: Daftar pustaka Python yang diperlukan untuk menjalankan proyek ini.

## Cara Menjalankan Proyek 💻

### 1. Menjalankan Jupyter Notebook

Untuk menjalankan analisis di **Jupyter Notebook**:

1. Pastikan semua dependensi sudah terpasang dengan perintah berikut:
   ```bash
   pip install -r requirements.txt
   ```
2. Jalankan Jupyter Notebook:
   ```bash
   jupyter notebook notebook.ipynb
   ```

### 2. Menjalankan Dasbor Streamlit

Proyek ini juga menyediakan dashboard interaktif menggunakan **Streamlit**. Ikuti langkah berikut untuk menjalankannya:

1. Instal semua dependensi menggunakan:
   ```bash
   pip install -r requirements.txt
   ```
2. Jalankan aplikasi **Streamlit**:
   ```bash
   streamlit run dashboard.py
   ```

## Insight Utama 📊

**1. Bagaimana pengaruh musim terhadap jumlah total pengguna (cnt) yang menggunakan sepeda?**
- Dari analisis yang dilakukan, terlihat bahwa musim memiliki dampak yang signifikan terhadap jumlah total pengguna sepeda. **Musim panas** mencatat rata-rata jumlah penyewa yang tertinggi, dengan angka yang menunjukkan aktivitas penyewaan yang sangat tinggi pada hari-hari cerah dan hangat. Hal ini dapat dihubungkan dengan meningkatnya minat masyarakat untuk berolahraga dan bersantai di luar ruangan selama cuaca yang baik.
- **Musim semi** juga menunjukkan rata-rata jumlah penyewa yang cukup tinggi, 
- **Musim gugur** menunjukkan penurunan jumlah penyewa dibandingkan dengan dua musim sebelumnya, tetapi masih mempertahankan tingkat penyewaan yang layak. 
- Sebaliknya, **musim dingin** mencatat jumlah pengguna terendah. Suhu yang sangat dingin, kemungkinan salju, dan kondisi cuaca yang tidak nyaman membuat orang cenderung memilih moda transportasi lain.

**2. Apa pola penggunaan sepeda berdasarkan jam dalam sehari, dan bagaimana faktor cuaca mempengaruhi jumlah pengguna pada jam-jam tertentu?**
- Analisis pola penggunaan sepeda berdasarkan jam dalam sehari menunjukkan bahwa jam-jam sibuk terjadi terutama antara pagi dan sore. Peningkatan signifikan dalam jumlah penyewa pada jam-jam ini konsisten dengan pola aktivitas harian masyarakat, di mana banyak orang menggunakan sepeda untuk pergi bekerja, sekolah, atau aktivitas luar ruangan lainnya.
- Jam puncak pagi dan sore mencerminkan pola perjalanan yang umum, di mana pengguna lebih cenderung menyewa sepeda saat menuju atau pulang dari pekerjaan. Analisis ini sangat penting untuk memahami kapan permintaan terhadap penyewaan sepeda berada di puncaknya.

## Dataset

Dataset yang digunakan dalam proyek ini adalah:

- **day.csv**: Dataset harian yang mencatat data penyewaan sepeda termasuk informasi tentang suhu, kondisi cuaca, dan status hari libur.
- **hour.csv**: Dataset per jam yang mencatat data penyewaan sepeda per jam, memberikan detail yang lebih spesifik terkait waktu.

## Library yang Digunakan

- **Python**: Bahasa pemrograman yang digunakan untuk analisis dan visualisasi data.
- **Streamlit**: Library Python untuk membuat aplikasi web interaktif.
- **Matplotlib & Seaborn**: Digunakan untuk visualisasi data.
- **Pandas**: pustaka sumber terbuka yang digunakan untuk analisis dan manipulasi data.
- **Seaborn**: pustaka visualisasi data Python yang berbasis pada matplotlib
