import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Carregar os dados
df = pd.read_csv("pizzas.csv")

# Criar o modelo de regressão linear
modelo = LinearRegression()
x = df[['diametro']]
y = df[['preco']]

# Treinar o modelo
modelo.fit(x, y) 

# Título da aplicação
st.title('Previsão de valores de uma pizza') 

# Divider para atualização automática da página web
st.divider() 

# Entrada do usuário para o diâmetro da pizza
diametro = st.number_input('Digite o diâmetro da pizza: ') 

# Fazer a previsão quando um diâmetro é fornecido
if diametro:
    preco_previsto = modelo.predict([[diametro]])[0][0] 
    st.write(f"O valor da pizza com diâmetro de {diametro:.2f}cm é de R${preco_previsto:.2f}.") 