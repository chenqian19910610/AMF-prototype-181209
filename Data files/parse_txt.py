import numpy as np
import pandas as pd


# widen the output prints
# pd.set_option('display.height',1000)
pd.set_option('display.max_columns',500)
# pd.set_option('display.max_rows',1000)
# pd.set_option('display.width',1000)

# read data from the text files, make sure the text file is saved as 'utf-8' encoded
def df_data_txt(file_name):
    df = pd.read_csv(file_name,sep='\t',engine='python',header=None)
    df = df.drop([0])
    df = df.drop([1])
    df = df.reset_index()
    df = df.drop(['index'],axis=1)
    return df

df_takeoff_col = df_data_txt('Structural Column Material Takeoff.txt')
df_takeoff_col = df_takeoff_col.rename(columns={0:"element ID",1:"Family",2:"Type",3:"Material: Name",
                               4:"Material: Volume",5:"Length",6:"load-bearing capacity",
                               7:"Base Level",8:"Column Location Mark",9:"Count",10:"task ID",11:"order ID",12:"RFID"})
df_takeoff_col.columns = df_takeoff_col.columns.str.strip().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')