import xml.sax

class Listener(xml.sax.ContentHandler):
  def __init__(self):
    self.currentData = ""
    self.latitude = ""
    self.longitude = ""
    self.nome = ""
    self.tipo = ""
    self.temNome = False
    self.temTipo = False

  def startElement(self, tag, attributes):    
    self.currentData = ""
    
    if tag =="node":  
      self.latitude = attributes.get("lat")  
      self.longitude = attributes.get("lon")

    if tag =="tag":
        if attributes.get("k") =="amenity":
              self.tipo = attributes.get("v")
              self.temTipo = True
        if attributes.get("k") =="name":
              self.nome = attributes.get("v")   
              self.temNome = True   
              
  def endElement(self, tag):    
    if tag =="nome":	
      if (self.temTipo == True and self.temNome == True):
            print("Nome: ", self.nome, "/Tipo: ", self.tipo, "/Latitude: ", self.latitude, "/Longitude: ", self.longitude("lon"))

  def characters(self, content):	
    self.currentData += content

parser =  xml.sax.make_parser()

Handler = Listener()
parser.setContentHandler(Handler)

print("Starting SAX Parser...")
parser.parse('map.osm')