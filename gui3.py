from PIL import Image, ImageTk
from pathlib import Path
from TrainAI import TRAIN_DATA
from main import TEST
import  tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path("assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def on_cancel(*args):
    window.quit()
def Train_btn_click():
    print("Button Train clicked!")
    TRAIN_DATA()
def Test_btn_click():
    print("Button TEST clicked!")
    TEST()
window = Tk()
window.title("Face Recognition")
window.geometry("972x587")
window.configure(bg = "#FFFFFF")

class GUI3:
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

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=Test_btn_click,
        relief="flat"
    )
    button_1.place(
        x=402.0,
        y=368.0,
        width=167.0,
        height=61.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=Train_btn_click,
        relief="flat"
    )
    button_2.place(
        x=160.0,
        y=368.0,
        width=167.0,
        height=61.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=on_cancel,
        relief="flat"
    )
    button_3.place(
        x=644.0,
        y=368.0,
        width=167.0,
        height=61.0
    )

    canvas.create_text(
        291.0,
        80.0,
        anchor="nw",
        text="FACE RECOGNITION",
        fill="#FFFFFF",
        font=("OpenSansRoman ExtraBold", 40 * -1)
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        486.0,
        246.0,
        image=image_image_2
    )
window.resizable(False, False)
window.mainloop()
