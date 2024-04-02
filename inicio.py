import streamlit as st

# Definindo o layout da página
st.set_page_config(page_title="Passos Mágicos - Transformação Digital", layout="wide")

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

# Botão de Navegação
if st.button("Comece a Explorar"):
    st.write("Navegue pelas seções para descobrir mais sobre o projeto...")

# Sumário
st.header("Sumário")
st.write("""
- Introdução e Objetivos
- Requisitos e Visão Geral da Solução
- Arquitetura e Implementação
- Dicionário de Dados
- Storytelling Interativo
""")

# Rodapé
st.write("Em cada dado, uma história. Em cada história, uma vida transformada. Juntos, damos passos mágicos em direção a um futuro de esperança e inovação.")