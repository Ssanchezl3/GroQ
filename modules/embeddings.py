import streamlit as st
import plotly.express as px
from utils.embedding_utils import get_embeddings, reduce_dimensionality

def run():
    st.header("📐 Geometría de Embeddings")

    words = st.text_input("Ingresa palabras separadas por coma", "king, man, woman, queen")

    if words:
        word_list = [w.strip() for w in words.split(",")]

        vectors = get_embeddings(word_list)
        reduced = reduce_dimensionality(vectors)

        fig = px.scatter(
            x=reduced[:,0],
            y=reduced[:,1],
            text=word_list,
            title="Embeddings en 2D"
        )

        st.plotly_chart(fig)

        if all(w in word_list for w in ["king", "man", "woman", "queen"]):
            st.info("Verifica visualmente: king - man + woman ≈ queen")