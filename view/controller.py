
import subprocess

class Controller():

    def abrirVentanaClientes(self):
        # Ruta al script que deseas abrir
        script_path = 'G:/TECNICATURA EN DESARROLLO DE SOFTWARE/PROGRAMACIONFINAL/veterinariaPythonAndTkinter/view/ventanaClientes.py'
# G:/TECNICATURA EN DESARROLLO DE SOFTWARE/PROGRAMACIONFINAL/veterinariaPythonAndTkinter/view/images
# C:/Users/Usuario/Desktop/TPFinal/veterinariaPythonAndTkinter/view/images

        # Ejecutar el script usando subprocess
        subprocess.Popen(["python", script_path])


    def abrirVentanaProductos(self):
        # Ruta al script que deseas abrir
        script_path = 'G:/TECNICATURA EN DESARROLLO DE SOFTWARE/PROGRAMACIONFINAL/veterinariaPythonAndTkinter/view/ventanaProductos.py'
# G:/TECNICATURA EN DESARROLLO DE SOFTWARE/PROGRAMACIONFINAL/veterinariaPythonAndTkinter/view/images
# C:/Users/Usuario/Desktop/TPFinal/veterinariaPythonAndTkinter/view/images


        # Ejecutar el script usando subprocess
        subprocess.Popen(["python", script_path])