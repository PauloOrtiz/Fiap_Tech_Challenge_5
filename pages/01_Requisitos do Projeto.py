import streamlit as st

# Definindo o layout da página
st.set_page_config(page_title="Passos Mágicos - Transformação Digital")

with open("./src/css/style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# Título
st.title("Bem-vindo à Transformação Digital de 'Passos Mágicos'")

