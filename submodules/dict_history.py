import mysql.connector
import tkinter as tk 
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

def history():
    root = tk.Tk()
    root.title('Dictionary History')

    w=1000
    h=628
    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen

    # calculate x and y coordinates for the Tk win window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    image_icon=PhotoImage(file='E:/Minor Project/images/dict_logo.png')
    root.iconphoto(0, image_icon)
    root.resizable(0,0)

    #Label
    bgimage=PhotoImage(file='E:/Minor Project/images/bg2.png')
    lblbg=Label(root, image=bgimage)
    lblbg.place(x=0, y=0)
    
    tree=ttk.Treeview(root)
    tree['show']='headings'

    s=ttk.Style(root)
    s.theme_use('clam')

    s.configure(".", font=("Helvetica", 11), foreground='green', rowheight=35)
    s.configure("Treeview.Heading", foreground="#660066", background='violet', font=("Helvetica", 12, "bold"))


    # Define no of columns
    tree['columns']=('s.no', 'word', 'meaning', 'synonym', 'antonym')

    #Assign the width, minwidth and anchor to the respective columns
    tree.column('s.no', width=50, minwidth=50, anchor=tk.CENTER)
    tree.column('word', width=120, minwidth=120, anchor=tk.CENTER)
    tree.column('meaning', width=900, minwidth=900, anchor=tk.CENTER)
    tree.column('synonym', width=150, minwidth=150, anchor=tk.CENTER)
    tree.column('antonym', width=150, minwidth=150, anchor=tk.CENTER)

    # Assign the heading names to the respective columns
    tree.heading('s.no', text='S.No', anchor=tk.CENTER)
    tree.heading('word', text='Word', anchor=tk.CENTER)
    tree.heading('meaning', text='Meaning', anchor=tk.CENTER)
    tree.heading('synonym', text='Synonym', anchor=tk.CENTER)
    tree.heading('antonym', text='Antonym', anchor=tk.CENTER)
    try:
        connect=mysql.connector.connect(host='localhost', user='root', password='', database='dictionary', port='3306')
        conn = connect.cursor()
        conn.execute('SELECT * FROM dict')
    
        i=0
        for ro in conn:
            tree.insert('', i, text='', values=(i+1, ro[0], ro[1], ro[2], ro[3]))
            i=i+1
    except:
        messagebox.showerror('Error', 'Database Connection Failed.')

    hsb=ttk.Scrollbar(root, orient='horizontal')
    hsb.configure(command=tree.xview)
    tree.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X, side= 'bottom')

    vsb=ttk.Scrollbar(root, orient='vertical')
    vsb.configure(command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)
    vsb.pack(fill=Y, side= 'right')

    tree.pack()

    root.mainloop()

history()
