import streamlit as st
import plotly.express as px
import pandas as pd

# Título do Dashboard
st.title("Dashboard de Exemplo com Streamlit")

# Texto explicativo
st.markdown("Este é um exemplo de dashboard simples com gráficos interativos usando Streamlit e Plotly.")

# Carregando dados de exemplo (gapminder)
df = px.data.gapminder()

# Gráfico interativo: gráfico de dispersão com Plotly
fig = px.scatter(df, x="gdpPercap", y="lifeExp", color="continent", size="pop", hover_name="country", log_x=True, size_max=60)

# Exibindo o gráfico interativo no Streamlit
st.plotly_chart(fig)

# Seção de filtro para visualizar dados
st.sidebar.header("Filtros")

# Filtro por continente
continent_filter = st.sidebar.selectbox("Escolha o continente", df['continent'].unique())

# Filtrando os dados com base no filtro
df_filtered = df[df['continent'] == continent_filter]

# Exibindo uma tabela filtrada
st.write(f"Dados do continente: {continent_filter}")
st.write(df_filtered)

# Exibindo uma estatística simples
st.subheader("Estatísticas Descritivas")
st.write(df_filtered.describe())
