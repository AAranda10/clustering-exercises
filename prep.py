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

def prep_zillow_data():
    df = acquire.get_zillow_data()
    df = df.drop(columns = {'airconditioningtypeid', 'architecturalstyletypeid', 'basementsqft',
                            'taxdelinquencyyear', 'buildingclasstypeid', 'decktypeid', 'finishedfloor1squarefeet',
                            'finishedsquarefeet13', 'finishedsquarefeet15', 'finishedsquarefeet50',
                            'finishedsquarefeet6', 'fireplacecnt', 'hashottuborspa', 'poolsizesum',
                            'pooltypeid10', 'pooltypeid2', 'pooltypeid7', 'storytypeid', 'threequarterbathnbr',
                            'typeconstructiontypeid', 'yardbuildingsqft17', 'yardbuildingsqft26', 'numberofstories',
                            'fireplaceflag', 'taxdelinquencyflag', 'buildingqualitytypeid', 'garagecarcnt',
                            'garagetotalsqft', 'poolcnt', 'regionidneighborhood', 'propertyzoningdesc',
                            'propertycountylandusecode', 'id', 'parcelid', 'transactiondate', 'finishedsquarefeet12',
                            'censustractandblock', 'logerror'})
    df['propertylandusetypeid'] = df['propertylandusetypeid'].astype(float)
    df['calculatedfinishedsquarefeet'] = df['calculatedfinishedsquarefeet'].fillna((df['calculatedfinishedsquarefeet'].mean()))
    df['calculatedbathnbr'] = df['calculatedbathnbr'].fillna((df['calculatedbathnbr'].mean()))
    df['fullbathcnt'] = df['fullbathcnt'].fillna((df['fullbathcnt'].mean()))
    df['heatingorsystemtypeid'] = df['heatingorsystemtypeid'].fillna((df['heatingorsystemtypeid'].mean()))
    df['lotsizesquarefeet'] = df['lotsizesquarefeet'].fillna((df['lotsizesquarefeet'].mean()))
    df['regionidcity'] = df['regionidcity'].fillna((df['regionidcity'].mean()))
    df['regionidzip'] = df['regionidzip'].fillna((df['regionidzip'].mean()))
    df['unitcnt'] = df['unitcnt'].fillna((df['unitcnt'].mean()))
    df['yearbuilt'] = df['yearbuilt'].fillna((df['yearbuilt'].mean()))
    df['calculatedfinishedsquarefeet'] = df.calculatedfinishedsquarefeet[(np.abs(stats.zscore(df.calculatedfinishedsquarefeet)) < 3)]
    df = df.dropna()
    return df


# In[3]:





# In[ ]:




