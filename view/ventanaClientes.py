import tkinter as tk
from tkinter import ttk
from anadirCliente import abrir_anadir_cliente

def abrir_ventana_clientes():
        # Crear una ventana secundaria.
    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.title("Ventana clientes")
    ventana_secundaria.config(width=900, height=500)
    
        # Crear un botón dentro de la ventana secundaria
        # para cerrar la misma.
    boton_cerrar = ttk.Button(
        ventana_secundaria,
        text="Volver", 
        command=ventana_secundaria.destroy
        )
    boton_cerrar.place(x=10, y=10)

    boton_anadir = ttk.Button(
        ventana_secundaria,
        text="Añadir", 
        command=abrir_anadir_cliente
        )
    
    boton_anadir.place(x=750, y=450)
    # Crear la ventana principal.
