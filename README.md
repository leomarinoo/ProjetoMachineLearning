# ProjetoMachineLearning

## Apresentação do Projeto

Este projeto utiliza técnicas de **Machine Learning** para prever o valor de uma pizza com base em seu diâmetro. O objetivo é treinar um modelo de regressão linear com um conjunto de dados contendo informações sobre o diâmetro e o preço das pizzas. Após o treinamento, o modelo é capaz de prever o preço de uma pizza para qualquer valor de diâmetro inserido.

- O processo é dividido em duas partes principais:

1. **Análise e Treinamento**: Utilizamos um notebook Jupyter para explorar os dados e treinar o modelo de regressão linear. O notebook facilita a análise dos dados e o desenvolvimento do modelo com a flexibilidade das células de código.

2. **Aplicação Web**: Desenvolvemos uma aplicação interativa com Streamlit que permite ao usuário inserir o diâmetro de uma pizza e obter a previsão do seu valor com base no modelo treinado. 

Assim, o projeto combina análise de dados e desenvolvimento web (Streamlit) para fornecer uma ferramenta prática de previsão de preços de pizza com base em dados históricos.
 

## Requisitos

- Pandas
- Scikit-learn
- Streamlit

## Estrutura do Projeto

Projeto-ML/
├── pasta_1/
│ └── testes.ipynb
├── pasta_2/
│ └── app.py
├── pizzas.csv
└── README.md

## Como usar

1- Para rodar o streamlit tem que escrever no terminal:

streamlit run app.py 

## Documentação

https://docs.streamlit.io/

https://pandas.pydata.org/docs/

https://scikit-learn.org/0.21/documentation.html 