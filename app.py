import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import random

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

# Generar datos de riesgo en tiempo real
@st.cache_data(ttl=60)  # Se actualiza cada 60 segundos
def generate_real_time_risk_data():
    areas = ['Área A', 'Área B', 'Área C', 'Área D', 'Área E']
    tipos_riesgo = ['Ergonómico', 'Químico', 'Físico', 'Psicosocial']
    
    # Generar datos de las últimas 24 horas
    ahora = datetime.now()
    timestamps = [ahora - timedelta(hours=x) for x in range(24, 0, -1)]
    
    datos = []
    for timestamp in timestamps:
        for area in areas:
            for tipo in tipos_riesgo:
                # Simular nivel de riesgo aleatorio entre 1 y 10
                nivel = random.randint(1, 10)
                datos.append({
                    'Timestamp': timestamp,
                    'Área': area,
                    'Tipo de Riesgo': tipo,
                    'Nivel': nivel
                })
    
    return pd.DataFrame(datos)

# Cargar datos
eficiencia_df, evolucion_df, riesgo_df = load_data()

# Sidebar para navegación
st.sidebar.title("📋 Navegación")
st.sidebar.markdown("---")
pagina = st.sidebar.selectbox(
    "Selecciona una sección:",
    ["🏠 Inicio", "📋 Introducción", "🔬 Metodología", "📊 Resultados", "🎯 Dashboard Interactivo", "📝 Conclusiones"]
)

# Página de Inicio
if pagina == "🏠 Inicio":
    st.title("🚀 Revolución Inteligente del Análisis de Datos")
    st.markdown("### 🤖 IA como Aliada Estratégica")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### 📖 Contexto de la Investigación
        
        Esta investigación analiza cómo la implementación de tecnologías de automatización basadas en inteligencia artificial puede mejorar:
        
        - **La eficiencia** en el ciclo analítico
        - **La precisión** en los resultados  
        - **El impacto estratégico** del trabajo del analista de datos
        
        Explora los resultados interactivos y descubre cómo la IA está transformando el análisis de datos en contextos empresariales reales.
        """)
        
        st.markdown("### 🎯 Características Principales")
        st.markdown("""
        - **Reducción del 81.7%** en tiempo de limpieza de datos
        - **Aumento del 37%** en precisión predictiva
        - **Mejora del 40%** en satisfacción del analista
        - **Prevención de 12 incidentes** en el último mes
        """)
    
    with col2:
        st.image("https://via.placeholder.com/400x300?text=IA+para+Análisis+de+Datos", 
                 caption="IA transformando el análisis de datos", use_column_width=True)
        
        st.metric("📉 Reducción Global de Tiempo", "82.5%", "⏱️")
        st.metric("🎯 Precisión Promedio", "89%", "📈")
        st.metric("😊 Satisfacción del Usuario", "8.7/10", "⭐")

# Página de Introducción
elif pagina == "📋 Introducción":
    st.title("📋 Introducción")
    
    st.markdown("""
    ### 🌍 Contexto de la Investigación
    
    Vivimos en una época donde los datos se han convertido en uno de los activos más valiosos para las organizaciones. Cada día se generan volúmenes enormes de información a partir de múltiples canales: redes sociales, plataformas digitales, dispositivos inteligentes, transacciones internas y externas, entre otros.
    
    Gestionar de forma eficiente esta gran cantidad de datos no solo se ha vuelto un reto técnico, sino también una condición indispensable para mantenerse competitivo.
    
    ### ⚠️ Problema de Investigación
    
    A pesar del creciente acceso a herramientas tecnológicas, muchas organizaciones aún enfrentan limitaciones operativas al momento de gestionar el proceso analítico. Actividades como la limpieza de datos, la generación de reportes, el modelado estadístico y la visualización de resultados continúan siendo ejecutadas de manera manual o con baja integración tecnológica.
    
    ### 🎯 Objetivos
    
    #### General:
    Analizar cómo la implementación de tecnologías de automatización basadas en inteligencia artificial puede mejorar la eficiencia, la precisión y el impacto estratégico del trabajo del analista de datos.
    
    #### Específicos:
    1. **Identificar herramientas actuales** de IA utilizadas en la automatización
    2. **Diseñar y ejecutar casos** de aplicación práctica
    3. **Medir el impacto** de la automatización
    4. **Proponer guías** de buenas prácticas
    """)

# Página de Metodología
elif pagina == "🔬 Metodología":
    st.title("🔬 Metodología de Investigación")
    
    st.markdown("""
    ### 📊 Enfoque de Investigación
    
    Se adopta un enfoque descriptivo con elementos exploratorios, cuyo objetivo principal es caracterizar y comprender a fondo los patrones encontrados en los datos recolectados.
    
    ### 🔄 Fases del Proyecto
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### 1. 📋 Planificación
        - Definición de objetivos y alcance
        - Selección de herramientas (SQL, Python, Tableau)
        - Establecimiento de cronograma
        
        #### 2. 🔧 Desarrollo
        - Revisión teórica y conceptual
        - Preparación de instrumentos
        - Configuración del entorno de análisis
        """)
    
    with col2:
        st.markdown("""
        #### 3. 🚀 Implementación
        - Recolección y limpieza de datos
        - Análisis exploratorio
        - Interpretación de resultados
        
        #### 4. ✅ Evaluación
        - Valoración crítica del proceso
        - Identificación de aciertos y limitaciones
        - Propuestas de mejora
        """)
    
    st.markdown("### 🛠️ Tecnologías Utilizadas")
    
    tech_data = {
        'Categoría': ['Automatización ML', 'IA Generativa', 'Visualización', 'Lenguajes', 'Gestión de Datos'],
        'Tecnologías': ['AutoML, H2O.ai', 'Copilot, ChatGPT', 'Tableau, Power BI', 'Python, SQL', 'Apache Airflow'],
        'Aplicación': ['Modelado predictivo', 'Asistencia técnica', 'Dashboards interactivos', 'Procesamiento', 'Orquestación']
    }
    
    tech_df = pd.DataFrame(tech_data)
    st.dataframe(tech_df, use_container_width=True)

# Página de Resultados
elif pagina == "📊 Resultados":
    st.title("📊 Resultados de la Investigación")
    
    st.markdown("### ⚡ Impacto en Eficiencia Operativa")
    
    # Gráfico de barras comparativo
    st.subheader("📈 Comparativo de Eficiencia por Etapa Analítica")
    st.bar_chart(eficiencia_df.set_index('Etapa'))
    
    # Tabla con reducciones
    eficiencia_df['Reducción (%)'] = ((eficiencia_df['Tradicional'] - eficiencia_df['Con IA']) / eficiencia_df['Tradicional'] * 100).round(1)
    st.dataframe(eficiencia_df, use_container_width=True)
    
    st.markdown("### 📈 Evolución de la Precisión Predictiva")
    
    # Gráfico de líneas
    st.subheader("📊 Evolución Temporal de Precisión")
    st.line_chart(evolucion_df.set_index('Mes'))
    
    st.markdown("### 🔥 Mapa de Calor de Riesgos por Departamento")
    
    # Crear mapa de calor visual
    st.subheader("🌡️ Visualización de Riesgos por Departamento")
    
    # Preparar datos para el mapa de calor
    heatmap_data = riesgo_df.set_index('Departamento')
    
    # Crear figura
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Crear mapa de calor
    sns.heatmap(heatmap_data, annot=True, cmap='Reds', fmt='g', 
                cbar_kws={'label': 'Nivel de Riesgo (1-10)'}, ax=ax)
    
    # Configurar título
    ax.set_title('Mapa de Calor de Riesgos por Departamento', fontsize=14, weight='bold')
    
    # Mostrar en Streamlit
    st.pyplot(fig)
    
    # Mostrar tabla también
    st.subheader("📋 Datos Detallados de Riesgos")
    st.dataframe(riesgo_df.set_index('Departamento'), use_container_width=True)
    
    # Resaltar valores altos
    st.markdown("""
    **Áreas Críticas Identificadas:**
    - 🔴 **Producción**: Riesgo ergonómico (9) y químico (7)
    - 🟠 **Logística**: Riesgo físico (9)
    - 🟡 **Mantenimiento**: Riesgo químico (8)
    """)

# Dashboard Interactivo
elif pagina == "🎯 Dashboard Interactivo":
    st.title("🎯 Dashboard Interactivo de Monitoreo")
    
    st.markdown("### 📊 KPIs en Tiempo Real")
    
    col1, col2, col3, col4 = st.columns(4)
    
    col1.metric("⏱️ Tiempo Promedio Análisis", "2.1h", "-80%")
    col2.metric("🎯 Precisión Detección Riesgos", "95%", "+25%")
    col3.metric("🛡️ Incidentes Prevenidos", "12", "Últimos 30 días")
    col4.metric("😊 Satisfacción del Analista", "8.7/10", "+40%")
    
    st.markdown("---")
    
    st.markdown("### 🎛️ Simulador de Escenarios")
    
    st.markdown("Ajusta los parámetros para ver cómo impacta la implementación de IA:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        automatizacion = st.slider("🤖 Nivel de Automatización (%)", 0, 100, 80)
        inversion = st.slider("💰 Inversión en IA (USD)", 1000, 100000, 25000)
    
    with col2:
        tiempo_analisis = 8.2 * (1 - automatizacion/100)
        precision = 65 + (automatizacion * 0.3)
        roi = (inversion * 0.8) - inversion
        
        st.metric("⏱️ Tiempo de Análisis (horas)", f"{tiempo_analisis:.1f}")
        st.metric("🎯 Precisión (%)", f"{precision:.1f}")
        st.metric("💰 ROI Estimado (USD)", f"${roi:,.0f}")
    
    st.markdown("---")
    
    st.markdown("### 🗺️ Mapa de Riesgos en Tiempo Real")
    
    # Generar datos en tiempo real
    riesgo_tiempo_real = generate_real_time_risk_data()
    
    # Filtros para el mapa de riesgos
    col1, col2 = st.columns(2)
    
    with col1:
        tipo_riesgo_filtro = st.selectbox("Filtrar por tipo de riesgo:", 
                                          ['Todos'] + list(riesgo_tiempo_real['Tipo de Riesgo'].unique()))
    
    with col2:
        area_filtro = st.selectbox("Filtrar por área:", 
                                   ['Todas'] + list(riesgo_tiempo_real['Área'].unique()))
    
    # Aplicar filtros
    datos_filtrados = riesgo_tiempo_real.copy()
    if tipo_riesgo_filtro != 'Todos':
        datos_filtrados = datos_filtrados[datos_filtrados['Tipo de Riesgo'] == tipo_riesgo_filtro]
    if area_filtro != 'Todas':
        datos_filtrados = datos_filtrados[datos_filtrados['Área'] == area_filtro]
    
    # Mostrar últimos datos
    st.subheader("📊 Últimas 24 horas - Niveles de Riesgo")
    
    # Crear gráfico de dispersión para mostrar riesgos en tiempo real
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Preparar datos para el gráfico
    scatter_data = datos_filtrados.copy()
    scatter_data['Hora'] = scatter_data['Timestamp'].dt.hour
    
    # Crear scatter plot
    scatter = ax.scatter(scatter_data['Hora'], scatter_data['Nivel'], 
                        c=scatter_data['Nivel'], cmap='Reds', s=100, alpha=0.7)
    
    # Configurar gráfico
    ax.set_xlabel('Hora del Día')
    ax.set_ylabel('Nivel de Riesgo (1-10)')
    ax.set_title('Niveles de Riesgo en Tiempo Real - Últimas 24 Horas')
    ax.set_ylim(0, 11)
    ax.set_xlim(-1, 24)
    
    # Añadir barra de color
    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label('Nivel de Riesgo')
    
    # Mostrar en Streamlit
    st.pyplot(fig)
    
    # Mostrar tabla con datos más recientes
    st.subheader("📋 Datos Recientes de Riesgos")
    
    # Obtener los 10 registros más recientes
    datos_recientes = datos_filtrados.sort_values('Timestamp', ascending=False).head(10)
    
    # Formatear timestamp para mejor visualización
    datos_recientes['Timestamp'] = datos_recientes['Timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S')
    
    st.dataframe(datos_recientes, use_container_width=True)
    
    # Añadir botón para actualizar datos
    if st.button("🔄 Actualizar Datos en Tiempo Real"):
        st.cache_data.clear()
        st.experimental_rerun()
    
    st.markdown("---")
    
    st.markdown("### 📊 Análisis Comparativo en Tiempo Real")
    
    # Gráfico comparativo interactivo
    etapa_seleccionada = st.selectbox("Selecciona una etapa para analizar:", 
                                      ['Limpieza', 'Modelado', 'Reportes', 'Visualización'])
    
    datos_etapa = eficiencia_df[eficiencia_df['Etapa'] == etapa_seleccionada]
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric(f"⏱️ {etapa_seleccionada} - Método Tradicional", 
                 f"{datos_etapa['Tradicional'].values[0]} horas")
    
    with col2:
        st.metric(f"🤖 {etapa_seleccionada} - Con IA", 
                 f"{datos_etapa['Con IA'].values[0]} horas",
                 f"-{datos_etapa['Reducción (%)'].values[0]}%")

# Página de Conclusiones
elif pagina == "📝 Conclusiones":
    st.title("📝 Conclusiones y Recomendaciones")
    
    st.markdown("""
    ### 🎯 Conclusiones Principales
    
    1. **🚀 Optimización del Ciclo Analítico**: La automatización mediante IA reduce significativamente los tiempos operativos (hasta 87.3% en visualización) y elimina tareas repetitivas.
    
    2. **📈 Mejora en Precisión**: La integración de algoritmos predictivos aumenta la precisión en un 37%, permitiendo detección temprana de patrones críticos.
    
    3. **🎯 Toma de Decisiones Basada en Datos**: La IA proporciona evidencias claras para priorizar riesgos y acciones preventivas.
    
    4. **✅ Reducción de Errores Humanos**: La automatización fortalece la precisión en procesos como limpieza de datos y clasificación de riesgos.
    
    5. **📊 Monitoreo en Tiempo Real**: Los dashboards interactivos permiten actualizaciones constantes y retroalimentación visual automatizada.
    """)
    
    st.markdown("---")
    
    st.markdown("### 💡 Recomendaciones")
    
    recomendaciones = [
        "🔧 Implementar sistemas automatizados de monitoreo con sensores IoT y plataformas de IA",
        "🧹 Utilizar algoritmos de limpieza y validación de datos para garantizar calidad",
        "🔮 Diseñar modelos predictivos para anticipar eventos de riesgo",
        "📊 Integrar dashboards dinámicos con IA explicativa (XAI)",
        "👨‍🏫 Capacitar a analistas en uso ético y técnico de herramientas automatizadas",
        "🏢 Fomentar una cultura organizacional basada en datos"
    ]
    
    for i, rec in enumerate(recomendaciones, 1):
        st.markdown(f"**{i}.** {rec}")
    
    st.markdown("---")
    
    st.markdown("### 🚀 Próximos Pasos")
    
    st.markdown("""
    - **📋 Fase 1**: Implementación piloto en departamentos seleccionados
    - **📈 Fase 2**: Escalado a toda la organización
    - **🔗 Fase 3**: Integración con sistemas empresariales existentes
    - **📊 Fase 4**: Monitoreo continuo y mejora del modelo
    """)
    
    st.markdown("---")
    
    st.markdown("### 📚 Referencias")
    
    st.markdown("""
    - García, M., & Delgado, L. (2020). *Análisis de datos aplicado a la prevención de riesgos laborales*. Editorial Académica Española.
    - Hernández Sampieri, R., et al. (2014). *Metodología de la investigación* (6.ª ed.). McGraw-Hill Education.
    - Sharma, S. (2022). *Automating Data Analysis with Artificial Intelligence: Techniques and Tools for Business Analytics*. Springer.
    """)

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("© 2025 - Semillero de Investigación IA")
st.sidebar.markdown("👤 Gloria María Araujo Chambó")
st.sidebar.markdown("📧 gloria.araujo@universidad.edu")
