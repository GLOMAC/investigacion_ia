import streamlit as st
import pandas as pd
import numpy as np

st.title("Revolución Inteligente del Análisis de Datos")
st.markdown("### IA como Aliada Estratégica")

# Sidebar para navegación
st.sidebar.title("Navegación")
pagina = st.sidebar.selectbox(
    "Selecciona una sección:",
    ["🏠 Inicio", "📊 Resultados", "📝 Conclusiones"]
)

# Página de Inicio
if pagina == "🏠 Inicio":
    st.markdown("""
    ### Contexto de la Investigación
    
    Esta investigación analiza cómo la implementación de tecnologías de automatización basadas en inteligencia artificial puede mejorar:
    - La eficiencia en el ciclo analítico
    - La precisión en los resultados
    - El impacto estratégico del trabajo del analista de datos
    """)
    
    st.markdown("### 🚀 Características Principales")
    st.markdown("""
    - **Reducción del 81.7%** en tiempo de limpieza de datos
    - **Aumento del 37%** en precisión predictiva
    - **Mejora del 40%** en satisfacción del analista
    """)

# Página de Resultados
elif pagina == "📊 Resultados":
    st.markdown("### Impacto en Eficiencia Operativa")
    
    # Datos de eficiencia
    eficiencia_data = {
        'Etapa': ['Limpieza', 'Modelado', 'Reportes', 'Visualización'],
        'Tradicional': [8.2, 12.4, 6.8, 5.5],
        'Con IA': [1.5, 3.2, 0.9, 0.7]
    }
    
    df = pd.DataFrame(eficiencia_data)
    
    # Tabla comparativa
    st.dataframe(df)
    
    # Gráfico
    st.bar_chart(df.set_index('Etapa'))
    
    # Métricas
    col1, col2, col3 = st.columns(3)
    col1.metric("Reducción Global", "82.5%", "⏱️")
    col2.metric("Precisión", "89%", "🎯")
    col3.metric("Satisfacción", "8.7/10", "😊")

# Página de Conclusiones
elif pagina == "📝 Conclusiones":
    st.markdown("""
    ### Conclusiones Principales
    
    1. **Optimización del Ciclo Analítico**: La automatización mediante IA reduce significativamente los tiempos operativos.
    
    2. **Mejora en Precisión**: La integración de algoritmos predictivos aumenta la precisión en un 37%.
    
    3. **Toma de Decisiones Basada en Datos**: La IA proporciona evidencias claras para priorizar acciones.
    
    ### Recomendaciones
    
    - Implementar sistemas automatizados de monitoreo con IA
    - Utilizar algoritmos de limpieza y validación de datos
    - Diseñar modelos predictivos para anticipar eventos
    - Capacitar a analistas en uso ético y técnico de herramientas IA
    """)

st.sidebar.markdown("---")
st.sidebar.markdown("© 2025 - Gloria María Araujo Chambó")
