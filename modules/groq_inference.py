import streamlit as st
from utils.groq_utils import query_groq

def run():
    st.header("🤖 Inferencia con Groq")

    system_prompt = st.text_area("System Prompt", "You are a helpful assistant")
    user_prompt = st.text_area("User Prompt", "Explain transformers simply")

    temp_value = float(temperature)
    top_p_value = float(top_p)

    if st.button("Generar respuesta"):
        response, metrics = query_groq(system_prompt, user_prompt, temperature, top_p)

        st.subheader("Respuesta:")
        st.write(response)

        st.subheader("Métricas:")
        st.write(metrics)
