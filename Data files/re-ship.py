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

df_reship = pd.read_sql_query('select * from inspection',conn)
df_reship.columns = df_reship.columns.str.strip().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')


df_reship = df_reship[['RFID','Family','Type']]
df_reship['replacement'] = pd.Series([ ' ' for i in range(len(df_reship))],index=df_reship.index)
df_reship['reship_date'] = pd.Series([ ' ' for i in range(len(df_reship))],index=df_reship.index)
df_reship['reship_supplier'] = pd.Series([ ' ' for i in range(len(df_reship))],index=df_reship.index)

df_reship.to_sql('reship',conn, if_exists='replace',index=False)  # remove index as a separate column

cur.close()
conn.close()