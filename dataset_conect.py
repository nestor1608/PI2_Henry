import pandas as pd




def csv_date(url:str):
    data= pd.read_csv(url,index_col='Date')
    data.index=pd.to_datetime(data.index)
    return data

cierre =csv_date('metricas/cierre_syp.csv')
volumen= csv_date('metricas/volumen_syp.csv')
maximos= csv_date('metricas/maximos_syp.csv')
minimos= csv_date('metricas/minimos_syp.csv')
apertura = csv_date('metricas/apertura_syp.csv')

sypActual= pd.read_csv('dataset/syp.csv')
#changeSyp = pd.read_csv('cambios_syp.csv')
sectores_anual= pd.read_csv('dataset/business_anual.csv',index_col='Unnamed: 0')