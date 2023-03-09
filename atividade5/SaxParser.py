from html.parser import HTMLParser
import urllib.request

class MyHTMLParser(HTMLParser):
  def __init__(self):
    super().__init__()
    self.currentData = ""
    self.title = ""
    self.image = ""

  def handle_starttag(self, tag, attrs):
    self.currentData = ""
    
    if tag =="img":  
      for k, v in attrs:
        if k == "src":
          self.image = v

  def handle_endtag(self, tag):
    if tag =="title": 
      self.title = self.currentData      

  def handle_data(self, data):
    self.currentData += data    

arquivo = open("seeds.txt","r")
for linha in arquivo.readlines():
    page = urllib.request.urlopen(linha)
    parser = MyHTMLParser()
    parser.feed(str(page.read().decode('utf-8')))
    print("Título:", parser.title)
    print("Imagem:", parser.image)
    
    
