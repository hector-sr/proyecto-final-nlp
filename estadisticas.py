def contar_palabras(texto):
    limpio = texto.lower().replace(",", "").replace(".","").replace("?","").replace("¿","").replace("!","").replace("¡","")
    palabras = limpio.split()
    return len(palabras)



def contar_caracteres_con_espacios(texto):
    return len(texto)



def contar_caracteres_sin_espacios(texto):
    sin_espacios = texto.replace(" ", "").replace("\n", "")
    return len(sin_espacios)



def contar_oraciones(texto):
    solo_puntos = texto.replace("!", ".").replace("?", ".")
    oraciones = solo_puntos.split(".")
    if solo_puntos[-1] != ".":
       return len(oraciones) 
    else:
       return len(oraciones)-1



def lon_promedio_palabras(texto):
    caracteres = contar_caracteres_sin_espacios(texto)
    palabras = contar_palabras(texto)
    return round(caracteres/palabras)



def lon_promedio_oraciones(texto):
    oraciones = contar_oraciones(texto)
    palabras = contar_palabras(texto)
    return round(palabras/oraciones)
