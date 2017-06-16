# -*- coding: utf-8 -*-
import pandas as pd
df=pd.read_csv('C:\\Users\\alexander.henssen\Dropbox\M2.5_LogSCM_Projekte_mit_der_Industrie\Daten\Originaldaten\SecFC_InScope_Encoded_Indexed.csv',index_col=0)
df['SDD']=pd.to_datetime(df.SDD) #casts datetime format on SDD
df['SDDWD']=df.SDD.dt.dayofweek #creates new attribute from SDD: Weekday (Mon == 0 , Sun == 6)
df['SDDWOY']=df.SDD.dt.weekofyear #creates new attribute from SDD: Calendar week of SDD
df['Y']=df.SDD.dt.year #creates new attribute from SDD: Year of SDD
df['DOBB']=pd.to_numeric(df.SDD) #creates new attribute from SDD: Distance from DateOfBigBang = 1.1.1970 in s*10**(-9)

    



