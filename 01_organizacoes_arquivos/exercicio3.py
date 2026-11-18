import os
import shutil

pasta_destino='pratica2'

if not os.path.exists(pasta_destino):
    os.makedirs("pratica2")

arquivos=os.listdir()
for arquivo in arquivos:
    if arquivo.endswith(".txt"):
        origem = arquivo
        destino = os.path.join(pasta_destino)
        shutil.move(origem,destino)
        print("rodou")
