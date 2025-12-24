import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Encabezado de la aplicación
st.header('Análisis de anuncios de venta de coches')

# Cargar datos
car_data = pd.read_csv("vehicles_us.csv")

# Botones
hist_button = st.button('Construir histograma')
scatter_button = st.button('Construir gráfico de dispersión')

# Histograma
if hist_button:
    st.write('Histograma de la distribución del odómetro')

    fig = go.Figure(
        data=[go.Histogram(x=car_data['odometer'])]
    )

    fig.update_layout(
        title='Distribución del Odómetro',
        xaxis_title='Odómetro',
        yaxis_title='Frecuencia'
    )

    st.plotly_chart(fig, use_container_width=True)

# Gráfico de dispersión
if scatter_button:
    st.write('Gráfico de dispersión: Precio vs Odómetro')

    fig = go.Figure(
        data=[
            go.Scatter(
                x=car_data['odometer'],
                y=car_data['price'],
                mode='markers'
            )
        ]
    )

    fig.update_layout(
        title='Precio vs Odómetro',
        xaxis_title='Odómetro',
        yaxis_title='Precio'
    )

    st.plotly_chart(fig, use_container_width=True)
