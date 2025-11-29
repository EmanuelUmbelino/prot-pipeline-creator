import pandas as pd

from src.enums.columns import Columns, ClusterizedColumns

class ClusterizedDataframe:
    __df: pd.DataFrame
    
    def __init__(self, df: pd.DataFrame = None):
        self.__initial_treatment(df)
    
    def __len__(self):
        return len(self.__df)
    
    def __getitem__(self, key: str):
        return self.__df[key]
    
    def __repr__(self):
        return repr(self.__df)
        
    def __initial_treatment(self, df: pd.DataFrame):
        self.__df = df.groupby(Columns.ECNumber).agg(
            SuperFamilyCount=(Columns.SuperFamily, 'nunique'),
            ProteinCount=(Columns.Entry, 'nunique'),
            SuperFamily=(Columns.SuperFamily, 'unique'),
            ProteinEntries=(Columns.Entry, list),
        ).reset_index()
    
    @property
    def cols(self):
        return list(self.__df)
    
    @property
    def count_proteins(self):
        return self.__df[ClusterizedColumns.ProteinCount].sum()
    
    
    