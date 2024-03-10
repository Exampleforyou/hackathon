import os
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_pdf(url, download_path):
    try:
        headers = {'User-Agent': UserAgent().random}
        response = requests.get(url, headers=headers, timeout=10, stream=True)

        if response.status_code == 200:
            with open(download_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        file.write(chunk)
            print(f"Downloaded: {url}")
        else:
            print(f"Failed to download {url}. Status code: {response.status_code}")

    except Exception as e:
        print(f"Error downloading {url}: {e}")

base_url = 'http://www.cbr.ru/Queries/UniDbQuery/File/90134/'
download_path = "XsltBlock"
num_of_files = 4000

if not os.path.exists(download_path):
    os.makedirs(download_path)

#pdf_links = [base_url + str(i) for i in range(14, 2308)]
pdf_links = [
"https://www.cbr.ru/Queries/XsltBlock/File/90538/5206",
"https://www.cbr.ru/Queries/XsltBlock/File/90538/5206/note",
"https://www.cbr.ru/Queries/XsltBlock/File/90538/5205",
"https://www.cbr.ru/Queries/XsltBlock/File/90538/5205/note",
"https://www.cbr.ru/Queries/XsltBlock/File/90538/5204",
"https://www.cbr.ru/Queries/XsltBlock/File/90538/5204/note",
"https://www.cbr.ru/Queries/XsltBlock/File/90538/5203",
"https://www.cbr.ru/Queries/XsltBlock/File/90538/5203/note",
"https://www.cbr.ru/Queries/XsltBlock/File/90538/5202",
"https://www.cbr.ru/Queries/XsltBlock/File/90538/5202/note",
"https://www.cbr.ru/Queries/XsltBlock/File/90538/5201",
"https://www.cbr.ru/Queries/XsltBlock/File/90538/5201/note",
"https://www.cbr.ru/Queries/XsltBlock/File/90538/5200/comment",
"https://www.cbr.ru/Queries/XsltBlock/File/90538/5199/comment",
"https://www.cbr.ru/Queries/XsltBlock/File/90538/5198",
"https://www.cbr.ru/Queries/XsltBlock/File/90538/5198/note",
"https://www.cbr.ru/Queries/XsltBlock/File/90538/5197",
"https://www.cbr.ru/Queries/XsltBlock/File/90538/5197/note",
"https://www.cbr.ru/Queries/XsltBlock/File/90538/5151/comment",
"https://www.cbr.ru/Queries/XsltBlock/File/90538/5139/comment",
"https://www.cbr.ru/Queries/XsltBlock/File/90538/5138/comment",

]

counter = 0
for i, pdf_link in enumerate(pdf_links, start=1):
  if counter < 10000:
    filename = f"{pdf_link[pdf_link.rfind('/')+1:]}.pdf"
    download_path_file = os.path.join(download_path, filename)
    download_pdf(pdf_link, download_path_file)
    counter += 1
  else:
    break