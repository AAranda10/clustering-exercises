#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import acquire
from scipy import stats


# In[2]:
'''
    This function is going to take in the acquired data and clean it. Removing null values, outliers, and columns we will not need to assess the data or build our models. 
    '''

def missing_rows(df):
    num_rows_missing = df.isnull().sum()
    pct_rows_missing = df.isnull().sum() / (df.isnull().sum() + df.notnull().sum())
    missing_rows = pd.DataFrame({'num_rows_missing':num_rows_missing,'pct_rows_missing':pct_rows_missing})
    return missing_rows



def missing_cols(df):
    num_cols_missing = df.isnull().sum(axis=1)
    pct_cols_missing = df.isnull().sum(axis=1) / (df.isnull().sum(axis=1) + df.notnull().sum(axis=1))
    num_rows = df.isnull().sum(axis=1).value_counts().sort_index().reset_index(drop=True)
    cols_missing = pd.DataFrame({'num_cols_missing':num_cols_missing, 'pct_cols_missing':pct_cols_missing, 'num_rows': num_rows})
    return cols_missing



def drop_nulls(df, prop_required_column = .70, prop_required_row = .70):
    threshold = int(round(prop_required_column*len(df.index),0))
    df.dropna(axis=1, thresh=threshold, inplace=True)
    threshold = int(round(prop_required_row*len(df.columns),0))
    df.dropna(axis=0, thresh=threshold, inplace=True)
    return df

def prep_zillow_data():
    df = acquire.get_zillow_data()
    df = missing_rows(df)
    df = missing_cols(df)
    df = drop_nulls(df, prop_required_column = .70, prop_required_row = .70)
    return df
    
