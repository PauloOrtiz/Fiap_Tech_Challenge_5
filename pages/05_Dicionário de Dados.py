import streamlit as st
from PIL import Image

st.set_page_config(page_title="Dicionário de Dados - Passos Mágicos")

with open("./src/css/style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

image =  Image.open("./src/img/dicionario.jpg")
st.image(image)
# Definindo o layout da página



st.title("Dicionário de Dados - Passos Mágicos")
st.header("Visão Geral do Dicionário de Dados")
st.write("""
O Dicionário de Dados é uma ferramenta essencial para compreender a estrutura das informações 
gerenciadas no projeto 'Passos Mágicos'. Abaixo estão detalhadas as tabelas utilizadas, seus campos 
e como eles se inter-relacionam.
""")

# Tabela Exemplo 1
st.subheader("Tabela: Turmas")
st.write("""
| Campo       | Tipo        | Descrição                    | Restrições                  |
|-------------|-------------|------------------------------|----------------------------|
| Cod_Turmas  | Alfanumérico| Identificador único da turma | Valores únicos, Chave Primária |
| Nome_Turmas | Alfanumérico| Descrição ou nome da turma   | -                          |
""", unsafe_allow_html=True)

# Tabela Exemplo 2 (Adicione mais tabelas conforme necessário)
st.subheader("Tabela: Alunos")
st.write("""
| Campo      | Tipo        | Descrição                            | Restrições                        |
|------------|-------------|--------------------------------------|----------------------------------|
| Matricula  | Numérico    | Número de matrícula do aluno         | Valores únicos, Chave Primária    |
| Nome_Aluno | String      | Nome completo do aluno               | Campo obrigatório                |
| Turma      | Alfanumérico| Código da turma do aluno             | Chave Estrangeira (Turmas.Cod_Turmas) |
| Sexo       | String      | Sexo do aluno                        | Opções: F, M, I                  |
| Idade      | Numérico    | Idade do aluno                       | Campo obrigatório                |
""", unsafe_allow_html=True)

st.subheader("Tabela: Formulário IPP (Strings)")
st.write("""
| Campo               | Tipo   | Descrição                                 | Restrições                    |
|---------------------|--------|-------------------------------------------|------------------------------|
| Matricula           | Numérico | Número de matrícula do aluno             | Chave Estrangeira (Alunos.Matricula) |
| Desempenho Cognitivo | String | Avaliação do desempenho cognitivo        | -                            |
| Estado Emocional    | String | Avaliação do estado emocional            | -                            |
| Comportamento       | String | Avaliação do comportamento do aluno      | -                            |
| Interações Sociais  | String | Avaliação das interações sociais         | -                            |
""", unsafe_allow_html=True)


st.subheader("Tabela: Índice IPP (Numéricos)")
st.write("""
| Campo               | Tipo   | Descrição                                 | Restrições                    |
|---------------------|--------|-------------------------------------------|------------------------------|
| Matricula           | Numérico | Número de matrícula do aluno             | Chave Estrangeira (Alunos.Matricula) |
| Desempenho Cognitivo | Numérico | Índice numérico do desempenho cognitivo | -                            |
| Estado Emocional    | Numérico | Índice numérico do estado emocional     | -                            |
| Comportamento       | Numérico | Índice numérico do comportamento        | -                            |
| Interações Sociais  | Numérico | Índice numérico das interações sociais  | -                            |
""", unsafe_allow_html=True)
# Conclusão
st.write("""
Este dicionário de dados proporciona uma base sólida para a compreensão e gestão eficaz dos dados 
dentro do projeto 'Passos Mágicos'.
""")

