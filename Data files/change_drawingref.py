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

df_draw_ref = pd.read_sql_query('select * from changes_field',conn)
df_draw_ref.columns = df_draw_ref.columns.str.strip().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')


df_draw_ref = df_draw_ref[['element_ID']]
df_draw_ref['A_changes_ref'] = pd.Series([ '' for i in range(len(df_draw_ref))],index=df_draw_ref.index)  # the reference link has a naming with name of responsible person and date
df_draw_ref['E_changes_ref'] = pd.Series(['' for i in range(len(df_draw_ref))],index=df_draw_ref.index)
df_draw_ref['P_changes_ref'] = pd.Series(['' for i in range(len(df_draw_ref))],index=df_draw_ref.index)


df_draw_ref.to_sql('drawings_sum',conn, if_exists='replace',index=False)  # remove index as a separate column

cur.close()
conn.close()