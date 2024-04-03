import streamlit as st
from PIL import Image


# Definindo o layout da página
st.set_page_config(page_title="Requisitos do Projeto - Passos Mágicos")

with open("./src/css/style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

image =  Image.open("./src/img/Capa_pagina01.jpg")
st.image(image)


# Título da página
st.title("Requisitos do Projeto - Passos Mágicos")

# Seção de Detalhamento das Necessidades da Organização
st.header("Detalhamento das Necessidades da Organização")
st.write("""
"Passos Mágicos" busca aprimorar sua capacidade de coleta, gerenciamento e análise de dados 
para melhorar a eficiência operacional e a eficácia das decisões. As principais necessidades 
incluem automatização da coleta de dados, gestão centralizada de dados, análise de dados e 
relatórios, flexibilidade e escalabilidade do sistema, e conformidade e segurança de dados.
""")

# Seção de Requisitos Funcionais
st.header("Requisitos Funcionais")
st.write("""
- **Formulários Digitais Customizáveis:** Criação e modificação de formulários para coleta de dados.
- **Automatização do Fluxo de Dados:** Transferência automática de dados dos formulários para um sistema de armazenamento.
- **Indexação Automática de Respostas:** Classificação de respostas dos formulários em categorias para análise.
- **Armazenamento Seguro de Dados:** Um sistema confiável no SharePoint para armazenamento de dados.
- **Integração com Power BI:** Importação e processamento de dados no Power BI para análise e visualização.
""")

# Seção de Requisitos Não Funcionais
st.header("Requisitos Não Funcionais")
st.write("""
- **Segurança:** Garantir a segurança dos dados com controle de acesso e proteção contra vazamentos e acessos não autorizados.
- **Performance:** Processamento e análise de grandes volumes de dados com eficiência.
- **Confiabilidade:** Alta disponibilidade do sistema com mínima manutenção e tempo de inatividade.
- **Usabilidade:** Interface intuitiva e fácil de usar para usuários com diferentes níveis de habilidades técnicas.
- **Escalabilidade:** Capacidade de adaptação a mudanças e crescimento da organização.
- **Conformidade com Normas de Privacidade:** Adesão às leis e regulamentos de proteção de dados vigentes.
""")

