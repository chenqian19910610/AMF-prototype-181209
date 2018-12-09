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

df_changes_sd = pd.read_sql_query('Select * from changes_field',conn)


df_changes_sd.columns = df_changes_sd.columns.str.strip().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
df_changes_sd = df_changes_sd[['element_ID']]
df_changes_sd['prod_changes_dcp'] = pd.Series(['None' for i in range(len(df_changes_sd))],index=df_changes_sd.index)      # None and 0000 are default value for no change orders occuring
df_changes_sd['request_dept'] = pd.Series([' ' for i in range(len(df_changes_sd))],index=df_changes_sd.index)
df_changes_sd['request_date'] = pd.Series([' ' for i in range(len(df_changes_sd))],index=df_changes_sd.index)
df_changes_sd['request_ID'] = pd.Series(['0000' for i in range(len(df_changes_sd))],index=df_changes_sd.index)
df_changes_sd['request_category'] = pd.Series([' ' for i in range(len(df_changes_sd))],index=df_changes_sd.index)
df_changes_sd['change_status'] = pd.Series([' ' for i in range(len(df_changes_sd))],index=df_changes_sd.index)

df_changes_sd.to_sql('changes_production',conn, if_exists='replace',index=False)  # remove index as a separate column

cur.close()
conn.close()