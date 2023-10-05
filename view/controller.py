
import subprocess

class Controller():

    def abrirVentanaClientes(self):
        # Ruta al script que deseas abrir
        script_path = 'C:/Users/Usuario/Desktop/TPFinal/veterinariaPythonAndTkinter/view/ventanaClientes.py'

        # Ejecutar el script usando subprocess
        subprocess.Popen(["python", script_path])

    def abrirVentanaProductos(self):
        # Ruta al script que deseas abrir
        script_path = 'C:/Users/Usuario/Desktop/TPFinal/veterinariaPythonAndTkinter/view/ventanaProductos.py'

        # Ejecutar el script usando subprocess
        subprocess.Popen(["python", script_path])