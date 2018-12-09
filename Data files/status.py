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

df_status = pd.read_sql_query('select * from changes_field',conn)
df_status.columns = df_status.columns.str.strip().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

df_status = df_status[['element_ID']]
df_status['status'] = pd.Series([ ' ' for i in range(len(df_status))],index=df_status.index)

df_status.to_sql('status',conn, if_exists='replace',index=False)  # remove index as a separate column

cur.close()
conn.close()