
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: data.py : python script for data collection                                                 -- #
# -- author: YOUR GITHUB USER NAME                                                                       -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: YOUR REPOSITORY URL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""
import time as time
import numpy as np
import pandas as pd
import yfinance as yf
import functions as fn
from os import listdir, path
from os.path import isfile, join
from main import  k
from  main import  c
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width',None)
pd.set_option('display.expand_frame_repr',False)

# Lista con los nombres de los archivos csv a leer
abspath= path.abspath('c:/Users/luzitaifi/Documents/Micro_Estructuras_Trading/Lab_1/myst_if708591_lab1/NAFTRAC_holdings')
arc= [f[8:-4] for f in listdir(abspath) if isfile(join(abspath, f))]
arc= ['NAFTRAC_' + i.strftime('%d%m%y') for i in sorted(pd.to_datetime(arc))]
# Crear un diccionario para almacenar todos los datos
dato_arc= {}
for i in arc:
    i = arc[0]
    # leer los archivos despues de los primeros renglones
    dato= pd.read_csv('c:/Users/luzitaifi/Documents/Micro_Estructuras_Trading/Lab_1/myst_if708591_lab1/NAFTRAC_holdings/' + arc[0] + '.csv',skiprows=2,header=None)
    # Renombrar las columnas
    dato.columns = list(dato.iloc[0, :])
    dato = dato.iloc[:, pd.notnull(dato.columns)]
    dato.iloc[1:-1].reset_index(drop=True, inplace=False)
    # Alimine la columan 1 y 37 por el error que me sale del nombre de las columnas
    dato = dato.drop([0, 37])
    # Limpieza de datos
    # Eliminar comas en columna de precio
    dato['Precio'] = [i.replace(',', '') for i in dato['Precio']]
    # Eliminar * de columna tickers
    dato['Ticker'] = [i.replace('*', '') for i in dato['Ticker']]
    # Conversion de type str a float
    conv = {'Ticker': str, 'Nombre': str, 'Peso (%)': float}
    dato = dato.astype(conv)
    # Conversion a decimal la culumna 'Peso (%)'
    dato['Peso (%)'] = dato['Peso (%)'] / 100
    # Guardar cambios en diccionario
    dato_arc[i] = dato
    # Pesos del primer archivo
    dato_arc[arc[0]]['Peso (%)']

# 1.3 Vector de fechas apartir de vector de nombres de archivos
fechas= fn.f_fech(p_arc=arc)
# 1.4 Vector de fechas apartir de YF
gti= fn.gt(pa=arc,dt=dato_arc)
# 1.5 Descarga y orden de datos historicos
ppr= fn.pr(gt=gti,iif=fechas['i_f'])




# Primer archivo de la carpeta ordenado alfabeticamente por Tickers
pos_dat = dato_arc[arc[0]].copy()[['Ticker','Nombre','Peso (%)']]
# Agregar MX
pos_dat['Ticker']=pos_dat['Ticker'] + '.MX'
# Corregir el tickers
pos_dat['Ticker']=pos_dat['Ticker'].replace('GFREGIOO.MX','RA.MX')
pos_dat['Ticker']=pos_dat['Ticker'].replace('MEXCHEM.MX','ORBIA.MX')
pos_dat['Ticker']= pos_dat['Ticker'].replace('LIVEPOLC.1.MX', 'LIVEPOLC-1.MX')
# Ordenar alfabeticamente respecto a Ticker
pos_dat=pos_dat.sort_values('Ticker')
# Resetear index  (Evita tener problemas con iloc)
pos_dat.reset_index(inplace=True,drop=True)
# Lista de activos a eliminar del archivo 1
c_act = ['KOFL', 'BSMXB', 'MXN']
i_activos = ([pos_dat[list(pos_dat['Ticker'].isin(c_act))].index])
# Eliminar activos del primer archivo
pos_dat=pos_dat.drop([7,21,26])

# Precios para la posicion
pos_dat['Precio']=np.array(ppr.iloc[0,[i in pos_dat['Ticker'].to_list() for i in ppr.columns.to_list()]])
# Capital destinado por accion (proporcion del capital menos comisiones por posicion)
pos_dat['Capital']=pos_dat['Peso (%)']*k-pos_dat['Peso (%)']*k*c
#pos_dat['Titulos']=pos_dat['Capital']/pos_dat['Precio']
#print(pos_dat)
# print(dato_arc[arc[0]].copy().sort_values('Ticker').isin(c_act))

#Fecha en la que se busca hacer el match de precios
match= 7
ppr.index.to_list()[match]
# Precios necesarios para la posicion metodo 1
#m1=np.array(precios.iloc[match, [i in pos_dat['Ticker'].to_list() for i in precios.columns.to_list().index(i)]])
#m2=[precios.iloc[0, precios.columns.to_list().index(i)] for i in pos_dat['Ticker']]
#pos_dat['Precios:m1']= m1
#pos_dat['Precios:m2']=m2
#print(m1)
#print((precios.iloc[0,0:]))
print(pos_dat)
