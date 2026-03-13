import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar dataset limpio
df = pd.read_csv("data/processed/ventas_clean.csv", parse_dates=["order_date"], dayfirst=True)
#----------------------------------------------

#Titulo
st.title(" Dashboard de Inteligencia de Ventas")
st.write("Este dashboard muestra KPIs, tendencias y análisis de ventas.")

# KPIs 
st.metric("Ventas Totales", f"${df['sales'].sum():,.2f}")
st.metric("Promedio por Orden", f"${df['sales'].mean():,.2f}")
st.metric("Número de Clientes", df['customer_id'].nunique())

#Filtros interactivos
fecha_inicio = st.date_input("Fecha inicio", df["order_date"].min())
fecha_fin = st.date_input("Fecha fin", df["order_date"].max())
df_filtrado = df[(df["order_date"] >= pd.to_datetime(fecha_inicio)) & (df["order_date"] <= pd.to_datetime(fecha_fin))]

# Graficos de Ventas por Fecha
fig, ax = plt.subplots(figsize=(10,5))
df_filtrado.groupby("order_date")["sales"].sum().plot(ax=ax)
ax.set_title("Ventas por fecha")
st.pyplot(fig)

#Top productos mas vendidos
top_productos = df_filtrado.groupby("product_id")["sales"].sum().sort_values(ascending=False).head(10)
fig, ax = plt.subplots(figsize=(8,5))
sns.barplot(x=top_productos.index, y=top_productos.values, ax=ax)
ax.set_title("Top 10 productos más vendidos")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
st.pyplot(fig)

#Estacionalidad (Ventas por mes)
df_filtrado["mes"] = df_filtrado["order_date"].dt.month
ventas_por_mes = df_filtrado.groupby("mes")["sales"].sum()

fig, ax = plt.subplots(figsize=(8,5))
ventas_por_mes.plot(kind="bar", ax=ax)
ax.set_title("Ventas por mes (estacionalidad)")
st.pyplot(fig)
