import streamlit as st

st.title("Revolución Inteligente del Análisis de Datos")
st.write("### IA como Aliada Estratégica")

st.write("Aplicación funcionando correctamente!")
import streamlit as st
import pandas as pd

st.title("Revolución Inteligente del Análisis de Datos")
st.markdown("### IA como Aliada Estratégica")

# Datos de ejemplo
data = {
    'Etapa': ['Limpieza', 'Modelado', 'Reportes', 'Visualización'],
    'Tradicional': [8.2, 12.4, 6.8, 5.5],
    'Con IA': [1.5, 3.2, 0.9, 0.7]
}

df = pd.DataFrame(data)

st.dataframe(df)
st.success("¡Aplicación funcionando con datos!")
