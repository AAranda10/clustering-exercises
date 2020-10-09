# File for creating an acquire and prepping of files for regression exercises.

# importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler

# Turn off warnings
import warnings
warnings.filterwarnings("ignore")

# split_scale
# import split_scale

# libraries needed for preparing the data:
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
# from sklearn.preprocessing import StandardScaler, QuantileTransformer, PowerTransformer, RobustScaler, MinMaxScaler
# from sklearn.preprocessing import MinMaxScaler
import sklearn.preprocessing

# Setting up the user credentials:
from env import host, user, password



##### This is the key function that returns 6 dataframes #####
def train_validate_test(df):
    '''
    this function takes in a dataframe and splits it into 3 samples, 
    a test, which is 20% of the entire dataframe, 
    a validate, which is 24% of the entire dataframe,
    and a train, which is 56% of the entire dataframe. 
    It then splits each of the 3 samples into a dataframe with independent variables
    and a series with the dependent, or target variable. 
    The function returns 3 dataframes and 3 series:
    X_train (df) & y_train (series), X_validate & y_validate, X_test & y_test. 
    '''
    # split df into test (20%) and train_validate (80%)
    train_validate, test = train_test_split(df, test_size=.2, random_state=123)

    # split train_validate off into train (70% of 80% = 56%) and validate (30% of 80% = 24%)
    train, validate = train_test_split(train_validate, test_size=.3, random_state=123)

        
    # split train into X (dataframe, drop target) & y (series, keep target only)
    X_train = train.drop(columns= ['taxvaluedollarcnt', 'assessmentyear', 'roomcnt', 'fips', 'heatingorsystemtypeid', 
                                   'lotsizesquarefeet', 'propertylandusetypeid', 'regionidcity', 'regionidcounty', 'regionidzip', 
                                   'roomcnt', 'unitcnt', 'yearbuilt', 'assessmentyear', 'propertylandusetypeid', 'latitude',
                                   'longitude', 'rawcensustractandblock', 'structuretaxvaluedollarcnt',
                                   'landtaxvaluedollarcnt', 'taxamount'])
    X_validate = validate.drop(columns= ['taxvaluedollarcnt', 'assessmentyear', 'roomcnt', 'fips', 'heatingorsystemtypeid', 
                                   'lotsizesquarefeet', 'propertylandusetypeid', 'regionidcity', 'regionidcounty', 'regionidzip', 
                                   'roomcnt', 'unitcnt', 'yearbuilt', 'assessmentyear', 'propertylandusetypeid', 'latitude',
                                   'longitude', 'rawcensustractandblock', 'structuretaxvaluedollarcnt',
                                   'landtaxvaluedollarcnt', 'taxamount'])
    X_test = test.drop(columns= ['taxvaluedollarcnt', 'assessmentyear', 'roomcnt', 'fips', 'heatingorsystemtypeid', 
                                   'lotsizesquarefeet', 'propertylandusetypeid', 'regionidcity', 'regionidcounty', 'regionidzip', 
                                   'roomcnt', 'unitcnt', 'yearbuilt', 'assessmentyear', 'propertylandusetypeid', 'latitude',
                                   'longitude', 'rawcensustractandblock', 'structuretaxvaluedollarcnt',
                                   'landtaxvaluedollarcnt', 'taxamount'])

    y_train = train[['taxvaluedollarcnt']]
    y_validate = validate[['taxvaluedollarcnt']]
    y_test = test[['taxvaluedollarcnt']]
    return X_train, y_train, X_validate, y_validate, X_test, y_test


def min_max_scale(X_train, X_validate, X_test):
    '''
    this function takes in 3 dataframes with the same columns, 
    a list of numeric column names (because the scaler can only work with numeric columns),
    and fits a min-max scaler to the first dataframe and transforms all
    3 dataframes using that scaler. 
    it returns 3 dataframes with the same column names and scaled values. 
    '''
    # create the scaler object and fit it to X_train (i.e. identify min and max)
    # if copy = false, inplace row normalization happens and avoids a copy (if the input is already a numpy array).
    
    scaler = MinMaxScaler(copy = True).fit(X_train)

    X_train_scaled = scaler.transform(X_train)
    X_validate_scaled = scaler.transform(X_validate)
    X_test_scaled = scaler.transform(X_test)
    X_train_scaled = pd.DataFrame(X_train_scaled, columns = X_train.columns.values).set_index([X_train.index.values])
    X_validate_scaled = pd.DataFrame(X_validate_scaled, columns = X_validate.columns.values).set_index([X_validate.index.values])
    X_test_scaled = pd.DataFrame(X_test_scaled, columns = X_test.columns.values).set_index([X_test.index.values])

    
    return X_train_scaled, X_validate_scaled, X_test_scaled







print("wrangle.py functions loaded successfully")