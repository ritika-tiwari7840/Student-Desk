from tkinter import *
from tkinter import ttk
import subprocess

def preload():
    subprocess.run(['python', 'submodules/student.py'])
preload()


win=Tk()
win.title('Student Desk')
image_icon=PhotoImage(file='images/sd.gif')
win.iconphoto(0, image_icon)
win.config(bg='white')

#function

def noteskeeper():
    subprocess.run(['python', 'submodules/noteskeeper.py'])

def translator():
    subprocess.run(['python', 'submodules/g_translator.py'])

def games():
    subprocess.run(['python', 'submodules/games.py'])

def dictionary():
    subprocess.run(['python', 'submodules/dictionary_app.py'])

def paint():
    subprocess.run(['python', 'submodules/studentpad.py'])

def locker():
    subprocess.run(['python', 'submodules/new.py'])

def about():
    # win.destroy()
    subprocess.run(['python', 'submodules/about.py'])
def help():
    subprocess.run(['python', 'submodules/help.py'])

w = 870 # width for the Tk win
h = 630 # height for the Tk win
ws = win.winfo_screenwidth() # width of the screen
hs = win.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk win window
x = (ws/2) - (w/2)
# x = 300
y = (hs/2) - (h/2)

win.geometry('%dx%d+%d+%d' % (w, h, x, y))
win.resizable(0,0)
# variables
theme_color1='#311e60' # '#311e60'
subapp_color='#864202'

tframe=Frame(win, bg=theme_color1, width=900, height=100)
tframe.place(x=0, y=0)
lbl=Label(tframe,text="Welcome to Student Desk!!!",font=('castellar',25,'bold'), bg=theme_color1, fg='white')
lbl.place(x=140,y=30)


img=PhotoImage(file='images/nt.png')
btn1=Button(win,image=img,width=150,height=150,bg=subapp_color,bd=8,relief="groove", command=lambda:noteskeeper())
btn1.place(x=100,y=124)
btn1lbl=Label(win, text='Notes Keeper', font=('arial', 19, 'bold'), fg='white', bg=subapp_color, bd=3, relief='groove')
btn1lbl.place(x=100, y=282)


img1=PhotoImage(file='images/demodict.png')
btn2=Button(win,image=img1,width=150,height=150,bg=subapp_color,bd=8,relief="groove", command=lambda:dictionary())
btn2.place(x=350,y=124)
btn2lbl=Label(win, text='Dictionary', font=('arial', 18, 'bold'), fg='white', bg=subapp_color, bd=3, relief='groove', padx=22)
btn2lbl.place(x=350, y=282)


img2=PhotoImage(file="images/gt.png")
btn3=Button(win,image=img2,width=150,height=150,bg=subapp_color,bd=8,relief="groove", command=translator)
btn3.place(x=600,y=124)
btn2lbl=Label(win, text='Translator', font=('arial', 18, 'bold'), fg='white', bg=subapp_color, bd=3, relief='groove', padx=22)
btn2lbl.place(x=600, y=282)


img3=PhotoImage(file="images/lk.png")
btn4=Button(win,image=img3,width=150,height=150,bg=subapp_color,bd=8,relief="groove", command=lambda:locker())
btn4.place(x=100,y=352)
btn2lbl=Label(win, text='Locker', font=('arial', 18, 'bold'), fg='white', bg=subapp_color, bd=3, relief='groove', padx=42)
btn2lbl.place(x=100, y=510)


img4=PhotoImage(file="images/game.png")
btn5=Button(win,image=img4,width=150,height=150,bg=subapp_color,bd=8,relief="groove", command= games)
btn5.place(x=350,y=352)
btn2lbl=Label(win, text='Game', font=('arial', 18, 'bold'), fg='white', bg=subapp_color, bd=3, relief='groove', padx=47)
btn2lbl.place(x=350, y=510)


img5=PhotoImage(file="images/w_b.png")
btn6=Button(win,image=img5,width=150,height=150,bg=subapp_color,bd=8,relief="groove", command=paint)
btn6.place(x=600,y=352)
btn2lbl=Label(win, text='White Board', font=('arial', 18, 'bold'), fg='white', bg=subapp_color, bd=3, relief='groove', padx=10)
btn2lbl.place(x=600, y=510)


btn_about=Button(win,text="About Us",width=8,height=1,bg=theme_color1,fg="white",font=('arial',13, 'bold'), bd=8,relief="groove", activebackground=theme_color1, activeforeground="white", cursor="hand2", command=about)
btn_about.place(x=650,y=570)

btn_help=Button(win,text="Help",width=7,height=1,bg="#cc0000",fg="white",font=('arial',13, 'bold'),bd=8,relief="groove", activebackground="#cc0000",activeforeground="white", cursor="hand2", command=help)
btn_help.place(x=765, y=570)

win.mainloop()
