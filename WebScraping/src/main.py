from extract import extract_links
from download import download_files


url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

folder = r"WebScraping\resources\anexos"
base_url = url
links = extract_links(url)

def main():
    
    extract_links(url)
    download_files(links, folder, base_url)


if __name__ == "__main__":
    main()