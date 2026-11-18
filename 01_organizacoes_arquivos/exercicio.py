import os
import shutil

pasta="pratica"

if not os.path.exists(pasta):
    os.makedirs(pasta)
    print("Pasta criada!")

arquivos = os.listdir()

for arquivo in arquivos:
    if arquivo.endswith('.txt'):
        origem=arquivo
        destino = os.path.join(pasta,arquivo)
        shutil.move(origem,destino)
        print('rodou')
