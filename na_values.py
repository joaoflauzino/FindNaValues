import pandas as pd
import numpy as np

df = pd.read_csv('CC GENERAL.csv', sep = ",", na_values = ['?', '', 'NA'])
columns = df.columns 
types_na = {"float64": lambda x: df[x].mean() if np.isnan(x) else x, 
         "int64": lambda x: int(df[x].mean()) if np.isnan(x) else x, 
         "object": lambda x: df[x].mode() if str(x) == 'nan' else x}

def check_na_values():
    for i, v in enumerate(columns):
        df[v] = df[v].apply(types_na[str(df[v].dtype)])

    print(df.isnull().sum())

if __name__ == "__main__":

    check_na_values()

    
                                       
