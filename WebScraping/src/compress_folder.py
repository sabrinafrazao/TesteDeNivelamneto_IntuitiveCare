import shutil

def compress_folder(folder_origin, name_file):
    """Compress all files in the folder into a ZIP"""
    
    path_zip = shutil.make_archive(name_file, "zip", folder_origin)
    
    return path_zip
