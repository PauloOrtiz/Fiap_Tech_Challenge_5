import streamlit as st

# Definindo o layout da página
st.set_page_config(page_title="Introdução e Objetivos - Passos Mágicos")
with open("./src/css/style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Título
st.title("Introdução e Objetivos do Projeto Passos Mágicos")


st.markdown("""
        # Bem-vindo à Nova Era da Associação Passos Mágicos

        Desde 1992, a Associação Passos Mágicos vem sendo uma luz guia na transformação da vida de crianças e jovens de Embu-Guaçu, oferecendo não apenas educação de qualidade, mas também assistência psicológica e uma visão ampliada do mundo. Idealizada por Michelle Flues e Dimetri Ivanoff, a associação começou sua jornada mágica em orfanatos e, em 2016, ampliou seu alcance, tornando-se um farol de esperança e mudança.

        ## Nosso Projeto: Digitalização para Ampliar Horizontes

        Com o apoio da FIAP em um projeto de pós-graduação, nós embarcamos em uma missão vital: transformar a maneira como a "Passos Mágicos" coleta e analisa dados. Movidos pelo desejo de otimizar os processos e trazer eficiência, reformulamos o sistema de 260 formulários no Google Forms para um modelo mais enxuto e poderoso, integrando apenas três formulários essenciais ao SharePoint. Esta inovação não só simplifica a coleta de dados, mas também facilita a análise, permitindo à associação focar ainda mais em seu objetivo principal: transformar vidas.

        ### Objetivos: Tecnologia a Serviço da Transformação Social

        Nossa meta com este projeto é clara:
        - **Redução de Complexidade:** Minimizar a quantidade de formulários para facilitar o gerenciamento de dados.
        - **Automatização e Integração:** Utilizar as ferramentas da Microsoft, incluindo Forms, Power Automate e Power BI, para automatizar o fluxo de dados e gerar análises profundas e insights.
        - **Impacto Ampliado:** Permitir que a equipe de "Passos Mágicos" dedique mais tempo e recursos àquilo que fazem de melhor - transformar a vida de jovens e crianças.

        #### O Futuro é Agora

        Este projeto não é apenas uma mudança de sistema; é um passo em direção a um futuro onde cada criança e jovem de Embu-Guaçu tem a oportunidade de realizar seus sonhos. É uma jornada para tornar a "Passos Mágicos" ainda mais eficiente, eficaz e equipada para ser uma agente de mudança transformadora nas vidas que toca.

        Junte-se a nós nesta jornada emocionante de transformação e inovação.
    """)

# Rodapé
st.write("Em cada dado, uma história. Em cada história, uma vida transformada. Juntos, damos passos mágicos em direção a um futuro de esperança e inovação.")