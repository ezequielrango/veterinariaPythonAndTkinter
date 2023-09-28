from ventanaTurnos import abrir_ventana_turnos
from ventanaClientes import abrir_ventana_clientes
from ventanaProductos import abrir_ventana_productos
import tkinter as tk
from tkinter import ttk

# Crear la ventana principal.
ventana_principal = tk.Tk()
ventana_principal.config(width=900, height=500)
ventana_principal.title("Pets Python Code")

# Crear un botón dentro de la ventana principal
# que al ejecutarse invoca a la función
# abrir_ventana_clientes.
boton_abrirClientes = ttk.Button(
    ventana_principal,
    text="Clientes",
    command=abrir_ventana_clientes
)

# abrir_ventana_productos.

boton_abrirProductos = ttk.Button(
    ventana_principal,
    text="Productos",
    command=abrir_ventana_productos
)

# abrir_ventana_turnos.

boton_turnos = ttk.Button(
    ventana_principal,
    text="Turnos",
    command=abrir_ventana_turnos
)


boton_abrirClientes.place(x=300, y=100)
boton_abrirProductos.place(x=500, y=100)
boton_turnos.place(x=400, y=300)
ventana_principal.mainloop()