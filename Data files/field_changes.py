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

df_changes_field = df_data_excel('Takeoff.xlsx', 'Columns',{"element ID":str,"Family":str,"Type":str,"Material: Name":str,
                                                       "Material: Volume":str,"Length":str,"load-bearing capacity":float,
                                                       "Base Level":str,"Column Location Mark":str,"Count":int,"task ID":str,"order ID":str,"RFID":str})


df_changes_field.columns = df_changes_field.columns.str.strip().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
df_changes_field = df_changes_field[['element_ID']]
df_changes_field['field_changes_dcp'] = pd.Series([ 'None' for i in range(len(df_changes_field))],index=df_changes_field.index)
df_changes_field['request_dept'] = pd.Series(['' for i in range(len(df_changes_field))],index=df_changes_field.index)
df_changes_field['request_date'] = pd.Series(['' for i in range(len(df_changes_field))],index=df_changes_field.index)
df_changes_field['request_ID'] = pd.Series(['0000' for i in range(len(df_changes_field))],index=df_changes_field.index)
df_changes_field['request_category'] = pd.Series(['' for i in range(len(df_changes_field))],index=df_changes_field.index)
df_changes_field['change_status'] = pd.Series(['' for i in range(len(df_changes_field))],index=df_changes_field.index)


df_changes_field.to_sql('changes_field',conn, if_exists='replace',index=False)  # remove index as a separate column

cur.close()
conn.close()