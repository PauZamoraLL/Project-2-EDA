
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn as sns
from tqdm.notebook import tqdm_notebook
import time
import plotly.express as px


def missingdata_percentage(df):
    missing = pd.DataFrame(columns=['category','percentage'])
    for col in tqdm_notebook(df.columns):
        if df[col].isna().values.any():
            percentage = 100*df[col].isna().sum()/df.shape[0]
            missing = missing.append({'category' : col, 'percentage' : percentage}, ignore_index=True)
    return missing.sort_values('percentage', ascending=False)


def additional_common_columns(df1, df2):
    additional_feat = []
    common_feat = []
    for col in tqdm_notebook(df1.columns):
        if col not in df2.columns:
            additional_feat.append(col)
        else:
            common_feat.append(col)  
    print(len(additional_feat))
    print(len(common_feat))
    print(common_feat)


    
def numeric_features(df):
    numeric_features = []
    for col in tqdm_notebook(df.columns):
        if df[col].dtype == float or df[col].dtype == int:
            numeric_features.append(col)
    return numeric_features

    
def vale_label_per_defaulter(df, col):
    new_df = pd.DataFrame(columns=['Value', 'Percentage of Defaulter'])
    
    for value in tqdm_notebook(df[col].unique()):
        default_cnt = df[(df[col] == value) & (df.TARGET == 1)].shape[0]
        total_cnt = df[df[col] == value].shape[0]
        new_df = new_df.append({'Value' : value , 'Percentage of Defaulter' :                                     (default_cnt*100/total_cnt)}, ignore_index=True)
    return new_df.sort_values(by='Percentage of Defaulter', ascending=False)
    
    
    
    
    
    
    
    
