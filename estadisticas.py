def contar_palabras(texto:str) -> int:
    """Limpia los signos de puntuación básicos y devuelve el total de palabras del texto"""
    limpio = texto.lower().replace(",", "").replace(".","").replace("?","").replace("¿","").replace("!","").replace("¡","")
    palabras = limpio.split()
    return len(palabras)



def contar_caracteres_con_espacios(texto:str) -> int:
    """Calcula el número total de caracteres del texto, incluyendo espacios y puntuación"""
    return len(texto)



def contar_caracteres_sin_espacios(texto:str)->int:
    """Calcula el total de caracteres del texto ignorando espacios en blanco y saltos de línea"""
    sin_espacios = texto.replace(" ", "").replace("\n", "")
    return len(sin_espacios)



def contar_oraciones(texto:str)->int:
    """Cuenta el total de oraciones separadas por puntos, signos de exclamación o interrogación"""
    solo_puntos = texto.replace("!", ".").replace("?", ".")
    oraciones = solo_puntos.split(".")
    if solo_puntos[-1] != ".":
       return len(oraciones) 
    else:
       return len(oraciones)-1



def lon_promedio_palabras(texto:str)->int:
    """Calcula la longitud promedio de caracteres por palabra y devuelve la cantidad redondeada"""
    caracteres = contar_caracteres_sin_espacios(texto)
    palabras = contar_palabras(texto)
    return round(caracteres/palabras)



def lon_promedio_oraciones(texto:str)->int:
    """Calcula la longitud promedio de caracteres por oración y devuelve la cantidad redondeada"""
    oraciones = contar_oraciones(texto)
    palabras = contar_palabras(texto)
    return round(palabras/oraciones)
