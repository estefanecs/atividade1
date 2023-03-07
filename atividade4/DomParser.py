from xml.dom.minidom import parse
import time
import json

pontos = dict()
list = []

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
        lat = n.getAttribute("lat");
        lon = n.getAttribute("lon");
        feature = dict();
        geometry = dict();
        properties = dict();
        properties["nome"] = nome
        properties["tipo"]= tipo
        geometry["type"]= "Point"
        geometry["coordinates"]= [float(lon),float(lat)]
        feature["type"]="Feature"
        feature["geometry"]= geometry
        feature["properties"]= properties
        list.append(feature)
        
fim = time.time()
print("Tempo de execução: ",fim - inicio)

pontos["type"]="FeatureCollection"
pontos["features"]=list
jsonStr = json.dumps(pontos, indent=4, ensure_ascii=False)
arquivo = open("pontos.json", "x")
arquivo.write(jsonStr)