import streamlit as st

# Definindo o layout da página
st.set_page_config(page_title="Requisitos do Projeto - Passos Mágicos")

with open("./src/css/style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title("Requisitos do Projeto - Passos Mágicos")

# Seção de Detalhamento das Necessidades da Organização
st.header("Detalhamento das Necessidades da Organização")
st.write("""
A "Passos Mágicos" busca aprimorar sua capacidade de coleta, gerenciamento e análise de dados 
para melhorar a eficiência operacional e a eficácia das decisões. Com a implementação deste projeto, 
pretendemos alcançar os seguintes objetivos:
- **Automatização de Coleta de Dados:** Capacidade de coletar dados de forma rápida e estruturada através de formulários digitais.
- **Gestão Centralizada de Dados:** Necessidade de um repositório central para armazenar e acessar dados facilmente.
- **Análise de Dados e Relatórios:** Ferramentas para analisar dados e gerar relatórios visuais e interativos que facilitem a compreensão das informações.
- **Flexibilidade e Escalabilidade:** O sistema deve ser capaz de se adaptar a mudanças e crescimento da organização.
- **Conformidade e Segurança de Dados:** Garantir que a coleta e o armazenamento de dados estejam em conformidade com as leis de privacidade e proteção de dados.
""")

# Seção de Requisitos Funcionais
st.header("Requisitos Funcionais")
st.write("""
Os requisitos funcionais do projeto incluem:
- **Formulários Digitais Customizáveis:** Capacidade de criar e modificar formulários para coleta de dados.
- **Automatização do Fluxo de Dados:** Transferência automática de dados dos formulários para um sistema de armazenamento.
- **Indexação Automática de Respostas:** Classificar respostas dos formulários em categorias pré-definidas para análise.
- **Armazenamento Seguro de Dados:** Um sistema confiável no SharePoint para armazenar dados coletados e tabelas auxiliares.
- **Integração com Power BI:** Capacidade de importar e processar dados no Power BI para análise e visualização.
""")

# Seção de Requisitos Não Funcionais
st.header("Requisitos Não Funcionais")
st.write("""
Os requisitos não funcionais incluem:
- **Segurança:** O sistema deve garantir a segurança dos dados com controle de acesso e proteção contra vazamentos e acessos não autorizados.
- **Performance:** Capacidade de processar e analisar grandes volumes de dados com eficiência.
- **Confiabilidade:** Alta disponibilidade do sistema com mínima manutenção e tempo de inatividade.
- **Usabilidade:** Interface intuitiva e fácil de usar para usuários com diferentes níveis de habilidades técnicas.
- **Escalabilidade:** O sistema deve ser escalável para acomodar o crescimento da organização e o aumento do volume de dados.
- **Conformidade com Normas de Privacidade:** Adesão às leis e regulamentos de proteção de dados vigentes.
""")


