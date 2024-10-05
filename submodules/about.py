from tkinter import *
import subprocess

def about():
    root=Tk()

    w = 600 # width for the Tk win
    h = 630 # height for the Tk win
    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen
    # calculate x and y coordinates for the Tk win window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(0,0)
    root.title('About Developers')
    root.config(bg='white')


    tframe=Frame(root, bg='#311e60', width=600, height=100)  # #006666
    tframe.place(x=0, y=0)
    lbl=Label(tframe,text="About Developers",font=('castellar',25,'bold'), bg='#311e60', fg='white')
    lbl.place(x=100,y=30)

    txt='This project is developed by students of Government Polytechnic Ghaziabad, pursing Diploma in Information Technology branch, in their college curriculum as Minor Project.\n\nDeveloped By:'
    lbl_detail=Label(root, text=txt, wraplength=600, justify='left', fg='black', font=('arial', 16, 'bold'), bg='white')
    lbl_detail.place(x=20, y=120)
    names='Ritika Tiwari\nPrerna Sharma\nAkansha Shishodia\nVishal Choudhary'
    lbl_name=Label(root, text=names, justify='left', fg='black', font=('arial', 16, 'bold'), bg='white')
    lbl_name.place(x=50, y=270)
    root.mainloop()

about()