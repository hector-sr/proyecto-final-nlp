import auxiliar

ruta = auxiliar.seleccionar_archivo()
with open (ruta, "r") as file:
    texto = file.read()

if texto.replace(" ", "").replace("\n", "") == "":
    print("El texto es un texto vacio")
#else:


