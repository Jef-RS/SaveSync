import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

diretorio_atual = os.getcwd()
import os

def buscar_arquivos_por_extensao(caminho, extensao):
    arquivos_encontrados = []

    # Percorre todos os arquivos e diretórios no caminho especificado
    for root, dirs, files in os.walk(caminho):
        for file in files:
            # Verifica se a extensão do arquivo corresponde à extensão procurada
            if file.endswith(extensao):
                # Retorna o caminho completo do arquivo encontrado
                caminho_arquivo = os.path.join(root, file)
                arquivos_encontrados.append(caminho_arquivo)

    # Retorna a lista de arquivos encontrados
    return arquivos_encontrados

# Exemplo de uso
caminho_documentos = os.path.expanduser("~\\Documents")
extensao_procurada = ".txt"

arquivos_encontrados = buscar_arquivos_por_extensao(caminho_documentos, extensao_procurada)

if arquivos_encontrados:
    print(f"Arquivos encontrados com a extensão '{extensao_procurada}':")
    for arquivo in arquivos_encontrados:
        print(arquivo)
else:
    print(f"Nenhum arquivo encontrado com a extensão '{extensao_procurada}'.")
