from extract import extract_links
from download import download_files
from compress_folder import compress_folder

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

folder = r"WebScraping\resources\attachment"
base_url = url
links = extract_links(url)
name_zip = r"WebScraping\resources\zipped_attachments"


def main():
    
    extract_links(url)

    download_files(links, folder, base_url)

    compress_folder(folder, name_zip)


if __name__ == "__main__":
    main()
    