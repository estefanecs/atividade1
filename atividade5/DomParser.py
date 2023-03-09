import urllib.request
import os
from bs4 import BeautifulSoup

arquivo = open("seeds.txt","r");
for linha in arquivo.readlines():
  print(linha)
  page = urllib.request.urlopen(linha)

  html = str(page.read().decode('utf-8'))

  soup = BeautifulSoup(html, 'lxml')

  print("Título:", soup.title.string)
  for img in soup.find_all('img'):
    print("src: ", img.attrs.get("src"))
    break

