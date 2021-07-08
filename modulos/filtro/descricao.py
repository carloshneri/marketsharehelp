#carregar bibliotecas.
import pandas as pd
import numpy as np
import xlsxwriter
import csv
import openpyxl
from pandas.io.excel import ExcelWriter
from modulos.filtro.blacklist import blacklist

#############################################################################################################
#############################################################################################################

def filtroDescricao(sheet_name, empresa, dataframe):
    df_temp=[]
    for pais in empresa['PAIS DE ORIGEM']:
        if pais != 'FIM':
            print(pais)
            df_temp.append(dataframe[dataframe['PAIS_DE_ORIGEM'].str.contains(pais)])
        else:
            break
    df_pais = pd.concat(df_temp)
    
    df_temp1=[]       
    for produto in empresa['DESCRICAO DO PRODUTO']:
        produto=str(produto)
        print(produto)
        df_temp1.append(df_pais[df_pais['DESCRICAO_DO_PRODUTO'].str.contains(produto)])
    df_filtrada = pd.concat(df_temp1)
        
    df_filtrada = df_filtrada.drop_duplicates()
    
    print('df_fitrada enviada para o Blacklist')
    print(df_filtrada)

    df_black = blacklist(df_filtrada)

    print(df_black)

    input('pause')

    try:
        with ExcelWriter('importações.xlsx', mode='a', engine="openpyxl") as writer:
            df_black.to_excel(writer, sheet_name = sheet_name)
    except:
        df_black.to_excel('importações.xlsx', sheet_name = sheet_name)
    print(sheet_name +'.xlsx'+' criado')
    print('\n')