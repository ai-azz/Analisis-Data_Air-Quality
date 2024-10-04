import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Mengatur gaya seaborn
sns.set(style='dark')
data = pd.read_csv("main_data.csv")

# Menambahkan kolom date dan Day_Type
data['date'] = pd.to_datetime(data[['year', 'month', 'day']])
data['Day_Type'] = data['date'].dt.dayofweek.apply(lambda x: 'Weekend' if x >= 5 else 'Weekday')

# Q1: Visualisasi polutan berdasarkan lokasi
def plot_pollutants_by_location(data):
    fig, ax = plt.subplots(figsize=(12, 6))
    melted_data = data.melt(id_vars=['station', 'month'], 
                             value_vars=['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3'])
    sns.barplot(data=melted_data, x='station', y='value', hue='variable', ax=ax)  
    ax.set_title('🌍 Kualitas Udara Berdasarkan Stasiun Pemantauan', fontsize=16)
    ax.set_ylabel('Konsentrasi Polutan (μg/m³)', fontsize=12)
    ax.set_xlabel('Stasiun Pemantauan', fontsize=12)
    ax.legend(title='Jenis Polutan', fontsize=10)
    ax.tick_params(axis='x', rotation=45)
    plt.tight_layout()
    st.pyplot(fig)

# Q2: Visualisasi perbandingan polusi antara weekdays dan weekends
def plot_weekdays_vs_weekends(data):
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(data=data.melt(id_vars=['Day_Type'], 
                                  value_vars=['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']),
                 x='Day_Type', y='value', hue='variable', ax=ax)
    ax.set_title('📅 Perbandingan Kualitas Udara antara Weekdays dan Weekends', fontsize=16)
    ax.set_ylabel('Konsentrasi Polutan (μg/m³)', fontsize=12)
    ax.set_xlabel('Tipe Hari', fontsize=12)
    ax.legend(title='Jenis Polutan', fontsize=10)
    plt.tight_layout()
    st.pyplot(fig)

# Q3: Visualisasi pengaruh kecepatan angin
def plot_wind_effect(data):
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.scatterplot(data=data, x='WSPM', y='PM2.5', color='blue', label='PM2.5', s=100, ax=ax)
    sns.scatterplot(data=data, x='WSPM', y='O3', color='orange', label='O3', s=100, ax=ax)
    ax.set_title('🌬️ Pengaruh Kecepatan Angin terhadap Konsentrasi Polutan', fontsize=16)
    ax.set_ylabel('Konsentrasi Polutan (μg/m³)', fontsize=12)
    ax.set_xlabel('Kecepatan Angin (m/s)', fontsize=12)
    ax.legend(fontsize=10)
    plt.tight_layout()
    st.pyplot(fig)

# Judul Dashboard
st.title('Dashboard Analisis Kualitas Udara 🌿💨')

# Sidebar untuk informasi penulis
st.sidebar.header('🌟 Author info : 🌟')
st.sidebar.write("👤 Nama: Aini Azzah")
st.sidebar.write("📧 Email: aini.azzah@example.com")
st.sidebar.write("🆔 ID Dicoding: aini_azzah")
st.sidebar.write("---") 
st.sidebar.write("📚 Selamat datang di dashboard analisis kualitas udara! ")
st.sidebar.write("📝 Temukan pola, perbandingan, dan pengaruh polusi udara di sini. ✨")

# Q1
with st.expander('❓ Pertanyaan 1: Bagaimana pola temporal dan spasial polutan udara?'):
    st.subheader('Pola Temporal dan Spasial Polutan Udara')
    plot_pollutants_by_location(data)

    st.subheader('🔍 Kesimpulan Pertanyaan 1')
    st.write(""" 
        Analisis polutan udara (PM2.5, PM10, SO2, NO2, CO, O3) menunjukkan bahwa kualitas udara bervariasi baik berdasarkan lokasi maupun waktu. 
        Di stasiun Aotizhongxin, rata-rata PM2.5 mencapai 72.43 μg/m³, tertinggi dibandingkan dengan stasiun lain seperti Dingling, 
        yang hanya 60.55 μg/m³. Hal ini menunjukkan bahwa faktor lokal seperti aktivitas industri dan kepadatan penduduk memengaruhi kualitas udara.
        
        Dari segi waktu, terdapat bulan-bulan tertentu dengan polusi lebih tinggi. Misalnya, Maret 2014 memiliki rata-rata PM2.5 tertinggi, 
        106.51 μg/m³, sedangkan Januari 2014 menunjukkan angka tinggi untuk NO2 dan SO2, kemungkinan karena aktivitas industri dan kondisi cuaca.
        
        Musim juga berpengaruh, dengan polusi cenderung lebih tinggi di bulan dingin, seperti Januari dan Februari, akibat penggunaan bahan bakar untuk pemanas 
        dan inversi suhu yang menyebabkan penumpukan polusi.
    """)

# Q2
with st.expander('❓ Pertanyaan 2: Apakah terdapat perbedaan signifikan dalam tingkat polusi udara antara weekdays dan weekends?'):
    st.subheader('Perbandingan Polusi Antara Weekdays dan Weekends')
    plot_weekdays_vs_weekends(data)
    st.subheader('🔍 Kesimpulan Pertanyaan 2')
    st.write(""" 
        Terdapat perbedaan yang signifikan dalam tingkat polusi udara antara hari kerja (weekdays) dan akhir pekan (weekends). 
        Pada akhir pekan, konsentrasi polutan seperti PM2.5 (73.48 µg/m³), PM10 (96.05 µg/m³), SO2 (15.23 µg/m³), dan O3 (59.25 µg/m³) 
        cenderung lebih tinggi dibandingkan dengan hari kerja, di mana konsentrasi PM2.5 tercatat 68.90 µg/m³ dan PM10 91.39 µg/m³.
        
        Peningkatan ini mungkin disebabkan oleh perubahan aktivitas manusia pada akhir pekan, seperti peningkatan penggunaan transportasi pribadi dan kegiatan rekreasi.
    """)

# Q3
with st.expander('❓ Pertanyaan 3: Bagaimana pengaruh arah dan kecepatan angin terhadap penyebaran polutan udara?'):
    st.subheader('Pengaruh Arah dan Kecepatan Angin terhadap Polutan Udara')
    plot_wind_effect(data)
    st.subheader('🔍 Kesimpulan Pertanyaan 3')
    st.write(""" 
        Pengaruh arah dan kecepatan angin terhadap penyebaran polutan udara sangat signifikan. 
        Kecepatan angin yang rendah, terutama di arah timur, berhubungan dengan konsentrasi polutan yang lebih tinggi seperti PM2.5, PM10, NO2, dan SO2.
        
        Sebaliknya, pada kecepatan angin yang lebih tinggi, terutama dari arah barat daya, konsentrasi partikel polutan seperti PM2.5 dan PM10 cenderung menurun. 
        Namun, konsentrasi ozon (O3) mengalami peningkatan yang signifikan pada kecepatan angin tinggi.
    """)

# Kesimpulan Umum
with st.expander('🔍 Kesimpulan Umum'):
    st.write(""" 
        Secara keseluruhan, analisis menunjukkan bahwa kualitas udara sangat dipengaruhi oleh faktor lokasi, waktu, dan kondisi meteorologi.
    """)
