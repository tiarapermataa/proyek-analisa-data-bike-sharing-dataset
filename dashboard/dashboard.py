import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Menampilkan informasi proyek
st.title("Proyek Analisis Data: Bike Sharing Dataset")
st.markdown("- **Nama:** Tiara Permata Sari")
st.markdown("- **Email:** tiarapermatasari25@gmail.com")
st.markdown("- **ID Dicoding:** tiarapermataa")

# Mengimpor dataset
@st.cache
def load_data():
    # Ganti dengan path yang sesuai untuk dataset Anda
    day_df = pd.read_csv('data/day.csv')
    hour_df = pd.read_csv('data/hour.csv')
    return day_df, hour_df

day_df, hour_df = load_data()

# Data Wrangling
st.header("Data Wrangling")

# Menampilkan beberapa baris awal dari masing-masing dataset
st.subheader("Beberapa Baris Pertama dari Dataset 'day.csv'")
st.write(day_df.head())

st.subheader("Beberapa Baris Pertama dari Dataset 'hour.csv'")
st.write(hour_df.head())

# Menilai informasi dasar dari dataset 'day.csv'
st.subheader("Informasi Dasar dari Dataset 'day.csv'")
st.write(day_df.info())

# Statistik deskriptif dari dataset 'day.csv'
st.subheader("Statistik Deskriptif dari Dataset 'day.csv'")
st.write(day_df.describe())

# Menilai informasi dasar dari dataset 'hour.csv'
st.subheader("Informasi Dasar dari Dataset 'hour.csv'")
st.write(hour_df.info())

# Statistik deskriptif dari dataset 'hour.csv'
st.subheader("Statistik Deskriptif dari Dataset 'hour.csv'")
st.write(hour_df.describe())

# Mengecek nilai yang hilang dalam dataset 'day.csv'
missing_day = day_df.isnull().sum()
st.subheader("Jumlah Nilai yang Hilang di Dataset 'day.csv'")
st.write(missing_day[missing_day > 0])

# Mengecek nilai yang hilang dalam dataset 'hour.csv'
missing_hour = hour_df.isnull().sum()
st.subheader("Jumlah Nilai yang Hilang di Dataset 'hour.csv'")
st.write(missing_hour[missing_hour > 0])

# Menghapus kolom yang tidak diperlukan
day_df_cleaned = day_df.drop(columns=['instant'], errors='ignore')
hour_df_cleaned = hour_df.drop(columns=['instant'], errors='ignore')

# Memeriksa duplikasi data
duplicates_day = day_df_cleaned.duplicated().sum()
duplicates_hour = hour_df_cleaned.duplicated().sum()
st.subheader("Jumlah Duplikasi di Dataset")
st.write(f"Jumlah duplikasi di dataset 'day.csv': {duplicates_day}")
st.write(f"Jumlah duplikasi di dataset 'hour.csv': {duplicates_hour}")

# Menghapus duplikasi jika ada
day_df_cleaned = day_df_cleaned.drop_duplicates()
hour_df_cleaned = hour_df_cleaned.drop_duplicates()

# Visualisasi distribusi jumlah total pengguna (cnt) dalam dataset 'day.csv'
st.header("Visualisasi Distribusi Jumlah Total Pengguna (cnt) per Hari")
plt.figure(figsize=(12, 6))
counts, bin_edges = np.histogram(day_df_cleaned['cnt'], bins=30)

for i in range(len(counts)):
    plt.bar(bin_edges[i], counts[i], width=bin_edges[i + 1] - bin_edges[i], 
            color='lightblue', alpha=0.5, edgecolor='black', linewidth=1.5)

max_count = counts.max()
max_bin_index = np.argmax(counts)

plt.bar(bin_edges[max_bin_index], 
         counts[max_bin_index], 
         width=bin_edges[max_bin_index + 1] - bin_edges[max_bin_index], 
         color='darkblue', alpha=0.7, edgecolor='black', linewidth=1.5, label='Balok Tertinggi')

plt.title('Distribusi Jumlah Total Pengguna (cnt) per Hari')
plt.xlabel('Jumlah Total Pengguna')
plt.ylabel('Frekuensi')
plt.axvline(max_count, color='red', linestyle='--', linewidth=2, label='Jumlah Pengguna Tertinggi')
plt.legend()
plt.grid()
st.pyplot(plt)

# Visualisasi hubungan antara suhu dan kelembapan dengan garis tren
st.header("Hubungan antara Suhu dan Kelembapan")
plt.figure(figsize=(12, 6))
sns.scatterplot(data=day_df_cleaned, x='temp', y='hum', hue='weathersit', palette='viridis', alpha=0.7)
sns.regplot(data=day_df_cleaned, x='temp', y='hum', scatter=False, color='red', line_kws={'linewidth': 2})
plt.title('Hubungan antara Suhu dan Kelembapan')
plt.xlabel('Suhu (normalisasi)')
plt.ylabel('Kelembapan')
plt.legend(title='Situasi Cuaca')
plt.grid()
st.pyplot(plt)

# Boxplot untuk melihat variasi jumlah penyewa berdasarkan musim
st.header("Variasi Jumlah Penyewa berdasarkan Musim")
plt.figure(figsize=(12, 6))
sns.boxplot(data=day_df_cleaned, x='season', y='cnt')
plt.title('Variasi Jumlah Penyewa berdasarkan Musim')
plt.xlabel('Musim')
plt.ylabel('Jumlah Penyewa')
plt.xticks(ticks=[0, 1, 2, 3], labels=['Musim Dingin', 'Musim Semi', 'Musim Panas', 'Musim Gugur'])
plt.grid()
st.pyplot(plt)

# Heatmap untuk melihat korelasi antara variabel
st.header("Heatmap Korelasi antara Variabel")
plt.figure(figsize=(12, 8))
numeric_cols = day_df_cleaned.select_dtypes(include=[np.number])
correlation_matrix = numeric_cols.corr()
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Heatmap Korelasi antara Variabel')
st.pyplot(plt)

# Mengonversi kolom 'dteday' ke tipe datetime
day_df_cleaned['dteday'] = pd.to_datetime(day_df_cleaned['dteday'])

# Memilih rentang data dari 2012-07 hingga 2013-01
start_date = '2012-07-01'
end_date = '2013-01-31'
filtered_data = day_df_cleaned[(day_df_cleaned['dteday'] >= start_date) & 
                                 (day_df_cleaned['dteday'] <= end_date)]

# Menghitung jumlah penyewa harian
day_trend = filtered_data.groupby('dteday').agg({'cnt': 'sum'}).reset_index()

# Menghitung perubahan jumlah penyewa dari hari ke hari
day_trend['change'] = day_trend['cnt'].diff()

# Menemukan indeks dengan kenaikan paling tinggi
max_increase_index = day_trend['change'].idxmax()
max_increase_value = day_trend['change'].max()

# Plot tren penyewaan sepeda
st.header("Trend Penyewaan Sepeda Harian (Juli 2012 - Januari 2013)")
plt.figure(figsize=(12, 6))
sns.lineplot(data=day_trend, x='dteday', y='cnt', label='Jumlah Penyewa', color='blue')
plt.scatter(day_trend['dteday'][max_increase_index], 
            day_trend['cnt'][max_increase_index], 
            color='red', s=100, label='Kenaikan Tertinggi', edgecolor='black')

plt.title('Trend Penyewaan Sepeda Harian')
plt.xlabel('Tanggal')
plt.ylabel('Jumlah Penyewa')
plt.xticks(rotation=45)
plt.grid()
plt.legend()
st.pyplot(plt)

# Pengaruh Musim terhadap Jumlah Total Pengguna (cnt)
st.header("Pengaruh Musim terhadap Jumlah Total Pengguna (cnt)")
if 'season' in day_df_cleaned.columns:
    # Menghitung rata-rata jumlah pengguna berdasarkan musim
    season_avg = day_df_cleaned.groupby('season')['cnt'].mean().reset_index()

    # Mengatur nama musim untuk visualisasi yang lebih jelas
    season_avg['season'] = season_avg['season'].map({
        1: 'Musim Dingin',
        2: 'Musim Semi',
        3: 'Musim Panas',
        4: 'Musim Gugur'
    })

    # Menampilkan rata-rata pengguna berdasarkan musim
    st.subheader("Rata-rata Jumlah Pengguna Berdasarkan Musim")
    st.write(season_avg)

    # Visualisasi rata-rata jumlah pengguna berdasarkan musim
    plt.figure(figsize=(8, 5))
    sns.barplot(data=season_avg, x='season', y='cnt', palette='Blues')
    plt.title('Rata-rata Jumlah Pengguna Sepeda Berdasarkan Musim')
    plt.xlabel('Musim')
    plt.ylabel('Rata-rata Jumlah Pengguna')
    plt.grid()

    # Menambahkan anotasi pada balok
    for index, row in season_avg.iterrows():
        plt.text(index, row['cnt'], round(row['cnt'], 2), color='black', ha="center")

    st.pyplot(plt)
else:
    st.error("Kolom 'season' tidak ditemukan dalam dataset.")

# Pola Penggunaan Sepeda Berdasarkan Jam dalam Sehari
st.header("Pola Penggunaan Sepeda Berdasarkan Jam dalam Sehari")
hour_avg = hour_df_cleaned.groupby('hr').agg({'cnt': 'mean'}).reset_index()

# Visualisasi pola penggunaan sepeda berdasarkan jam 
plt.figure(figsize=(12, 6))
sns.lineplot(data=hour_avg, x='hr', y='cnt', marker='o', color='blue')
max_index = hour_avg['cnt'].idxmax()
max_value = hour_avg['cnt'].max()
plt.scatter(hour_avg['hr'][max_index], max_value, color='red', s=100, label='Lonjakan Tertinggi', edgecolor='black')
plt.title('Pola Penggunaan Sepeda Berdasarkan Jam dalam Sehari')
plt.xlabel('Jam')
plt.ylabel('Rata-rata Jumlah Pengguna')
plt.xticks(range(0, 24))  # Set x-ticks untuk jam
plt.grid()
plt.legend()
st.pyplot(plt)

# Visualisasi pengaruh cuaca terhadap pola penggunaan sepeda
st.header("Pengaruh Cuaca terhadap Penggunaan Sepeda berdasarkan Jam")
hour_counts = hour_df_cleaned.groupby('hr').agg({'cnt': 'sum'}).reset_index()
plt.figure(figsize=(12, 6))
bars = plt.bar(hour_counts['hr'], hour_counts['cnt'], color='lightblue', alpha=0.7)
max_count_index = hour_counts['cnt'].idxmax()
bars[max_count_index].set_color('darkblue')
plt.title('Pengaruh Cuaca terhadap Penggunaan Sepeda berdasarkan Jam')
plt.xlabel('Jam')
plt.ylabel('Jumlah Pengguna')
plt.xticks(range(0, 24))
plt.grid()
st.pyplot(plt)

# Menampilkan penjelasan
st.header("Penjelasan Analisis")
st.write("Pola penggunaan sepeda menunjukkan bahwa jam-jam sibuk terjadi antara pagi dan sore. Penggunaan sepeda cenderung meningkat pada jam-jam tersebut, kemungkinan berkaitan dengan jam kerja dan aktivitas luar ruangan.")
st.write("Cuaca juga berpengaruh terhadap penggunaan sepeda, dengan variasi yang signifikan berdasarkan situasi cuaca.")

# Distribusi pengguna berdasarkan kategori
st.header("Distribusi Pengguna Berdasarkan Kategori")
user_distribution = {
    'Rendah': sum(day_df_cleaned['cnt'] <= day_df_cleaned['cnt'].quantile(0.33)),
    'Sedang': sum((day_df_cleaned['cnt'] > day_df_cleaned['cnt'].quantile(0.33)) & 
                   (day_df_cleaned['cnt'] <= day_df_cleaned['cnt'].quantile(0.66))),
    'Tinggi': sum(day_df_cleaned['cnt'] > day_df_cleaned['cnt'].quantile(0.66))
}

plt.figure(figsize=(8, 5))
user_categories = list(user_distribution.keys())
user_counts = list(user_distribution.values())
colors = ['lightblue' if count < max(user_counts) else 'darkblue' for count in user_counts]

# Menggunakan hue untuk memberikan warna kategori
sns.barplot(x=user_categories, y=user_counts, palette=colors)
plt.title('Distribusi Jumlah Pengguna berdasarkan Kategori')
plt.xlabel('Kategori Pengguna')
plt.ylabel('Jumlah Pengguna')
plt.grid()

# Menambahkan anotasi pada balok
for index, count in enumerate(user_counts):
    plt.text(index, count, count, color='black', ha='center')

st.pyplot(plt)
