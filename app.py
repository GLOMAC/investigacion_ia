import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from mente_maestra import (
    QuestionDatabase, SageDatabase, PowerUpSystem,
    GameSession, PlayerProfile, get_share_text, get_rank_emoji,
    get_rank_thresholds
)


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
st.sidebar.title("📋 Navegación")
st.sidebar.markdown("---")
pagina = st.sidebar.selectbox(
    "Selecciona una sección:",
    ["🏠 Inicio", "📋 Introducción", "🔬 Metodología", "📊 Resultados", "🎯 Dashboard Interactivo", "📝 Conclusiones", "🧠 Mente Maestra"]
)

# Página de Inicio
if pagina == "🏠 Inicio":
    st.title(" Revolución Inteligente del Análisis de Datos")
    st.markdown("### 🤖 IA como Aliada Estratégica")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        ###  Contexto de la Investigación

        Esta investigación analiza cómo la implementación de tecnologías de automatización basadas en inteligencia artificial puede mejorar:

        - **La eficiencia** en el ciclo analítico
        - **La precisión** en los resultados  
        - **El impacto estratégico** del trabajo del analista de datos

        Explora los resultados interactivos y descubre cómo la IA está transformando el análisis de datos en contextos empresariales reales.
        """)

        st.markdown("### Características Principales")
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
    st.title(" Introducción")
    
    st.markdown("""
    ###  Contexto de la Investigación
    
    Vivimos en una época donde los datos se han convertido en uno de los activos más valiosos para las organizaciones. Cada día se generan volúmenes enormes de información a partir de múltiples canales: redes sociales, plataformas digitales, dispositivos inteligentes, transacciones internas y externas, entre otros.
    
    Gestionar de forma eficiente esta gran cantidad de datos no solo se ha vuelto un reto técnico, sino también una condición indispensable para mantenerse competitivo.
    
    ###  Problema de Investigación
    
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
    ###  Enfoque de Investigación
    
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
    st.dataframe(tech_df, container_width=True)

# Página de Resultados
elif pagina == "📊 Resultados":
    st.title(" Resultados de la Investigación")
    
    st.markdown("###  Impacto en Eficiencia Operativa")
    
    # Gráfico de barras comparativo
    st.subheader(" Comparativo de Eficiencia por Etapa Analítica")
    st.bar_chart( eficiencia_df.set_index('Etapa'))
    
    # Tabla con reducciones
    eficiencia_df['Reducción (%)'] = ((eficiencia_df['Tradicional'] - eficiencia_df['Con IA']) / eficiencia_df['Tradicional'] * 100).round(1)
    st.dataframe(eficiencia_df, container_width=True)
    
    st.markdown("###  Evolución de la Precisión Predictiva")
    
    # Gráfico de líneas
    st.subheader(" Evolución Temporal de Precisión")
    st.line_chart(evolucion_df.set_index('Mes'))
    
    st.markdown("###  Mapa de Calor de Riesgos por Departamento")
    
    # Mapa de calor
    st.subheader("🌡️ Niveles de Riesgo por Departamento")
    st.dataframe(riesgo_df.set_index('Departamento'), container_width=True)
    
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
    
    # KPIs en Tiempo Real
    st.markdown("### 📊 KPIs en Tiempo Real")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("⏱️ Tiempo Promedio Análisis", "2.1h", "-80%")
    
    with col2:
        st.metric("🎯 Precisión Detección Riesgos", "95%", "+25%")
    
    with col3:
        st.metric("🛡️ Incidentes Prevenidos", "12", "Últimos 30 días")
    
    with col4:
        st.metric("😊 Satisfacción del Analista", "8.7/10", "+40%")
    
    st.markdown("---")
    
    # Simulador de Escenarios
    st.markdown("### 🎛️ Simulador de Escenarios")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("**Parámetros de Configuración**")
        automatizacion = st.slider("🤖 Nivel de Automatización (%)", 0, 100, 80)
        inversion = st.slider("💰 Inversión en IA (USD)", 1000, 100000, 25000)
    
    with col2:
        st.markdown("**Resultados Estimados**")
        tiempo_analisis = 8.2 * (1 - automatizacion/100)
        precision = 65 + (automatizacion * 0.3)
        roi = (inversion * 0.8) - inversion
        
        st.metric("⏱️ Tiempo de Análisis", f"{tiempo_analisis:.1f} horas")
        st.metric("🎯 Precisión", f"{precision:.1f}%")
        st.metric("💰 ROI Estimado", f"${roi:,.0f}")
    
    st.markdown("---")
    
    # Mapa de Riesgos en Tiempo Real
    st.markdown("### 🗺️ Mapa de Riesgos en Tiempo Real")
    
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
    
    # Gráfico de dispersión interactivo
    st.subheader("📊 Distribución de Riesgos en Tiempo Real")
    fig = px.scatter(riesgo_tiempo_real, x='Timestamp', y='Nivel', 
                    color='Tipo de Riesgo', title='Monitoreo de Riesgos en Tiempo Real')
    st.plotly_chart(fig, use_container_width=True)
    
    # Tabla de alertas críticas
    st.subheader("🚨 Alertas Críticas Recientes")
    
    alertas_criticas = riesgo_tiempo_real[riesgo_tiempo_real['Nivel'] >= 8].sort_values('Timestamp', ascending=False).head(10)
    
    if not alertas_criticas.empty:
        alertas_criticas['Timestamp'] = alertas_criticas['Timestamp'].dt.strftime('%d/%m/%Y %H:%M')
        alertas_criticas = alertas_criticas.rename(columns={
            'Timestamp': 'Fecha/Hora',
            'Área': 'Área',
            'Tipo de Riesgo': 'Tipo',
            'Nivel': 'Nivel'
        })
        
        st.dataframe(alertas_criticas, container_width=True)
    else:
        st.success("✅ No hay alertas críticas en este momento")
    
    # Botón de actualización
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if st.button("🔄 Actualizar Datos", type="primary", use_container_width=True):
            st.experimental_rerun()
            st.success("✅ Datos actualizados correctamente")
    
    st.markdown("---")
    
    # Análisis Comparativo
    st.markdown("### 📈 Análisis Comparativo en Tiempo Real")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📊 Riesgos por Tipo")
        tipo_counts = riesgo_tiempo_real['Tipo de Riesgo'].value_counts()
        fig_tipo = px.pie(values=tipo_counts.values, 
                          names=tipo_counts.index,
                          title="Distribución por Tipo de Riesgo")
        st.plotly_chart(fig_tipo, container_width=True)
    
    with col2:
        st.subheader("📍 Riesgos por Área")
        area_counts = riesgo_tiempo_real['Área'].value_counts()
        fig_area = px.bar(x=area_counts.index, 
                          y=area_counts.values,
                          title="Incidencias por Área",
                          labels={'x': 'Área', 'y': 'Cantidad'})
        st.plotly_chart(fig_area, container_width=True)
    
    # Resumen estadístico - VERSIÓN CORREGIDA
    st.markdown("### 📋 Resumen Estadístico")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_registros = len(riesgo_tiempo_real)
        st.metric("📊 Total Registros", total_registros)
    
    with col2:
        promedio_riesgo = riesgo_tiempo_real['Nivel'].mean()
        st.metric("⚠️ Nivel Promedio", f"{promedio_riesgo:.1f}")
    
    with col3:
        max_riesgo = riesgo_tiempo_real['Nivel'].max()
        st.metric("🔴 Riesgo Máximo", max_riesgo)
    
    with col4:
        alertas_altas = len(riesgo_tiempo_real[riesgo_tiempo_real['Nivel'] >= 8])
        st.metric("🚨 Alertas Altas", alertas_altas)

# Ahora sí puede empezar el siguiente bloque
elif pagina == "📝 Conclusiones":
    st.title("📝 Conclusiones y Recomendaciones")
    
    st.markdown("""
    ### 🎯 Conclusiones Principales
    
    1. **🚀 Optimización del Ciclo Analítico**: La automatización mediante IA reduce significativamente los tiempos operativos.
    
    2. **📈 Mejora en Precisión**: La integración de algoritmos predictivos aumenta la precisión en un 37%.
    
    3. **🎯 Toma de Decisiones Basada en Datos**: La IA proporciona evidencias claras para priorizar acciones.
    
    4. **✅ Reducción de Errores Humanos**: La automatización fortalece la precisión en procesos.
    
    5. **📊 Monitoreo en Tiempo Real**: Los dashboards interactivos permiten actualizaciones constantes.
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
    
    
    st.markdown("### 📚 Referencias")
    
    st.markdown("""
    - García, M., & Delgado, L. (2020). *Análisis de datos aplicado a la prevención de riesgos laborales*. Editorial Académica Española.
    - Hernández Sampieri, R., et al. (2014). *Metodología de la investigación* (6.ª ed.). McGraw-Hill Education.
    - Sharma, S. (2022). *Automating Data Analysis with Artificial Intelligence: Techniques and Tools for Business Analytics*. Springer.
    """)

# Página de Mente Maestra
elif pagina == "🧠 Mente Maestra":
    st.title("🧠 Mente Maestra: El Torneo de los Sabios")
    st.markdown("### ¡Demuestra tu sabiduría en el torneo más desafiante!")
    
    # Initialize session state
    if 'player' not in st.session_state:
        st.session_state.player = PlayerProfile()
        st.session_state.game = None
        st.session_state.question_db = QuestionDatabase()
        st.session_state.sage_db = SageDatabase()
        st.session_state.powerup_system = PowerUpSystem()
    
    player = st.session_state.player
    
    # Sidebar with player stats
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 👤 Perfil del Jugador")
    
    # Player name input
    new_name = st.sidebar.text_input("Nombre", value=player.name, key="player_name_input")
    if new_name != player.name:
        player.name = new_name
    
    # Avatar selection
    avatars = ["🎓", "🧙", "👑", "🦉", "📚", "⚡", "🌟", "🔮", "🎯", "🏆"]
    avatar_index = avatars.index(player.avatar_emoji) if player.avatar_emoji in avatars else 0
    new_avatar = st.sidebar.selectbox("Avatar", avatars, index=avatar_index, key="avatar_select")
    if new_avatar != player.avatar_emoji:
        player.avatar_emoji = new_avatar
    
    st.sidebar.markdown(f"**{player.avatar_emoji} {player.name}**")
    st.sidebar.markdown(f"🏆 **Rango:** {player.rank}")
    st.sidebar.markdown(f"⭐ **Fragmentos:** {player.wisdom_fragments}")
    st.sidebar.markdown(f"📊 **Nivel:** {player.current_level}/6")
    st.sidebar.markdown(f"🎯 **Precisión:** {player.get_accuracy():.1f}%")
    st.sidebar.markdown(f"✅ **Correctas:** {player.questions_correct}/{player.questions_answered}")
    
    # Main content area
    tab1, tab2, tab3, tab4 = st.tabs(["🎮 Jugar", "💫 Poder-ups", "🏆 Perfil", "📊 Clasificación"])
    
    with tab1:
        # Game play area
        if st.session_state.game is None or st.session_state.game.completed:
            st.markdown("## Selecciona tu Desafío")
            
            # Display available sages
            for i in range(1, 7):
                sage = st.session_state.sage_db.get_sage_by_level(i)
                if sage:
                    col1, col2, col3 = st.columns([1, 3, 1])
                    
                    with col1:
                        st.markdown(f"## {sage.avatar}")
                    
                    with col2:
                        st.markdown(f"### Nivel {sage.level}: {sage.name}")
                        st.markdown(f"*{sage.title}*")
                        st.markdown(f"**Especialidad:** {sage.specialty}")
                        st.markdown(sage.description)
                        
                        # Check if level is unlocked
                        is_unlocked = i <= player.current_level
                        is_completed = i in player.completed_levels
                        
                        if is_completed:
                            st.success(f"✅ Completado")
                        elif not is_unlocked:
                            st.warning(f"🔒 Desbloquea completando el nivel anterior")
                    
                    with col3:
                        if is_unlocked and not is_completed:
                            if st.button(f"Desafiar", key=f"challenge_{i}"):
                                # Start new game
                                if sage.level == 6:  # Gran Consejo
                                    questions = st.session_state.question_db.get_random_questions(10)
                                else:
                                    questions = st.session_state.question_db.get_questions_by_category(sage.specialty, 5)
                                
                                st.session_state.game = GameSession(player, sage.level)
                                st.session_state.game.start_level(questions, sage)
                                st.rerun()
                        elif is_completed:
                            if st.button(f"Repetir", key=f"repeat_{i}"):
                                # Restart completed level
                                if sage.level == 6:
                                    questions = st.session_state.question_db.get_random_questions(10)
                                else:
                                    questions = st.session_state.question_db.get_questions_by_category(sage.specialty, 5)
                                
                                st.session_state.game = GameSession(player, sage.level)
                                st.session_state.game.start_level(questions, sage)
                                st.rerun()
                    
                    st.markdown("---")
        
        else:
            # Active game
            game = st.session_state.game
            question = game.get_current_question()
            
            if question:
                # Display game header
                col1, col2, col3 = st.columns([2, 2, 1])
                
                with col1:
                    st.markdown(f"### {game.sage.avatar} {game.sage.name}")
                    st.markdown(f"*{game.sage.title}*")
                
                with col2:
                    st.metric("Racha", f"🔥 {game.streak}")
                    st.metric("Puntuación", f"⭐ {game.score}")
                
                with col3:
                    st.metric("Pregunta", f"{game.current_question_index + 1}/{len(game.questions)}")
                
                st.markdown("---")
                
                # Display question
                st.markdown(f"## {question.question}")
                st.markdown(f"**Categoría:** {question.category} | **Dificultad:** {'⭐' * question.difficulty}")
                
                # Power-up buttons
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    if player.power_ups_owned.get("vision_futuro", 0) > 0:
                        if st.button(f"🔮 Visión del Futuro ({player.power_ups_owned['vision_futuro']})", key="use_vision"):
                            if game.use_power_up("vision_futuro"):
                                hint = game.get_hint()
                                if hint:
                                    st.info(f"💡 Pista: {hint}")
                
                with col2:
                    if player.power_ups_owned.get("eco_pasado", 0) > 0:
                        if st.button(f"⏮️ Eco del Pasado ({player.power_ups_owned['eco_pasado']})", key="use_eco"):
                            st.info("💭 Esta habilidad se activa automáticamente al completar el nivel")
                
                with col3:
                    if player.power_ups_owned.get("escudo_sabio", 0) > 0:
                        if st.button(f"🛡️ Escudo del Sabio ({player.power_ups_owned['escudo_sabio']})", key="use_escudo"):
                            if game.use_power_up("escudo_sabio"):
                                st.success("🛡️ Escudo activado! Tu racha estará protegida.")
                
                with col4:
                    if player.power_ups_owned.get("duplicador", 0) > 0:
                        if st.button(f"✨ Duplicador ({player.power_ups_owned['duplicador']})", key="use_duplicador"):
                            if game.use_power_up("duplicador"):
                                st.success("✨ Duplicador activado! Los fragmentos se duplicarán si respondes bien.")
                
                # Show active power-ups
                active_powerups = [k for k, v in game.active_power_ups.items() if v]
                if active_powerups:
                    st.info(f"🌟 Poder-ups activos: {', '.join(active_powerups)}")
                
                st.markdown("---")
                
                # Answer options
                st.markdown("### Selecciona tu respuesta:")
                
                answer_choice = st.radio(
                    "Opciones:",
                    options=range(len(question.options)),
                    format_func=lambda x: f"{chr(65+x)}) {question.options[x]}",
                    key=f"answer_{game.current_question_index}"
                )
                
                col1, col2, col3 = st.columns([1, 1, 2])
                
                with col1:
                    if st.button("✅ Confirmar Respuesta", type="primary", use_container_width=True):
                        use_dup = game.active_power_ups.get("duplicador", False)
                        result = game.answer_question(answer_choice, use_duplicator=use_dup)
                        
                        # Store result in session state to display
                        st.session_state.last_result = result
                        st.session_state.last_question = question
                        st.rerun()
                
                with col2:
                    if st.button("❌ Abandonar Nivel", use_container_width=True):
                        st.session_state.game = None
                        st.rerun()
                
                # Display last result if available
                if hasattr(st.session_state, 'last_result'):
                    result = st.session_state.last_result
                    last_q = st.session_state.last_question
                    
                    st.markdown("---")
                    if result['correct']:
                        st.success(f"✅ ¡Correcto! Ganaste {result['fragments_earned']} fragmentos de sabiduría")
                        if result['streak'] > 1:
                            st.info(f"🔥 ¡Racha de {result['streak']}! Sigue así.")
                    else:
                        st.error(f"❌ Incorrecto. La respuesta correcta era: {last_q.options[last_q.correct_answer]}")
                        if last_q.hint:
                            st.info(f"💡 Pista: {last_q.hint}")
                    
                    if result['completed']:
                        st.balloons()
                        st.success(f"🎉 ¡Nivel completado! Ganaste {result['total_score']} fragmentos en total.")
                        
                        if game.level == 6:
                            st.markdown("## 🏆 ¡Has ganado la Copa de la Mente Maestra! 🏆")
                            st.markdown("### Eres un verdadero Maestro Supremo del conocimiento")
                    
                    # Clear last result
                    del st.session_state.last_result
                    del st.session_state.last_question
            
            else:
                st.error("No hay pregunta disponible")
    
    with tab2:
        st.markdown("## 💫 Tienda de Poder-ups")
        st.markdown("Usa tus fragmentos de sabiduría para adquirir habilidades especiales")
        
        st.info(f"⭐ Tienes **{player.wisdom_fragments}** fragmentos de sabiduría disponibles")
        
        # Display power-ups
        power_ups = st.session_state.powerup_system.get_all_power_ups()
        
        for power_up in power_ups:
            col1, col2, col3 = st.columns([1, 3, 1])
            
            with col1:
                st.markdown(f"## {power_up.icon}")
            
            with col2:
                st.markdown(f"### {power_up.name}")
                st.markdown(power_up.description)
                st.markdown(f"**Costo:** {power_up.cost} fragmentos")
                
                # Show how many player owns
                power_up_id = st.session_state.powerup_system.get_power_up_id(power_up)
                owned = player.power_ups_owned.get(power_up_id, 0)
                if owned > 0:
                    st.markdown(f"*Tienes: {owned}*")
            
            with col3:
                power_up_id = st.session_state.powerup_system.get_power_up_id(power_up)
                
                if st.button(f"Comprar", key=f"buy_{power_up_id}"):
                    if player.wisdom_fragments >= power_up.cost:
                        player.wisdom_fragments -= power_up.cost
                        if power_up_id not in player.power_ups_owned:
                            player.power_ups_owned[power_up_id] = 0
                        player.power_ups_owned[power_up_id] += 1
                        st.success(f"✅ ¡{power_up.name} adquirido!")
                        st.rerun()
                    else:
                        st.error(f"❌ No tienes suficientes fragmentos")
            
            st.markdown("---")
    
    with tab3:
        st.markdown("## 🏆 Tu Perfil")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown(f"# {player.avatar_emoji}")
            st.markdown(f"# {player.name}")
            
            rank_emoji = get_rank_emoji(player.rank)
            st.markdown(f"## {rank_emoji} {player.rank}")
        
        with col2:
            st.markdown("### Estadísticas")
            
            col_a, col_b = st.columns(2)
            
            with col_a:
                st.metric("⭐ Fragmentos de Sabiduría", player.wisdom_fragments)
                st.metric("📊 Nivel Actual", f"{player.current_level}/6")
                st.metric("✅ Preguntas Correctas", player.questions_correct)
            
            with col_b:
                st.metric("🎯 Precisión", f"{player.get_accuracy():.1f}%")
                st.metric("📝 Total Respondidas", player.questions_answered)
                st.metric("🏆 Niveles Completados", len(player.completed_levels))
        
        st.markdown("---")
        
        # Progress bars for rank
        st.markdown("### Progreso al Siguiente Rango")
        
        rank_thresholds = get_rank_thresholds()
        
        current_rank_idx = next((i for i, (name, _, _) in enumerate(rank_thresholds) if name == player.rank), 0)
        
        if current_rank_idx < len(rank_thresholds) - 1:
            _, min_val, max_val = rank_thresholds[current_rank_idx]
            next_rank, _, _ = rank_thresholds[current_rank_idx + 1]
            
            progress = min((player.wisdom_fragments - min_val) / (max_val - min_val), 1.0)
            st.progress(progress)
            st.markdown(f"Progreso a **{next_rank}**: {player.wisdom_fragments}/{max_val} fragmentos")
        else:
            st.success("🎉 ¡Has alcanzado el rango máximo!")
        
        st.markdown("---")
        
        # Social sharing
        st.markdown("### Comparte tu Progreso")
        
        share_text = get_share_text(player)
        
        st.text_area("Texto para compartir:", share_text, height=150)
        
        st.markdown("""
        Comparte en:
        - 🐦 [Twitter](https://twitter.com/intent/tweet)
        - 📘 [Facebook](https://www.facebook.com/sharer/sharer.php)
        - 💼 [LinkedIn](https://www.linkedin.com/sharing/share-offsite/)
        """)
        
        # Failed questions review (Eco del Pasado)
        if player.failed_questions:
            st.markdown("---")
            st.markdown("### ⏮️ Preguntas para Repasar")
            st.markdown("Estas son las preguntas que has fallado recientemente:")
            
            for i, q in enumerate(player.failed_questions[-5:], 1):
                with st.expander(f"{i}. {q.question}"):
                    st.markdown(f"**Respuesta correcta:** {q.options[q.correct_answer]}")
                    st.markdown(f"**Categoría:** {q.category}")
                    if q.hint:
                        st.markdown(f"**Pista:** {q.hint}")
    
    with tab4:
        st.markdown("## 📊 Tabla de Clasificación")
        st.markdown("### Rankings Globales")
        
        # Show rank system
        st.markdown("### Sistema de Rangos")
        
        rank_thresholds = get_rank_thresholds()
        rank_descriptions = {
            "Aprendiz": "El comienzo de tu viaje",
            "Estudiante": "Avanzando en el conocimiento",
            "Erudito": "Dominio de múltiples áreas",
            "Sabio": "Sabiduría excepcional",
            "Gran Sabio": "Maestría completa",
            "Maestro Supremo": "La cúspide del conocimiento",
        }
        
        for rank_name, min_frag, max_frag in rank_thresholds:
            col1, col2, col3 = st.columns([2, 2, 3])
            
            rank_emoji = get_rank_emoji(rank_name)
            threshold_text = f"{min_frag}-{max_frag-1} fragmentos" if max_frag < 10000 else f"{min_frag}+ fragmentos"
            description = rank_descriptions.get(rank_name, "")
            
            with col1:
                st.markdown(f"**{rank_emoji} {rank_name}**")
            
            with col2:
                st.markdown(threshold_text)
            
            with col3:
                st.markdown(f"*{description}*")
                
                # Highlight player's current rank
                if rank_name == player.rank:
                    st.success("← Tu rango actual")
        
        st.markdown("---")
        
        st.markdown("### 🏆 Tu Posición")
        st.markdown(f"**{player.avatar_emoji} {player.name}** - {player.rank}")
        st.markdown(f"⭐ {player.wisdom_fragments} fragmentos | 🎯 {player.get_accuracy():.1f}% precisión")
    
# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("© 2025 - Semillero de Investigación IA")
st.sidebar.markdown("👤 Gloria María Araujo Chambo")
st.sidebar.markdown("📧 gloria.araujo@universidad.edu")

st.write("✅ La app se ejecutó correctamente.")





















