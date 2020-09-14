
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: main.py : python script with the main functionality                                         -- #
# -- author: YOUR GITHUB USER NAME                                                                       -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: YOUR REPOSITORY URL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""
import  functions as fn
from data import  arc
from data import dato_arc
import pandas as pd
import  numpy as np
# data. py
# ---------------------------------------Paso 1: Datos------------------------------------------------------
# 1.1 Lista de archivos a importar
# 1.2 Leer archivos y ponerlos en diccionario

# functions.py
# 1.3 Vector de fechas apartir de vector de nombres de archivos
fechas= fn.f_fech(p_arc=arc)
# 1.4 Vector de tickers apartir de YF
gti= fn.gt(pa=arc,dt=dato_arc)
# 1.5 Descarga y orden de datos historicos
ppr= fn.pr(gt=gti,iif=fechas['i_f'])

#main.py
#1.6 Posicion inicial
# Posicion inicial
# Capital inicial
k = 1000000
# Comisiones
c = .00125
#dato_arc[arc[0]]['Peso (%)']
# Vector de comisiones historicas.
comisiones = []
# Diccionario como resultdo final
inv_pasiva = {'tinestamp': ['05-01-2018'], 'capital': [k]}

# functions.py
# 1.7 Ordenar y eliminar del Dataframe
oe_arc= fn.oe(pa=arc,dt=dato_arc)

# 1.8 Jalar precios para la posicion inicial
dp=fn.pp(ps=ppr,pt=oe_arc,k=k,cc=c)

# main.py
# 1.9 Evolucion de la posicion (Inversion Pasiva)
for l in [np.arange(0,32,1)]:
    po= np.array(ppr.iloc[l, [i in dp['Ticker'].to_list() for i in ppr.columns.to_list()]])

for h in [np.arange(0,32,1)]:
    #Valor de la posicion de cada activo en todos los meses
    pad=np.transpose(np.array(oe_arc['Titulos'])*po[h])
    o=pd.DataFrame(pad)
    df_pasiva= pd.DataFrame()
    df_pasiva['Capital']= o[h].sum()
    # no se pudo eliminar nan
    df_pasiva['rend']=((df_pasiva['Capital']/df_pasiva['Capital'].shift(1))-1).dropna()
    df_pasiva['rend_acum']= (df_pasiva['rend'].cumsum()).dropna()


# visualizations.py
#1.10 Visualizacion de la evolucion del capital
# Grafica evolucion de capital
print(df_pasiva)

