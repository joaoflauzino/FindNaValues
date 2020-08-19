import pandas as pd
import numpy as np

df = pd.read_csv('CC GENERAL.csv', sep = ",")
columns = df.columns 
types_na = {"float64": lambda x: df[x].mean() if np.isnan(x) else x, 
         "int64": lambda x: int(df[x].mean()) if np.isnan(x) else x, 
         "object": lambda x: df[x].mode() if str(x) == 'nan' else x}

types_na_str = {"float64": lambda x: df[x].mean() if x == 0 else x, 
         "int64": lambda x: int(df[x].mean()) if x == 0 else x, 
         "object": lambda x: df[x].mode() if str(x) == '0' else x}

def check_na_values():
    for i, v in enumerate(columns):
        df[v] = df[v].apply(types[str(df[v].dtype)])

    return df.isnull().sum()

def check_na_values_as_string():
    for i, v in enumerate(columns):
        df[v] = df[v].apply(lambda x: '0' if x == '?' else x)

        try:
            df[v] = df[v].astype(float)
        except:
            try:
                df[v] = df[v].astype(int)
            except:
                df[v] = df[v].astype(str)
        
        df[v] = df[v].apply(types[str(df[v].dtype)])

        return df.isnull().sum() 
        

if __name__ == "__main__":

    pass

    
                                       
