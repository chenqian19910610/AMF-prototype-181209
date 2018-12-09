import numpy as np
import pandas as pd
import sqlite3
import csv

conn=sqlite3.connect('Aturm.sqlite')
cur=conn.cursor()


# widen the output prints
# pd.set_option('display.height',1000)
pd.set_option('display.max_columns',500)
# pd.set_option('display.max_rows',1000)
# pd.set_option('display.width',1000)

# read data from the excel/csv files
def df_data_excel(excelname, sheetname, converter):
    df=pd.read_excel(str(excelname),sheet_name=sheetname, skiprows=0, converters=converter)
    return df

df_inspection = df_data_excel('Takeoff.xlsx','Columns',{"element ID":str,"Family":str,"Type":str,"Material: Name":str,
                                                       "Material: Volume":str,"Length":str,"load-bearing capacity":float,
                                                       "Base Level":str,"Column Location Mark":str,"Count":int,"task ID":str,"order ID":str,"RFID":str})
df_inspection.columns = df_inspection.columns.str.strip().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')


df_inspection = df_inspection[['RFID','Family','Type']]
df_inspection['quality_check'] = pd.Series([ ' ' for i in range(len(df_inspection))],index=df_inspection.index)
df_inspection['certification'] = pd.Series([ ' ' for i in range(len(df_inspection))],index=df_inspection.index)
df_inspection['defect'] = pd.Series([ ' ' for i in range(len(df_inspection))],index=df_inspection.index)
df_inspection['defect_transport'] = pd.Series([ ' ' for i in range(len(df_inspection))],index=df_inspection.index)

df_inspection.to_sql('inspection',conn, if_exists='replace',index=False)  # remove index as a separate column

cur.close()
conn.close()