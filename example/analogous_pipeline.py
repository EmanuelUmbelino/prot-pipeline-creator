
from src.protein_dataframe import PPC_Dataframe
from src.helpers.printer_helper import PPC_Printer
from src.enums.clusters import PPC_Clusters

class AnalogousPipeline():
    
    def research(df: PPC_Dataframe, path: str):
        try:
            print()
            print(f"Analogous Research - Starting: {path}")
            
            print(f"Analogous Research - HISE NISE")
            PPC_Printer.print_in_file(f'{path}/hise_info_bnf.txt', df, AnalogousPipeline.hise_bnf_info)
            AnalogousPipeline.hise_bnf(df, f'{path}/hise_bnf.tsv')
            PPC_Printer.print_in_file(f'{path}/nise_info_bnf.txt', df, AnalogousPipeline.nise_bnf_info)
            AnalogousPipeline.nise_bnf(df, f'{path}/nise_bnf.tsv')
            
            print(f"Analogous Research - NISE with PDB")
            PPC_Printer.print_in_file(f'{path}/pdb_nise_info_bnf.txt', df.has_pdb, AnalogousPipeline.nise_bnf_info)
            AnalogousPipeline.nise_bnf(df.has_pdb, f'{path}/pdb_nise_bnf.tsv')
            
            print(f"Analogous Research - Concluded successfully")
            
        except FileNotFoundError:
            print(f"Analogous Research Error: The file was not found.")
        except:
            print(f"Analogous Research Error: Unknown.")
    

    def hise_bnf_info(df: PPC_Dataframe):
        print(f"HISE.bnf")
        print(f"EC Complete, not promiscuous, single supfam")
        print()
        print(f"Clusterize by EC, in which all enzymes display one single SUPFAM")
        print(f"annotation and share the same SUPFAM.")
        print()
        
        df = df.ec_complete.not_promiscuous.single_supfam
        PPC_Printer.print_cluster_by_ec_class(df, PPC_Clusters.homologous_ec_clusters)
        
        print()
        print()
        print(f"BY SUPER KINGDOM")
        print()
        PPC_Printer.analysis_by_kingdom(df, PPC_Printer.print_cluster_by_ec_class, PPC_Clusters.homologous_ec_clusters)
    
    def nise_bnf_info(df: PPC_Dataframe):
        print(f"NISE.bnf")
        print(f"EC Complete, not promiscuous, single supfam")
        print()
        print(f"Clusterize by EC, in which all enzymes display one single SUPFAM")
        print(f"annotation and share different SUPFAM.")
        print()
        
        df = df.ec_complete.not_promiscuous.single_supfam
        PPC_Printer.print_cluster_by_ec_class(df, PPC_Clusters.non_homologous_ec_clusters)
        
        print()
        print()
        print(f"BY SUPER KINGDOM")
        print()
        PPC_Printer.analysis_by_kingdom(df, PPC_Printer.print_cluster_by_ec_class, PPC_Clusters.non_homologous_ec_clusters)
    

    def hise_bnf(df: PPC_Dataframe, path: str):
        df = df.ec_complete.not_promiscuous.single_supfam
        print()
        print(f"Initiate creating TSV file: {path}.")
        df.homologous_ec_clusters.to_tsv(path)
        print(f"TSV created successfully.")
    

    def nise_bnf(df: PPC_Dataframe, path: str):
        df = df.ec_complete.not_promiscuous.single_supfam
        print()
        print(f"Initiate creating TSV file: {path}.")
        df.non_homologous_ec_clusters.to_tsv(path)
        print(f"TSV created successfully.")
    

    def hise_multi(df: PPC_Dataframe, print_detail: bool = False):
        if (print_detail):
            print(f"HISE.multi")
            print(f"EC Complete, not promiscuous, multiple supfam")
            print()
            print(f"Clusterize by EC, in which all enzymes display multiple SUPFAM")
            print(f"annotation and share the same SUPFAM.")
            print()
        
        df = df.ec_complete.not_promiscuous.multi_supfam
        PPC_Printer.print_cluster_by_ec_class(df, PPC_Clusters.homologous_ec_clusters)

    def hise_sgl(df: PPC_Dataframe, print_detail: bool = False):
        if (print_detail):
            print(f"HISE.sgl")
            print(f"EC Complete, not promiscuous")
            print()
            print(f"Clusterize by EC with one single enzyme")
            print()
        
        df = df.ec_complete.not_promiscuous
        PPC_Printer.print_cluster_by_ec_class(df, PPC_Clusters.single_enzymes_clusters)
    

    def nise_multi(df: PPC_Dataframe, print_detail: bool = False):
        if (print_detail):
            print(f"NISE.multi")
            print(f"EC Complete, not promiscuous, multiple supfam")
            print()
            print(f"Clusterize by EC, in which all enzymes display multiple SUPFAM")
            print(f"annotation has different SUPFAM.")
            print()
        
        df = df.ec_complete.not_promiscuous.multi_supfam
        PPC_Printer.print_cluster_by_ec_class(df, PPC_Clusters.non_homologous_ec_clusters)
