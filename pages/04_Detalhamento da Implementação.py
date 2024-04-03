import streamlit as st

# Definindo o layout da página
st.set_page_config(page_title="Detalhamento da Implementação - Passos Mágicos")

with open("./src/css/style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title("Detalhamento da Implementação - Passos Mágicos")



# Introdução à Implementação
st.header("Mergulhe nos Detalhes da Implementação")
st.markdown("""
#### 🚀 Descubra Como a Magia Acontece em 'Passos Mágicos'

Bem-vindo à espinha dorsal tecnológica de nosso projeto revolucionário! Nesta seção, vamos levá-lo por trás das cortinas para revelar **cada passo crucial** na jornada de transformação dos dados em 'Passos Mágicos'.

🔍 **Da Teoria à Prática:** Acompanhe-nos na fascinante jornada desde o esboço inicial dos formulários digitais, passando pela incrível orquestração de dados automatizada pelo Power Automate, até a culminância no mundo vibrante de análises e insights fornecidos pelo Power BI.

💡 **Transparência e Engajamento:** Nosso objetivo aqui é não apenas informar, mas também inspirar. Queremos que você veja a inovação e o pensamento estratégico em cada decisão técnica e sinta o mesmo entusiasmo que tivemos ao criar estas soluções.

Prepare-se para explorar o coração pulsante da nossa missão, onde a tecnologia encontra o propósito social, e juntos, criam algo verdadeiramente mágico!
""")

# Seção de Automatização dos Formulários
st.header("Automatização dos Formulários")
st.write("""
- **Microsoft Forms:** Criação de formulários digitais customizados para coletar dados relevantes.
- **Configuração:** Detalhes sobre a estrutura dos formulários, tipos de perguntas e opções de resposta.
""")

# Seção de Integração com Power Automate
st.header("Integração com Power Automate")
st.write("""
- **Fluxos de Automação:** Descrição dos fluxos criados no Power Automate para capturar e processar as respostas dos formulários.
- **Processamento de Dados:** Explicação dos cálculos e transformações aplicados aos dados coletados.
""")

# Seção de Armazenamento de Dados no SharePoint
st.header("Armazenamento de Dados no SharePoint")
st.write("""
- **Configuração do SharePoint:** Como as listas e tabelas foram estruturadas para armazenar dados coletados dos formulários.
- **Mapeamento de Dados:** Detalhes sobre o relacionamento entre os dados dos formulários e as listas no SharePoint.
""")

# Seção de Análise de Dados com Power BI
st.header("Análise de Dados com Power BI")
st.write("""
- **Integração com Power BI:** Processo de importação e tratamento dos dados do SharePoint no Power BI.
- **Visualizações e Dashboards:** Descrição das visualizações de dados criadas, incluindo tipos de gráficos e insights fornecidos.
""")

# Conclusão
st.write("""
A implementação detalhada destaca como a tecnologia pode ser utilizada para otimizar processos, melhorar a gestão de dados e fornecer insights valiosos, alavancando o impacto social de 'Passos Mágicos'.
""")



