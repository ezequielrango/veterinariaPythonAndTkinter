import tkinter as tk
from tkinter import ttk
from anadirTurno import abrir_anadir_turno

def abrir_ventana_turnos():
        # Crear una ventana.
    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.title("Ventana Turnos")
    ventana_secundaria.config(width=900, height=500)
        # Crear un botón dentro de la ventana
        # para cerrar la misma.
    boton_cerrar = ttk.Button(
        ventana_secundaria,
        text="Volver", 
        command=ventana_secundaria.destroy
        )
    
        # Boton para añadir turnos
    boton_anadir = ttk.Button(
        ventana_secundaria,
        text="Añadir", 
        command=abrir_anadir_turno
        )
    boton_anadir.place(x=750, y=450)

    boton_cerrar.place(x=10, y=10)

