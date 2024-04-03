import streamlit as st
from PIL import Image

image =  Image.open("./src/img/Capa_pagina01.jpg")
st.image(image)


# Definindo o layout da página
st.set_page_config(page_title="Detalhamento da Implementação - Passos Mágicos")


with open("./src/css/style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title("Detalhamento da Implementação - Passos Mágicos")

tab1, tab2 , tab3, tab4, tab5 = st.tabs(['Introdução', 'Formularios', 'Power Automate', 'Sharepoint', 'Power Bi'])

with tab1: 
    st.header("Mergulhe nos Detalhes da Implementação")
    st.markdown("""
    #### 🚀 Descubra Como a Magia Acontece em 'Passos Mágicos'

    Bem-vindo à espinha dorsal tecnológica de nosso projeto revolucionário! Nesta seção, vamos levá-lo por trás das cortinas para revelar **cada passo crucial** na jornada de transformação dos dados em 'Passos Mágicos'.

    🔍 **Da Teoria à Prática:** Acompanhe-nos na fascinante jornada desde o esboço inicial dos formulários digitais, passando pela incrível orquestração de dados automatizada pelo Power Automate, até a culminância no mundo vibrante de análises e insights fornecidos pelo Power BI.

    💡 **Transparência e Engajamento:** Nosso objetivo aqui é não apenas informar, mas também inspirar. Queremos que você veja a inovação e o pensamento estratégico em cada decisão técnica e sinta o mesmo entusiasmo que tivemos ao criar estas soluções.

    Prepare-se para explorar o coração pulsante da nossa missão, onde a tecnologia encontra o propósito social, e juntos, criam algo verdadeiramente mágico!
    """)
    st.write("""
    A implementação detalhada destaca como a tecnologia pode ser utilizada para otimizar processos, melhorar a gestão de dados e fornecer insights valiosos, alavancando o impacto social de 'Passos Mágicos'.
    """)

with tab2:
    st.header("Automatização dos Formulários: A Arte da Coleta de Dados")
    st.markdown("""
    Em nossa jornada para revolucionizar a 'Passos Mágicos', os formulários digitais no Microsoft Forms desempenham um papel fundamental. Eles são a ponte que nos conecta às informações cruciais, e cada um foi cuidadosamente desenhado para capturar os dados mais relevantes de maneira eficiente e intuitiva.

    📝 **Personalização e Precisão:** 
    Cada formulário foi habilmente personalizado para atender às necessidades específicas do projeto. Navegue pelas estruturas únicas de cada um, com uma variedade de tipos de perguntas e opções de resposta, projetadas para maximizar a precisão e relevância dos dados coletados.

    🔗 **Acesse Nossos Formulários:** 
    Prontos para ver nossos formulários em ação? Confira-os nos links abaixo e veja como a simplicidade encontra a eficácia:
    - [Formulário IPP](https://forms.office.com/e/VFx55t2zPU)
    - [Questionário IPV](https://forms.office.com/e/DqpdiN0sjQ)
    - [Questionário IPS](https://forms.office.com/e/jFuixbVhG3)

    Cada clique, cada resposta coletada, nos aproxima mais de nosso objetivo de transformação social através da 'Passos Mágicos'.
    """, unsafe_allow_html=True)

with tab3: 
    st.header("Integração com Power Automate")
    st.write("""
    - **Fluxos de Automação:** Descrição dos fluxos criados no Power Automate para capturar e processar as respostas dos formulários.
    - **Processamento de Dados:** Explicação dos cálculos e transformações aplicados aos dados coletados.
    """)

with tab4:
    st.header("Armazenamento de Dados no SharePoint")
    st.write("""
    - **Configuração do SharePoint:** Como as listas e tabelas foram estruturadas para armazenar dados coletados dos formulários.
    - **Mapeamento de Dados:** Detalhes sobre o relacionamento entre os dados dos formulários e as listas no SharePoint.
    """)

with tab5:
    st.header("Análise de Dados com Power BI")
    st.write("""
    - **Integração com Power BI:** Processo de importação e tratamento dos dados do SharePoint no Power BI.
    - **Visualizações e Dashboards:** Descrição das visualizações de dados criadas, incluindo tipos de gráficos e insights fornecidos.
    """)

# Conclusão




