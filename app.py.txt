import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import base64
from io import BytesIO

# Configuración de la página
st.set_page_config(
    page_title="Revolución Inteligente del Análisis de Datos",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Cargar datos simulados
@st.cache_data
def load_data():
    # Datos de eficiencia
    eficiencia_data = {
        'Etapa': ['Limpieza', 'Modelado', 'Reportes', 'Visualización'],
        'Tradicional': [8.2, 12.4, 6.8, 5.5],
        'Con IA': [1.5, 3.2, 0.9, 0.7]
    }
    
    # Datos de evolución
    evolucion_data = {
        'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'],
        'Tradicional': [65, 67, 68, 70, 71, 72],
        'Con IA': [75, 80, 83, 86, 88, 89]
    }
    
    # Datos de riesgos
    riesgo_data = {
        'Departamento': ['Producción', 'Logística', 'Mantenimiento', 'Calidad', 'Administración'],
        'Ergonómico': [9, 6, 7, 4, 2],
        'Químico': [7, 4, 8, 3, 1],
        'Físico': [8, 9, 5, 2, 3],
        'Psicosocial': [6, 5, 4, 8, 7],
        'Biológico': [4, 3, 6, 2, 1]
    }
    
    return pd.DataFrame(eficiencia_data), pd.DataFrame(evolucion_data), pd.DataFrame(riesgo_data)

# Cargar datos
eficiencia_df, evolucion_df, riesgo_df = load_data()

# Sidebar para navegación
st.sidebar.title("Navegación")
st.sidebar.markdown("---")
pagina = st.sidebar.selectbox(
    "Selecciona una sección:",
    ["🏠 Inicio", "📋 Introducción", "🔬 Metodología", "📊 Resultados", "🎯 Dashboard Interactivo", "📝 Conclusiones"]
)

# Página de Inicio
if pagina == "🏠 Inicio":
    st.title("Revolución Inteligente del Análisis de Datos")
    st.markdown("### IA como Aliada Estratégica")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        Esta investigación analiza cómo la implementación de tecnologías de automatización basadas en inteligencia artificial puede mejorar:
        - La eficiencia en el ciclo analítico
        - La precisión en los resultados
        - El impacto estratégico del trabajo del analista de datos
        
        Explora los resultados interactivos y descubre cómo la IA está transformando el análisis de datos en contextos empresariales reales.
        """)
        
        st.markdown("### 🚀 Características Principales")
        st.markdown("""
        - **Reducción del 81.7%** en tiempo de limpieza de datos
        - **Aumento del 37%** en precisión predictiva
        - **Mejora del 40%** en satisfacción del analista
        - **Prevención de 12 incidentes** en el último mes
        """)
    
    with col2:
        st.image("https://via.placeholder.com/400x300?text=IA+para+Análisis+de+Datos", 
                 caption="IA transformando el análisis de datos", use_column_width=True)
        
        st.metric("Reducción Global de Tiempo", "82.5%", "⏱️")
        st.metric("Precisión Promedio", "89%", "🎯")
        st.metric("Satisfacción del Usuario", "8.7/10", "😊")

# Página de Introducción
elif pagina == "📋 Introducción":
    st.title("Introducción")
    
    st.markdown("""
    ### Contexto de la Investigación
    
    Vivimos en una época donde los datos se han convertido en uno de los activos más valiosos para las organizaciones. Cada día se generan volúmenes enormes de información a partir de múltiples canales: redes sociales, plataformas digitales, dispositivos inteligentes, transacciones internas y externas, entre otros.
    
    Gestionar de forma eficiente esta gran cantidad de datos no solo se ha vuelto un reto técnico, sino también una condición indispensable para mantenerse competitivo.
    
    ### Problema de Investigación
    
    A pesar del creciente acceso a herramientas tecnológicas, muchas organizaciones aún enfrentan limitaciones operativas al momento de gestionar el proceso analítico. Actividades como la limpieza de datos, la generación de reportes, el modelado estadístico y la visualización de resultados continúan siendo ejecutadas de manera manual o con baja integración tecnológica.
    
    ### Objetivos
    
    - **General**: Analizar cómo la implementación de tecnologías de automatización basadas en inteligencia artificial puede mejorar la eficiencia, la precisión y el impacto estratégico del trabajo del analista de datos.
    
    - **Específicos**:
        1. Identificar herramientas actuales de IA utilizadas en la automatización
        2. Diseñar y ejecutar casos de aplicación práctica
        3. Medir el impacto de la automatización
        4. Proponer guías de buenas prácticas
    """)

# Página de Metodología
elif pagina == "🔬 Metodología":
    st.title("Metodología de Investigación")
    
    st.markdown("""
    ### Enfoque de Investigación
    
    Se adopta un enfoque descriptivo con elementos exploratorios, cuyo objetivo principal es caracterizar y comprender a fondo los patrones encontrados en los datos recolectados.
    
    ### Fases del Proyecto
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### 1. Planificación
        - Definición de objetivos y alcance
        - Selección de herramientas (SQL, Python, Tableau)
        - Establecimiento de cronograma
        
        #### 2. Desarrollo
        - Revisión teórica y conceptual
        - Preparación de instrumentos
        - Configuración del entorno de análisis
        """)
    
    with col2:
        st.markdown("""
        #### 3. Implementación
        - Recolección y limpieza de datos
        - Análisis exploratorio
        - Interpretación de resultados
        
        #### 4. Evaluación
        - Valoración crítica del proceso
        - Identificación de aciertos y limitaciones
        - Propuestas de mejora
        """)
    
    st.markdown("### Tecnologías Utilizadas")
    
    tech_data = {
        'Categoría': ['Automatización ML', 'IA Generativa', 'Visualización', 'Lenguajes', 'Gestión de Datos'],
        'Tecnologías': ['AutoML, H2O.ai', 'Copilot, ChatGPT', 'Tableau, Power BI', 'Python, SQL', 'Apache Airflow'],
        'Aplicación': ['Modelado predictivo', 'Asistencia técnica', 'Dashboards interactivos', 'Procesamiento', 'Orquestación']
    }
    
    tech_df = pd.DataFrame(tech_data)
    st.dataframe(tech_df, use_container_width=True)

# Página de Resultados
elif pagina == "📊 Resultados":
    st.title("Resultados de la Investigación")
    
    st.markdown("### 1. Impacto en Eficiencia Operativa")
    
    # Gráfico de barras comparativo
    fig_eficiencia = px.bar(eficiencia_df.melt(id_vars='Etapa', var_name='Método', value_name='Horas'),
                           x='Etapa', y='Horas', color='Método', barmode='group',
                           title='Comparativo de Eficiencia por Etapa Analítica',
                           color_discrete_map={'Tradicional': '#e74c3c', 'Con IA': '#3498db'})
    
    fig_eficiencia.update_layout(
        xaxis_title='Etapa del Ciclo Analítico',
        yaxis_title='Horas',
        legend_title='Método'
    )
    
    st.plotly_chart(fig_eficiencia, use_container_width=True)
    
    st.markdown("### 2. Evolución de la Precisión Predictiva")
    
    # Gráfico de líneas
    fig_evolucion = px.line(evolucion_df.melt(id_vars='Mes', var_name='Método', value_name='Precisión'),
                           x='Mes', y='Precisión', color='Método', markers=True,
                           title='Evolución de la Precisión Predictiva',
                           color_discrete_map={'Tradicional': '#e74c3c', 'Con IA': '#3498db'})
    
    fig_evolucion.update_layout(
        xaxis_title='Mes',
        yaxis_title='Precisión (%)',
        legend_title='Método'
    )
    
    st.plotly_chart(fig_evolucion, use_container_width=True)
    
    st.markdown("### 3. Mapa de Calor de Riesgos por Departamento")
    
    # Mapa de calor
    riesgo_melt = riesgo_df.melt(id_vars='Departamento', var_name='Tipo de Riesgo', value_name='Nivel')
    
    fig_riesgo = px.density_heatmap(riesgo_melt, x='Tipo de Riesgo', y='Departamento', z='Nivel',
                                   title='Mapa de Calor de Riesgos por Departamento',
                                   color_continuous_scale='Reds')
    
    st.plotly_chart(fig_riesgo, use_container_width=True)
    
    st.markdown("### 4. Distribución del Tiempo del Analista")
    
    # Gráfico circular
    tiempo_data = {
        'Actividad': ['Limpieza', 'Modelado', 'Reportes', 'Visualización', 'Análisis Estratégico'],
        'Sin IA': [35, 25, 20, 15, 5],
        'Con IA': [5, 10, 5, 5, 75]
    }
    
    tiempo_df = pd.DataFrame(tiempo_data)
    
    fig_tiempo = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
    
    fig_tiempo.add_trace(go.Pie(labels=tiempo_df['Actividad'], values=tiempo_df['Sin IA'], name="Sin IA"), 1, 1)
    fig_tiempo.add_trace(go.Pie(labels=tiempo_df['Actividad'], values=tiempo_df['Con IA'], name="Con IA"), 1, 2)
    
    fig_tiempo.update_traces(hole=.4, hoverinfo="label+percent+name")
    fig_tiempo.update_layout(
        title_text="Distribución del Tiempo del Analista (Antes vs. Después de IA)",
        annotations=[dict(text='Sin IA', x=0.18, y=0.5, font_size=20, showarrow=False),
                    dict(text='Con IA', x=0.82, y=0.5, font_size=20, showarrow=False)]
    )
    
    st.plotly_chart(fig_tiempo, use_container_width=True)

# Dashboard Interactivo
elif pagina == "🎯 Dashboard Interactivo":
    st.title("Dashboard Interactivo de Monitoreo")
    
    st.markdown("### KPIs en Tiempo Real")
    
    col1, col2, col3, col4 = st.columns(4)
    
    col1.metric("Tiempo Promedio Análisis", "2.1h", "-80%")
    col2.metric("Precisión Detección Riesgos", "95%", "+25%")
    col3.metric("Incidentes Prevenidos", "12", "Últimos 30 días")
    col4.metric("Satisfacción del Analista", "8.7/10", "+40%")
    
    st.markdown("---")
    
    st.markdown("### Simulador de Escenarios")
    
    st.markdown("Ajusta los parámetros para ver cómo impacta la implementación de IA:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        automatizacion = st.slider("Nivel de Automatización (%)", 0, 100, 80)
        inversion = st.slider("Inversión en IA (USD)", 1000, 100000, 25000)
    
    with col2:
        tiempo_analisis = 8.2 * (1 - automatizacion/100)
        precision = 65 + (automatizacion * 0.3)
        roi = (inversion * 0.8) - inversion
        
        st.metric("Tiempo de Análisis (horas)", f"{tiempo_analisis:.1f}")
        st.metric("Precisión (%)", f"{precision:.1f}")
        st.metric("ROI Estimado (USD)", f"${roi:,.0f}")
    
    st.markdown("---")
    
    st.markdown("### Mapa de Riesgos en Tiempo Real")
    
    # Generar datos aleatorios para simulación
    np.random.seed(42)
    areas = ['Área A', 'Área B', 'Área C', 'Área D', 'Área E']
    tipos_riesgo = ['Ergonómico', 'Químico', 'Físico', 'Psicosocial']
    
    riesgo_tiempo_real = pd.DataFrame({
        'Área': np.random.choice(areas, 50),
        'Tipo de Riesgo': np.random.choice(tipos_riesgo, 50),
        'Nivel': np.random.randint(1, 11, 50),
        'Timestamp': pd.date_range(start='2025-06-01', periods=50, freq='H')
    })
    
    fig_tiempo_real = px.scatter(riesgo_tiempo_real, x='Timestamp', y='Nivel', 
                                color='Tipo de Riesgo', size='Nivel',
                                hover_data=['Área'],
                                title='Monitoreo de Riesgos en Tiempo Real')
    
    st.plotly_chart(fig_tiempo_real, use_container_width=True)

# Página de Conclusiones
elif pagina == "📝 Conclusiones":
    st.title("Conclusiones y Recomendaciones")
    
    st.markdown("""
    ### Conclusiones Principales
    
    1. **Optimización del Ciclo Analítico**: La automatización mediante IA reduce significativamente los tiempos operativos (hasta 87.3% en visualización) y elimina tareas repetitivas.
    
    2. **Mejora en Precisión**: La integración de algoritmos predictivos aumenta la precisión en un 37%, permitiendo detección temprana de patrones críticos.
    
    3. **Toma de Decisiones Basada en Datos**: La IA proporciona evidencias claras para priorizar riesgos y acciones preventivas.
    
    4. **Reducción de Errores Humanos**: La automatización fortalece la precisión en procesos como limpieza de datos y clasificación de riesgos.
    
    5. **Monitoreo en Tiempo Real**: Los dashboards interactivos permiten actualizaciones constantes y retroalimentación visual automatizada.
    """)
    
    st.markdown("---")
    
    st.markdown("### Recomendaciones")
    
    recomendaciones = [
        "Implementar sistemas automatizados de monitoreo con sensores IoT y plataformas de IA",
        "Utilizar algoritmos de limpieza y validación de datos para garantizar calidad",
        "Diseñar modelos predictivos para anticipar eventos de riesgo",
        "Integrar dashboards dinámicos con IA explicativa (XAI)",
        "Capacitar a analistas en uso ético y técnico de herramientas automatizadas",
        "Fomentar una cultura organizacional basada en datos"
    ]
    
    for i, rec in enumerate(recomendaciones, 1):
        st.markdown(f"**{i}.** {rec}")
    
    st.markdown("---")
    
    st.markdown("### Próximos Pasos")
    
    st.markdown("""
    - **Fase 1**: Implementación piloto en departamentos seleccionados
    - **Fase 2**: Escalado a toda la organización
    - **Fase 3**: Integración con sistemas empresariales existentes
    - **Fase 4**: Monitoreo continuo y mejora del modelo
    """)

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("© 2025 - Semillero de Investigación IA")
st.sidebar.markdown("Gloria María Araujo Chambó")