# Functions to acquire zillow data from codeup database and write to a local csv file

import pandas as pd
import numpy as np

from env import host, user, password


def get_connection(db, user=user, host=host, password=password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

    '''
    this function will return the zillow data from the CodeUp Database, you will need your own env.py file to gain access 
    '''

def get_zillow_data():
    
    sql_query = '''SELECT p17.*, pt.propertylandusetypeid, pred17.logerror, pred17.transactiondate
                FROM properties_2017 AS p17
                JOIN propertylandusetype as pt ON p17.propertylandusetypeid = pt.propertylandusetypeid
                JOIN predictions_2017 AS pred17 ON p17.parcelid = pred17.parcelid
                WHERE pred17.transactiondate BETWEEN '2017-05-01' AND '2017-06-30'
                AND pt.propertylandusetypeid <> 31 AND pt.propertylandusetypeid <> 46 
                AND pt.propertylandusetypeid <> 47 AND pt.propertylandusetypeid <> 267 
                AND pt.propertylandusetypeid <> 269 AND pt.propertylandusetypeid <> 270 
                AND pt.propertylandusetypeid <> 271 AND pt.propertylandusetypeid <> 274 
                AND pt.propertylandusetypeid <> 273 AND pt.propertylandusetypeid <> 290 
                AND pt.propertylandusetypeid <> 291'''
    
    df = pd.read_sql(sql_query, get_connection('zillow'))
    df.to_csv('zillow_hot_months.csv')
    return df

print('acquire.py functions loaded successfully')