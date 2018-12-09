import numpy as np
import pandas as pd
import sqlite3

conn=sqlite3.connect('Aturm.sqlite')
cur=conn.cursor()


# widen the output prints
# pd.set_option('display.height',1000)
pd.set_option('display.max_columns',500)
# pd.set_option('display.max_rows',1000)
# pd.set_option('display.width',1000)

df_order_control = pd.read_sql_query('select * from Structural_Column_Material_Takeoff',conn)
df_order_control.columns = df_order_control.columns.str.strip().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')


df_gpbyorder = df_order_control.groupby(['task_ID','order_ID']).count()
df_gpbyorder = df_gpbyorder.reset_index()
df_gpbyorder = df_gpbyorder[['task_ID','order_ID', 'Count']]


df_gpbytyp = df_order_control.groupby(['Family','Type']).count()
df_gpbytyp = df_gpbytyp.reset_index()
df_gpbytyp = df_gpbytyp[['Family','Type', 'Count']]


df_gpbyorder.to_sql('order_tracking',conn, if_exists='replace',index=False)  # remove index as a separate column
df_gpbytyp.to_sql('type_tracking',conn, if_exists='replace',index=False)  # remove index as a separate column


cur.close()
conn.close()