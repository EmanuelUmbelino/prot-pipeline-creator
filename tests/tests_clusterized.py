import unittest
import pandas as pd
from src.clusterized_dataframe import ClusterizedDataframe
from src.enums.columns import PPC_Columns, PPC_ClusterizedColumns

class TestClusterizedDataframe(unittest.TestCase):

    def test_clustering_aggregation(self):
        # Scenario: 3 Proteins.
        # P1 and P2 have the same EC '1.1.1.1'.
        # P3 has EC '2.2.2.2'.
        data = {
            PPC_Columns.Entry: ['P1', 'P2', 'P3'],
            PPC_Columns.ECNumber: ['1.1.1.1', '1.1.1.1', '2.2.2.2'],
            PPC_Columns.SuperFamily: ['FamA', 'FamB', 'FamC'],
            PPC_Columns.ProteinNames: ['Name1', 'Name2', 'Name3']
        }
        df = pd.DataFrame(data)

        # Initialize the ClusterizedDataframe
        cluster_df = ClusterizedDataframe(df)

        # We should have 2 rows now (one for 1.1.1.1 and another for 2.2.2.2)
        self.assertEqual(len(cluster_df), 2)

        group_1 = cluster_df._ClusterizedDataframe__df[
            cluster_df._ClusterizedDataframe__df[PPC_Columns.ECNumber] == '1.1.1.1'
        ]
        self.assertEqual(group_1[PPC_ClusterizedColumns.ProteinCount].iloc[0], 2)
        self.assertEqual(group_1[PPC_ClusterizedColumns.SuperFamilyCount].iloc[0], 2)

        group_2 = cluster_df._ClusterizedDataframe__df[
            cluster_df._ClusterizedDataframe__df[PPC_Columns.ECNumber] == '2.2.2.2'
        ]
        self.assertEqual(group_2[PPC_ClusterizedColumns.ProteinCount].iloc[0], 1)
        self.assertEqual(group_2[PPC_ClusterizedColumns.SuperFamilyCount].iloc[0], 1)
        

    def test_count_proteins_property(self):
        # The total unique proteins in the clusterized dataset must match the input
        data = {
            PPC_Columns.Entry: ['P1', 'P2'],
            PPC_Columns.ECNumber: ['1.1', '1.1'],
            PPC_Columns.SuperFamily: ['A', 'A'],
            PPC_Columns.ProteinNames: ['N1', 'N2']
        }
        df = pd.DataFrame(data)
        cluster_df = ClusterizedDataframe(df)
        
        self.assertEqual(cluster_df.count_proteins, 2)

if __name__ == '__main__':
    unittest.main()