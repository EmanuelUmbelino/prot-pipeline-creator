class Columns:
    Entry = 'Entry'
    EntryName = 'Entry Name'
    ECNumber = 'EC number'
    IsECComplete = 'Is EC Complete'
    SuperFamily = 'SUPFAM'
    SuperKingdom = 'Super Kingdom'
    ProteinNames = 'Protein names'
    GeneNames = 'Gene names'
    Organism = 'Organism'
    LastModify = 'Date of last modification'
    EntryVersion = 'Entry version'
    PDB = 'PDB'
    AlphaFoldDB = 'AlphaFold DB'
    TaxonomicLineage = 'Taxonomic lineage'

class ClusterizedColumns:
    SuperFamilyCount = 'SuperFamilyCount'
    ProteinCount = 'ProteinCount'
    SuperFamily = Columns.SuperFamily
    ProteinEntries = Columns.ProteinNames
