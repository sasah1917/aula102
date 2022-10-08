import os
import shutil

origem = "C:/Users/sarah/Desktop/Curso programação/byjus/aleatorias"
destino = "C:/Users/sarah/Desktop/Curso programação/byjus/receber"

listaDosArquivos = os.listdir(origem)
#print(listaDosArquivos)

for fileName in listaDosArquivos:
    name, extension = os.path.splitext(fileName)

    if extension == "":
        continue
    if extension in ['.png', '.gif', '.jpg', '.jpeg', '.jfif', '.pptx']:
        path1 = origem + "/" + fileName
        path2 = destino + "/" + "nova pasta"
        path3 = destino + "/" + "nova pasta" + "/" + fileName

    if os.path.exists(path2):
        print("movendo arquivos " +  fileName + "...")
        shutil.move(path1, path3)
    else: 
        os.mkdir(path2)
        print("movendo arquivos " +  fileName + "...")
        shutil.move(path1, path3)