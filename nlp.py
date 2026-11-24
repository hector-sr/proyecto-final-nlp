
def eliminacion_Stopwords(texto):
    limpio = texto.lower().replace(",", "").replace(".","").replace("?","").replace("¿","").replace("!","").replace("¡","")
    stopwords = set(["el", "la", "los", "las", "de", "en", "y", "que", "un", "una", "con", "por", "a"])
    sin_stopworks=[]
    for palabra in limpio.split():
        if palabra not in stopwords:
            sin_stopworks.append(palabra)
    return sin_stopworks

def palabras_masrepetidas(texto):
    limpio = texto.lower().replace(",", "").replace(".","").replace("?","").replace("¿","").replace("!","").replace("¡","")
    conteo=dict()
    palabras2=limpio.split()
    for palabra in palabras2 :
        if palabra in conteo:
            conteo[palabra]+=1
        else:
            conteo[palabra]=1
    return conteo

#def diversidad_lexica (texto):
