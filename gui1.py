import  tkinter as tk
import subprocess
from pathlib import Path
# from gui2 import GUI2
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path("assets/frame2")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def open_gui2():
    window.destroy()
    subprocess.Popen(["python", "gui2.py"])

# Hàm xử lý sự kiện khi thoát ứng dụng
def open_gui3():
    window.destroy()
    subprocess.Popen(["python", "gui3.py"])

window = Tk()
window.title("Face Recognition")
window.geometry("972x587")
window.configure(bg = "#FFFFFF")

class GUI1:
    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 587,
        width = 972,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        486.0,
        295.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        701.0,
        293.0,
        image=image_image_2
    )

    canvas.create_text(
        111.0,
        150.0,
        anchor="nw",
        text="HOME PAGE",
        fill="#FFFFFF",
        font=("OpenSansRoman ExtraBold", 40 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command= open_gui3,
        relief="flat"
    )
    button_1.place(
        x=111.0,
        y=387.0,
        width=239.0,
        height=61.0
    )


    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=open_gui2,
        relief="flat"
    )
    button_2.place(
        x=111.0,
        y=256.0,
        width=239.0,
        height=61.0
    )
window.resizable(False, False)
window.mainloop()
