import streamlit as st
import pandas as pd
from suport_streamli import *
import plotly.express as px
import plotly.graph_objs as go


st.set_option('deprecation.showPyplotGlobalUse', False)

def scater_plot(data,x,y):
    fig= px.scatter(data, x=x, y=y, symbol=data.index)
    return fig


sectores = sectores
st.title('Sectores del S&P 500')
st.markdown('***')
st.header('Top 5 porcentaje promedio crecimiento')
st.markdown('_puede agregar otros sectores o quitarlos_')

default = sectores_anual.sort_values('growth',ascending=False).index.values[:5]
multisectores = st.multiselect('Seleccione sectores a analizar:', sectores, default=default)
fig=px.line(sectores_anual[sectores_anual.index.isin(multisectores)].transpose())
st.plotly_chart(fig,use_container_width=True)   

###----------------------------------------------------------------------------------------------

sector = st.selectbox(label='Sectores',options=sectores)
st.header(f'{sector}')
data=search_bussine_anual(sector)
fig= scater_plot(data, x='mean_total',y='growth')
st.plotly_chart(fig,use_container_width=True)

##-------------------------------------------------------------------------------
st.header('Filtrar x crecimiento y precio promedio ')

growth = st.slider('Crecimiento (growth):',int(data.growth.min().round()),int(data.growth.max().round()),value=int(data.growth.min().round()))
value=st.slider('Promedio de precio:',int(data['mean_total'].min().round()),int(data['mean_total'].max().round()),value=int(data['mean_total'].min().round()))
new_date=filter_grow_value(data,growth,value)
bussines = st.multiselect('Seleccione empresas/organizaciones a analizar:', close_anual.index,default=new_date.index.values)
fig= scater_plot(new_date, x='mean_total',y='growth')
st.plotly_chart(fig,use_container_width=True)

##--------------------------------------------------------------------------
st.header('Valor promedio por Año')
crecimiento= data_sector_mean(sector,close_anual)
fig =px.bar(crecimiento.transpose())
st.plotly_chart(fig,use_container_width=True)

##-----------------------------------------------------------------------------------

st.header('Porcentaje promedio de crecimiento por año')
por_creci=data_sector_mean(sector,creci)
fig =px.bar(por_creci.transpose())
st.plotly_chart(fig,use_container_width=True)
val_cre = (crecimiento.loc[0].pct_change()*100).mean().round(3)
st.markdown('* Porcentaje promedio de crecimiento:')
fig=go.Figure(go.Scatter(x=[0],y=[0], text=[val_cre],mode='text',textfont=dict(size=52)))
fig.add_shape(type='circle',xref='x',yref='y',x0=-1,y0=-1,x1=1,y1=1,line=dict(color='royalblue',width=4))
fig.update_layout(width=200,height=300)
st.plotly_chart(fig)
st.markdown('_este valor coresponde a la medicion hasta el 2022_')

##---------------------------------------------------------------------------------
st.header(f'{sector}')
st.markdown('***')
st.dataframe(search_mean(cierre,bussines),use_container_width= True)


prome={}
for sec in sectores:
    promedio=data_sector_mean(sec,close_anual)
    prome[sec]=(promedio.loc[0][:-4].pct_change()*100).mean().round(2)

prome= pd.DataFrame.from_dict(prome,orient='index',columns=['mean_growth'])
st.markdown('***')
st.dataframe(prome.sort_values('mean_growth',ascending=False),use_container_width= True)
st.markdown('_Porcentaje promedio de crecimiento incluyendo los registros que va hasta 2023_')