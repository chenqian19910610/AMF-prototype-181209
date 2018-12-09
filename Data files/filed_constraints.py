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

df_constraints = df_data_excel('Project1.xlsx','Task_Data',{'Task_Name':str,'Duration':str,'Start_Date':str,'Finish_Date':str,
                                                   'Baseline_Start':str,'Baseline_Finish':str,'Actual_Start':str, 'Actual_Finish':str})
df_constraints = df_constraints.drop([0])
df_constraints = df_constraints.reset_index()
df_constraints.columns = df_constraints.columns.str.strip().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
df_constraints = df_constraints[['Task_Name']]
df_constraints = df_constraints.rename(columns={'Task_Name':'task_ID'})

index_milestone = []
for i in range(len(df_constraints)):
    if 'milestone' in df_constraints.loc[i,'task_ID']:
        index_milestone.append(i)

df_constraints = df_constraints.drop(index_milestone)
df_constraints = df_constraints.reset_index(drop=True)
for i in range(len(df_constraints)):
        df_constraints.loc[i,'takt_Zone'] = str(df_constraints.loc[i,'task_ID'])[6:]


df_constraints['space_prep'] = pd.Series(['100' for i in range(len(df_constraints))],index=df_constraints.index)
df_constraints['machine_prep'] = pd.Series(['100' for i in range(len(df_constraints))],index=df_constraints.index)
df_constraints['labor_prep'] = pd.Series(['100' for i in range(len(df_constraints))],index=df_constraints.index)
df_constraints['precedentials'] = pd.Series(['Removed' for i in range(len(df_constraints))],index=df_constraints.index)
df_constraints['permits'] = pd.Series(['100' for i in range(len(df_constraints))],index=df_constraints.index)

df_constraints.to_sql('construction_constraints',conn, if_exists='replace',index=False)  # remove index as a separate column

cur.close()
conn.close()