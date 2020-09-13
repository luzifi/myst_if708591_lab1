
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
# data. py
# ---------------------------------------Paso 1: Datos------------------------------------------------------
# 1.1 Lista de archivos a importar
# 1.2 Leer archivos y ponerlos en diccionario

# functions.py
# 1.3 Vector de fechas apartir de vector de nombres de archivos
fechas= fn.f_fech(p_arc=arc)
# 1.4 Vector de fechas apartir de YF
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
dato_arc[arc[0]]['Peso (%)']
# Vector de comisiones historicas.
comisiones = []
# Diccionario como resultdo final
inv_pasiva = {'tinestamp': ['05-01-2018'], 'capital': [k]}
#1.7 Evaluacion de la posicion (inversion pasiva)

# visualizations.py
#1.8 Visualizacion de la evolucion del capital
# Grafica evolucion de capital