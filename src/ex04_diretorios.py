import os

def listar_diretorio(caminho, nivel=0):

    print("  " * nivel + os.path.basename(caminho))

    for item in os.listdir(caminho):

        completo = os.path.join(caminho, item)

        if os.path.isdir(completo):
            listar_diretorio(completo, nivel + 1)

        else:
            print("  " * (nivel + 1) + item)