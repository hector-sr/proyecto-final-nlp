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