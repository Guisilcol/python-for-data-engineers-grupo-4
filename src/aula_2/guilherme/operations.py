#COMMIT DA AULA 2

import pandas as pd 

def map(df: pd.DataFrame, cols: list):
    """Retorna um dataframe com as colunas informadas"""
    return df[cols]

def apply_to_every_row(df: pd.DataFrame, output_col: str, func):
    """Para cada linha aplica a função informada, jogando o output na informada como parâmetro"""
    df = df.copy()
    df[output_col] = df.apply(func, axis = 1)
    return df

def create_column(df: pd.DataFrame, col_name: str, col_type: str, col_default_value):
    """Cria uma nova coluna no dataframe"""
    df = df.copy()
    df[col_name] = col_default_value
    df[col_name] = df[col_name].astype(col_type)
    return df

def rename_cols(df: pd.DataFrame, columns: dict):
    """Renomeia as colunas do Dataframe"""
    return df.rename(columns=columns)

def join(df_left: pd.DataFrame, df_right: pd.DataFrame, left_on: list, right_on: list, how: str):
    "Aplica um join entre os dataframes informados"
    return pd.merge(left=df_left, right=df_right, left_on=left_on, right_on=right_on, how=how)

def distinct(df: pd.DataFrame):
    """Aplica um distinct no dataframes informado"""
    return df.drop_duplicates()

def query(df: pd.DataFrame, condition: str):
    """Aplica uma query (DataFrame.query()) no dataframe informado"""
    return df.query(condition)

def convert_type(df: pd.DataFrame, col: str, type: str, fill_na):
    """Converte o tipo da coluna informada"""
    df = df.copy()
    df[col] = df[col].astype(type).fillna(fill_na)
    return df

def display(df: pd.DataFrame):
    """Imprime o dataframe"""
    import IPython

    IPython.display.clear_output()
    IPython.display.display(df)
    return df

