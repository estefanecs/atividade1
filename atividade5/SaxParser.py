from html.parser import HTMLParser
import urllib.request

tag = "<html>\n<head>\n<title>Atividade 5</title>\n</head>\n<body>\n<h1>Atividade 5</h1>\n"
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
  tag +='<h4>'+parser.title+'</h4>\n<p>'
  nomeImg = ""
  if len(parser.image)>0:
    if parser.image.__contains__("http") != True :
      image = parser.image.split("/")
      if len(image)==1:
        nomeImg = linha+"/"+parser.image
      elif "Atividade1" in parser.image or "Atividade 1" in parser.image or "atividade 1" in parser.image or "atividade1" in parser.image:
        if len(image)>1:
          nomeImg = linha+"/"+image[1]
      else:
        nomeImg = linha+parser.image
      print("imagem:",nomeImg)
      tag +='<img src="'+ nomeImg+'" width="400"></p>\n'
    else: 
      print("Imagem:", parser.image)
      tag +='<img src="'+ parser.image+'" width="400"></p>\n'

tag +="</body>\n</html>"
arquivoHtml = open("index.html","w")
arquivoHtml.write(tag)
arquivoHtml.close()
    
    
