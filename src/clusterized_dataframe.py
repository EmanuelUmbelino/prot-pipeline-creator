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
        if df.empty:
            self.__df = pd.DataFrame(columns=[
                PPC_Columns.ECNumber, 
                PPC_ClusterizedColumns.SuperFamilyCount, 
                PPC_ClusterizedColumns.ProteinCount,
                PPC_ClusterizedColumns.Entries
            ])
            return
        
        temp_df = df.copy()
        
        family_groups = temp_df.groupby([
            PPC_Columns.ECNumber, PPC_Columns.SuperFamily
        ])[PPC_Columns.Entry].apply(list).reset_index()

        temp_df['Entry_With_SupFam'] = temp_df.apply(
            lambda row: f"{row[PPC_Columns.Entry]} {str(row[PPC_Columns.SuperFamily])}", 
            axis=1
        )
        
        family_groups['FormattedFamily'] = family_groups.apply(
            lambda row: f"{str(row[PPC_Columns.SuperFamily])}: {str(row[PPC_Columns.Entry])}", 
            axis=1
        )
        
        detailed_entries = family_groups.groupby(PPC_Columns.ECNumber)['FormattedFamily'].apply(list).reset_index()
        detailed_entries.rename(columns={'FormattedFamily': PPC_ClusterizedColumns.Entries}, inplace=True)
        
        stats_df = temp_df.groupby(PPC_Columns.ECNumber).agg(
            SuperFamilyCount=(PPC_Columns.SuperFamily, 'nunique'),
            ProteinCount=(PPC_Columns.Entry, 'nunique'),
        ).reset_index()
        
        self.__df = pd.merge(stats_df, detailed_entries, on=PPC_Columns.ECNumber, how='left')
    
    def to_tsv(self, path: str):
        self.__df.to_csv(path, sep='\t', encoding='utf-8', index=False, header=True)
    
    @property
    def cols(self):
        return list(self.__df)
    
    @property
    def count_proteins(self):
        return self.__df[PPC_ClusterizedColumns.ProteinCount].sum()
    
    
    