def sentir(texto:str)-> str:
    positivas = {
    "feliz": 5, "felicidad": 10, "alegria": 9, "amor": 10, "carino": 7, "hermoso": 6, "bonito": 5, "amistad": 8, "esperanza": 7, "sonrisa": 6,
    "bondad": 7, "maravilloso": 9, "agradable": 5, "tranquilo": 4, "diversion": 7, "exito": 9, "generoso": 6, "amable": 6, "emocion": 7, "precioso": 8,
    "admirable": 7, "encantador": 8, "optimismo": 8, "positivo": 6, "contento": 7, "satisfecho": 6, "orgulloso": 7, "agradecido": 8, "ilusion": 7, "paz": 8,
    "pasion": 8, "ternura": 7, "divertido": 6, "excelente": 9, "perfecto": 9, "genial": 8, "fantastico": 9, "increible": 8, "extraordinario": 9, "victoria": 8,
    "triunfo": 9, "logro": 7, "superacion": 8, "motivacion": 7, "inspiracion": 8, "confianza": 7, "respeto": 7, "compasion": 7, "solidaridad": 8, "apoyo": 6,
    "compania": 6, "felicitar": 7, "celebrar": 7, "reir": 6, "sonreir": 7, "abrazar": 6, "cuidar": 6, "proteger": 6, "ayudar": 7, "compartir": 6,
    "disfrutar": 7, "encantado": 8, "emocionado": 8, "maravilla": 9, "belleza": 8, "dulzura": 7, "calma": 6, "serenidad": 7, "libertad": 8, "amistoso": 7,
    "honesto": 7, "leal": 7, "valiente": 8, "fuerte": 6, "capaz": 6, "brillante": 8, "creativo": 7, "inteligente": 7, "sabiduria": 8, "salud": 8,
    "bienestar": 9, "prosperidad": 8, "riqueza": 6, "abundancia": 7, "suerte": 7, "bendicion": 8, "regalo": 6, "aventura": 7, "divino": 8, "luminoso": 7,
    "agradablemente": 5, "paciencia": 6, "tolerancia": 7, "empatia": 8, "inclusivo": 7, "esperanzador": 8, "reconocimiento": 7, "sorprendente": 8, "encanto": 8, "apasionante": 8}

    negativas = {
    "triste": -5, "tristeza": -8, "odio": -10, "sufrir": -8, "cruel": -7, "miedo": -6, "soledad": -9, "hambre": -4, "dolor": -8, "rechazo": -7,
    "llorar": -5, "terrible": -9, "feo": -3, "enojado": -6, "desprecio": -10, "abandonado": -8, "preocupado": -5, "desgracia": -9, "fracaso": -8, "decepcion": -7,
    "infeliz": -9, "angustia": -8, "ansiedad": -7, "desesperacion": -10, "frustracion": -7, "enojo": -7, "ira": -9, "rabia": -9, "rencor": -8, "resentimiento": -8,
    "envidia": -6, "celos": -5, "mentira": -7, "traicion": -10, "engaño": -8, "injusticia": -9, "violencia": -10, "agresion": -9, "maltrato": -10, "abuso": -10,
    "insulto": -8, "humillacion": -9, "discriminacion": -9, "desigualdad": -8, "pobreza": -7, "miseria": -9, "enfermedad": -7, "debilidad": -5, "cansancio": -4, "agotamiento": -6,
    "aburrimiento": -4, "desinteres": -5, "desmotivacion": -7, "pesimismo": -8, "desconfianza": -7, "incertidumbre": -5, "inseguridad": -7, "peligro": -8, "amenaza": -9, "riesgo": -6,
    "muerte": -10, "perdida": -8, "duelo": -8, "despedida": -6, "ausencia": -6, "vacío": -7, "desamparo": -9, "desilusion": -7, "descontento": -6, "insatisfaccion": -7,
    "mediocre": -5, "horrible": -9, "espantoso": -9, "asqueroso": -9, "repugnante": -9, "lamentable": -8, "desastroso": -9, "negativo": -6, "malo": -5, "peor": -7,
    "terriblemente": -8, "molesto": -6, "irritado": -6, "furioso": -9, "desesperado": -9, "desconsolado": -9, "abatido": -7, "deprimido": -9, "melancolia": -7, "nostalgia": -3,
    "culpa": -6, "vergüenza": -6, "arrepentimiento": -6, "remordimiento": -7, "fracasar": -8, "perder": -5, "rechazar": -7, "lastimar": -8, "herir": -8}


    feliz = 0
    triste = 0
    limpio = texto.lower().replace(",", "").replace(".","").replace("?","").replace("¿","").replace("!","").replace("¡","")

    
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
    

