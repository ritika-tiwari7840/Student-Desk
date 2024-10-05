from tkinter import *
import subprocess
from tkinter import ttk

def about():
    root=Tk()

    w = 700 # width for the Tk win
    h = 630 # height for the Tk win
    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen
    # calculate x and y coordinates for the Tk win window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(0,0)
    root.title('Help')
    root.config(bg='white')


    tframe=Frame(root, bg='#311e60', width=750, height=100)  # #006666
    tframe.place(x=0, y=0)
    lbl=Label(tframe,text="Help",font=('castellar',25,'bold'), bg='#311e60', fg='white')
    lbl.place(x=300,y=30)

    txt='NOTES KEEPER'
    lbl_detail=Label(root, text=txt, justify='left', fg='black', font=('arial', 12, 'bold'), bg='white')
    lbl_detail.place(x=12, y=110)
    names='You can save your notes here, and can access these notes whenever you want\n.'
    lbl_name=Label(root, text=names, wraplength=650, justify='left', fg='black', font=('arial', 12), bg='white')
    lbl_name.place(x=15, y=135)

    lbl_detail=Label(root, text='DICTIONARY', justify='left', fg='black', font=('arial', 12, 'bold'), bg='white')
    lbl_detail.place(x=12, y=160)
    names='You can find the several meanings, antonym and synonym of a word by using this dictionary. You can also see all the searched words through HISTORY button and have a quick revision.'
    lbl_name=Label(root, text=names, wraplength=650, justify='left', fg='black', font=('arial', 12), bg='white')
    lbl_name.place(x=15, y=185)

    lbl_detail=Label(root, text='TRANSLATOR', justify='left', fg='black', font=('arial', 12, 'bold'), bg='white')
    lbl_detail.place(x=12, y=230)
    names='This helps you to translate a word or statement from one language to another in a very user friendly interface.'
    lbl_name=Label(root, text=names, wraplength=600, justify='left', fg='black', font=('arial', 12), bg='white')
    lbl_name.place(x=15, y=250)

    lbl_detail=Label(root, text='LOCKER', justify='left', fg='black', font=('arial', 12, 'bold'), bg='white')
    lbl_detail.place(x=12, y=300)
    names='You can save your confidential documents here in a secure manner just like a locker, which can be accessed using Username and Password.'
    lbl_name=Label(root, text=names, wraplength=600, justify='left', fg='black', font=('arial', 12), bg='white')
    lbl_name.place(x=15, y=325)

    lbl_detail=Label(root, text='WHITEBOARD', justify='left', fg='black', font=('arial', 12, 'bold'), bg='white')
    lbl_detail.place(x=12, y=370)
    names='You can use this just like a board on which you can write or draw anything and save it as an image.'
    lbl_name=Label(root, text=names, wraplength=600, justify='left', fg='black', font=('arial', 12), bg='white')
    lbl_name.place(x=15, y=395)
    tree=ttk.Treeview(root)
    hsb=ttk.Scrollbar(root, orient='horizontal')
    hsb.configure(command=tree.xview)
    tree.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X, side= 'bottom')

    vsb=ttk.Scrollbar(root, orient='vertical')
    vsb.configure(command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)
    vsb.pack(fill=Y, side= 'right')

    root.mainloop()
    # subprocess.run(['python', 'main.py'])

about()