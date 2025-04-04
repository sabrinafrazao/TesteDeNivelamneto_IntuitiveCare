from extract_data import extract_data
from file_csv import transform_file_to_csv
from compress import compress_to_zip

df = extract_data()
file_csv = r"DataTransfTest\resources\Teste_Sabrina.csv"
file_zip =  r"DataTransfTest\resources\Teste_Sabrina.zip"

def main():

    extract_data()
    transform_file_to_csv(df, file_csv)
    compress_to_zip(file_csv, file_zip)

    
if __name__ == "__main__":
    main()