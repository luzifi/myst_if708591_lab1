
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: functions.py : python script with general functions                                         -- #
# -- author: YOUR GITHUB USER NAME                                                                       -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: YOUR REPOSITORY URL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""
import pandas as pd
import numpy as np
import time as time
import yfinance as yf
from os import listdir, path
from os.path import isfile, join

# 1.3 Vector de fechas apartir de vector de nombres de archivos
def f_fech(p_arc):
    # Crear vector de fechas apartir del vector de nombres de archivo
    t_f = [i.strftime('%d-%m-%Y') for i in
           sorted([pd.to_datetime(i[8:]).date() for i in p_arc])]
    # Lista de fechas ordenadas (para usarse con indexadores de archivos)
    i_f = [j.strftime('%Y-%m-%d') for j in sorted([pd.to_datetime(i[8:]).date() for i in p_arc])]
    r_f= {'i_f': i_f, 't_f': t_f}
    return r_f
# 1.4 Vector de fechas apartir de YF
def gt(pa,dt):
    # Descargar y acomodar datos
    tickers = []
    for i in pa:
        i = pa[0]
        l_tickers = list(dt[i]['Ticker'])
        [tickers.append(i + '.MX') for i in l_tickers]
    global_tickers = np.unique(tickers).tolist()
    # Remplazar en lista global_tickers
    global_tickers = [i.replace('GFREGIOO.MX', 'RA.MX') for i in global_tickers]
    global_tickers = [i.replace('MEXCHEM.MX', 'ORBIA.MX') for i in global_tickers]
    global_tickers = [i.replace('LIVEPOLC.1.MX', 'LIVEPOLC-1.MX') for i in global_tickers]
    # KOFL.MX, KOFUBL.MX, USD.MXN, y BSMXB.MX
    # Se eliminan los activos para dejarlos como cash
    [global_tickers.remove(i) for i in ['BSMXB.MX']]
    [global_tickers.remove(i) for i in ['KOFL.MX']]
    [global_tickers.remove(i) for i in ['MXN.MX']]

    return global_tickers
def pr(gt,iif):
    # Descarga de datos historicos de YF
    inicio = time.time()
    dato = yf.download(gt, start="2017-08-21", end="2020-08-24", actions=False,
                       group_by="close", interval='1d', auto_adjust=False, prepost=False, threads=True)
    # print('se tardo', time.time() - inicio, 'segundos')
    # Convertir columna a datos por activo de precios
    da_clo = pd.DataFrame({i: dato[i]['Close'] for i in gt})
    # Tomar solo fechas de interes  (utilizando teoria de conjuntos )
    ic_fech = sorted(list(set(da_clo.index.astype(str).tolist()) & set(iif)))
    precios = da_clo.iloc[[int(np.where(da_clo.index.astype(str) == i)[0]) for i in ic_fech]]
    # Ordenar columnas lexicograficamente
    precios = precios.reindex(sorted(precios.columns), axis=1)

    return precios

