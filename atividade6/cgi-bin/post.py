#coding: utf8
import os, cgi
from datetime import datetime

form = cgi.FieldStorage()
data = datetime.now()
autor = form["autor"].value 
mensagem = form["mensagem"].value

print(autor)
print(mensagem)
print(data)
arquivo = open("cgi-bin/mensagens.txt", "a")
arquivo.write("Envio da mensagem:  "+data)
arquivo.write("Autor: "+autor)
arquivo.write("Mensagem: "+mensagem)
arquivo.write("----------------------------------")