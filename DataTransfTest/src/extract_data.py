import pandas as pd
import tabula

def extract_data():
    '''Extract tables from PDF and return a combined DataFrame'''
    
    tables = tabula.read_pdf(
            r"DataTransfTest\resources\Anexo_1.pdf",
            pages='3-181',
            lattice=True,
            multiple_tables=True,
            encoding='utf-8',
        )
             
    combined_table = pd.concat(tables, ignore_index=True)
            
    return combined_table
        