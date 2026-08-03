import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Análisis de Gasto Público en Chile')
st.caption('Órdenes de compra vía licitación — Semestre 1, 2026 (Mercado Público / ChileCompra)')

df = pd.read_csv('data/processed/ordenes_compra_licitacion_limpio.csv', parse_dates=['FechaEnvioOC'])


# --- Filtros ---
st.sidebar.header('Filtros')
regiones_disponibles = sorted(df['RegionUnidadCompra'].unique().tolist())
regiones_seleccionadas = st.sidebar.multiselect(
    'Región',
    regiones_disponibles,
    default=[]
)

if regiones_seleccionadas:
    df_filtrado = df[df['RegionUnidadCompra'].isin(regiones_seleccionadas)]
else:
    df_filtrado = df

st.divider()
col1, col2, col3 = st.columns(3)
col1.metric("Gasto total", f"${(df_filtrado['MontoNetoItem_final'].sum()/1e6):,.0f}M")
col2.metric("Órdenes de compra", f"{df_filtrado['codigoOC'].nunique():,}")
col3.metric("Instituciones", f"{df_filtrado['Institucion'].nunique():,}")
st.divider()

# --- Gasto por región ---
st.header('Gasto por región')

gasto_por_orden = df_filtrado.drop_duplicates(subset='codigoOC')[['codigoOC', 'RegionUnidadCompra', 'MontoNetoOC_final']]
gasto_por_region = gasto_por_orden.groupby('RegionUnidadCompra')['MontoNetoOC_final'].sum().sort_values(ascending=False)
gasto_por_region_millones = (gasto_por_region / 1_000_000).round(1)

fig = px.bar(
    x=gasto_por_region_millones.values,
    y=gasto_por_region_millones.index,
    orientation='h',
    labels={'x': 'Gasto total (millones de CLP)', 'y': ''},
    color_discrete_sequence=['#4C78A8']
)
fig.update_layout(
    yaxis={'categoryorder': 'total ascending'},
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    height=600,
)
st.plotly_chart(fig, use_container_width=True)

st.info("""
**Hallazgo:** La Región Metropolitana concentra el mayor gasto público
(\$65.807 millones), más de 5 veces el monto de la segunda región
(Valparaíso, \$12.539 millones). Esto es esperable dado que gran parte de
los organismos centrales del Estado tienen su sede en la RM.
""")

# --- Categorías de gasto ---
st.header('Top 10 categorías de gasto')

gasto_por_rubro = df_filtrado.groupby('RubroN1')['MontoNetoItem_final'].sum().sort_values(ascending=False)
gasto_por_rubro_millones = (gasto_por_rubro / 1_000_000).round(1).head(10)

fig2 = px.bar(
    x=gasto_por_rubro_millones.values,
    y=gasto_por_rubro_millones.index,
    orientation='h',
    labels={'x': 'Gasto total (millones de CLP)', 'y': ''},
    color_discrete_sequence=['#59A14F']
)
fig2.update_layout(
    yaxis={'categoryorder': 'total ascending'},
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    height=600,
)
st.plotly_chart(fig2, use_container_width=True)

st.info("""
**Hallazgo:** La categoría "Servicios de defensa nacional, orden público y
seguridad" concentra el mayor gasto ($41.042 millones), casi el doble que
la segunda categoría (construcción y mantenimiento). Categorías de salud
aparecen en el top 10, pero considerablemente por debajo de seguridad y
construcción.
""")

# --- Estacionalidad ---
st.header('Evolución mensual del gasto')

gasto_por_orden_fecha = df_filtrado.drop_duplicates(subset='codigoOC')[['codigoOC', 'FechaEnvioOC', 'MontoNetoOC_final']]
gasto_por_orden_fecha['mes'] = gasto_por_orden_fecha['FechaEnvioOC'].dt.month
gasto_por_mes = gasto_por_orden_fecha.groupby('mes')['MontoNetoOC_final'].sum()
gasto_por_mes_millones = (gasto_por_mes / 1_000_000).round(1)

fig3 = px.line(
    x=gasto_por_mes_millones.index,
    y=gasto_por_mes_millones.values,
    markers=True,
    labels={'x': 'Mes', 'y': 'Gasto total (millones de CLP)'},
    color_discrete_sequence=['#E15759']
)
fig3.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    height=500,
)
st.plotly_chart(fig3, use_container_width=True)

st.info("""
**Hallazgo:** El gasto muestra un pico marcado en febrero ($46.021
millones), más del doble que enero, seguido de una caída sostenida hasta
mayo. Nota: el dataset solo contiene datos hasta el 31 de mayo de 2026
(desfase de actualización del portal ChileCompra), por lo que no se puede
evaluar el semestre completo.
""")
# --- Instituciones ---
st.header('Top 10 instituciones por gasto')

gasto_por_institucion = gasto_por_orden.merge(df_filtrado[['codigoOC', 'Institucion']].drop_duplicates(), on='codigoOC')
gasto_por_institucion = gasto_por_institucion.groupby('Institucion')['MontoNetoOC_final'].sum().sort_values(ascending=False)
gasto_por_institucion_millones = (gasto_por_institucion / 1_000_000).round(1).head(10)

fig4 = px.bar(
    x=gasto_por_institucion_millones.values,
    y=gasto_por_institucion_millones.index,
    orientation='h',
    labels={'x': 'Gasto total (millones de CLP)', 'y': ''},
    color_discrete_sequence=['#B07AA1']
)
fig4.update_layout(
    yaxis={'categoryorder': 'total ascending'},
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    height=600,
)
st.plotly_chart(fig4, use_container_width=True)

st.info("""
**Hallazgo:** El Servicio Nacional de Reinserción Social Juvenil concentra
el mayor gasto individual, casi 4 veces más que la segunda institución. El
top 10 está dominado por organismos de educación y protección de la niñez,
un panorama distinto al de categorías de producto, donde domina seguridad.
""")

st.divider()
st.caption('Fuente: Datos abiertos ChileCompra | Datos: enero-mayo 2026 | Proyecto de portafolio')