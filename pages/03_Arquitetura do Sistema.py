import streamlit as st
from PIL import Image

# Definindo o layout da página
st.set_page_config(page_title="Arquitetura do Sistema - Passos Mágicos")

with open("./src/css/style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title("Arquitetura do Sistema - Passos Mágicos")

# Introdução à Arquitetura do Sistema
st.header("Visão Geral da Arquitetura do Sistema")
st.write("""
A arquitetura do sistema para o projeto 'Passos Mágicos' é projetada para otimizar a coleta, 
gerenciamento e análise de dados, utilizando uma combinação de ferramentas da Microsoft. 
Este sistema integrado proporciona uma solução eficiente e escalável para atender às necessidades da organização.
""")

# Inclusão dos Diagramas
st.subheader("Diagrama da Arquitetura do Sistema")

image = Image.open("./src/img/Diagrama.png")
st.image(image)

# Descrição dos Componentes do Sistema
st.header("Componentes do Sistema e Suas Interconexões")

# Descrição do Microsoft Forms
st.subheader("Microsoft Forms")
st.write("""
- **Função:** Coleta de dados através de formulários online.
- **Características:** Permite a criação de formulários customizáveis para a coleta de informações variadas.
""")

# Descrição do Power Automate
st.subheader("Power Automate")
st.write("""
- **Função:** Automatiza o fluxo de dados entre Microsoft Forms e SharePoint.
- **Características:** Cria fluxos de trabalho automatizados para transferir dados dos formulários para as listas do SharePoint.
""")

# Descrição do SharePoint
st.subheader("SharePoint")
st.write("""
- **Função:** Armazenamento e gestão de dados coletados.
- **Características:** Funciona como um sistema de gerenciamento de dados, armazenando informações dos formulários em listas.
""")

# Descrição do Power BI
st.subheader("Power BI")
st.write("""
- **Função:** Análise e visualização de dados.
- **Características:** Ferramenta para análise de dados armazenados no SharePoint, permitindo a criação de relatórios e dashboards interativos.
""")

# Conclusão
st.write("""
Esta arquitetura integrada permite uma coleta de dados mais eficiente, um armazenamento seguro e uma análise de dados avançada, contribuindo para um impacto social mais efetivo da 'Passos Mágicos'.
""")


