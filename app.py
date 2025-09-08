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
    
    # Generar datos de riesgos
    @st.cache_data(ttl=60)  # Actualiza cada 60 segundos
    def generar_datos_riesgos():
        np.random.seed(int(datetime.now().timestamp()))
        areas = ['Área A', 'Área B', 'Área C', 'Área D', 'Área E']
        tipos_riesgo = ['Ergonómico', 'Químico', 'Físico', 'Psicosocial']
        
        # Generar datos de las últimas 24 horas
        horas = pd.date_range(start=datetime.now() - pd.Timedelta(hours=24), 
                             end=datetime.now(), freq='H')
        
        datos = []
        for hora in horas:
            for area in areas:
                tipo = np.random.choice(tipos_riesgo)
                nivel = np.random.randint(1, 11)
                datos.append({
                    'Timestamp': hora,
                    'Área': area,
                    'Tipo de Riesgo': tipo,
                    'Nivel': nivel
                })
        
        return pd.DataFrame(datos)
    
    # Cargar datos de riesgos
    df_riesgos = generar_datos_riesgos()
    
    # Filtros interactivos
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        tipo_filtro = st.selectbox("🔍 Filtrar por Tipo de Riesgo", 
                                   ['Todos'] + sorted(df_riesgos['Tipo de Riesgo'].unique()))
    
    with col2:
        area_filtro = st.selectbox("📍 Filtrar por Área", 
                                  ['Todas'] + sorted(df_riesgos['Área'].unique()))
    
    with col3:
        nivel_min = st.slider("⚠️ Nivel Mínimo de Riesgo", 1, 10, 7)
    
    # Aplicar filtros
    df_filtrado = df_riesgos.copy()
    if tipo_filtro != 'Todos':
        df_filtrado = df_filtrado[df_filtrado['Tipo de Riesgo'] == tipo_filtro]
    if area_filtro != 'Todas':
        df_filtrado = df_filtrado[df_filtrado['Área'] == area_filtro]
    df_filtrado = df_filtrado[df_filtrado['Nivel'] >= nivel_min]
    
    # Gráfico de dispersión interactivo
    st.subheader("📊 Distribución de Riesgos en Tiempo Real")
    
    fig = px.scatter(df_filtrado, 
                     x='Timestamp', 
                     y='Nivel',
                     color='Tipo de Riesgo',
                     size='Nivel',
                     hover_data=['Área'],
                     title='Evolución de Riesgos por Tipo',
                     color_discrete_map={
                         'Ergonómico': '#FF6B6B',
                         'Químico': '#4ECDC4',
                         'Físico': '#45B7D1',
                         'Psicosocial': '#96CEB4'
                     })
    
    fig.update_layout(
        xaxis_title="Fecha y Hora",
        yaxis_title="Nivel de Riesgo (1-10)",
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Tabla de alertas críticas
    st.subheader("🚨 Alertas Críticas Recientes")
    
    alertas_criticas = df_filtrado[df_filtrado['Nivel'] >= 8].sort_values('Timestamp', ascending=False).head(10)
    
    if not alertas_criticas.empty:
        alertas_criticas['Timestamp'] = alertas_criticas['Timestamp'].dt.strftime('%d/%m/%Y %H:%M')
        alertas_criticas = alertas_criticas.rename(columns={
            'Timestamp': 'Fecha/Hora',
            'Área': 'Área',
            'Tipo de Riesgo': 'Tipo',
            'Nivel': 'Nivel'
        })
        
        st.dataframe(alertas_criticas, use_container_width=True)
    else:
        st.success("✅ No hay alertas críticas en este momento")
    
    # Botón de actualización
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if st.button("🔄 Actualizar Datos", type="primary", use_container_width=True):
            st.cache_data.clear()
            st.experimental_rerun()
            st.success("✅ Datos actualizados correctamente")
    
    st.markdown("---")
    
    # Análisis Comparativo
    st.markdown("### 📈 Análisis Comparativo en Tiempo Real")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📊 Riesgos por Tipo")
        tipo_counts = df_filtrado['Tipo de Riesgo'].value_counts()
        fig_tipo = px.pie(values=tipo_counts.values, 
                          names=tipo_counts.index,
                          title="Distribución por Tipo de Riesgo")
        st.plotly_chart(fig_tipo, use_container_width=True)
    
    with col2:
        st.subheader("📍 Riesgos por Área")
        area_counts = df_filtrado['Área'].value_counts()
        fig_area = px.bar(x=area_counts.index, 
                          y=area_counts.values,
                          title="Incidencias por Área",
                          labels={'x': 'Área', 'y': 'Cantidad'})
        st.plotly_chart(fig_area, use_container_width=True)
    
    # Resumen estadístico
    st.markdown("### 📋 Resumen Estadístico")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_registros = len(df_filtrado)
        st.metric("📊 Total Registros", total_registros)
    
    with col2:
        promedio_riesgo = df_filtrado['Nivel'].mean()
        st.metric("⚠️ Nivel Promedio", f"{promedio_riesgo:.1f}")
    
    with col3:
        max_riesgo = df_filtrado['Nivel'].max()
        st.metric("🔴 Riesgo Máximo", max_riesgo)
    
    with col4:
        alertas_altas = len(df_filtrado[df_filtrado['Nivel'] >= 8])
        st.metric("🚨 Alertas Altas", alertas_altas)
