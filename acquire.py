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
    
    sql_query = '''
                select * from properties_2017
                join (select id, logerror, pid, tdate from predictions_2017 pred_2017
                join (SELECT parcelid as pid, Max(transactiondate) as tdate FROM predictions_2017 GROUP BY parcelid) as sq1
                on (pred_2017.parcelid = sq1.pid and pred_2017.transactiondate = sq1.tdate)) as sq2
                on (properties_2017.parcelid = sq2.pid)
                left join airconditioningtype using (airconditioningtypeid)
                left join architecturalstyletype using (architecturalstyletypeid)
                left join buildingclasstype using (buildingclasstypeid)
                left join heatingorsystemtype using (heatingorsystemtypeid)
                left join propertylandusetype using (propertylandusetypeid)
                left join storytype using (storytypeid)
                left join typeconstructiontype using (typeconstructiontypeid)
                left join unique_properties using (parcelid)
                where latitude is not null and longitude is not null;
'''
    
    df = pd.read_sql(sql_query, get_connection('zillow'))
    df.to_csv('zillow.csv')
    return df

print('acquire.py functions loaded successfully')


############################################Summary of Missing Values#################################

def missing_data(df):
    num_rows_missing = df.isnull().sum()
    pct_rows_missing = df.isnull().sum() / (df.isnull().sum() + df.notnull().sum())
    nulls = pd.DataFrame({'num_rows_missing':num_rows_missing,'pct_rows_missing':pct_rows_missing})
    return nulls

############################################Get Mall Data#################################

def get_mallcustomer_data():
    df = pd.read_sql('SELECT * FROM customers;', get_connection('mall_customers'))
    return df.set_index('customer_id')

