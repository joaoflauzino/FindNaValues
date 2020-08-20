import pandas as pd
import numpy as np
import argparse

def get_args():
    
  parser = argparse.ArgumentParser()
  parser.add_argument(
      '-filename',
      default = 'CC GENERAL copy.csv',
      type = str,
      help = 'name of file that will be worked')
  parser.add_argument(
      '-sep',
      default = ',',
      help = 'column identifier')
  parser.add_argument(
      '-dec',
      default = '.',
      help = 'decimal identifier')
  parser.add_argument(
      '-navalues',
      default = ['?', '', 'NA'],
      nargs = '+',
      help = 'list will be considered as null values'
  )

  return parser.parse_args()

def replace_na_values(df):
    
    columns = df.columns
    for i in columns:
        for j, k in enumerate(df[i]):  
            if pd.isnull(k): #if k is None: #if math.isnan(x):#if np.isnan(x): 
                if str(df[i].dtype) == 'int64':
                    df[i] = df[i].apply(lambda x: int(df[i].mean()))
                elif str(df[i].dtype) == 'float64':
                    df[i] = df[i].apply(lambda x: df[i].mean())
                else:
                    df[i] = df[i].apply(lambda x: df[i].mode()[0])            
    return df

if __name__ == "__main__":
    
    args = get_args()
    df = pd.read_csv(r'input/' + args.filename, sep=args.sep, decimal=args.dec, na_values=args.navalues)
    df_replaced = replace_na_values(df)
    df_replaced.to_csv(r'output/dataframe_replaced.csv', sep=args.sep, decimal=args.dec, index=False, mode='w')

    
