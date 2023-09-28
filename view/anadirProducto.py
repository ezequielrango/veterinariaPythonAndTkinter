import tkinter as tk
from tkinter import ttk

def abrir_anadir_Producto():
    # Crear una ventana
    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.title("Ventana añadir")
    ventana_secundaria.config(width=900, height=500)
        # Crear un botón dentro de la ventana
        # para cerrar la misma.
    boton_cerrarAn = ttk.Button(
        ventana_secundaria,
        text="Volver", 
        command=ventana_secundaria.destroy
        )
    boton_cerrarAn.place(x=10, y=10)