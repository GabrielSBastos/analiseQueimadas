import numpy as np
import pandas as pd
import plotly.express as px

# Carrega o CSV
df = pd.read_csv("./incendios-sample.csv")

estadosMais = df.groupby('state')['number'].sum().sort_values(ascending=False).head(10).reset_index()

fig = px.bar(
    estadosMais,
    x='number',
    y='state',
    orientation='h',
    title='Top 10 estados por número',
    category_orders={'state': estadosMais['state']},
labels = {
    "number": "N° de queimadas",
    "state": "Estado",
},
)
fig.show()
