import requests
from bs4 import BeautifulSoup

link = 'https://mangalivre.net/'
link = requests.get(link)
soup = link.text

soup = BeautifulSoup(soup, 'html.parser')
# soup = soup.prettify()
for soups in soup:
    print(soup.find_all('div'))
    continue
