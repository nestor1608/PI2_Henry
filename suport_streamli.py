import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from dataset_conect import *

cierre= cierre

sypActual=sypActual


def anual_data(data):
    data.index=pd.to_datetime(data.index)
    x_anio = data.groupby(data.index.year).mean().round(3)
    x_anio = x_anio.transpose()
    return x_anio

def plot_six_m(data,valores):
    fig, ax = plt.subplots(figsize=(10,5))
    for i in valores:
        ax.plot(data.index,data[[i]],label=i)
    plt.legend()
    return plt.show()

def searcch_bussines(search):
    x = sypActual[sypActual.Symbol.isin(search)]
    return x

def mean_bussines(data, round:bool=True):
    if round == True: 
        group= pd.DataFrame(data.transpose().mean(axis=1).round(3), columns=['Promedio'])
    else:
        group= pd.DataFrame(data.transpose().mean(axis=1), columns=['Promedio'])
    return group

def five_year_back(data,anios:list=[2018,2019,2020,2021,2022,2023]):
    prome= {}
    for anio in anios:
        prome[anio]= data[data.index.year ==anio].transpose().mean(axis=1).round(3)
    prome['mean_total']= cierre.transpose().mean(axis=1).round(3)
    prome['current']= data[data.index.year ==2023].transpose().iloc[:,-1]
    datos= pd.DataFrame(prome)
    creci= (datos[datos.columns[:-3]].pct_change(axis=1)*100).round(3)
    datos['growth']=creci.mean(axis=1).round(3)
    return datos,creci

def search_mean(data,search):
    datos= five_year_back(data)[0]
    result = datos[datos.index.isin(search)]
    return result


close_anual = anual_data(cierre)



close_anual.replace([np.inf, -np.inf],0.0,inplace=True)
close_anual['mean_total'] =close_anual.mean(axis=1).round(3)
close_anual['current']=(cierre[cierre.index.year ==2023].transpose().iloc[:,-1]).round(3)
creci= close_anual[close_anual.columns[:-3]].pct_change(axis=1)*100
close_anual['growth']=creci.mean(axis=1).round(3)

x= close_anual.iloc[3,4:-3].round()
cre =x.pct_change()*100
close_anual.iloc[3,].growth = cre.mean().round(2)

posicion = close_anual.index.get_loc(close_anual[close_anual['growth']== np.inf].index[0])  
c=close_anual.iloc[posicion,4:-4].pct_change()*100
close_anual.iloc[posicion,].growth = c.mean().round(2)

creci=creci.round(3)
creci=creci.replace([np.inf,-np.inf], 0) 
sectores=sypActual['GICS Sector'].unique()


def data_sector_mean(sector,data):
    sector=sypActual[sypActual['GICS Sector']==sector]['Symbol'].values
    promedio= data[data.index.isin(sector)]
    promedio = promedio.mean(axis=0).round().to_frame().T
    return promedio

def sector_browth_grafic(sector):
    promedio= data_sector_mean(sector,close_anual)
    return promedio.transpose()[:-4].plot.bar()


"""busca dentro del sector especificado y devuelve los valores de las empresas"""
def search_bussine_anual(sector):
    symbol= sypActual[sypActual['GICS Sector']==sector]['Symbol'].values
    result= close_anual[close_anual.index.isin(symbol)]
    return result

"""filtrar por pormedio de precio (close) y valor de crecimiento"""
def filter_grow_value(data,grow,value):
    select = data[(data['growth']>= grow) & (data['mean_total']>value)]
    return select