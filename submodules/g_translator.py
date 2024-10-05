from ast import Delete
from email import message
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from googletrans import Translator, LANGUAGES
from PIL import ImageTk, Image


# function to change source text into destination text

def g_translator():

    # change funtion to translate the text

    def change(text="type", src="English", dest="Hindi"):
        text1 = text
        src1 = src
        dest1 = dest
        trans = Translator()
        trans1 = trans.translate(text, src=src1, dest=dest1)
        return trans1.text

    def data():
        try:
            s = comb_src.get()
            d = comb_dest.get()
            msg = src_text.get(1.0, END)
            textget = change(text=msg, src=s, dest=d)
            dest_text.delete(1.0, END)
            dest_text.insert(END, textget)
        except Exception as e:

            if str(e) == "[Errno 11001] getaddrinfo failed":
                messagebox.showerror(
                    "googletrans", "please try again ...please make sure that you are connected to internet!!")
                print(e)

            elif str(e) == "list index out of range":
                messagebox.showerror(
                    "googletrans", "please write  text in the Source 'Text Box' !!")
            else:
                messagebox.showerror(
                    "googletrans", "Try again !!\n\nmake sure you have selected 'Source Text language' and 'Destination Text Language' From 'Language List'")
                print(e)

    root = Tk()
    root.title("Translator")
    path = 'E:/Minor Project/images/languages.png'
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
    root.config(bg="white")

    path = 'E:/Minor Project/images/translator.jpg'
    img = ImageTk.PhotoImage(Image.open(path))  # image access from path
    lblp = Label(root, image=img)
    lblp.image = img  # keep image reference
    lblp.place(x=95, y=70)

    lab_text = Label(root, text="Translator",
                     bg='#ffffff', fg='black', font=('casetaller', 25, 'bold'))
    lab_text.place(x=220, y=20, height=40, width=400)

    frame = Frame(root,).pack(side=BOTTOM)

    lab_text = Label(root, text="Source Text", fg='black',
                     bg='#fefef6', font=('casetaller', 15, 'bold'))

    lab_text.place(x=250, y=110, height=35, width=300)

    src_text = Text(frame, bd=2, relief='solid', pady=5,
                    padx=5, cursor='hand2', bg="#f5eda1")
    src_text.place(x=185, y=150, height=60, width=450)

    scrollbar2 = Scrollbar(src_text)
    scrollbar2.pack(side="right", fill="y")
    scrollbar2.configure(command=src_text.yview)
    src_text.configure(yscrollcommand=scrollbar2.set)

    list_text = list(LANGUAGES.values())


# combo for source text to choose language
    comb_src = ttk.Combobox(frame, value=list_text,
                            font=('casetaller', 10, 'bold'))
    comb_src.place(x=185, y=130, height=20, width=100)
    comb_src.set("English")

# button_change=Button(frame, text="Translate", relief=RAISED,command=data)

# button_change.place(x=170,y=300,height=40,width=150)

    translate = Button(root, text="Translate", font="roboto 15 bold italic", relief="groove",
                       activebackground="#e4894f", cursor="hand2", bd=5, bg='#8d5324', fg='#fff1b1', command=data)
    translate.place(x=330, y=250, width=150, height=50)

    lab_text = Label(root, text="Destination Text", fg='black',
                     bg='#fefef6', font=('casetaller', 15, 'bold'))

    lab_text.place(x=250, y=340, height=35, width=300)

# combo for destination text to choose language
    comb_dest = ttk.Combobox(frame, value=list_text,
                             font=('casetaller', 10, 'bold'))
    comb_dest.place(x=185, y=360, height=20, width=100)
    comb_dest.set("Hindi")

    dest_text = Text(frame, bd=2, relief='solid', pady=5,
                     padx=5, cursor='hand2', bg="#f5eda1")
    dest_text.place(x=185, y=380, height=60, width=450)

    scrollbar2 = Scrollbar(dest_text)
    scrollbar2.pack(side="right", fill="y")
    scrollbar2.configure(command=dest_text.yview)
    dest_text.configure(yscrollcommand=scrollbar2.set)

    root.mainloop()


g_translator()
