
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess
from facecap import Face_Cap


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\hoang\Desktop\DESIGN\build\assets\frame1")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def open_gui3():
    print(get_name(),"---",get_face_id())
    Face_Cap(get_name(), get_face_id())
    subprocess.Popen(["python", "gui3.py"])

# Hàm xử lý sự kiện khi thoát ứng dụng
def on_cancel(*args):
    window.quit()
def get_name():
    return entry_2.get()

def get_face_id():
    return entry_1.get()

window = Tk()
window.title("Face Recognition")
window.geometry("972x587")
window.configure(bg = "#FFFFFF")

class GUI2:
    global entry_1
    global entry_2
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

    canvas.create_text(
        135.0,
        101.0,
        anchor="nw",
        text="ENTER THE NAME",
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
        x=357.0,
        y=395.0,
        width=167.0,
        height=61.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command= on_cancel(),
        relief="flat"
    )
    button_2.place(
        x=110.0,
        y=395.0,
        width=151.0,
        height=61.0
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        317.0,
        319.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=130.0,
        y=300.0,
        width=350.0,
        height=45.0
    )
    entry_1.configure(font=("Open Sans SemiBold", 24))
    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        317.0,
        232.5,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=130.0,
        y=210.0,
        width=350.0,
        height=50.0
    )
    entry_2.configure(font=("Open Sans SemiBold", 24))

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        761.0,
        289.0,
        image=image_image_2
    )
    window.resizable(False, False)
    window.mainloop()
