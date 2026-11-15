import streamlit as st
import fitz
import numpy as np
import faiss
import re
from sentence_transformers import SentenceTransformer

st.title("RAGBOT")

@st.cache_resource
def load_all():
    doc = fitz.open("C:/Users/raviteja/Downloads/ACS_Handwritten_Notes.html")
    text = ""
    for page in doc:
        text += page.get_text() + "\n"

    chunks = re.split(r'\n(?=Q\d+\.)', text)
    chunks = [c.strip() for c in chunks if len(c.strip()) > 50]

    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(chunks)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))
    return model, chunks, index

model, chunks, index = load_all()

question = st.text_input("enter the question: ")

if st.button("Ask"):
    q_emb = model.encode([question])
    D, I = index.search(np.array(q_emb), k=1)
    st.write("=== BEST MATCH ===")
    st.write(chunks[I[0][0]])
