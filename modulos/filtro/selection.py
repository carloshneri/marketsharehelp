
import pandas as pd
import numpy as np
import xlsxwriter
import csv
import openpyxl
from pandas.io.excel import ExcelWriter
import json

def dataframe(caminho, arquivos, ncms):
    
    with open("json\\cabecalhos\\cabecalho.json") as g:
        cabecalho = json.load(g).get('cabecalho')
    filtro = pd.read_json("json\\filtros\selecao.json", orient= "split")
    titulos = filtro.loc[filtro["selecao"] == "True","titulo"]
    

    
    df_final = pd.DataFrame(columns = titulos)

    for arquivo in arquivos:
        file = caminho + arquivo
        print("abrindo arquivo: " + file)  
        df_temp = pd.read_csv(file, encoding='iso-8859-1', sep ='@', error_bad_lines= False, usecols = titulos, quoting=csv.QUOTE_NONE, names=cabecalho, low_memory=False, skiprows=1)
        df_temp["COD_NCM"] = df_temp['COD_NCM'].astype(str)
        df = df_temp[df_temp["COD_NCM"].isin(ncms)]
        df_final = pd.concat([df_final,df])
        
    
    df_final["DESCRICAO_DO_PRODUTO"]=df_final["DESCRICAO_DO_PRODUTO"].str.upper().str.rstrip()
    df_final["QTD_COMERCIAL"]=pd.to_numeric(df_final["QTD_COMERCIAL"].str.strip().str.replace(',','.'))
    df_final["VALOR_UN_PROD_DOLAR"]=pd.to_numeric(df_final["VALOR_UN_PROD_DOLAR"].str.strip().str.replace(',','.'))
    df_final["TOT_UN_PROD_DOLAR"]=pd.to_numeric(df_final["TOT_UN_PROD_DOLAR"].str.strip().str.replace(',','.'))

    df_final['index'] = df_final.index

    df_final.to_excel('dataframe.xlsx',index=False)
    
    return(df_final)


#####################################################################

