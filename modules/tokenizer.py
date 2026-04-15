import streamlit as st
from utils.tokenizer_utils import tokenize_text

def run():
    st.header("🔤 Laboratorio del Tokenizador")

    text = st.text_area("Ingresa un texto")

    if text:
        tokens, ids = tokenize_text(text)

        st.subheader("Tokens:")
        colored_text = ""
        colors = ["#FFDDC1", "#C1FFD7"]

        for i, token in enumerate(tokens):
            colored_text += f"<span style='background-color:{colors[i%2]}; padding:4px'>{token}</span> "

        st.markdown(colored_text, unsafe_allow_html=True)

        st.subheader("Token IDs:")
        st.write(ids)

        st.subheader("Métrica:")
        st.write(f"Caracteres: {len(text)}")
        st.write(f"Tokens: {len(tokens)}")