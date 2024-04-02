import streamlit as st

# Definindo o layout da página
st.set_page_config(page_title="Passos Mágicos - Transformação Digital")

with open("./src/css/style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Título
st.title("Bem-vindo à Transformação Digital de 'Passos Mágicos'")



# Introdução com Storytelling
st.write("""
Imagine uma organização onde cada passo conta, onde cada ação cria um eco de mudança e esperança. 
"Passos Mágicos" é essa organização, uma entidade dedicada a iluminar vidas e construir futuros melhores 
através de suas causas sociais. Este projeto, uma colaboração entusiasmada em uma datathon, é uma jornada 
para levar "Passos Mágicos" para o próximo patamar na era digital.

Neste espaço digital, você embarcará em uma viagem de inovação e impacto. Vamos guiar você através de como, 
com a ajuda das ferramentas da Microsoft – Forms, Power Automate, SharePoint e Power BI – transformamos dados 
dispersos em histórias de sucesso, ideias em ações, e desafios em soluções. Cada formulário preenchido, cada 
dado processado, e cada insight gerado no Power BI, não é apenas um número; é uma vida, um sonho, um passo em 
direção a um futuro brilhante.
""")

# Rodapé
st.write("Em cada dado, uma história. Em cada história, uma vida transformada. Juntos, damos passos mágicos em direção a um futuro de esperança e inovação.")