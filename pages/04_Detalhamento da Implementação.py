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
    #### 🚀 Descubra Como a Magia Acontece em Passos Mágicos

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
    - [Formulário Psicologia](https://forms.office.com/e/xdv9Au27bL)

    Cada clique, cada resposta coletada, nos aproxima mais de nosso objetivo de transformação social através da Passos Mágicos.
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
    """, unsafe_allow_html=True)

    file_path = './src/data/FormularioIPP_20240407122026.zip'

    # Lendo o arquivo em modo binário
    with open(file_path, "rb") as file:
        btn = st.download_button(
                label="Baixar Exemplo de Fluxo do Power Automate (arquivo zip)",
                data=file,
                file_name="Codigo da automação.zip",
                mime="application/octet-stream"
            )


    st.markdown("""
    #### 📊 Tabelas de Índices - Entendendo os Números:
    Compreenda como cada resposta nos formulários é convertida em um índice numérico valioso. Cada formulário possui sua própria lógica de pontuação:
    - **Tabela de Índices do Formulário 1:**
    """, unsafe_allow_html=True)
    image1 = Image.open("./src/img/tabela_IPP.png")
    st.image(image1, caption= "Tabela IPP - Gerado pela Passos Magicos")
    st.markdown("""- **Tabela de Índices do Formulário 2:** Detalhes aqui.
    """, unsafe_allow_html=True)
    image2 = Image.open("./src/img/tabela_IPS.png")
    st.image(image2, caption= "Tabela IPS - Gerado pela Passos Magicos")
    st.markdown("""- **Tabela de Índices do Formulário 3:** Detalhes aqui.
    """, unsafe_allow_html=True)
    image3 = Image.open("./src/img/tabele_IPV.png")
    st.image(image3, caption= "Tabela IPV - Gerado pela Passos Magicos")
    st.markdown("""Explore estes recursos e veja como dados simples são transformados em poderosos insights!
    """, unsafe_allow_html=True)
    
    


with tab4:
    st.header("Armazenamento de Dados Avançado no SharePoint")
    st.markdown("""
    ### 📚 Organizando Dados com Precisão e Eficiência

    O SharePoint desempenha um papel vital em nossa missão com 'Passos Mágicos', atuando como o repositório central para os dados que moldam o futuro das crianças e jovens. A escolha desta ferramenta não foi aleatória; ela oferece uma integração impecável com o Power BI, o que facilita uma transição suave dos dados para a análise.

    #### 🌐 Configuração Detalhada do SharePoint:
    - **Tabelas Estratégicas:** Criamos estruturas de tabelas e listas meticulosamente planejadas para cada tipo de dado coletado.
    - **Tabela Alunos:** Contém informações detalhadas dos alunos, como matrícula, nome, turma, sexo e idade.
    - **Tabela Turmas:** Registra informações das turmas, incluindo código e nome.
    - **Formulários e Tabelas de Índice:** Para cada formulário, temos uma tabela correspondente de respostas e uma tabela de índices.

    #### 🔗 Mapeamento de Dados - A Arte de Criar Conexões:
    - Cada dado coletado nos formulários encontra seu caminho e propósito em nossas tabelas no SharePoint. O mapeamento é feito com precisão, garantindo que cada peça de informação esteja no lugar certo.

    #### 🚀 Por Que SharePoint?
    - **Sinergia com Power BI:** Uma das razões fundamentais para escolher o SharePoint é sua facilidade de integração com o Power BI. Essa combinação permite que transformemos dados brutos em insights valiosos e visuais interativos de forma rápida e eficaz.

    #### 🖼️ Uma Visão Clara com Imagens:
    - **Imagens das Tabelas:** Abaixo, você encontrará capturas de tela das nossas tabelas no SharePoint, oferecendo uma visão clara de como os dados são organizados:
    """, unsafe_allow_html=True)
    image4 = Image.open("./src/img/Tabela_Aluno.PNG")
    st.image(image4, caption= "Tabela Aluno - Gerado pelo grupo")

    image5 = Image.open("./src/img/Tabela_Turmas.PNG")
    st.image(image5, caption= "Tabela Turmas - Gerado pelo grupo")

    image6 = Image.open("./src/img/tabela_Formulario_IPP.PNG")
    st.image(image6, caption= "Tabela Formulario IPP - Gerado pelo grupo")

    image7 = Image.open("./src/img/tabela_Formulario_IPS.PNG")
    st.image(image7, caption= "Tabela Formulario IPS - Gerado pelo grupo")

    image8 = Image.open("./src/img/tabela_Formulario_IPV.PNG")
    st.image(image8, caption= "Tabela Formulario IPV - Gerado pelo grupo")

    image9 = Image.open("./src/img/tabela_Indice_IPP.PNG")
    st.image(image9, caption= "Tabela Indice IPP - Gerado pelo grupo")

    image10 = Image.open("./src/img/tabela_Indice_IPS.PNG")
    st.image(image10, caption= "Tabela Indice IPS - Gerado pelo grupo")

    image11 = Image.open("./src/img/tabela_Indice_IPV.PNG")
    st.image(image11, caption= "Tabela Indice IPV - Gerado pelo grupo")

    st.markdown("""       
    Mergulhe nos detalhes e veja como organizamos nossos dados para maximizar o impacto e a eficiência de nossas iniciativas!
    """, unsafe_allow_html=True)

with tab5:
    st.header("Decifrando Dados: A Magia do Power BI")
    st.markdown("""
    ### 🔍 Desvendando Histórias por Trás dos Números

    Na 'Passos Mágicos', transformamos dados em histórias e insights, e o Power BI é nosso fiel escudeiro nessa jornada de descoberta. Vamos mergulhar em como os dados do SharePoint ganham vida no Power BI, revelando padrões, tendências e oportunidades.

    #### 🔄 Do SharePoint ao Power BI:
    - **Fluxo de Dados Refinado:** A integração começa com a importação meticulosa dos dados armazenados no SharePoint. Nosso processo assegura que cada dado seja tratado e refinado, preparando o palco para análises profundas.
    - **Transformação e Enriquecimento de Dados:** Cada número, cada resposta é mais do que um dado; é uma peça do quebra-cabeça que montamos no Power BI.

    #### 📊 Construindo Dashboards Impactantes:
    - **Narrativas Visuais Poderosas:** Nos dashboards, cada gráfico, cada visualização é uma história. Utilizamos uma variedade de gráficos para ilustrar as nuances dos dados - desde gráficos de barra e linha até mapas de calor e muito mais.
    - **Insights em Tempo Real:** Com o Power BI, fornecemos insights que impulsionam decisões e estratégias. É aqui que dados se transformam em ação.

    #### 🖼️ Veja Com Seus Próprios Olhos:
    - **Diagrama das Tabelas:** Abaixo, você pode ver como as tabelas estão estruturadas no Power BI:
    """, unsafe_allow_html=True)
    
    image12 = Image.open("./src/img/diagrama_powerbi.png")
    st.image(image12, caption= "Diagrama de tabela no power bi - Gerado pelo grupo")

    st.markdown("""
    #### 🚀 Para uma Experiência Imersiva:
    - **Explore Nosso Dashboard:** Não perca nosso dashboard interativo! Para uma experiência completa, visite a página 'Dashboard' no menu lateral e veja como a análise de dados pode ser transformadora.

    Prepare-se para ser fascinado pela beleza dos dados e pelo poder das visualizações que transformam informações em ações.
    """, unsafe_allow_html=True)
