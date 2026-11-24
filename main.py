with open("texto_prueba.txt", "r", encoding = "utf-8") as archivo:
    texto = archivo.read()

if texto.replace(" ", "").replace("\n", "") == "":
    print("El texto es un texto vacio")
#else:


