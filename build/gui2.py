import tkinter as tk
from tkinter import Button, Canvas, PhotoImage
from pathlib import Path
import sys

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets/frame2")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def display_info(color, text):
    window = tk.Toplevel()
    window.geometry("800x396")
    window.configure(bg="#202020")
    window.overrideredirect(True)
    # icon = tk.PhotoImage(file="./assets/favicon.png")
    # icon = window.iconphoto(True, icon)  # Set window icon

    canvas = Canvas(
        window,
        bg="#202020",
        height=396,
        width=800,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(400.0, 43.0, image=image_image_1)

    button_1 = Button(
        window,
        text=text,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        bg=color
    )
    button_1.place(x=58.0, y=178.0, width=99.0, height=100.0)

    # Other buttons...


window = tk.Tk()
window.geometry("800x396")
window.configure(bg="#202020")
window.overrideredirect(True)

button_1 = Button(
    window,
    text="Sample Text",
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    bg="#FFD166"  # Default color
)
button_1.place(
    x=58.0,
    y=178.0,
    width=99.0,
    height=100.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=253.0,
    y=178.0,
    width=99.0,
    height=100.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=448.0,
    y=178.0,
    width=99.0,
    height=100.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=643.0,
    y=178.0,
    width=99.0,
    height=100.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: sys.exit(),
    relief="flat"
)
button_5.place(
    x=762.0,
    y=6.0,
    width=30.0,
    height=30.0
)
window.resizable(False, False)
window.mainloop()
