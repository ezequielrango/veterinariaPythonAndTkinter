import tkinter as tk
from tkinter import ttk
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from controller import *
from db_connector import DBConnector
from productos import Producto
from producto_repositorio import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:/Users/Usuario/Desktop/TPFinal/veterinariaPythonAndTkinter/images")
# G:\TECNICATURA EN DESARROLLO DE SOFTWARE\PROGRAMACIONFINAL\veterinariaPythonAndTkinter\view\images
# C:\Users\Usuario\Desktop\TPFinal\veterinariaPythonAndTkinter\view\images

db_connector = DBConnector() 
repo = ProductoRepository(db_connector)  

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def agregar_cliente():
    nombre = entry_nombre.get()
    cantidad = entry_cantidad.get()
    
    if nombre and cantidad:
        label_mensaje.config(text="")

        # Crear un cliente con los valores ingresados
        producto = Producto(
            nombre,
            cantidad,
        )

        print(producto)
        
        # Guardar el cliente en la base de datos
        repo.guardar_producto(producto)

        # Actualizar la tabla con los datos del cliente
        actualizar_tabla(producto)
        
        # Limpiar los campos de entrada después de agregar un cliente
        entry_nombre.delete(0, "end")
        entry_cantidad.delete(0, "end")
      
        label_mensaje.config(text="Producto creado", bg="green")

    else:
        label_mensaje.config(text="Por favor, complete todos los campos.", bg="red")

def editar_producto():
    selected_item = tabla_productos.selection()
    if selected_item:
        label_mensaje.config(text="")
        
        # Obtener los valores actuales de la fila seleccionada
        valores_actuales = tabla_productos.item(selected_item)["values"]

    print(valores_actuales)
    # Mostrar los valores actuales en los campos de entrada
    entry_nombre.delete(0, tk.END)
    entry_nombre.insert(0, valores_actuales[0])

    entry_cantidad.delete(0, tk.END)
    entry_cantidad.insert(0, valores_actuales[1])

window = Tk()
window.title("Productos")
window.geometry("1000x600")
window.resizable(False, False) 

# Cargar una imagen para el icono
icono = PhotoImage(file=relative_to_assets("perrito.png"))
window.iconphoto(False, icono)

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    500.0,
    300.0,
    image=image_image_1
)

def actualizar_tabla(producto):
    tabla_productos.insert("", "end", values=(
        producto.get_nombre(), 
        producto.get_cantidad(),
    ))

# Frame para botones
frame_botones = tk.Frame(window, bg="#9E02B8")
frame_botones.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

boton_agregar = tk.Button(frame_botones,bg="white", text="Agregar Producto", command=agregar_cliente)
boton_eliminar = tk.Button(frame_botones,bg="white", text="Editar Medicamento", command=editar_producto)

boton_agregar.pack(side=tk.LEFT, padx=5)
boton_eliminar.pack(side=tk.LEFT, padx=5)

# Crear la tabla de productos
tabla_productos = ttk.Treeview(window, columns=("Nombre", "Cantidad"), height=20)
tabla_productos.heading("#1", text="Nombre", anchor=tk.W)
tabla_productos.heading("#2", text="Cantidad", anchor=tk.W)

# Cambiar el color de fondo y fuente de las etiquetas de encabezado de columna usando un estilo personalizado
style = ttk.Style()
style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"))
style.configure("Treeview", background="lightgray")

tabla_productos.pack()

label_mensaje = tk.Label(window, fg="white", bg="red")
label_mensaje.pack()

# Crear un estilo para el fondo del marco
style = ttk.Style()
style.configure("TFrame", background="#9E02B8")

# Crear un marco para las etiquetas e entradas
frame_etiquetas_entradas = ttk.Frame(window, style="TFrame")
frame_etiquetas_entradas.pack(side=tk.TOP, fill=tk.BOTH, padx=10, pady=10)

# ...
frame_etiquetas_entradas.configure(style="Color.TFrame")
style = ttk.Style()
style.configure("Color.TFrame", background="#9E02B8")
# ...
# Etiquetas en la columna izquierda
label_nombre = tk.Label(frame_etiquetas_entradas, text="Nombre:")
label_nombre.grid(row=0, column=0, padx=5, pady=5, sticky="w")
label_cantidad = tk.Label(frame_etiquetas_entradas, text="Cantidad:")
label_cantidad.grid(row=1, column=0, padx=5, pady=5, sticky="w")


# Entradas en la columna derecha
entry_nombre = tk.Entry(frame_etiquetas_entradas, width=20)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)
entry_cantidad = tk.Entry(frame_etiquetas_entradas, width=20)
entry_cantidad.grid(row=1, column=1, padx=5, pady=5)

for producto in repo.listar_productos():
    actualizar_tabla(producto)


# ...

window.mainloop()