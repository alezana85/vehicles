import streamlit as st
import pandas as pd
import plotly_express as px
 
car_data = pd.read_csv('vehicles_us.csv')
header = st.header('Datos de Anuncios de Ventas de Autos')
build_scatter = st.checkbox('Crear Grafico de Dispersion')
build_histogram = st.checkbox('Construir un histograma')
hist_button = st.button('Construir Histograma')

# contruir un Histograma con el boton con checkbox
if hist_button:
    st.write('Creación un Histograma con los datos <img src="histogram_image.png" style="width:100px;">', unsafe_allow_html=True)    
    fig = px.histogram(car_data, x='odometer', color_discrete_sequence=['#0E0E52', '#3943B7', '#78C0E0'])
    fig.show()

if build_scatter:
    st.write('Crea un grafico de Dispersion con los datos <img src="scatter_image.png" style="width:100px;">', unsafe_allow_html=True)    
    fig = px.scatter(car_data, x="odometer", y="price", color='model')
    fig.show()
    