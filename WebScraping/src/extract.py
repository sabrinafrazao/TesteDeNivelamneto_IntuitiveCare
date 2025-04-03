import requests
from bs4 import BeautifulSoup


url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"


def extract_links(url):

    response = requests.get(url)

    keyword = ["Anexo I", "Anexo II"]

    soup = BeautifulSoup(response.text, "html.parser")
    links = []

    for link in soup.find_all("a", href=True):
        if any(word in link.get_text(strip=True) for word in keyword):
            links.append(link["href"])


    return links
