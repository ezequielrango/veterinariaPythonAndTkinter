
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"G:\TECNICATURA EN DESARROLLO DE SOFTWARE\PROGRAMACIONFINAL\veterinariaPythonAndTkinter\images")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1000x600")
window.configure(bg = "#FFFFFF")


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

canvas.create_rectangle(
    80.0,
    29.0,
    919.0,
    170.0,
    fill="#862B8E",
    outline="")

canvas.create_text(
    310.0,
    74.0,
    anchor="nw",
    text="PETS PYTHON CODE",
    fill="#FFCD29",
    font=("Comic Sans MS", 38 * -1, "italic")
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_2 = canvas.create_image(
    150.0,
    99.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_3 = canvas.create_image(
    827.0,
    99.0,
    image=image_image_3
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_1 = Button(
    background="black",
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_1.place(
    x=510.0,
    y=300.0,
    width=240.0,
    height=80.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_3 = Button(
    background="black",
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_3.place(
    x=250.0,
    y=300.0,
    width=240.0,
    height=80.0
)
window.resizable(False, False)
window.mainloop()
