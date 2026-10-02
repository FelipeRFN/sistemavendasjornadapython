# título - Sistema de vendas
# Seção Cadastrar Vendas
    # Campo Data
    # Campo Vendedor - Ana, Bruno, Carla
    # Campo Produto - Notebook, Fone, Celular
    # Campo Quantidade
    # Campo Valor
    # Botão Cadastrar Vendas
        # Quando eu clicar no botão -> adicionar a venda na tabela
# Seção Vendas Cadastradas
    # Tabela com as Vendas
# Seção Dashboard
    # Card/Métrica -> Faturamento Total
    # Gráfico de Barra/Coluna -> Venda por vendedor
    # Gráfico de Pizza -> Venda por produto


# Streamlit -> Criar sites / apps
# pandas -> Base de dados
# plotly -> Criação de sites

import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar a base de vendas
tabela_vendas = pd.read_csv("vendas.csv")

st.write("# Sistema de Vendas")



# Seção de cadastro de vendas
st.sidebar.write("## Cadastrar Vendas") # O sidebar já deixa o texto no canto da tela.
data = st.sidebar.date_input("Data") # input de data com o nome "Data"
vendedor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla"]) # Inupt para selecionar um nome de uma lista. Coloco o nome do campo e depois a lista
produto = st.sidebar.selectbox("Produto", ["Notebook", "Celular", "Fone"])
quantidade = st.sidebar.number_input("Quantidade", step=1) # Caixa de campo numérico pra informar quantidade. Step para definir número inteiro
valor = st.sidebar.number_input("Valor")
botao_cadastrar = st.sidebar.button("Cadastrar Venda")

# Lógica de cadastro
if botao_cadastrar:
    nova_venda = [str(data), vendedor, produto, quantidade, valor] # Captura os valores dos campos
    ultima_linha = len(tabela_vendas) # Identifica a última linha vazia da tabela
    tabela_vendas.loc[ultima_linha] = nova_venda # Transforma a última linha identificada da tabela na lista de info preenchidas
    tabela_vendas.to_csv("vendas.csv", index=False)
    st.success("Venda Cadastrada!") # Notificação de Sucesso

# Seção de visualizar as vendas
st.write("## Vendas Cadastradas")
st.dataframe(tabela_vendas) # Criar um DF na página

# Seção de Dashboard
st.write("## Dashboard")

# Card/Métrica -> Faturamento Total
faturamento = tabela_vendas["valor"].sum()
st.metric("Faturamento Total", f"R$ {faturamento}") # Criar um cartão na tela.

# Gráfico de Barra/Coluna -> Venda por vendedor
grafico1 = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto")
grafico1.update_yaxes(nticks=5) # Para definir quantas linhas de grade o eixo Y terá
st.plotly_chart(grafico1) # Para exibir os gráficos na página criada

# Gráfico de Pizza -> Venda por produto
grafico2 = px.pie(tabela_vendas, names="produto", values="valor", hole=0.5) # O gráfico de pizza precisa apenas dos nomes que serão filtrados e valores para fatias. Hole varia de 0 a 1 e define o gráfico de rosca
st.plotly_chart(grafico2)

