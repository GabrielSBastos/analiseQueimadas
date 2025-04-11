import pandas as pd
import numpy as np

# Limpeza de dados

data = pd.read_csv("./Incendios.csv", sep=";")
select_data = data[["year", "state", "month", "number"]] # Seleciona as colunas do arquivo
select_data = select_data.replace(["", " ", "  "], np.nan)  # Remove os dados faltantes
select_data_filter = select_data.dropna()
amostra = select_data_filter.sample(n=2500)

amostra.to_csv("incendios-sample.csv", index=False)

st.subheader("Estatísticas")

