import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import competidores_cabello_espana as data

# Configuración de la página
st.set_page_config(
    page_title="Análisis de Competidores - Cuidado Capilar España",
    page_icon="💇‍♀️",
    layout="wide"
)

# Título y descripción
st.title("💇‍♀️ Análisis de Competidores en el Mercado Español de Cuidado Capilar")
st.markdown("""
Este dashboard presenta un análisis detallado de los principales competidores en el mercado español 
de cuidado capilar, incluyendo su segmentación, productos y canales de distribución.
""")

# Cargar datos
df = pd.DataFrame(data.competidores)

# Sidebar con filtros
st.sidebar.title("Filtros")
segmento_seleccionado = st.sidebar.multiselect(
    "Segmento de Mercado",
    options=df['segmento'].unique(),
    default=df['segmento'].unique()
)

categoria_seleccionada = st.sidebar.multiselect(
    "Categoría",
    options=df['categoria'].unique(),
    default=df['categoria'].unique()
)

# Filtrar datos
df_filtrado = df[
    (df['segmento'].isin(segmento_seleccionado)) & 
    (df['categoria'].isin(categoria_seleccionada))
]

# Layout de columnas
col1, col2 = st.columns(2)

with col1:
    # Gráfico de distribución por segmento
    fig_segmento = px.pie(
        df_filtrado,
        names='segmento',
        title='Distribución por Segmento de Mercado',
        hole=0.4
    )
    fig_segmento.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_segmento, use_container_width=True)

with col2:
    # Gráfico de distribución por categoría
    fig_categoria = px.pie(
        df_filtrado,
        names='categoria',
        title='Distribución por Categoría',
        hole=0.4
    )
    fig_categoria.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_categoria, use_container_width=True)

# Gráfico de productos más comunes
st.subheader("Productos más Comunes")
productos_count = {}
for productos_list in df_filtrado['productos']:
    for producto in productos_list:
        productos_count[producto] = productos_count.get(producto, 0) + 1

df_productos = pd.DataFrame({
    'Producto': list(productos_count.keys()),
    'Cantidad': list(productos_count.values())
}).sort_values('Cantidad', ascending=True)

fig_productos = px.bar(
    df_productos,
    x='Cantidad',
    y='Producto',
    orientation='h',
    title='Productos más Comunes entre los Competidores',
    color='Cantidad',
    color_continuous_scale='Blues'
)
st.plotly_chart(fig_productos, use_container_width=True)

# Gráfico de canales de distribución
st.subheader("Canales de Distribución")
canales_count = {}
for canales_list in df_filtrado['canales']:
    for canal in canales_list:
        canales_count[canal] = canales_count.get(canal, 0) + 1

df_canales = pd.DataFrame({
    'Canal': list(canales_count.keys()),
    'Cantidad': list(canales_count.values())
}).sort_values('Cantidad', ascending=True)

fig_canales = px.bar(
    df_canales,
    x='Cantidad',
    y='Canal',
    orientation='h',
    title='Canales de Distribución más Utilizados',
    color='Cantidad',
    color_continuous_scale='Greens'
)
st.plotly_chart(fig_canales, use_container_width=True)

# Tabla detallada de competidores
st.subheader("Detalle de Competidores")
st.dataframe(
    df_filtrado[['nombre', 'dominio', 'segmento', 'categoria', 'productos', 'canales']],
    use_container_width=True
)

# Análisis de oportunidades
st.subheader("📊 Análisis de Oportunidades")
col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    ### Oportunidades de Producto
    - **Tratamientos Específicos**: Solo 30% de los competidores ofrecen mascarillas
    - **Acondicionadores**: Solo 10% de los competidores tienen línea de acondicionadores
    - **Serums**: Oportunidad en productos de tratamiento específicos
    """)

with col4:
    st.markdown("""
    ### Oportunidades de Canal
    - **E-commerce**: Solo 40% de los competidores tienen presencia online
    - **Tiendas Especializadas**: Oportunidad para expandir distribución
    - **Salones Premium**: Segmento con menor competencia
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>Dashboard generado el {}</p>
    <p>© 2024 Análisis de Mercado - Cuidado Capilar España</p>
</div>
""".format(datetime.now().strftime("%d/%m/%Y %H:%M")), unsafe_allow_html=True) 