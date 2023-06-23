import os


diretório = os.path.dirname(__file__)
name_arq = os.path.basename(diretório)
diretório_raiz= diretório[:-len(name_arq)]
print(diretório_raiz)