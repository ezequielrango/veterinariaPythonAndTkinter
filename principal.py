import tkinter as tk
from tkinter import ttk
def abrir_ventana_clientes():
        # Crear una ventana secundaria.
    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.title("Ventana clientes")
    ventana_secundaria.config(width=300, height=200)
        # Crear un botón dentro de la ventana secundaria
        # para cerrar la misma.
    boton_cerrar = ttk.Button(
        ventana_secundaria,
        text="Volver", 
        command=ventana_secundaria.destroy
        )
    boton_cerrar.place(x=75, y=75)
    # Crear la ventana principal.

def abrir_ventana_productos():
        # Crear una ventana secundaria.
    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.title("Ventana productos")
    ventana_secundaria.config(width=300, height=200)
        # Crear un botón dentro de la ventana secundaria
        # para cerrar la misma.
    boton_cerrar = ttk.Button(
        ventana_secundaria,
        text="Volver", 
        command=ventana_secundaria.destroy
        )
    boton_cerrar.place(x=75, y=75)

def abrir_ventana_turnos():
        # Crear una ventana secundaria.
    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.title("Ventana Turnos")
    ventana_secundaria.config(width=300, height=200)
        # Crear un botón dentro de la ventana secundaria
        # para cerrar la misma.
    boton_cerrar = ttk.Button(
        ventana_secundaria,
        text="Volver", 
        command=ventana_secundaria.destroy
        )
    boton_anadir = ttk.Button(
        ventana_secundaria,
        text="Añadir", 
        
        )

    boton_cerrar.place(x=75, y=75)
    boton_anadir.place(x=150, y=75)
    # Crear la ventana principal.

ventana_principal = tk.Tk()
ventana_principal.config(width=900, height=500)
ventana_principal.title("Pets Python Code")
# Crear un botón dentro de la ventana principal
# que al ejecutarse invoca a la función
# abrir_ventana_secundaria().
boton_abrirClientes = ttk.Button(
    ventana_principal,
    text="Clientes",
    command=abrir_ventana_clientes
)

boton_abrirProductos = ttk.Button(
    ventana_principal,
    text="Productos",
    command=abrir_ventana_productos
)

boton_turnos = ttk.Button(
    ventana_principal,
    text="Turnos",
    command=abrir_ventana_productos
)

boton_abrirClientes.place(x=300, y=100)
boton_abrirProductos.place(x=500, y=100)
boton_turnos.place(x=400, y=300)
ventana_principal.mainloop()