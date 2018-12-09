import numpy as np
import pandas as pd
import sqlite3
import csv
from datetime import timedelta

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

df_production = df_data_excel('Takeoff.xlsx','Columns',{"element ID":str,"Family":str,"Type":str,"Material: Name":str,
                                                       "Material: Volume":str,"Length":str,"load-bearing capacity":float,
                                                       "Base Level":str,"Column Location Mark":str,"Count":int,"task ID":str,"order ID":str,"RFID":str})
df_production.columns = df_production.columns.str.strip().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')


df_production = df_production[['order_ID','Family','Type']]
df_production['supplier_name'] = pd.Series([ 'SACAC' for i in range(len(df_production))],index=df_production.index)

df_production['production_run'] = pd.Series([ ' ' for i in range(len(df_production))],index=df_production.index)

df_production['m_leadtime'] = pd.Series([ '5' for i in range(len(df_production))],index=df_production.index)
df_production['Actual_release_date'] = pd.Series([ ' ' for i in range(len(df_production))],index=df_production.index)
df_production['release_for_production_day'] = pd.Series([ '2018-01-01 08:00:00' for i in range(len(df_production))],index=df_production.index)




df_transport = pd.read_sql_query('select * from transport_process',conn)
df_transport['release_for_transport_day'] = pd.to_datetime(df_transport['release_for_transport_day'])

# for i in range(len(df_production)):
#     for j in range(len(df_transport)):
#         if df_production.loc[i, 'order_ID'] == df_transport.loc[j, 'order_ID']:
#             df_production.loc[i, 'release_for_production_day'] = df_transport.loc[j, 'release_for_transport_day'] - timedelta(float(df_production.loc[i, 'm_leadtime']))


df_production.to_sql('manufacturing_process',conn, if_exists='replace',index=False)  # remove index as a separate column

cur.close()
conn.close()