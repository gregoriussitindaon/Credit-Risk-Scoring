# EDA Summary

**Shape:** 1000 rows × 9 cols

## Key Observations

- Dataset terdiri dari 1000 baris dan 9 kolom (8 fitur numerik + 1 target biner), ukuran yang relatif kecil untuk model kredit scoring yang robust di konteks UMKM.
- Target variabel memiliki distribusi yang hampir perfectly balanced (mean=0.502, std≈0.5), artinya sekitar 502 sampel berlabel 1 dan 498 berlabel 0 — kondisi ideal untuk klasifikasi biner tanpa perlu teknik resampling khusus.
- Semua fitur bertipe float64 dan tampak sudah dalam skala yang relatif terstandardisasi (mean mendekati 0 untuk beberapa fitur), mengindikasikan kemungkinan data sudah melalui preprocessing atau normalisasi sebelumnya.
- Feature_4 memiliki standar deviasi tertinggi (std=2.76) dan mean tertinggi (0.63), menunjukkan variabilitas dan spread data yang jauh lebih besar dibanding fitur lain — kemungkinan mengandung outlier signifikan atau distribusi yang lebih lebar.
- Nama fitur yang generik ('feature_1' hingga 'feature_8') mengindikasikan data telah dianonimisasi atau di-encode, sehingga interpretabilitas bisnis dan transparansi model (explainability) akan menjadi tantangan utama dalam konteks kredit scoring UMKM yang memerlukan justifikasi keputusan.

## Potential Issues

- Kurangnya konteks semantik fitur: nama kolom yang tidak deskriptif ('feature_1' dst.) menyulitkan validasi domain knowledge, padahal dalam credit scoring UMKM faktor seperti arus kas, lama usaha, atau omzet sangat krusial untuk interpretasi dan regulasi (POJK/OJK compliance).
- Ukuran dataset 1000 sampel sangat kecil untuk membangun model kredit scoring yang generalizable — risiko overfitting tinggi, terutama untuk model kompleks seperti ensemble atau deep learning, dan performa evaluasi bisa tidak stabil.
- Tidak ada informasi missing values yang eksplisit, namun perlu diverifikasi lebih lanjut karena data UMKM unbanked seringkali memiliki banyak nilai kosong pada fitur finansial formal.
- Feature_4 dengan std=2.76 berpotensi mendominasi model berbasis jarak atau gradient jika tidak dilakukan scaling ulang, dan kemungkinan mengandung outlier ekstrem yang dapat mendistorsi pembelajaran model.
- Tidak ada fitur temporal atau fitur kategorik yang terlihat, padahal perilaku pembayaran historis dan segmentasi industri UMKM adalah prediktor penting risiko kredit — dataset mungkin tidak merepresentasikan kompleksitas masalah nyata.

## Recommendations for Modeling

- Lakukan feature importance analysis (menggunakan Random Forest, XGBoost, atau SHAP values) sejak awal untuk mengidentifikasi fitur mana yang paling prediktif, mengingat nama fitur tidak informatif dan perlu diprioritaskan untuk interpretasi bisnis.
- Gunakan stratified k-fold cross-validation (k=5 atau 10) mengingat dataset kecil (1000 sampel) untuk mendapatkan estimasi performa yang lebih stabil dan menghindari variance tinggi pada split tunggal.
- Terapkan pipeline scaling (StandardScaler atau RobustScaler) terutama untuk feature_4 yang memiliki spread tinggi, dengan RobustScaler lebih disarankan jika terdapat outlier ekstrem.
- Prioritaskan model yang interpretable dan explainable seperti Logistic Regression dengan regularisasi, Decision Tree, atau XGBoost dengan SHAP — mengingat kebutuhan transparansi dalam keputusan kredit dan potensi audit regulasi OJK.
- Evaluasi model menggunakan metrik yang relevan untuk kredit scoring: AUC-ROC sebagai metrik utama, ditambah Precision-Recall curve, KS-Statistic, dan Gini Coefficient — hindari hanya mengandalkan accuracy mengingat implikasi bisnis asimetris antara false positive (kredit ditolak padahal layak) dan false negative (kredit diberikan ke peminjam berisiko tinggi).