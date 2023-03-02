from xml.dom.minidom import parse
import time

Document = parse('map.osm')
inicio = time.time()
print("Iniciando o parse DOM...")
for n in Document.getElementsByTagName("node"):
    tipo = ""
    nome = "";
    temTipo = False;
    temNome = False;
    for tag in n.getElementsByTagName("tag"):
        if (tag.getAttribute("k")=="amenity"):
            tipo =tag.getAttribute("v")
            temTipo = True
        if (tag.getAttribute("k")=="name"):
            nome =tag.getAttribute("v")
            temNome = True
    if (temTipo == True and temNome == True):
    	print("Nome: ", nome, "/Tipo: ", tipo, "/Latitude: ", n.getAttribute("lat"), "/Longitude: ", n.getAttribute("lon"))
fim = time.time()
print("Tempo de execução: ",fim - inicio)