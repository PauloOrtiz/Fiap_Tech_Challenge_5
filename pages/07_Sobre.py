import streamlit as st
from PIL import Image

st.set_page_config(page_title="Sobre", page_icon=":exclamation:")

with open("./src/css/style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True) 

image =  Image.open("./src/img/sobre.png")
st.image(image)

st.markdown("""
        # Sobre o Projeto

        Este projeto foi desenvolvido como parte do 5º Tech Challenge da turma de Data Science da FIAP. Foi uma oportunidade incrível para aprimorar nossas habilidades em análise de dados e colaboração em equipe, e gostaríamos de expressar nossa gratidão a todos que participaram deste desafio.

        ## Equipe do Projeto 

        - Amanda Bueno de Oliveira
        - João Guilherme Simões
        - Luiz Antonio Simette de Mello Campos
        - Paulo Henrique Barbosa Ortiz de Souza
                

        ## Orientadores 

        Este projeto não teria sido possível sem a orientação de nossos professores:

        - Edgard Joseph Kiriyama
        - Matheus Pavani

        Eles nos forneceram a estrutura necessária para concluir este desafio e estamos profundamente gratos pelo tempo e esforço que dedicaram à nossa aprendizagem.

        ##  Agradecimentos

        Também gostaríamos de agradecer aos nossos colegas de classe e a todos os envolvidos na organização deste desafio.

        ## Referências 📚

        **Documentação do Streamlit**. Disponível em: https://docs.streamlit.io/. Acesso em: 20 de Fevereiro de 2024.
        
        **Documentação da Microsoft**. Disponível em: https://learn.microsoft.com/. Acesso em: 20 de Fevereiro de 2024.
            
        **Site da Passos Magicos**. Disponível em: https://passosmagicos.org.br/. Acesso em: 20 de Fevereiro de 2024. 
        
        **SILVA, Dario Rodrigues da. Pesquisa Extensiva de Desenvolvimento Educacional - PEDE 2022. Associação Passos Mágicos. São Paulo, p.217. 2023.**
               
        Gostaríamos de expressar nossa gratidão a todas estas fontes por disponibilizar esses dados publicamente.
        """, unsafe_allow_html=True)