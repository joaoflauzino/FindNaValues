import pandas as pd
import numpy as np
import math

# Read csv
df = pd.read_csv('CC GENERAL.csv', sep = ",", na_values = ['?', '', 'NA'])

columns = df.columns

types_na = {"float64": lambda x: df[x].mean() if math.isnan(x) == True else x, 
         "int64": lambda x: int(df[x].mean()) if math.isnan(x) == True else x,
         "object": lambda x: df[x].mode() if str(x) == None else x}

def check_na_values():
    for i in columns:
        df[i] = df[i].apply(types_na[str(df[i].dtype)])
    
    print(df.isnull().sum())

if __name__ == "__main__":

    check_na_values()

