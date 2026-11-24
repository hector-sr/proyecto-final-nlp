with open("texto_prueba.txt", "r", encoding = "utf-8") as archivo:
    texto = archivo.read()

print(texto)
import estadisticas 
import sentimiento

print("Total de palabras:", estadisticas.contar_palabras(texto))
print("Total de caracteres con espacios", estadisticas.contar_caracteres_con_espacios(texto))
print("Total de caracteres sin espacios", estadisticas.contar_caracteres_sin_espacios(texto))
print("Total de oraciones", estadisticas.contar_oraciones(texto))
print("Longitud promedio de palabras", estadisticas.lon_promedio_palabras(texto))
print("Longitud promedio de oraciones", estadisticas.lon_promedio_oraciones(texto))
print("Si", sentimiento.palabras_masrepetidas(texto))
print("Sentimiento", sentimiento.sentir(texto))
