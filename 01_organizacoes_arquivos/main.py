import os
import shutil

pasta_destino="pdf_organizado"

if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)
    print("pasta criada!")

arquivos=os.listdir()
for arquivo in arquivos:
    if arquivo.endswith(".pdf"):
     origem=arquivo
     destino=os.path.join(pasta_destino,arquivo)
     shutil.move(origem, destino)
     print("Rodou")
