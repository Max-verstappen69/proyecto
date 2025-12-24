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
bar_button = st.button('Tipos de vehículo por fabricante')

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

# Gráfico de barras apiladas
if bar_button:
    st.write('Tipos de vehículo por fabricante')

    # Crear tabla de conteo
    grouped = (
        car_data
        .groupby(['manufacturer', 'type'])
        .size()
        .reset_index(name='count')
    )

    fig = go.Figure()

    # Crear una barra por cada tipo de vehículo
    for vehicle_type in grouped['type'].unique():
        data_type = grouped[grouped['type'] == vehicle_type]
        fig.add_trace(
            go.Bar(
                x=data_type['manufacturer'],
                y=data_type['count'],
                name=vehicle_type
            )
        )

    fig.update_layout(
        barmode='stack',
        title='Tipos de vehículo por fabricante',
        xaxis_title='Fabricante',
        yaxis_title='Cantidad',
        legend_title='Tipo de vehículo'
    )

    st.plotly_chart(fig, use_container_width=True)
