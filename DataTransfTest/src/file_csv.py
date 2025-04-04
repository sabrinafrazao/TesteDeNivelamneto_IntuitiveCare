file_csv= r"DataTransfTest\resources\Teste_Sabrina.csv"

def transform_file_to_csv(df, file_csv):
    '''Process DataFrame and save to CSV'''
    
    column_mapping = {
            'OD': 'Seg. Odontológica',
            'AMB': 'Seg. Ambulatorio'
    }
        
    end_df = df.rename(columns={
            k: v for k, v in column_mapping.items() 
            if k in df.columns
    })
        
    end_df.to_csv(
            file_csv,
            index=False,
            encoding='utf-8-sig',
            sep=';'
    )
        
    print(f"File {file_csv} saved successfully!")
 
    return True
        