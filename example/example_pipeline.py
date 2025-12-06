
from src.protein_dataframe import PPC_Dataframe
from example.analogous_pipeline import AnalogousPipeline
from example.enzymes_pipeline import EnzymesPipeline
from example.kingdom_pipeline import KingdomPipeline

class ExamplePipeline():
    
    def run_example():
        file_path = 'example/uniprotkb_reviewed_true_2025_11_29.tsv'
        print(f'Example Pipeline - Starting')
        try:
            print(f"Example Pipeline - Loading Dataframe from: {file_path}")
            df = PPC_Dataframe(file_path)
            print(f"Example Pipeline - Dataframe loaded successfully.")
            
            print()
            AnalogousPipeline.research(df, 'example/output/analogous')
            print()
            EnzymesPipeline.research(df, 'example/output/enzymes')
            print()
            KingdomPipeline.research(df, 'example/output/kingdom')
            print()
            
            print()
            print(f"Example Pipeline - Concluded successfully.")
            
        except FileNotFoundError:
            print(f"Analysis Error: The file was not found.")
