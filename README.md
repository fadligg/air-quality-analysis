# Proyek Analisis Data: Kualitas Udara Changping ✨

## Deskripsi Singkat
Proyek ini merupakan submission akhir untuk kelas Belajar Analisis Data dengan Python. Pada proyek ini dilakukan proses *data wrangling*, *exploratory data analysis* (EDA), hingga visualisasi data untuk melihat tren dan pola musiman polutan PM2.5 di stasiun pemantauan kualitas udara Changping (2013-2017).

## Setup Environment

**Menggunakan Anaconda:**
```bash
conda create --name analisisdata python=3.9
conda activate analisisdata
pip install -r requirements.txt
```

**Menggunakan venv**
```bash
python -m venv env
# Untuk Windows:
env\Scripts\activate
# Untuk Mac/Linux:
source env/bin/activate

pip install -r requirements.txt
```

## Run Streamlit
Untuk menjalankan dashboard secara lokal, arahkan terminal ke dalam root direktori proyek, lalu jalankan perintah berikut:
```bash
cd dashboard
streamlit run dashboard.py
```
