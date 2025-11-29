import pandas as pd
from enum import Enum

from src.pandas_helper import PandasHelper as pdHelper
from src.clusterized_dataframe import ClusterizedDataframe as clustDataframe
from src.enums.super_kingdom import SuperKingdom
from src.enums.columns import Columns

class ClusterEnum(Enum):
    single_enzymes_clusters = 1
    multiple_enzymes_clusters = 2
    homologous_ec_clusters = 3
    non_homologous_ec_clusters = 4

class ProteinDataframe:
    """
    A class to load, process, and analyze protein data from a .tsv file.

    This class serves as a high-level wrapper around a pandas DataFrame,
    providing specialized methods for common bioinformatics analyses like
    filtering by enzyme class, clustering by domain, and identifying
    homogeneous (HISE) and heterogeneous (NISE) enzyme groups.
    """
    
    __df: pd.DataFrame
    
    def __init__(self, file_path: str = '', df: pd.DataFrame = None):
        """
        Initializes the ProteinDataset object.

        Args:
            file_path (str): The full path to the input data file.
            df (DataFrame, optional): Internal use to duplicate the ProteinDataframe
        """
        if file_path:
            self.__read_file(file_path)
            self.__initial_treatment()
        else:
            self.__df = df
    
    def __len__(self):
        return len(self.__df)
    
    def __getitem__(self, key: str):
        return self.__df[key]
    
    def __repr__(self):
        return repr(self.__df)
    
    def __read_file(self, filename):
        self.__df = pd.read_csv(
            filename,
            sep='\t',
            header=0,
        )
        
    def __initial_treatment(self):
        self.__df[Columns.ECNumber] = pdHelper.transform_col_in_tuple(self.__df[Columns.ECNumber], ';')
        self.__df[Columns.SuperFamily] = pdHelper.transform_col_in_tuple(self.__df[Columns.SuperFamily], ';')
        self.__df[Columns.PDB] = pdHelper.transform_col_in_tuple(self.__df[Columns.PDB], ';')
        
        self.__df[Columns.SuperKingdom] = self.__df[Columns.TaxonomicLineage].apply(self.__extract_superkingdom)
        self.__df[Columns.IsECComplete] = self.__df[Columns.ECNumber].apply(self.__has_ec_complete)
    
    @property
    def cols(self):
        return list(self.__df)
    
    @property
    def ec_complete(self):
        filter = self.__df[Columns.IsECComplete]
        return ProteinDataframe(df = self.__df[filter])
    
    @property
    def no_ec(self):
        filter = self.__df[Columns.ECNumber].str.len() < 1
        return ProteinDataframe(df = self.__df[filter])
    
    @property
    def has_ec(self):
        filter = self.__df[Columns.ECNumber].str.len() > 0
        return ProteinDataframe(df = self.__df[filter])
    
    @property
    def has_ec(self):
        filter = self.__df[Columns.PDB].str.len() > 0
        return ProteinDataframe(df = self.__df[filter])
        
    @property
    def not_promiscuous(self):
        filter = self.__df[Columns.ECNumber].str.len() == 1
        return ProteinDataframe(df = self.__df[filter])
    
    @property
    def promiscuos(self):
        filter = self.__df[Columns.ECNumber].str.len() > 1
        return ProteinDataframe(df = self.__df[filter])
    
    @property
    def exploded_ec_clusters(self):
        exploded_supfam = self.__df.explode(Columns.ECNumber)
        
        clusters_df = pdHelper.clusterize_col(exploded_supfam, Columns.ECNumber)
        
        return clusters_df
    
    @property
    def ec_clusters(self):
        return pdHelper.clusterize_col(self.__df, Columns.ECNumber)
    
    def get_cluster(self, prop: ClusterEnum):
        match prop:
            case ClusterEnum.single_enzymes_clusters:
                return self.single_enzymes_clusters
            case ClusterEnum.multiple_enzymes_clusters:
                return self.multiple_enzymes_clusters
            case ClusterEnum.homologous_ec_clusters:
                return self.homologous_ec_clusters
            case ClusterEnum.non_homologous_ec_clusters:
                return self.non_homologous_ec_clusters
    
    @property
    def single_enzymes_clusters(self):      
        hise = self.__df.groupby(Columns.ECNumber).filter(
            lambda group: group[Columns.Entry].nunique() == 1
        )
        
        return clustDataframe(hise)
    
    @property
    def multiple_enzymes_clusters(self):      
        hise = self.__df.groupby(Columns.ECNumber).filter(
            lambda group: group[Columns.Entry].nunique() > 1
        )
        
        return clustDataframe(hise)
    
    @property
    def homologous_ec_clusters(self):      
        hise = self.__df.groupby(Columns.ECNumber).filter(
            lambda group: group[Columns.SuperFamily].nunique() == 1
        )
        
        return clustDataframe(hise)
    
    @property
    def non_homologous_ec_clusters(self):      
        nise = self.__df.groupby(Columns.ECNumber).filter(
            lambda group: group[Columns.SuperFamily].nunique() > 1
        )
        
        return clustDataframe(nise)
    
    @property
    def ec_value_counts(self):
        return self.__df[Columns.ECNumber].explode().value_counts()
    
    @property
    def no_supfam(self):
        filter = self.__df[Columns.SuperFamily].str.len() < 1
        return ProteinDataframe(df = self.__df[filter])
    
    @property
    def has_supfam(self):
        filter = self.__df[Columns.SuperFamily].str.len() > 0
        return ProteinDataframe(df = self.__df[filter])
    
    @property
    def single_supfam(self):
        filter = self.__df[Columns.SuperFamily].str.len() == 1
        return ProteinDataframe(df = self.__df[filter])
    
    @property
    def multi_supfam(self):
        filter = self.__df[Columns.SuperFamily].str.len() > 1
        return ProteinDataframe(df = self.__df[filter])
    
    @property
    def exploded_supfam_clusters(self):
        exploded_supfam = self.__df.explode(Columns.SuperFamily)
        
        clusters_df = pdHelper.clusterize_col(exploded_supfam, Columns.SuperFamily)
        
        return clusters_df
    
    @property
    def supfam_clusters(self):        
        return pdHelper.clusterize_col(self.__df, Columns.SuperFamily)
    
    @property
    def supfam_value_counts(self):
        return self.__df[Columns.SuperFamily].explode().value_counts()
    
    @property
    def supkingdom_value_counts(self):
        return self.__df[Columns.SuperKingdom].value_counts()
    
    
    @property
    def has_pdb(self):
        filter = self.__df[Columns.PDB].str.len() > 0
        return ProteinDataframe(df = self.__df[filter])
    
    @property
    def bacteria(self):
        return self.__supkingdom_is(SuperKingdom.Bacteria)
    
    @property
    def eukaryota(self):
        return self.__supkingdom_is(SuperKingdom.Eukaryota)
    
    @property
    def archaea(self):
        return self.__supkingdom_is(SuperKingdom.Archaea)
    
    @property
    def viruses(self):
        return self.__supkingdom_is(SuperKingdom.Viruses)
    
    @property
    def oxidoreductases(self):
        return self.__ec_init_with('1')
    
    @property
    def transferases(self):
        return self.__ec_init_with('2')
    
    @property
    def hydrolases(self):
        return self.__ec_init_with('3')
    
    @property
    def lyases(self):
        return self.__ec_init_with('4')
    
    @property
    def isomerases(self):
        return self.__ec_init_with('5')
    
    @property
    def ligases(self):
        return self.__ec_init_with('6')
    
    @property
    def translocases(self):
        return self.__ec_init_with('7')
    
    def __ec_init_with(self, ec_filter: str):
        filter = self.__df[Columns.ECNumber].apply(lambda x: any(ec.startswith(ec_filter) for ec in x))
        return ProteinDataframe(df = self.__df[filter])
    
    def __supkingdom_is(self, supkingdom: str):
        superKingdomColumn: str = f'{Columns.SuperKingdom}'
        filter = self.__df[superKingdomColumn].fillna('').str.lower() == supkingdom.lower()
        return ProteinDataframe(df = self.__df[filter])
    
    def __extract_superkingdom(self, lineage: str):
        if pd.isna(lineage):
            return None
        
        parts = lineage.split(', ')
        parts[0] = parts[0].split(' ')[0]
        
        if parts[0].lower() == SuperKingdom.Viruses.lower():
            return SuperKingdom.Viruses
        
        if len(parts) > 1:
            parts[1] = parts[1].split(' ')[0]
            return parts[1]
        
        return None
    
    def __has_ec_complete(self, ec_list):
        return any(self.__is_ec_complete(ec) for ec in ec_list)
    
    def __is_ec_complete(self, ec: str):
        if pd.isna(ec):
            return False
        
        parts = ec.split('.')
        
        if (len(parts) < 4):
            return False
        
        return all(x.isdigit() for x in parts)
    
    