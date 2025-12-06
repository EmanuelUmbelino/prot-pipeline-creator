from src.protein_dataframe import PPC_Dataframe
from src.helpers.printer_helper import PPC_Printer

class KingdomPipeline():
    def research(df: PPC_Dataframe, path: str):
        try:
            print()
            print(f"Kingdom Research - Starting: {path}")
            
            print(f"Kingdom Research - Dividing by Super Kingdom")
            PPC_Printer.print_in_file(path + '/kingdom_info.txt', df, KingdomPipeline.kingdom_info)
            KingdomPipeline.archaea_enzymes(df, path + '/archaea.tsv')
            KingdomPipeline.bacteria_enzymes(df, path + '/bacteria.tsv')
            KingdomPipeline.eukaryota_enzymes(df, path + '/eukaryota.tsv')
            KingdomPipeline.viruses_enzymes(df, path + '/viruses.tsv')
            
            print(f"Kingdom Research - Concluded successfully")
            
        except FileNotFoundError:
            print(f"Kingdom Research Error: The file was not found.")
        except:
            print(f"Kingdom Research Error: Unknown.")
    
    def kingdom_info(df: PPC_Dataframe):
        print(f"Enzymes by Superkingdom")
        print(f"EC Complete, not promiscuous, single supfam")
        print()
        df = df.not_promiscuous.ec_complete.single_supfam
        PPC_Printer.print_by_kingdom(df)
            
    def archaea_enzymes(df: PPC_Dataframe, path: str):
        df = df.not_promiscuous.ec_complete.single_supfam.archaea
        print()
        print(f"Initiate creating TSV file: {path}.")
        df.to_tsv(path)
        print(f"TSV created successfully.")
            
    def bacteria_enzymes(df: PPC_Dataframe, path: str):
        df = df.not_promiscuous.ec_complete.single_supfam.bacteria
        print()
        print(f"Initiate creating TSV file: {path}.")
        df.to_tsv(path)
        print(f"TSV created successfully.")
            
    def eukaryota_enzymes(df: PPC_Dataframe, path: str):
        df = df.not_promiscuous.ec_complete.single_supfam.eukaryota
        print()
        print(f"Initiate creating TSV file: {path}.")
        df.to_tsv(path)
        print(f"TSV created successfully.")
            
    def viruses_enzymes(df: PPC_Dataframe, path: str):
        df = df.not_promiscuous.ec_complete.single_supfam.viruses
        print()
        print(f"Initiate creating TSV file: {path}.")
        df.to_tsv(path)
        print(f"TSV created successfully.")