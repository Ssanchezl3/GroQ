import streamlit as st

def run():
    st.header("📊 Métricas de Desempeño")

    st.info("Las métricas se muestran después de hacer una consulta en el módulo de Groq.")

    st.markdown("""
    - ⏱ Time per Token
    - ⚡ Throughput
    - 🔢 Tokens entrada/salida
    """)