import streamlit as st
import pandas as pd
import plotly_express as px
 
car_data = pd.read_csv('vehicles_us.csv')
header = st.header('Datos de Anuncios de Ventas de Autos')
buil_scatter = st.checkbox('Crear Grafico de Dispersion')
build_histogram = st.checkbox('Construir un histograma')

# contruir un Histograma con el boton con checkbox
if build_histogram:
    st.write('Creación un histograma con los datos')    
    fig_hist = px.histogram(car_data, x='odomoter')

if buil_scatter:
    st.write('Crea un grafico de Dispersion con los datos')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", color='model')
    