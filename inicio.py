import streamlit as st

# Definindo o layout da página
st.set_page_config(page_title="Introdução e Objetivos - Passos Mágicos")
with open("./src/css/style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Título
st.title("Introdução e Objetivos do Projeto Passos Mágicos")

# Seção de Introdução
st.header("Introdução")
st.write("""
O projeto 'Passos Mágicos' representa uma iniciativa inovadora de transformação digital para uma organização dedicada a causas sociais significativas. Surgiu da necessidade de modernizar os processos de coleta, gestão e análise de dados, buscando uma maior eficiência e impacto nas ações da organização.
""")

# Seção de Objetivos
st.header("Objetivos do Projeto")
st.write("""
Os principais objetivos do projeto incluem:
- **Automatização de Formulários:** Utilizar Microsoft Forms para otimizar a coleta de dados.
- **Integração e Automatização de Processos:** Implementar o Power Automate para assegurar uma transferência eficiente de dados para o SharePoint.
- **Melhoria na Gestão de Dados:** Aproveitar as capacidades do SharePoint para armazenar e gerenciar dados de forma centralizada e segura.
- **Análise Avançada de Dados:** Utilizar o Power BI para transformar dados coletados em insights valiosos e relatórios interativos.
- **Impacto Social:** Contribuir para a eficácia e eficiência das decisões e ações da 'Passos Mágicos', potencializando seu impacto social.
""")

# Seção de Contexto
st.header("Contexto de Desenvolvimento")
st.write("""
Este projeto nasceu de uma datathon, onde o desafio era utilizar tecnologia para solucionar problemas reais enfrentados por organizações sem fins lucrativos. A 'Passos Mágicos' foi escolhida como beneficiária desta iniciativa, dada a sua importante missão social e a necessidade evidente de uma transformação digital.
""")

# Seção de Expectativas
st.header("Expectativas para o Futuro")
st.write("""
Esperamos que este projeto não apenas melhore os processos internos da 'Passos Mágicos', mas também inspire outras organizações a adotarem tecnologias digitais para ampliar seu impacto social. Acreditamos que a transformação digital é uma poderosa alavanca para o avanço social e estamos entusiasmados para ver as mudanças positivas que ela trará.
""")

# Rodapé
st.write("Em cada dado, uma história. Em cada história, uma vida transformada. Juntos, damos passos mágicos em direção a um futuro de esperança e inovação.")