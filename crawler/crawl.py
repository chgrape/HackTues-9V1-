from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urlparse
import urllib.request
import requests


#URLte trqbva da se upravqt
#biblioteka urlparse
# ...



used = dict()
urls = []


text_file = open('text.txt', 'at') 

with open('urls.txt', 'rt') as url_file:
    for line in url_file.readlines():
        urls.append(line.strip())       

url_file = open('urls.txt', 'at')

for url in urls:
    used[url] = True


def getText(soup):    
    for script in soup(["script", "style"]):
         script.extract() 

    text = soup.get_text()
    
    lines = (line.strip() for line in text.splitlines())   
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    
    text = '\n'.join(chunk for chunk in chunks if chunk)
    text_file.write(text)



def getData(URL):
    url_file.write(URL+'\n')
    used[URL] = True

    html_page = urllib.request.urlopen(URL)
    soup = BeautifulSoup(html_page, "html.parser")
    
    getText(soup)

    for link in soup.findAll('a'): 
        URL = link.get('href')
        if URL and not URL.startswith('#'):
            if not URL.startswith(DOMAIN):
                URL = DOMAIN + URL
            if used.get(URL):
                continue
            getData(URL)  



DOMAIN = "https://dir.bg/"
START_URL = "https://dir.bg/"

getData(START_URL)
