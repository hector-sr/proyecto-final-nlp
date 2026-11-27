import auxiliar

ruta = auxiliar.seleccionar_archivo()
with open (ruta, "r", encoding="utf-8") as file:
    texto = file.read()

if texto.replace(" ", "").replace("\n", "") == "":
    print("El texto es un texto vacio")
else:
    auxiliar.resultados(texto)


