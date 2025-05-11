import streamlit as st
import pandas as pd
import numpy as np
import datetime

# Título principal
st.set_page_config(page_title="AeroOptimize", layout="wide")
st.title("✈️ AeroOptimize – Optimización de carga y combustible con IA")

# Introducción
st.markdown("""
### ¿Qué es AeroOptimize?
AeroOptimize es una solución basada en inteligencia artificial que optimiza la distribución de carga y el consumo de combustible en aeronaves, a través de algoritmos avanzados y análisis de datos en tiempo real.

Esta demo simula los módulos clave del sistema explicando cómo funciona cada parte y mostrando resultados simulados.
""")

# Simulación de ingreso de datos
st.header("📥 Ingesta y Procesamiento de Datos")
st.markdown("""
Los datos son recolectados de:
- Sistemas de gestión de flota (peso, consumo, ruta)
- Meteorología
- Distribución de carga
""")

st.subheader("Carga de datos de vuelo")
data = {
    'Peso total (kg)': [18000],
    'Centro de gravedad (%)': [30],
    'Velocidad crucero (km/h)': [850],
    'Ruta': ['MAD → JFK'],
    'Viento en contra (km/h)': [60]
}
df = pd.DataFrame(data)
st.dataframe(df)

# Módulo de IA
st.header("🧠 Módulo de IA para optimización")
st.markdown("""
Utilizamos algoritmos para optimizar:
- Distribución de carga
- Ruta de vuelo (en función de viento y condiciones)
- Previsión de consumo total
""")

# Simulación de resultados del algoritmo
optim_result = {
    'Reducción estimada de combustible (%)': [7.3],
    'Aprovechamiento óptimo de carga (%)': [92],
    'Ruta recomendada': ['MAD → BOS → JFK'],
    'Emisiones evitadas (kg CO₂)': [890]
}
st.subheader("Resultados simulados del modelo")
st.table(pd.DataFrame(optim_result))

# Visualización y monitoreo
st.header("📊 Panel de visualización")
st.markdown("""
Monitoriza en tiempo real las métricas clave:
""")

kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric("🔋 Consumo original (L)", "12,300", "-7.3%")
kpi2.metric("🎯 Optimización carga", "92%", "+8%")
kpi3.metric("🌱 CO₂ evitado", "890 kg", "↓")

# Footer
st.markdown("""
---
#### Aplicación demo desarrollada con [Streamlit](https://streamlit.io/) | [Repositorio en GitHub](https://github.com/tuusuario/aerooptimize-demo)
""")
