import streamlit as st
import pandas as pd
import numpy as np

import plotly.express as px
from organi_suport import *
from suport_streamli import close_anual,searcch_bussines,creci
from syp import ratio_month,creci_porcentaje


st.title('Analisis por Empresas u Organizaciones')
st.markdown('***')
st.markdown('_Aqui podra comparar el crecimiento que tuvieron entre varias empresas(5 max)_')
selecionados=st.multiselect('Elija empresas u organizaciones',close_anual.index.values,max_selections=5)

fig=px.line(close_anual[close_anual.index.isin(selecionados)].transpose())
st.plotly_chart(fig,use_container_width=True)   

crecimiento=searcch_bussines(selecionados)

st.header('Datos de las empresas')
st.markdown('***')
st.dataframe(crecimiento,use_container_width=True)
st.markdown('***')
st.header('Promedios  porcentual de crecimiento')
fig=px.area(creci[creci.index.isin(selecionados)].transpose())
st.plotly_chart(fig,use_container_width=True)  

st.markdown('***')

if selecionados: 
    for org in selecionados:
        x= creci.loc[org].mean().round(3)
        st.markdown(f'* Crecimiento promedio porcentual anual de {org} es de: {x} %')
    st.markdown('_Seleccione alguana organizacion en particular de las elegidas para un analisis mas individual_')
    select=st.selectbox('Seleccionar: ', options=selecionados)
    if select:
        data=armar_data(select)
        anio = st.slider('Año',2000,2023)
        data.index = pd.to_datetime(data.index)
        grou= ratio_month(anio,data)
        
        st.markdown('***')
        st.header('Datos mensuales promedios')
        st.dataframe(grou,use_container_width=True)
        st.subheader('Valor crecimiento promedio mensuales')
        fig=px.bar(grou['Close'])
        st.plotly_chart(fig,use_container_width=True)
        datos = creci_porcentaje(grou)
        st.subheader('Porcentajes promedio de crecimiento mensuales')
        try:
            fig=px.bar(datos[1])
            st.plotly_chart(fig,use_container_width=True)
            st.markdown(f'* _Porcentaje promedio de crecimiento mensual {datos[0]} %_  ')
        except ValueError:
            st.warning('No hay suficientes datos')
else:
    st.warning('Elija algunas empresas u organizaciones')
    