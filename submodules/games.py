from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import subprocess
import os

print(os.getcwd())
def spaceship_game():
    subprocess.run(['python', f'{os.getcwd()}/submodules/spaceship_game.py'])
def game():
    root = Tk()
    root.title("Games")
    path = f'{os.getcwd()}/images/gm.jfif'
    icon = ImageTk.PhotoImage(Image.open(path))  # image access from path
    root.iconphoto(True, icon)
    w = 800  # width for the Tk win
    h = 600  # height for the Tk win
    ws = root.winfo_screenwidth()  # width of the screen
    hs = root.winfo_screenheight()  # height of the screen

# calculate x and y coordinates for the Tk win window
    x = (ws/2) - (w/2)
# x = 300
    y = (hs/2) - (h/2)

    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(0, 0)
    root.config(bg="black")

    lbl = Label(root, text="Welcome In Game Zone !!", font=(
        "casetaller", 30, "bold"), fg="white", bg="black")
    lbl.place(x=160, y=50)
    path1 = f"{os.getcwd()}/images/gamebtn.png"
    img1 = ImageTk.PhotoImage(Image.open(path1))

    btn = Button(root, image=img1, relief="raised", bd=5, command=lambda:spaceship_game())
    btn.place(x=250, y=160, width=300, height=200)

    lbl1 = Label(root, text="Spaceship", justify="center", font=(
        "casetaller", 20, "bold"), fg="white", bg="purple", relief="groove", bd=5)
    lbl1.place(x=300, y=380, width="200")

    root.mainloop()


game()
