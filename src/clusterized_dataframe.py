import pandas as pd

from src.enums.columns import PPC_Columns, PPC_ClusterizedColumns

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
        self.__df = df.groupby(PPC_Columns.ECNumber).agg(
            SuperFamilyCount=(PPC_Columns.SuperFamily, 'nunique'),
            ProteinCount=(PPC_Columns.Entry, 'nunique'),
            SuperFamily=(PPC_Columns.SuperFamily, 'unique'),
            ProteinEntries=(PPC_Columns.Entry, list),
        ).reset_index()
    
    def to_csv(self, path: str):
        self.__df.to_csv(path, sep='\t', encoding='utf-8', index=False, header=True)
    
    @property
    def cols(self):
        return list(self.__df)
    
    @property
    def count_proteins(self):
        return self.__df[PPC_ClusterizedColumns.ProteinCount].sum()
    
    
    