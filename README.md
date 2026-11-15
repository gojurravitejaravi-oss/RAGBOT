# RAGBOT - Ask Questions From Your Own PDF

RAGBOT is a Retrieval-Augmented Generation bot built using Python.
It answers questions ONLY from your uploaded PDF notes. No ChatGPT, no internet answers.

## Features
- Upload PDF at runtime
- Q-wise Chunking - Each question in PDF becomes one chunk
- FAISS + SentenceTransformer for fast semantic search
- Best Match Answer with Definition, Structure, Example, Notes
- No API Key needed

## How to Run
```bash
pip install -r requirements.txt
streamlit run ragbot.py
