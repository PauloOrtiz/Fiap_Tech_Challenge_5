import streamlit as st
from PIL import Image

# Definindo o layout da página
st.set_page_config(page_title="Detalhamento da Implementação - Passos Mágicos")


with open("./src/css/style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

image =  Image.open("./src/img/Implementacao.jpg")
st.image(image)




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
    st.header("Integração Revolucionária com Power Automate")
    st.markdown("""
    ### O Coração da Automação

    A magia por trás da eficiência de nossos formulários reside na integração com o Power Automate, uma ferramenta poderosa que transforma respostas simples em dados profundos e acionáveis.

    #### 🚀 Automatizando com Inteligência:
    - **Trigger de Início:** Cada vez que um formulário é respondido, o Power Automate entra em ação, iniciando com o gatilho "When a new response is submitted".
    - **Captura de Detalhes:** A ação "Get response details" é o primeiro passo para a magia acontecer, coletando cada resposta dada.

    #### 🔢 Cálculo de Índices - A Alquimia dos Dados:
    - Para cada questão dos formulários, uma variável é criada, transformando respostas textuais em números predeterminados pela 'Passos Mágicos'.
    - A culminância desse processo é uma variável final, calculando a média dessas respostas, oferecendo uma visão quantitativa única das informações coletadas.

    #### 💾 Armazenamento Estratégico no SharePoint:
    - As respostas dos formulários e os cálculos são armazenados meticulosamente em listas no SharePoint, tanto na forma textual integral quanto na forma de índices calculados.

    ### Material de Apoio e Exemplos Práticos:
    Abaixo, você encontrará materiais que exemplificam nosso processo e proporcionam uma compreensão mais profunda do trabalho realizado.

    #### 📥 Faça o Download do Exemplo de Fluxo no Power Automate:
    - [Baixar Exemplo de Fluxo do Power Automate (arquivo WinRAR)](link_para_download)

    #### 📊 Tabelas de Índices - Entendendo os Números:
    Compreenda como cada resposta nos formulários é convertida em um índice numérico valioso. Cada formulário possui sua própria lógica de pontuação:
    - **Tabela de Índices do Formulário 1:**
    """, unsafe_allow_html=True)
    image1 = Image.open("/src/img/tabela_IPP.png")
    st.image(image1, caption= "Tabela IPP - Gerado pela Passos Magicos")
    st.markdown("""- **Tabela de Índices do Formulário 2:** Detalhes aqui.
    """, unsafe_allow_html=True)
    image2 = Image.open("/src/img/tabela_IPS.png")
    st.image(image2, caption= "Tabela IPS - Gerado pela Passos Magicos")
    st.markdown("""- **Tabela de Índices do Formulário 3:** Detalhes aqui.
    """, unsafe_allow_html=True)
    image3 = Image.open("/src/img/tabele_IPV.png")
    st.image(image3, caption= "Tabela IPV - Gerado pela Passos Magicos")
    st.markdown("""Explore estes recursos e veja como dados simples são transformados em poderosos insights!
    """, unsafe_allow_html=True)
    

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




