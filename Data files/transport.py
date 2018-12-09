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

df_transport = pd.read_sql_query('select * from manufacturing_process',conn)
df_transport.columns = df_transport.columns.str.strip().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

df_transport = df_transport[['order_ID']]
df_transport['t_leadtime'] = pd.Series([ '0.5' for i in range(len(df_transport))],index=df_transport.index)
# df_transport['release_for_transport_day'] = pd.Series([ ' ' for i in range(len(df_transport))],index=df_transport.index)
# df_transport['driver_name'] = pd.Series([ ' ' for i in range(len(df_transport))],index=df_transport.index)
df_transport['current_location'] = pd.Series([ ' ' for i in range(len(df_transport))],index=df_transport.index)
df_transport['vehicle'] = pd.Series([ ' ' for i in range(len(df_transport))],index=df_transport.index)
df_transport['unloading_location'] = pd.Series([ 'Andreasstrasse 15 8046 Zurich' for i in range(len(df_transport))],index=df_transport.index)


df_tasks = pd.read_sql_query('select * from Tasks',conn)
df_tasks['Start_Date']=pd.to_datetime(df_tasks['Start_Date'])

df_takeoffs = pd.read_sql_query('select * from Structural_Column_Material_Takeoff',conn)
for i in range(len(df_takeoffs)):
    for j in range(len(df_tasks)):
        if df_takeoffs.loc[i,'task_ID'] == df_tasks.loc[j,'task_ID']:
            df_takeoffs.loc[i,'need_date'] = df_tasks.loc[j,'Start_Date']

for i in range(len(df_takeoffs)):
    for j in range(len(df_transport)):
        if df_transport.loc[j,'order_ID'] == df_takeoffs.loc[i,'order_ID']:
            df_transport.loc[j, 'release_for_transport_day'] = df_takeoffs.loc[i,'need_date'] - timedelta(float(df_transport.loc[j,'t_leadtime']))


df_transport.to_sql('transport_process',conn, if_exists='replace',index=False)
cur.close()
conn.close()