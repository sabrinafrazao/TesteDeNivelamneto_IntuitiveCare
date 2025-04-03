import os
import requests

folder = r"WebScraping\resources\attachment"

def download_files(links,folder, base_url):
    """Downloads PDF files from the provided links and saves them in the specified folder."""

    os.makedirs(folder, exist_ok=True)

    for link in links:
        full_url = link if link.startswith("http") else base_url + link
        response = requests.get(full_url)

        if response.status_code == 200 and response.headers.get("Content-Type") == "application/pdf":
            
            successful_downloads += 1

            path_files = os.path.join(folder, f"Anexo_{successful_downloads}.pdf")

            with open(path_files, "wb") as f:
                f.write(response.content)
            print(f"Downloaded: {path_files}")
        else:
            print(f"Error downloading {full_url} or file is not a valid PDF.")
