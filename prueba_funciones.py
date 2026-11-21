with open("texto_prueba.txt", "r") as archivo:
    texto = archivo.read()

print(texto)
import estadisticas 

print("Total de palabras:", estadisticas.contar_palabras(texto))
print("Total de caracteres con espacios", estadisticas.contar_caracteres_con_espacios(texto))
#print("Total de caracteres sin espacios", estadisticas.contar_caracteres_sin_espacios(texto))
#print("Total de oraciones", estadisticas.contar_oraciones(texto))