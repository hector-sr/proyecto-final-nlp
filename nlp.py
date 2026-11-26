
def eliminacion_Stopwords(texto):
    limpio = texto.lower().replace(",", "").replace(".","").replace("?","").replace("¿","").replace("!","").replace("¡","")
    stopwords = set(["el", "la", "los", "las", "de", "en", "y", "que", "un", "una", "con", "por", "a"])
    sin_stopworks=[]
    for palabra in limpio.split():
        if palabra not in stopwords:
            sin_stopworks.append(palabra)
    return sin_stopworks

def palabras_masrepetidas(textolimpio):
    conteo = dict()
    palabras2 = limpio.split()

    for palabra in palabras2:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1

    top5 = []

    for rep in range(5):
        mayor = 0
        palabra_mayor = ""

        for palabra in conteo:
            if conteo[palabra] > mayor:
                mayor = conteo[palabra]
                palabra_mayor = palabra

        

        top5.append([palabra_mayor, mayor])
        del conteo[palabra_mayor]

    return top5


#def diversidad_lexica (texto):
def TTR(texto:str) -> int:
    Palabras_unicas=len(set(eliminacion_Stopwords(texto)))
    Palabras_Tsinstop=len(eliminacion_Stopwords(texto))
    return Palabras_unicas/Palabras_Tsinstop
