from src.protein_dataframe import PPC_Dataframe
from src.helpers.printer_helper import PPC_Printer

class EnzymesPipeline():
    def research(df: PPC_Dataframe, path: str):
        try:
            print()
            print(f"Enzymes Research - Starting: {path}")
            
            print(f"Enzymes Research - Dividing by Enzyme Class")
            PPC_Printer.print_in_file(path + '/enzymes_info.txt', df, EnzymesPipeline.enzymes_info)
            EnzymesPipeline.oxidoreductases_enzymes(df, path + '/1_oxidoreductases.tsv')
            EnzymesPipeline.transferases_enzymes(df, path + '/2_ transferases.tsv')
            EnzymesPipeline.hydrolases_enzymes(df, path + '/3_hydrolases.tsv')
            EnzymesPipeline.lyases_enzymes(df, path + '/4_lyases.tsv')
            EnzymesPipeline.isomerases_enzymes(df, path + '/5_isomerases.tsv')
            EnzymesPipeline.ligases_enzymes(df, path + '/6_ligases.tsv')
            EnzymesPipeline.translocases_enzymes(df, path + '/7_translocases.tsv')
            
            print(f"Enzymes Research - Concluded successfully")
            
        except FileNotFoundError:
            print(f"Enzymes Research Error: The file was not found.")
        except:
            print(f"Enzymes Research Error: Unknown.")
    
    def enzymes_info(df: PPC_Dataframe):
        print(f"Enzymes")
        print(f"EC Complete, not promiscuous, single supfam")
        print()
        df = df.not_promiscuous.ec_complete.single_supfam
        PPC_Printer.print_by_ec_class(df)
            
    def oxidoreductases_enzymes(df: PPC_Dataframe, path: str):
        df = df.not_promiscuous.ec_complete.single_supfam.oxidoreductases
        print()
        print(f"Initiate creating TSV file: {path}.")
        df.to_tsv(path)
        print(f"TSV created successfully.")
            
    def transferases_enzymes(df: PPC_Dataframe, path: str):
        df = df.not_promiscuous.ec_complete.single_supfam.transferases
        print()
        print(f"Initiate creating TSV file: {path}.")
        df.to_tsv(path)
        print(f"TSV created successfully.")
            
    def hydrolases_enzymes(df: PPC_Dataframe, path: str):
        df = df.not_promiscuous.ec_complete.single_supfam.hydrolases
        print()
        print(f"Initiate creating TSV file: {path}.")
        df.to_tsv(path)
        print(f"TSV created successfully.")
            
    def lyases_enzymes(df: PPC_Dataframe, path: str):
        df = df.not_promiscuous.ec_complete.lyases
        print()
        print(f"Initiate creating TSV file: {path}.")
        df.to_tsv(path)
        print(f"TSV created successfully.")
            
    def isomerases_enzymes(df: PPC_Dataframe, path: str):
        df = df.not_promiscuous.ec_complete.single_supfam.isomerases
        print()
        print(f"Initiate creating TSV file: {path}.")
        df.to_tsv(path)
        print(f"TSV created successfully.")
            
    def ligases_enzymes(df: PPC_Dataframe, path: str):
        df = df.not_promiscuous.ec_complete.single_supfam.ligases
        print()
        print(f"Initiate creating TSV file: {path}.")
        df.to_tsv(path)
        print(f"TSV created successfully.")
            
    def translocases_enzymes(df: PPC_Dataframe, path: str):
        df = df.not_promiscuous.ec_complete.single_supfam.translocases
        print()
        print(f"Initiate creating TSV file: {path}.")
        df.to_tsv(path)
        print(f"TSV created successfully.")