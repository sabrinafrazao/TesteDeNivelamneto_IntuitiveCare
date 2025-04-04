import zipfile
import os

def compress_to_zip(file, file_zip=None):

    """ Compressing the file Teste_Sabrina.csv to ZIP """
    
    with zipfile.ZipFile(file_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(file, os.path.basename(file))

    print(" Compressing the file with successfully!")

    return file_zip
  