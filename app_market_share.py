#carregar bibliotecas.
import pandas as pd
import numpy as np
import xlsxwriter
import csv
import openpyxl
from pandas.io.excel import ExcelWriter
import json
from modulos.filtro.selection import dataframe
from modulos.filtro.descricao import filtroDescricao
import os

with open("json\\constantes\\constantes.json") as f:
    constantes = json.load(f)
    diretoriocsv = constantes.get("diretorios").get("csv")

df_ncms = pd.read_excel("json\\filtros\\ncm.xlsx")
ncms = [str(ncm) for ncm in df_ncms['ncms']]

arquivos = os.listdir("base de dados\CSV")

## Criação do DataFrame

dataframe = dataframe(diretoriocsv, arquivos, ncms)

sheet_names = pd.ExcelFile('json\market share\market_share.xlsx')

for sheet_name in sheet_names.sheet_names:
    print(sheet_name)
    empresa = pd.read_excel('json\market share\market_share.xlsx', sheet_name = sheet_name)
    filtroDescricao(sheet_name, empresa, dataframe)

