import pandas as pd
import numpy as np

def create_dataframe_with_embedding(datafile_path:str, embedding_column_name:str):
    
    df = pd.read_csv(datafile_path)
    df[embedding_column_name] = df[embedding_column_name].apply(eval).apply(np.array)
    return df