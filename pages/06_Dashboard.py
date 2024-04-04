import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

st.set_page_config(page_title="Dashboard - Passos Mágicos")

with open("./src/css/style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

image =  Image.open("./src/img/Capa_pagina01.jpg")
st.image(image)


 
# Título da página
st.title("Dashboard de Análise de Dados - Passos Mágicos")

# Introdução ao Dashboard
st.header("Visão Geral do Dashboard")
st.write("""
Explore os insights interativos gerados pelo nosso dashboard do Power BI. 
Este painel oferece uma visão aprofundada dos dados coletados e analisados no projeto 'Passos Mágicos'.
""")

# Incorporar o Dashboard do Power BI
# Substitua 'your_power_bi_report_url' pela URL do seu relatório do Power BI
power_bi_report_url = "https://app.powerbi.com/view?r=eyJrIjoiOWNjNDRiNGEtOGY2NC00Zjg5LTgxMTgtZGZjYTY5Y2I4ZWNiIiwidCI6IjQ1YmE3MjVmLWQyNjAtNDVjMy1hYzg1LTExZjQzMzQ3MTI3NyJ9&pageName=ReportSection359d4dbd6185031527ab"
st.subheader("Dashboard do Power BI")
components.iframe(power_bi_report_url, width=700, height=500, scrolling=True)