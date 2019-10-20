from bs4 import BeautifulSoup
import requests

source=requests.get('tagclub.in').text
soup=BeautifulSoup(source,'lxml')
article=soup.find('div',class_='small-margin').p.text
print(article)

