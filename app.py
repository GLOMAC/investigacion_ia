import streamlit as st
import pandas as pd

st.title("Revolución Inteligente del Análisis de Datos")
st.markdown("### IA como Aliada Estratégica")

# Datos de eficiencia
data = {
    'Etapa': ['Limpieza', 'Modelado', 'Reportes', 'Visualización'],
    'Tradicional': [8.2, 12.4, 6.8, 5.5],
    'Con IA': [1.5, 3.2, 0.9, 0.7]
}

df = pd.DataFrame(data)

# Mostrar tabla
st.subheader("Comparativo de Eficiencia")
st.dataframe(df)

# Gráfico de barras
st.subheader("Reducción de Tiempo por Etapa")
st.bar_chart(df.set_index('Etapa'))

# Métricas clave
st.subheader("Métricas de Impacto")
col1, col2, col3 = st.columns(3)
col1.metric("Reducción Global", "82.5%", "⏱️")
col2.metric("Precisión", "89%", "🎯")
col3.metric("Satisfacción", "8.7/10", "😊")

st.success("¡Aplicación con gráficos funcionando!")
