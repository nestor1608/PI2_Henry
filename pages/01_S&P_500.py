import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from syp import *

st.title('Información del ETLs del S&P 500')
st.markdown('***')
st.subheader('Crecimiento promedio por año')

select = st.selectbox(label='Metricas',options=anual_syp.columns)

fig = px.bar(anual_syp, x=anual_syp.index,y=anual_syp[select] )
st.plotly_chart(fig,use_container_width=True)



cre=creci_porcentaje(anual_syp)

st.header('Porcentaje de crecimiento año a año')
fig =px.bar(cre[1])
st.plotly_chart(fig,use_container_width=True)
st.markdown(f'* Promedio porcentual anual de : {cre[0]} %')

st.markdown('***')
st.header('Filtrar por año')

st.markdown('_podremos observar años a año y mes a mes el crecimiento porcentual_')
anio = st.slider('Año',2000,2023)
syp=syp
month=ratio_month(anio,syp)
r_month= creci_porcentaje(month)
st.markdown(f'* Crecimiento promedio porcentual mensual de : {r_month[0]}')
fig =px.bar(r_month[1])
st.plotly_chart(fig,use_container_width=True)
st.markdown('## Datos agrupados por años')
st.markdown('***')
st.table(anual_syp)
