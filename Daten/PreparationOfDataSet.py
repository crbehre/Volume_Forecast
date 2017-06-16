# -*- coding: utf-8 -*-
# change working directory
import os
os.chdir('C:\\Users\\alexander.henssen\Documents\Studium\DHL Projekt Data Mining')
import pandas as pd
# import original data set int frame and filter to IN SCOPE instances
df=pd.read_csv('RawData_SecFC.csv',sep=';')
dfs=df[df['IN_SCOPE'] != 0]
# read csv with key and create dictionary
key=pd.read_csv('Key_SecFC.csv',sep=';')
keydict=key.set_index('ID_ALT')['ID_NEU'].to_dict() 
# encode dataframe by mapping with keydict
dfsc=dfs.replace(to_replace=keydict)
#set date format
dfsc['SDD']=pd.to_datetime(dfsc.SDD)
#Create csv from Data Frame
dfsc.to_csv('SecFC_InScope_Encoded_Indexed.csv')


