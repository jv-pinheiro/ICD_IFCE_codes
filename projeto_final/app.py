import streamlit as st
import numpy as np
import joblib

#Carregamento do modelo treinado
modelo = joblib.load('detectaInadimplencia.pkl')

#Configurações da página
st.title("🔍 Previsão de Inadimplência")
st.markdown("Preencha os dados do cliente para prever se ele **se encaixa no perfil de inadimplente**.")
st.set_page_config(page_title="App Inadimplente", page_icon="🔍")


#Entradas do usuário
sexo = st.selectbox("Sexo", ['Masculino', 'Feminino'])  # 1 ou 2
educacao = st.selectbox("Nível de Escolaridade", ['Fundamental', 'Ensino Médio', 'Universitário'])  # 1, 2, 3
estado_civil = st.selectbox("Estado Civil", ['Casado(a)', 'Solteiro(a)', 'Outro'])  # 1, 2, 3
num_meses_atrasado = st.slider("Número de Meses Atrasado", 0, 12, 3)
maior_atraso = st.slider("Maior Atraso (em meses)", 0, 12, 4)
qtd_pagamentos_em_dia = st.number_input("Quantidade de Pagamentos em Dia", min_value=0, value=5)
variacao_fatura = st.number_input("Variação da Fatura (R$)", value=150.5)
pagamento_total = st.number_input("Pagamento Total (R$)", value=4000.0)
valor_credito = st.number_input("Valor Total de Crédito (R$)", value=20000.0)

#Conversão das categorias para números
sexo_val = 1 if sexo == 'Masculino' else 2
educacao_val = {'Fundamental': 1, 'Ensino Médio': 2, 'Universitário': 3}[educacao]
estado_civil_val = {'Casado(a)': 1, 'Solteiro(a)': 2, 'Outro': 3}[estado_civil]

#Entrada para o modelo
entrada = np.array([[
    sexo_val,
    educacao_val,
    estado_civil_val,
    num_meses_atrasado,
    maior_atraso,
    qtd_pagamentos_em_dia,
    variacao_fatura,
    pagamento_total,
    valor_credito
]])

# Botão para prever
if st.button("🔍 Prever Inadimplência"):
    pred = modelo.predict(entrada)
    if pred[0] == 0:
        st.success("🟢 Cliente se encaixa no perfil de **NÃO INADIMPLENTE**.")
    else:
        st.error("🔴 Cliente se encaixa no perfil de **INADIMPLENTE**.")