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

df_supplies = pd.read_sql_query('select * from type_tracking',conn)
df_supplies.columns = df_supplies.columns.str.strip().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
df_supplies = df_supplies.drop(columns=['Count'])

for i in range(len(df_supplies)):
    if df_supplies.loc[i,'Type'] == 'STB 50/50 cm, Concrete C30/37, insitu':
        df_supplies.loc[i, 'catalogue_ID'] = '004_C30/37'
    if df_supplies.loc[i,'Type'] == 'STB 50/50 cm, Concrete C50/60, insitu':
        df_supplies.loc[i, 'catalogue_ID'] = '004_C50/60'
    if df_supplies.loc[i,'Type'] == 'STB 55/50 cm, Concrete C30/37, insitu':
        df_supplies.loc[i, 'catalogue_ID'] = '005'
    if df_supplies.loc[i,'Type'] == 'STB 60/55 cm, Concrete C50/60, insitu':
        df_supplies.loc[i, 'catalogue_ID'] = '013_C50/60'
    if df_supplies.loc[i,'Type'] == 'STB 60/60 cm, Concrete C30/37, insitu':
        df_supplies.loc[i, 'catalogue_ID'] = '014_C30/37'
    if df_supplies.loc[i,'Type'] == 'STB 65/55 cm, Concrete C50/60, insitu':
        df_supplies.loc[i, 'catalogue_ID'] = '006_C50/60'
    if df_supplies.loc[i,'Type'] == 'STB 65/65 cm, Concrete C30/37, insitu':
        df_supplies.loc[i, 'catalogue_ID'] = '009_C30/37'
    if df_supplies.loc[i,'Type'] == 'STB 15/15 cm,  prefab.':
        df_supplies.loc[i, 'catalogue_ID'] = '008'
    if df_supplies.loc[i,'Type'] == 'STB 24/24 cm,  prefab.':
        df_supplies.loc[i, 'catalogue_ID'] = '001'
    if df_supplies.loc[i,'Type'] == 'STB 25/25 cm,  prefab.':
        df_supplies.loc[i, 'catalogue_ID'] = '007'
    if df_supplies.loc[i,'Type'] == 'STB 30/30 cm,  prefab.':
        df_supplies.loc[i, 'catalogue_ID'] = '002'
    if df_supplies.loc[i,'Type'] == 'STB 35/35 cm,  prefab.':
        df_supplies.loc[i, 'catalogue_ID'] = '011'
    if df_supplies.loc[i,'Type'] == 'STB 40/40 cm,  prefab.':
        df_supplies.loc[i, 'catalogue_ID'] = '012'
    if df_supplies.loc[i,'Type'] == 'STB 45/45 cm,  prefab.':
        df_supplies.loc[i, 'catalogue_ID'] = '003'
    if df_supplies.loc[i,'Type'] == 'STB 55/55 cm, prefab.':
        df_supplies.loc[i, 'catalogue_ID'] = '010'
    if df_supplies.loc[i,'Type'] == 'STB 65/65 cm,  prefab.':
        df_supplies.loc[i, 'catalogue_ID'] = '009'
    if df_supplies.loc[i,'Type'] == 'STB d=70cm, Concrete C50/60 prefab.':
        df_supplies.loc[i, 'catalogue_ID'] = '100'
    else:
        pass

print(df_supplies)

df_supplies.to_sql('supplier_catalogue',conn, if_exists='replace',index=False)  # remove index as a separate column


cur.close()
conn.close()