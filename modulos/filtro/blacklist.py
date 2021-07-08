
import pandas as pd
import numpy as np
import xlsxwriter
import csv

def blacklist(dataframe):
    
    blacklist = pd.read_excel('json\\black list\\black list.xlsx')
    indexNames=[]
    for black in blacklist['blacklist']:
        #df.index[df['BoolCol']].tolist()
        indexNames = dataframe[dataframe['DESCRICAO_DO_PRODUTO'].str.contains(str(black))]
        print(indexNames)
        # Delete these row indexes from dataFrame
           
        if len(indexNames) != 0:
            dataframe = dataframe.drop(indexNames.index)
        else:
            pass

    print(dataframe)
    return(dataframe)

