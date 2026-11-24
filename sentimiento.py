def palabras_masrepetidas(textolimpio):
    conteo=dict()
    palabras2=limpio.split()
    for palabra in palabras2 :
        if palabra in conteo:
            conteo[palabra]+=1
        else:
            conteo[palabra]=1
    return conteo
            

print(palabras_masrepetidas(limpio))

def sentimiento(textolimpio):
    positivas = {
    "feliz": 5,
    "alegria": 8,
    "amor": 10,
    "carino": 7,
    "hermoso": 6,
    "amistad": 9,
    "esperanza": 4,
    "sonrisa": 3,
    "bondad": 6,
    "maravilloso": 9,
    "agradable": 4,
    "tranquilo": 2,
    "diversion": 7,
    "exito": 8,
    "generoso": 5,
    "amable": 3,
    "emocion": 6,
    "felicidad": 10,
    "precioso": 7,
    "admirable": 5
}
    negativas = {
    "triste": -5,
    "odio": -10,
    "sufrir": -8,
    "cruel": -7,
    "miedo": -6,
    "soledad": -9,
    "hambre": -4,
    "dolor": -8,
    "rechazo": -7,
    "llorar": -5,
    "terrible": -9,
    "feo": -3,
    "enojado": -6,
    "desprecio": -10,
    "abandonado": -8,
    "preocupado": -4,
    "desgracia": -9,
    "fracaso": -7,
    "decepcion": -6,
    "infeliz": -5
}
    feliz=0
    triste=0
    
    
    for palabra in limpio.split():
        if palabra in positivas:
            feliz=feliz+1
        elif palabra in negativas:
            triste=triste+1
    sen_texto=feliz-triste
    
    if sen_texto<0:
        return "Texto es negativo"
    elif sen_texto>0:
        return "Texto es positivo"
    else:
        return "El texto es neutral"
    
def eliminacion_Stopwords(textolimpio):
    stopwords = set(["el", "la", "los", "las", "de", "en", "y", "que", "un", "una", "con", "por", "a"])
    sin_stopworks=[]
    for palabra in limpio.split():
        if palabra not in stopwords:
            sin_stopworks.append(palabra)
    return sin_stopworks
                
print(eliminacion_Stopwords(limpio))
