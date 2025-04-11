import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from streamlit_card import card
from streamlit_extras.dataframe_explorer import dataframe_explorer
import plotly.offline as py
import plotly.graph_objs as go
import plotly.express as px


st.title("Análise dos dados de queimadas no Brasil (2012-2023)")
st.markdown("Dados disponíveis em: https://terrabrasilis.dpi.inpe.br/")

st.divider()

st.header("Sobre os dados:")
st.write("Este trabalho analisa uma amostra do dataset sobre focos de queimadas no Brasil (2012-2023).")
st.write("Quantidade de linhas da amostra: 2500. Originalmente havia quase 12 mil linhas")
st.write("Colunas: ano, UF, mês,número de queimadas.")

st.divider()
st.header("Metas e objetivos:")
st.write("Analisar a distribuição e a evolução dos incêndios florestais no Brasil entre 2012 e 2023, com o objetivo de identificar padrões sazonais, as regiões mais afetadas, os períodos de maior incidência, além de mapear a distribuição geográfica para compreender como esses incêndios estão distribuídos pelo território nacional.")

st.divider()

st.subheader("Explore os dados")
st.write("Você pode selecionar uma ou mais colunas para filtrar abaixo:")
df = pd.read_csv("./incendios-sample.csv")
filter_df = dataframe_explorer(df)
st.dataframe(filter_df[["year", "state", "month", "number"]])
st.subheader("Estatísticas")

queimadas = np.sum(df.number).round()


col1, col2, col3 = st.columns(3,gap="small")

with col1:
    queimadas = card(
    title=str(queimadas),
    text="Queimadas",
    styles={
      "card": {
        "width": "180px",
        "height": "180px",
        "padding": "0px",
        "background-image": "linear-gradient(to right top, #051937, #00456b, #007899, #00adbd, #47e4d4)"
        }
    }
)

with col2:
    totalDados = card(
    title=str("Mais de 38 mil"),
    text="analizados",
    styles={
      "card": {
        "width": "180px",
        "height": "180px",
        "padding": "0",
        "background-image": "linear-gradient(to right top, #051937, #00456b, #007899, #00adbd, #47e4d4)"
        }
    }
)

with col3:
    totalDados = card(
    title=str("Diversos gráficos"),
    text="interativos",
    styles={
        "card": {
            "width": "180px",
            "height": "180px",
            "padding": "0",
            "background-image": "linear-gradient(to right top, #051937, #00456b, #007899, #00adbd, #47e4d4)"
                }
            }
        )

st.divider()


# Gráfico 1
st.header("Relação Anos e Incêndios")

ano = list(df.year.unique())

quantidadeIncendioAno = []

def converteInteiro(number):
    if str(number)[-2] == '.':
        return int(str(number)[:-2])
    if str(number)[1] == '.' or str(number)[2] == '.':
        return int(str(number).replace('.',''))

df["number"] = df.apply(lambda row: converteInteiro(row["number"]), axis=1)

for i in ano:
    total_incendios = df.loc[df['year'] == i].number.sum()
    quantidadeIncendioAno.append(total_incendios)

analise = {'year': ano, 'number': quantidadeIncendioAno}

analiseAno = pd.DataFrame(analise)

AnoQueimadas = px.bar(analiseAno, x="year", y="number",
labels = {
    "year": "Ano",
    "number": "Número",
}
)
st.plotly_chart(AnoQueimadas)

####### Fim Gráfico 1

st.divider()

# Gráfico 2
estadosMais = df.groupby('state')['number'].sum().sort_values(ascending=False).head(10).reset_index()
estadosMaisAnalise= pd.DataFrame(estadosMais)
st.header("10 estados com mais queimadas (2012-2023)")

estadosMaisQueimadas = px.bar(
    estadosMais,
    x='number',
    y='state',
    orientation='h',
    category_orders={'state': estadosMais['state']},
labels = {
    "number": "N° de queimadas",
    "state": "Estado",
},
)
st.plotly_chart(estadosMaisQueimadas)


