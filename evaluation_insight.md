# Evaluation & Business Insight

## Executive Summary

Sistem AI Credit Risk Scoring yang dikembangkan untuk penilaian kelayakan kredit UMKM telah berhasil mencapai akurasi 94% menggunakan model Random Forest, jauh melampaui baseline Logistic Regression di 78.5%. Artinya, dari setiap 100 pengajuan pinjaman, sistem mampu mengklasifikasikan 94 kasus secara benar — baik yang layak maupun yang berisiko tinggi. Dengan kemampuan ini, lembaga keuangan dapat memangkas waktu evaluasi kredit dari hitungan hari menjadi hitungan detik, mengurangi potensi NPL secara signifikan, sekaligus membuka akses pembiayaan bagi UMKM potensial yang selama ini tidak terlayani oleh sistem penilaian konvensional.

## Key Findings

- Model Random Forest mencapai akurasi dan F1-Score 94% — melampaui Gradient Boosting (91.5%) dan Logistic Regression (78.5%), menunjukkan keunggulan ensemble method dalam menangkap pola non-linear pada data kredit UMKM.
- Dataset memiliki distribusi target yang hampir sempurna seimbang (50.2% positif vs 49.8% negatif dari 1.000 sampel), sehingga metrik akurasi 94% dapat dipercaya tanpa bias kelas — tidak diperlukan teknik resampling seperti SMOTE atau oversampling.
- Feature_4 memiliki standar deviasi tertinggi (std=2.76) dan mean tertinggi (0.63) dibanding fitur lain, mengindikasikan variabel ini kemungkinan merupakan prediktor risiko paling dominan dan perlu diidentifikasi serta dimonitor secara khusus dalam konteks bisnis.
- ROC-AUC tidak tersedia dalam hasil evaluasi saat ini, yang merupakan celah kritis karena metrik ini esensial untuk mengukur kemampuan diskriminasi model di berbagai threshold keputusan kredit.
- Ukuran dataset 1.000 baris tergolong kecil untuk sistem credit scoring produksi — model berpotensi overfit dan belum tentu generalisasi optimal pada populasi UMKM yang lebih beragam di dunia nyata.

## Model Interpretation

Performa Random Forest dengan akurasi 94% dan F1-Weighted 94% pada dataset balanced tergolong sangat baik secara teknis, namun perlu dikontekstualisasikan dengan hati-hati. Pertama, tanpa ROC-AUC, kita belum bisa menilai seberapa baik model membedakan risiko di berbagai threshold — hal krusial dalam kredit scoring di mana cost of false negative (gagal deteksi peminjam buruk) dan false positive (menolak peminjam baik) sangat berbeda secara bisnis. Kedua, gap besar antara Random Forest (94%) dan Logistic Regression (78.5%) mengindikasikan hubungan antar fitur bersifat non-linear dan kompleks, yang membenarkan penggunaan model ensemble. Ketiga, dengan hanya 1.000 sampel dan 8 fitur anonim, ada risiko overfitting yang perlu divalidasi melalui cross-validation lebih ketat dan pengujian pada data out-of-sample. Secara keseluruhan, model ini menjanjikan sebagai proof-of-concept yang kuat, tetapi memerlukan validasi lebih lanjut sebelum deployment produksi.

## Business Recommendations

- **Identifikasi dan mapping fitur anonim (feature_1 hingga feature_8) ke variabel bisnis nyata — khususnya Feature_4 yang paling dominan — untuk memastikan model dapat dijelaskan kepada regulator dan nasabah (model explainability & compliance).** — Impact: Meningkatkan kepercayaan regulator OJK dan nasabah terhadap keputusan kredit otomatis, mengurangi risiko penolakan regulasi, serta memungkinkan tim analis memahami driver risiko utama untuk kebijakan underwriting. | Effort: medium
- **Implementasikan perhitungan ROC-AUC, Precision-Recall Curve, serta analisis confusion matrix dengan threshold optimization untuk menentukan cut-off score optimal yang menyeimbangkan NPL reduction dan approval rate UMKM.** — Impact: Memungkinkan lembaga keuangan mengatur agresivitas model sesuai risk appetite — misalnya menurunkan threshold untuk meningkatkan inklusi keuangan, atau menaikkan threshold saat kondisi ekonomi memburuk — berpotensi menurunkan NPL hingga 15-25% dibanding proses manual. | Effort: low
- **Perluas dataset minimal ke 10.000-50.000 sampel dengan data UMKM riil yang mencakup variabel alternatif seperti data transaksi digital, arus kas, histori pembayaran utilitas, dan data e-commerce untuk meningkatkan robustness model.** — Impact: Meningkatkan generalisasi model ke populasi UMKM yang lebih beragam, mengurangi risiko overfitting, dan berpotensi meningkatkan akurasi serta coverage scoring hingga 30-40% lebih banyak UMKM unbanked yang dapat dinilai. | Effort: high
- **Terapkan model Random Forest sebagai sistem scoring otomatis tahap pertama (pre-screening) yang menghasilkan credit score 0-100, dengan kasus borderline (skor 40-60) diteruskan ke analis manusia untuk review akhir — model hybrid human-AI.** — Impact: Memangkas waktu proses pengajuan kredit dari rata-rata 3-7 hari menjadi di bawah 24 jam untuk 80% kasus, meningkatkan kepuasan nasabah UMKM, dan memungkinkan analis fokus pada kasus kompleks bernilai tinggi. | Effort: medium
- **Bangun sistem monitoring model secara real-time dengan tracking data drift, concept drift, dan degradasi performa model menggunakan metrik NPL aktual vs prediksi setiap bulan, dengan trigger retraining otomatis jika akurasi turun di bawah 88%.** — Impact: Memastikan model tetap relevan dan akurat seiring perubahan kondisi ekonomi dan perilaku peminjam UMKM, mencegah model decay yang dapat menyebabkan lonjakan NPL tidak terdeteksi, dan menjaga kepercayaan stakeholder terhadap sistem AI. | Effort: high

## Limitations

- Dataset hanya 1.000 sampel dengan fitur anonim — terlalu kecil dan tidak transparan untuk deployment produksi; model belum tentu generalisasi pada populasi UMKM nyata yang jauh lebih heterogen dalam hal sektor usaha, geografi, dan skala bisnis.
- ROC-AUC tidak dihitung, sehingga kemampuan diskriminasi model di berbagai threshold belum terukur — ini adalah gap kritis karena dalam credit scoring, biaya kesalahan false positive dan false negative sangat asimetris secara finansial.
- Tidak ada informasi tentang metode validasi yang digunakan (train-test split ratio, cross-validation) sehingga risiko overfitting pada dataset kecil ini belum dapat dikuantifikasi dengan pasti.
- Fitur yang sudah dinormalisasi dan dianonimisasi membatasi kemampuan interpretasi bisnis dan compliance — regulator seperti OJK mensyaratkan transparansi variabel yang digunakan dalam keputusan kredit otomatis.
- Model saat ini tidak mempertimbangkan faktor temporal (time-series perilaku keuangan) yang sangat penting dalam credit scoring UMKM, di mana tren arus kas lebih prediktif daripada snapshot tunggal.

## Next Steps

- Lakukan evaluasi lengkap dengan menambahkan ROC-AUC, Precision, Recall, F1 per kelas, confusion matrix, dan analisis feature importance Random Forest untuk mengidentifikasi variabel bisnis paling berpengaruh — target selesai dalam 1-2 minggu.
- Jalankan k-fold cross-validation (k=10) dan learning curve analysis untuk memvalidasi apakah akurasi 94% stabil atau merupakan artefak dari dataset kecil, sebelum mengajukan proposal deployment ke stakeholder bisnis.
- Koordinasikan dengan tim bisnis dan legal untuk de-anonimisasi fitur dan pemetaan ke variabel kredit yang dapat dipertanggungjawabkan secara regulasi, sekaligus merancang pipeline pengumpulan data alternatif UMKM berskala lebih besar.
- Kembangkan dashboard monitoring kredit berbasis model ini untuk pilot program dengan 500-1.000 pengajuan UMKM nyata selama 3 bulan, dengan tracking NPL aktual sebagai ground truth validasi performa model di lingkungan produksi.
- Eksplorasi penambahan model XGBoost dan LightGBM serta teknik SHAP (SHapley Additive exPlanations) untuk meningkatkan akurasi sekaligus memenuhi kebutuhan explainable AI yang disyaratkan dalam regulasi kredit digital.

## KPIs to Monitor

- NPL Rate (Non-Performing Loan): Target penurunan dari baseline historis sebesar 20-30% dalam 6 bulan pertama pasca implementasi model scoring otomatis.
- Model Accuracy & F1-Score on Production Data: Monitoring bulanan dengan alert jika turun di bawah 88% — indikator utama kebutuhan retraining model.
- ROC-AUC Score: Target minimal 0.90 setelah implementasi evaluasi lengkap — metrik kunci kemampuan diskriminasi risiko kredit di berbagai threshold.
- Loan Approval Rate untuk UMKM Unbanked: Target peningkatan 25-40% dibanding proses manual — mengukur dampak inklusi keuangan dari sistem AI.
- Waktu Proses Pengajuan Kredit (Time-to-Decision): Target di bawah 24 jam untuk 80% aplikasi, turun dari rata-rata 3-7 hari proses manual.
- False Positive Rate (FPR) & False Negative Rate (FNR): Monitoring keseimbangan antara menolak peminjam baik (FPR) dan meloloskan peminjam buruk (FNR) sesuai risk appetite lembaga keuangan.
- Data Drift Index: Monitoring bulanan distribusi fitur input model — jika drift signifikan terdeteksi, trigger review dan retraining untuk mencegah degradasi performa.