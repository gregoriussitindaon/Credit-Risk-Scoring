# Deployment Options

## 1. Streamlit Community Cloud (Free, Easiest)

1. Push repo ke GitHub
2. Buka https://share.streamlit.io
3. New app → pilih repo ini
4. Main file path: `app/streamlit_app.py`
5. Deploy! Selesai.

## 2. Hugging Face Spaces (Free)

1. Buat Space baru di https://huggingface.co/new-space
2. SDK: Streamlit
3. Push file `app/streamlit_app.py`, `app/README_HF.md`, `requirements.txt`

## 3. Render (Free tier)

1. Connect repo di https://render.com
2. New Web Service → pilih repo
3. Build command: `pip install -r requirements.txt`
4. Start command: `streamlit run app/streamlit_app.py --server.port=$PORT --server.address=0.0.0.0`

## 4. Docker (lokal atau cloud apapun)

```bash
docker build -t portfolio-project .
docker run -p 8501:8501 portfolio-project
```

Buka http://localhost:8501
