# AI-Powered Credit Risk Scoring untuk Pinjaman UMKM

> Membangun sistem AI credit scoring yang transparan dan akurat untuk membuka akses pembiayaan UMKM Indonesia secara lebih adil dan efisien.

## 📋 Overview

Lembaga keuangan dan fintech menghadapi tantangan besar dalam menilai kelayakan kredit pelaku UMKM yang mayoritas tidak memiliki riwayat kredit formal (unbanked). Proses penilaian manual yang lambat dan subjektif menyebabkan tingginya Non-Performing Loan (NPL) serta banyak UMKM potensial yang gagal mendapatkan akses pembiayaan. Diperlukan sistem scoring otomatis berbasis AI yang mampu memprediksi risiko kredit secara akurat, cepat, dan transparan.

## 🎯 Objectives

- Membangun model machine learning klasifikasi untuk memprediksi probabilitas gagal bayar (default) peminjam UMKM berdasarkan data finansial dan non-finansial
- Mengidentifikasi fitur-fitur paling berpengaruh terhadap risiko kredit UMKM melalui analisis eksplorasi data dan feature importance
- Mengembangkan aplikasi web interaktif yang memungkinkan analis kredit memasukkan data nasabah dan mendapatkan skor risiko secara real-time

## 🔧 Tech Stack

- **Language:** Python
- **ML:** scikit-learn
- **Viz:** matplotlib, seaborn, plotly
- **App:** streamlit

## 📁 Project Structure

```
.
├── data/
│   ├── raw/         # Dataset original
│   ├── interim/     # Cleaned data
│   └── processed/   # Feature-engineered
├── notebooks/       # Jupyter notebooks
├── src/             # Modular Python code
├── reports/         # Insight & evaluation
├── app/             # Streamlit dashboard
└── README.md
```

## 🚀 How to Run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Open notebook
jupyter notebook notebooks/01_main_analysis.ipynb

# 3. Run dashboard
streamlit run app/streamlit_app.py
```

## 📊 Results

- **Best Model:** RandomForest
- **Best Score:** 0.94

Sistem AI Credit Risk Scoring yang dikembangkan untuk penilaian kelayakan kredit UMKM telah berhasil mencapai akurasi 94% menggunakan model Random Forest, jauh melampaui baseline Logistic Regression di 78.5%. Artinya, dari setiap 100 pengajuan pinjaman, sistem mampu mengklasifikasikan 94 kasus secara benar — baik yang layak maupun yang berisiko tinggi. Dengan kemampuan ini, lembaga keuangan dapat memangkas waktu evaluasi kredit dari hitungan hari menjadi hitungan detik, mengurangi potensi NPL secara signifikan, sekaligus membuka akses pembiayaan bagi UMKM potensial yang selama ini tidak terlayani oleh sistem penilaian konvensional.

## 📝 License

MIT License
