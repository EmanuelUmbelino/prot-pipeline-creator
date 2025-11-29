import pandas as pd

from src.enums.columns import PPC_Columns

class PandasHelper:
    @staticmethod
    def plot_full():
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)  
        # pd.set_option('display.max_colwidth', None) 
        
    @staticmethod
    def transform_col_in_tuple(col_df: pd.DataFrame, sep: str = None):
        col_df.fillna('', inplace=True)
        return col_df.apply(PandasHelper.__str_to_clear_tuple, args=(sep))
    
    @staticmethod
    def clusterize_col(df: pd.DataFrame, col: str):
        clusters_df = df.groupby(col).agg(
            ProteinEntries=(PPC_Columns.Entry, list),
            MemberCount=(PPC_Columns.Entry, 'nunique')
        ).reset_index()
        return clusters_df
    
    def __str_to_clear_tuple(str: str, sep: str = None):
        list = str.split(sep)
        list.sort()
        clean = [x.strip() for x in list]
        filtered = filter(lambda x: x, clean)
        return tuple(filtered)
    