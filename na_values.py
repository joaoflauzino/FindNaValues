import pandas as pd
import numpy as np

df = pd.read_csv('CC GENERAL.csv', sep = ",")
columns = df.select_dtypes(include=['float64', 'int64']).columns

if name == "main":
    print('Checando existência de colunas nulas.')
    print('--------------------------')
    print(df.isnull().sum())

    for i, v in enumerate(columns):
        df[v] = df[v].apply(lambda x: df[v].mean() if np.isnan(x) else x)
                                        
    print(' \n Validando se ainda existe colunas nulas.')
    print('--------------------------')
    print(df.isnull().sum())
