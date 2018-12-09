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

# read data from the excel/csv files
def df_data_excel(excelname, sheetname, converter):
    df = pd.read_excel(str(excelname),sheet_name=sheetname, skiprows=0, converters=converter)
    return df


# task information
df_task = df_data_excel('Project1.xlsx','Task_Data',{'Task_Name':str,'Duration':str,'Start_Date':str,'Finish_Date':str,
                                                   'Baseline_Start':str,'Baseline_Finish':str,'Actual_Start':str, 'Actual_Finish':str})
df_task = df_task.drop([0])
df_task = df_task.drop(['Duration'],axis=1)
df_task['Update']=pd.Series(['0' for i in range(len(df_task))],index=df_task.index)
# df_task=df_task.drop(columns=['ID','Active','Task_Mode','Predecessors','Resource_Names','Percent_Complete'])
# print(df_task)
# print(df_task.dtypes)
# print(df_task.shape)



df_task = df_task.rename(columns={'Task_Name':'task_ID'})
df_task.to_sql('Tasks',conn,if_exists='replace', index=False)   # remove index as a separate column



# material takeoff information
df_takeoff_col=df_data_excel('Takeoff_Dyn.xlsx','Columns',{"element ID":str,"Family":str,"Type":str,"Material: Name":str,
                                                       "Material: Volume":str,"Length":str,"load-bearing capacity":float,
                                                       "Base Level":str,"Column Location Mark":str,"Count":int,"task ID":str,"order ID":str,"RFID":str})
# print(df_takeoff.columns)
df_takeoff_col.columns = df_takeoff_col.columns.str.strip().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

df_takeoff_col.to_sql('Structural_Column_Material_Takeoff',conn, if_exists='replace',index=False)  # remove index as a separate column

# df_takeoff_col = pd.read_sql_query('select * from "Structural_Column_Material_Takeoff"', conn)
# df_takeoff_col['new'] = pd.Series([1 for i in range(len(df_takeoff_col))],index=df_takeoff_col.index)

# df_takeoff_col.to_sql('Structural_Column_Material_Takeoff',conn,if_exists='replace', index=False)
# df_takeoff_col = df_takeoff_col.drop(columns=['index'])  # 从sql读取数据的时候会自动添加index (如果index=True)

cur.close()
conn.close()