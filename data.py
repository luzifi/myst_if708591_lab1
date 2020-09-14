
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

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width',None)
pd.set_option('display.expand_frame_repr',False)

# 1.1 Lista de archivos a importar
abspath= path.abspath('c:/Users/luzitaifi/Documents/Micro_Estructuras_Trading/Lab_1/myst_if708591_lab1/NAFTRAC_holdings')
arc= [f[8:-4] for f in listdir(abspath) if isfile(join(abspath, f))]
arc= ['NAFTRAC_' + i.strftime('%d%m%y') for i in sorted(pd.to_datetime(arc))]
# 1.2 Leer archivos y ponerlos en diccionario
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
#1.6 Ordenar y eliminar del Dataframe
oe_arc= fn.oe(pa=arc,dt=dato_arc)
# 1.7 Jalar precios para la posicion

#dp=fn.pp(ps=ppr,pt=oe_arc,k=k,cc=c)
