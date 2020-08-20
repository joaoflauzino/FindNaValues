import pandas as pd
import numpy as np
import math

# Read csv
df = pd.read_csv('CC GENERAL.csv', sep = ",", na_values = ['?', '', 'NA'])

columns = df.columns

def check_float(x, column):
    if pd.isnull(x):
        print('if')
        return df[column].mean()
    else:
        return x

def check_int(x, column):
    if pd.isnull(x):
        return int(df[column].mean())
    else:
        return x

def check_object(x, column):
    if pd.isnull(x):
        return df[column].mode()
    else:
        return x

 

def check_na_values():
    for i in columns:
        for j, k in enumerate(df[i]):  
            if pd.isnull(k): #if k is None: #if math.isnan(x):#if np.isnan(x): 
                if str(df[i].dtype) == 'int64':
                    df[i] = df[i].apply(lambda x: check_int(x, i))
                elif str(df[i].dtype) == 'float64':
                    df[i] = df[i].apply(lambda x: check_float(x, i))
                elif str(df[i].dtype) == 'object':
                    df[i] = df[i].apply(lambda x: check_object(x, i))
                
    print(df.isnull().sum())

if __name__ == "__main__":

    check_na_values()

