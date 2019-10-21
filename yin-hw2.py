import pandas as pd
import io
import requests

# https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD

def create_dataframe(url):
    df = pd.read_csv(url)
    return df

def test_create_dataframe(df, column_names):
    """
    :params df: pandas dataframe to be checked
    :params column_names: list of names
    """
    # check unknown columns names
    for col in df.columns.values.tolist():
        if not col in column_names:
            raise ValueError("Unspecified column names in dataframe.")

    # check values in column have same type
    for col in df.columns.values.tolist():
        if df[col].dtype == 'O':
            raise ValueError('Data type not consistent in column {}'.format(col))

    # check number of rows in dataframe
    if df.shape[0] < 10:
        raise ValueError('Dataframe row count fewer than 10.')

    # if nothing happens, df passes the test
    return True