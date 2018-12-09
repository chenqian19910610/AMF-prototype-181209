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


df_takeoff_col=pd.read_sql_query('select * from "Structural_Column_Material_Takeoff"', conn)
df_takeoff_col.columns = df_takeoff_col.columns.str.strip().str.replace('_',' ')   # column name messy up with spaces. https://medium.com/@chaimgluck1/working-with-pandas-fixing-messy-column-names-42a54a6659cd
print(df_takeoff_col.dtypes)
writer_dynamo=pd.ExcelWriter('Takeoff.xlsx',engine='xlsxwriter')
df_takeoff_col.to_excel(writer_dynamo, sheet_name='Columns',index=False)
writer_dynamo.save()

cur.close()
conn.close()