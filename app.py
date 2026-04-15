import streamlit as st
from modules import tokenizer, embeddings, groq_inference, metrics

st.set_page_config(page_title="LLM Lab", layout="wide")

st.title("🧠 LLM Interactive Lab")

st.sidebar.title("Navegación")

option = st.sidebar.selectbox(
    "Selecciona un módulo",
    ["Tokenización", "Embeddings", "Groq", "Métricas"]
)

if option == "Tokenización":
    tokenizer.run()

elif option == "Embeddings":
    embeddings.run()

elif option == "Groq":
    groq_inference.run()

elif option == "Métricas":
    metrics.run()