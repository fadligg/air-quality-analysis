import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set konfigurasi halaman
st.set_page_config(page_title="Changping Air Quality", page_icon="🌤️")

# Load data dengan cache agar lebih cepat
@st.cache_data
def load_data():
    df = pd.read_csv("main_data.csv")
    df['datetime'] = pd.to_datetime(df['datetime'])
    return df

df = load_data()

# Sidebar untuk filter
st.sidebar.header("Filter Data")
selected_year = st.sidebar.selectbox("Pilih Tahun:", sorted(df['year'].unique()))
filtered_df = df[df['year'] == selected_year]

# Header Dashboard
st.title("Changping Air Quality Dashboard")
st.markdown("**Analisis Polusi Udara (PM2.5) di Stasiun Changping (2013-2017)**")

# Metrik Utama
col1, col2 = st.columns(2)
with col1:
    st.metric("Rata-rata PM2.5", f"{filtered_df['PM2.5'].mean():.2f} µg/m³")
with col2:
    st.metric("Nilai Maksimal PM2.5", f"{filtered_df['PM2.5'].max():.2f} µg/m³")

# Visualisasi 1: Tren Bulanan
st.subheader(f"Tren PM2.5 Bulanan di Tahun {selected_year}")
monthly_pm25 = filtered_df.groupby('month')['PM2.5'].mean().reset_index()
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=monthly_pm25, x='month', y='PM2.5', marker='o', color='#E63946', ax=ax)
ax.set_xticks(range(1, 13))
ax.set_xlabel("Bulan (1-12)")
ax.set_ylabel("Rata-rata PM2.5 (µg/m³)")
ax.grid(True, linestyle='--', alpha=0.6)
st.pyplot(fig)

# Visualisasi 2: Pola Harian
st.subheader(f"Pola PM2.5 Harian di Tahun {selected_year}")
hourly_pm25 = filtered_df.groupby('hour')['PM2.5'].mean().reset_index()
fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.barplot(data=hourly_pm25, x='hour', y='PM2.5', palette='viridis', ax=ax2)
ax2.set_xlabel("Jam dalam Sehari (0-23)")
ax2.set_ylabel("Rata-rata PM2.5 (µg/m³)")
ax2.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(fig2)

st.caption("Copyright (c) Fadli Haidar Nugraha 2026")