import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from urllib.request import urlretrieve


def download_webpage(url, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        with open(
            os.path.join(output_folder, "index.html"), "w", encoding="utf-8"
        ) as html_file:
            html_file.write(response.text)

        for css_link in soup.find_all("link", {"rel": "stylesheet"}):
            css_url = urljoin(url, css_link["href"])
            css_filename = os.path.join(output_folder, os.path.basename(css_url))
            urlretrieve(css_url, css_filename)

        for script_tag in soup.find_all("script", {"src": True}):
            js_url = urljoin(url, script_tag["src"])
            js_filename = os.path.join(output_folder, os.path.basename(js_url))
            urlretrieve(js_url, js_filename)

        for img_tag in soup.find_all("img", {"src": True}):
            img_url = urljoin(url, img_tag["src"])
            img_filename = os.path.join(output_folder, os.path.basename(img_url))
            urlretrieve(img_url, img_filename)

        print("Download complete.")
    else:
        print(f"Failed to download the webpage. Status code: {response.status_code}")


url_to_download = "https://askbootstrap.com/preview/groseri/intro.html"
output_directory = "downloaded_webpage"

download_webpage(url_to_download, output_directory)
