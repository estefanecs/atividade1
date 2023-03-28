#coding: utf8
import os, cgi
from datetime import datetime

form = cgi.FieldStorage()
data = datetime.now()
autor = form["autor"].value 
mensagem = form["mensagem"].value

arquivo = open("cgi-bin/mensagens.txt", "a")
arquivo.write("Envio da mensagem:  "+data)
arquivo.write("Autor: "+autor)
arquivo.write("Mensagem: "+mensagem)
arquivo.write("----------------------------------")

print ("Content-type: text/html;charset=utf-8")
print ("<html><head><title>Atividade 6</title></head><body>")
print("<h2 Align=\"center\">ENVIO DE MENSAGEM</h2>")
print("<form method=“POST” action=\"./cgi-bin/post.py\">")
print("Autor:")
print("<br>")
print("<input type=“text” name=“autor” placeholder=\"Autor\">")
print("<br>")
print("Mensagem:")
print("<br>")
print("<textarea name=“mensagem” placeholder=\"Digite aqui a sua mensagem\" rows=\"4\" cols=\"50\"></textarea>")
print("<br>")
print("<br>")
print("<button type=“submit” name=“btn”>Enviar</button>")
print("<input type=\"reset\">")
print("</form>")
print("</body>")

print ("Autor: "+ autor + "<br>")
print ("Mensagem: " +mensagem+ "<br>")
print ("Data/Hora envio: " +data+ "<br>")
print ("</body></html>")
