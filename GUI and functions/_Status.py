import datetime
from datetime import timedelta
import pandas as pd
import sqlite3
from tkinter import messagebox
from tkinter import *



pd.set_option('display.max_columns', 500)

conn = sqlite3.connect(
    'C:\\Users\\chenqi\\polybox\\Qian\\1 Doctoral Research\\16.02-AMF\\P6 GUI development\\data\\Aturm.sqlite')
cur = conn.cursor()


df_ETOs= pd.read_sql_query('select * from Structural_Column_Material_Takeoff', conn)
df_tasks= pd.read_sql_query('select * from Tasks', conn)
df_tasks['Start_Date'] = pd.to_datetime(df_tasks['Start_Date'])
df_transport = pd.read_sql_query('select * from transport_process', conn)
df_transport['release_for_transport_day'] = pd.to_datetime(df_transport['release_for_transport_day'])
df_manufacture = pd.read_sql_query('select * from manufacturing_process', conn)
df_manufacture['release_for_production_day'] = pd.to_datetime(df_manufacture['release_for_production_day'])


test_today = df_tasks.loc[10,'Start_Date']

# import pytz
# today_datetime = datetime.datetime.now(pytz.timezone('Europe/Zurich'))
# today_datetime = str(today_datetime)
# today_datetime = pd.to_datetime(today_datetime[:19])
# print(today_datetime > test_today)

# for i in range(len(df_ETOs)):                                     # The for-for-for makes the pandas too slow to read data!!!!!!!!!! breakdown the strutcure into separate pieces
#     for j in range(len(df_manufacture)):
#         for k in range(len(df_transport)):
#             if df_ETOs.loc[i, 'order_ID'] == df_manufacture.loc[j, 'order_ID'] and df_ETOs.loc[i, 'order_ID'] == \
#                     df_transport.loc[k, 'order_ID']:
#                 df_ETOs.loc[i, 'rel_transport'] = df_transport.loc[k, 'release_for_transport_day']
#                 df_ETOs.loc[i, 'rel_manufacture'] = df_manufacture.loc[j, 'release_for_production_day']
#                 if df_ETOs.loc[i, 'rel_manufacture'] <= test_today and df_ETOs.loc[i, 'rel_transport'] > test_today:
#                     print('2')
#                     df_ETOs.loc[i, 'Status'] = 'wait for delivery - store in consolidation center'
#                 elif df_ETOs.loc[i, 'rel_manufacture'] > test_today:
#                     print('3')
#                     df_ETOs.loc[i, 'Status'] = 'wait for manufacture - design coordination'
#                 elif df_ETOs.loc[i, 'rel_manufacture'] == test_today:
#                     print('4')
#                     df_ETOs.loc[i, 'Status'] = 'release for manufacture - design freeze'
#                 elif df_ETOs.loc[i, 'rel_transport'] == test_today:
#                     print('5')
#                     df_ETOs.loc[i, 'Status'] = 'release for delivery'
#                 elif df_ETOs.loc[i, 'rel_transport'] <= test_today:
#                     print('6')
#                     df_ETOs.loc[i, 'Status'] = 'onsite'
#                 else:
#                     pass
#             else:
#                 pass


for i in range(len(df_ETOs)):
    for j in range(len(df_transport)):
        if df_ETOs.loc[i, 'order_ID'] == df_transport.loc[j, 'order_ID']:
            df_ETOs.loc[i, 'rel_transport'] = df_transport.loc[j, 'release_for_transport_day']
        else:
            pass

for i in range(len(df_ETOs)):
    for j in range(len(df_manufacture)):
        if df_ETOs.loc[i, 'order_ID'] == df_manufacture.loc[j, 'order_ID']:
            df_ETOs.loc[i, 'rel_manufacture'] = df_manufacture.loc[j, 'release_for_production_day']
        else:
            pass


for i in range(len(df_ETOs)):
    if df_ETOs.loc[i, 'rel_manufacture'] <= test_today and df_ETOs.loc[i, 'rel_transport'] > test_today:
        df_ETOs.loc[i, 'Status'] = 'wait for delivery - store in consolidation center'
    elif df_ETOs.loc[i, 'rel_manufacture'] > test_today:
        df_ETOs.loc[i, 'Status'] = 'wait for manufacture - design coordination'
    elif df_ETOs.loc[i, 'rel_manufacture'] == test_today:
        df_ETOs.loc[i, 'Status'] = 'release for manufacture - design freeze'
    elif df_ETOs.loc[i, 'rel_transport'] == test_today:
        df_ETOs.loc[i, 'Status'] = 'release for delivery'
    elif df_ETOs.loc[i, 'rel_transport'] <= test_today:
        df_ETOs.loc[i, 'Status'] = 'onsite'
    else:
        pass

