import tkinter as tk
from tkinter import ttk
from anadirProducto import abrir_anadir_Producto

def abrir_ventana_productos():
    # Crear una ventana
    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.title("Ventana productos")
    ventana_secundaria.config(width=900, height=500, bg="grey")

    def mostrarMedicamentos():
        for i in range(4):
            frame = tk.Frame(ventana_secundaria, width=600, height=50, bg="white")
            frame.place(x=150, y=100 + i * 100)

            label1 = tk.Label(frame, text=f"Producto {i + 1}", font=("Helvetica", 14), bg="white")
            label1.place(x=100, y=25, anchor="center")
            label2 = tk.Label(frame, text=f"Dosificación {i + 1}", font=("Helvetica", 14), bg="white")
            label2.place(x=500, y=25, anchor="center")

    def mostrarBell():
        for i in range(4):
            frame = tk.Frame(ventana_secundaria, width=600, height=50, bg="white")
            frame.place(x=150, y=100 + i * 100)

            label1 = tk.Label(frame, text=f"Producto Belleza {i + 1}", font=("Helvetica", 14), bg="white")
            label1.place(x=100, y=25, anchor="center")
            label2 = tk.Label(frame, text=f"Cantidad {i + 1}", font=("Helvetica", 14), bg="white")
            label2.place(x=500, y=25, anchor="center")

    boton_medicamentos = ttk.Button(
        ventana_secundaria,
        text="Medicamentos",
        width=50, 
        command=mostrarMedicamentos
    )

    boton_belleza = ttk.Button(
        ventana_secundaria,
        text="Belleza", 
        width=50, 
        command=mostrarBell
    )

    boton_medicamentos.place(x=120, y=40)
    boton_belleza.place(x=470, y=40)

    # Crear un botón dentro de la ventana
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
        command=abrir_anadir_Producto
        )
    boton_anadir.place(x=750, y=450)
