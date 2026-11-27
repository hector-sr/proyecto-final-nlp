import estadisticas
import nlp
import sentimiento
import tkinter as tk
from tkinter import filedialog


def seleccionar_archivo(titulo: str = "Selecciona un archivo", tipos_archivo: list[tuple[str, str]] | None = None) -> str:
    """
    Abre el explorador de archivos para elegir un único archivo y devuelve su ruta.
    Si el usuario cancela la selección, devuelve una cadena vacía "".
    """
    if tipos_archivo is None:
        tipos_archivo = [("Todos los archivos", "*.*")]

    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal vacía de Tkinter
    root.attributes("-topmost", True)  # Intenta mostrar el diálogo al frente

    ruta_archivo = filedialog.askopenfilename(
        title=titulo,
        filetypes=tipos_archivo,
    )

    root.destroy()
    return ruta_archivo

def resultados(texto:str):
    print("Total de palabras:", estadisticas.contar_palabras(texto))
    print("Total de caracteres con espacios", estadisticas.contar_caracteres_con_espacios(texto))
    print("Total de caracteres sin espacios", estadisticas.contar_caracteres_sin_espacios(texto))
    print("Total de oraciones", estadisticas.contar_oraciones(texto))
    print("Longitud promedio de palabras", estadisticas.lon_promedio_palabras(texto))
    print("Longitud promedio de oraciones", estadisticas.lon_promedio_oraciones(texto))
    print("Sentimiento:", sentimiento.sentir(texto))
    print("Las 5 palabras más repetidas son:", nlp.palabras_masrepetidas(texto))
    print("Diversidad léxica (TTR):", nlp.TTR(texto))
