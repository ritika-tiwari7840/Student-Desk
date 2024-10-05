from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import subprocess
import pymysql

from tkinter import filedialog
from tkinter import ttk
import mysql.connector
import os

from datetime import datetime

from tkinter.filedialog import askopenfile


def locker():

    def read_data(user):  # read data
        try:
            # Creating a directory in system to save files

            # Directory
            folder = f"{user} locker Files"

# Parent Directory path
            Parent_dir = f"{os.getcwd()}/"

# Path
            folder_path = os.path.join(Parent_dir, folder)
            print("dir path is", folder_path)

            os.mkdir(folder_path, mode=0o777)
        except Exception as e:
            pass
        f_type = [('All files', '*.*')]
        fn = filedialog.asksaveasfilename(
            initialdir=folder_path, title="save file", filetypes=f_type)

        try:
            tableName = user+"_lockerFiles"

            mydb = mysql.connector.connect(
                host="localhost", user="root", password="", database="locker")
            mycursor = mydb.cursor()
            sql = f"Select filedata from {tableName} LiMIT 1"
            mycursor.execute(sql)
            r = mycursor.fetchall()
            for i in r:
                data = i[0]  # this is a binary from database

            with open(fn, "wb") as f:
                f.write(data)
            f.close()
            print("file saved")
            messagebox.showinfo("locker","file saved")


            mydb.commit()

        except Exception as e:
            messagebox.showerror("Error", "please try again ...")
            print(e)

    def show_win(user):

        window = Tk()

        window.title("show data")
        w = 800
        h = 600
        ws = window.winfo_screenwidth()
        hs = window.winfo_screenheight()

        x = (ws/2)-(w/2)

        y = (hs/2)-(h/2)

        window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        window.resizable(0, 0)
        # win.config(bg="yellow")
        main_frame = Frame(window)
        main_frame.pack(fill="both", expand=1)

# create a canvas
        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add a Scroll to the canvas
        my_scrollbar = ttk.Scrollbar(
            main_frame, orient=VERTICAL, command=my_canvas.yview)

        my_scrollbar.pack(side=RIGHT, fill=Y)

# configure the canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(
            scrollregion=my_canvas.bbox("all")))


# create another frame inside the canvas
        second_frame = Frame(my_canvas)


# add that new frame to a window in the canvas
        my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
        height = 100
        try:
            tableName = user+"_lockerFiles"
            mydb = mysql.connector.connect(
                host="localhost", user="root", password="", database="locker")
            mycursor = mydb.cursor()

            sql = f"Select * from {tableName}"
            mycursor.execute(sql)
            r = mycursor.fetchall()
            mydb.commit()

            Button(second_frame, text=" S.no."+"                  "+"File Name"+"                "+"Date"+"             ", font=('casetaller', 20, 'bold'), bg="#2984b6", fg="#c6c8c9", relief="raised", bd=10).pack(fill='x', expand=True,
                                                                                                                                                                                                                     padx=5, pady=10)

            for i in r:
                Button(second_frame, text=""+str(
                    i[0])+"                                 "+i[1]+"              "+str(i[3]), font=('casetaller', 15, 'bold'), width=62, bg="#c6c8c9", fg="#2984b6",  relief="raised", bd=5, command=lambda: read_data(user)).pack(padx=15, pady=3)
                print(i[0], i[1], i[3])
                height = height+50

        except Exception as e:
            messagebox.showerror("Error", "please try again ...")
            print("I am here in show_win function",e)

        window.mainloop()

    def lock(id, user):
        root = Tk()
        w = 800
        h = 600
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()

        x = (ws/2)-(w/2)

        y = (hs/2)-(h/2)

        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        root.resizable(0, 0)
        root.title("Handle Data")

        # FUNCTION

        def upload_file():
            f_type = [('All files', '*.*'),
                      ('Excel Files', '*.xlsx'),
                      ('Text Document', '*.txt'),
                      ('pdf', '*,pdf')]
            file1 = filedialog.askopenfilename(filetypes=f_type)
            if file1:
                try:
                    con = pymysql.connect(
                        host="localhost", user="root", password="", database="locker")
                    cur = con.cursor()
                    cur.execute("select * from desklock where id=%s ", (id))
                    row = cur.fetchone()
                    print(row)
                    con.commit()
                    con.close()
        # print(row)
                except Exception as es:
                    messagebox.showerror("Error", f"Error due to:{str(es)}")
                    

            # getting blob file
                fob = open(file1, 'rb')
                fob = fob.read()
                print(fob)
                filenamelist = file1.split("/")
                filename = filenamelist[-1]
                print(filename)

# getting current date

                now = datetime.now()
                date = now.strftime("%d/%m/%Y")
                time = now.strftime("%H:%M:%S")

                if row[1] == id:

                    try:
                        mydb = mysql.connector.connect(
                            host="localhost", user="root", password="", database="locker")
                        mycursor = mydb.cursor()

                        table_name = user+"_lockerFiles"
                        print(user)

                        sql = f"create table {table_name}(id int(11) not null,filename varchar(200),filedata longblob,date datetime)"
                        mycursor.execute(sql)
                        mydb.commit()
                        print(table_name,"created table,connected")
                    except Exception as e:

                        if "already exist" in str(e):
                            pass
                        else:
                            messagebox.showerror(
                                "Error", e)

                    try:
             
                        args = (filename, fob)
                        sql = f"insert into {table_name}(id, filename, filedata , date)values(1,%s,%s,NOW())"
                        mycursor.execute(sql, args)
                        print(sql, args)
                        print("filename is : ", filename)
                        messagebox.showinfo("locker","file saved in database")

                        mydb.commit()

                    except Exception as e:
                        messagebox.showerror(
                            "Error", "please try again ...")
                        print(e)

        # LABEL
        lb = Label(root, text='WELCOME TO LOCKER',
                   font=('algerian', 22, 'bold'))
        lb.place(x=220, y=60)
        lb1 = Label(root, text='🔒', font=('algerian', 56, 'bold'))
        lb1.place(x=530, y=40)

        # BUTTON
        img = Image.open(f"{os.getcwd()}/images/sav1.png")
        bg2 = ImageTk.PhotoImage(img)
        btn = Button(root, image=bg2, bg='whitesmoke', cursor='hand2',
                     relief=FLAT, command=lambda: show_win(user))
        btn.place(x=200, y=200)
        lbl_save = Label(root, text="Saved files", font=(
            'arial', 16, 'bold'), bg="#f0f0f0", fg="black")
        lbl_save.place(x=210, y=350)

        img = Image.open(f"{os.getcwd()}/images/ad2.png")
        bg1 = ImageTk.PhotoImage(img)
        btn1 = Button(root, image=bg1, bg='whitesmoke', cursor='hand2',
                      relief=FLAT, command=lambda: upload_file())
        btn1.place(x=450, y=200)
        lbl_add = Label(root, text="Add files", font=(
            'arial', 16, 'bold'), bg="#f0f0f0", fg="black")
        lbl_add.place(x=460, y=350)

        root.mainloop()

    def login():
        win = Tk()
        w = 800
        h = 600
        ws = win.winfo_screenwidth()
        hs = win.winfo_screenheight()

        x = (ws/2)-(w/2)

        y = (hs/2)-(h/2)

        win.geometry('%dx%d+%d+%d' % (w, h, x, y))
        win.resizable(0, 0)
        win.title("Create Locker")

        # function

        def click():
            win.destroy()
            # reg()

            subprocess.run(['python', 'submodules/reg.py'])

        def enter():

            if pdw.get() == "" and em.get() != "":
                messagebox.showerror("Error", "Please Enter Password")
            elif em.get() == "" and pdw.get() != "":
                messagebox.showerror("Error", "Please Enter Email Id")
            elif pdw.get() == "" or em.get() == "":
                print('all fields are required')
                messagebox.showerror("Error", f"Error due to:{str(es)}")
            else:
                try:
                    con = pymysql.connect(
                        host="localhost", user="root", password="", database="locker")
                    cur = con.cursor()
                    cur.execute(
                        "select * from desklock where id=%s and password=%s", (em.get(), pdw.get()))
                    row = cur.fetchone()
                    print(row)
                    if row == None:
                        messagebox.showerror(
                            "Error", "Invalid User or Password")
                        
                    else:
                        messagebox.showinfo(
                            "locker", "You Enter Successfully")
                        win.destroy()
                        lock(row[1], row[0])

                except Exception as es:
                    messagebox.showerror("Error", f"Error due to:{str(es)}")
                    print(es)

        # backgroundimage
        bg2 = PhotoImage(file='E:/Minor Project/images/lc1.png')
        label1 = Label(win, image=bg2)
        label1.place(x=0, y=100)

        # frame
        f1 = Frame(win, border=2, bg='#2c5e82', height=40, width=300)
        f1.place(x=150, y=105)

        # label
        lb = Label(f1, text="Welcome to locker", font=(
            'ALGERIAN', 20, 'bold'), fg='#367faf')
        lb.place(x=2, y=0)

        lb1 = Label(win, text="Email Id", font=(
            'arial', 16, 'bold'), bg='#fcfcfc', fg='#2c5e82')
        lb1.place(x=60, y=230)

        lb2 = Label(win, text="Password", font=(
            'arial', 16, 'bold'), bg='#fcfcfc', fg='#2c5e82')
        lb2.place(x=60, y=280)

        l3 = Label(win, text='New User?', font=(
            'arial', 12, 'bold'), fg='#214560')
        l3.place(x=580, y=530)

        # entry
        em = Entry(win, font=('arial', 14, 'bold'), width=25)
        em.place(x=200, y=230)
        pdw = Entry(win, font=('arial', 14, 'bold'), width=25)
        pdw.place(x=200, y=280)

        # button
        log = Button(win, text="Enter", width=12, font=('arial', 12, 'bold'),
                     fg='#214560', cursor='hand2', relief='groove', command=enter)
        log.place(x=220, y=370)

        log1 = Button(win, text="Create", width=10, font=('arial', 10, 'bold'),
                      fg='#214560', cursor='hand2', relief='groove', command=click)
        log1.place(x=680, y=530)

        win.mainloop()

    login()


locker()
