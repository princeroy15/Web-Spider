import requests
import re
import urllib.parse as urlparse

target_url = "http://10.0.2.12/mutillidae/"
target_link = []

def extract_link_from(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', response.content.decode(errors="ignore"))

def crawl(url):
    href_link = extract_link_from(url)
    for link in href_link:
        link = urlparse.urljoin(url, link)

        if "#" in link:
            link = link.split("#")[0]

        if target_url in link and link not in target_link:
            target_link.append(link)
            print(link)
            crawl(link)

crawl(target_url)