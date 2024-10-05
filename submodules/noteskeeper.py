from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from datetime import datetime
import os
from tkinter import messagebox
from PIL import ImageTk, Image


def noteskeeper():

    root = Tk()

    path = f'{os.getcwd()}/images/notes.jpg'
    icon = ImageTk.PhotoImage(Image.open(path))  # image access from path
    root.iconphoto(True, icon)

# creting global variable for saving filename for file from device
    global filename

    try:
        # Creating a directory in system to save files

        # Directory
        directory = "Notes Keeper File"

# Parent Directory path
        parent_dir = f"{os.getcwd()}/"

# Path
        dir_path = os.path.join(parent_dir, directory)
        print("dir path is", dir_path)

        os.mkdir(parent_dir, mode=0o777)
    except (FileExistsError):
        print("not executed")
        pass


# connecting database with app
    try:
        mydb = mysql.connector.connect(
            host="localhost", user="root", password="", database="notes")
        mycursor = mydb.cursor()
    except:
        messagebox.showerror(
            "Notes Keeper", "please try again ...please make sure that you are connected to Server and Database!!")
    try:
        sql="create table image(id int(11) not null,filename varchar(200),filedata longblob,date datetime)"
        mycursor.execute(sql)
        mydb.commit()
    except Exception as e:
        # messagebox.showinfo("Notes Keeper", e)
        pass
    try:
        sql1="create table video(id int(11) not null,filename varchar(200),filedata longblob,date datetime)"
        mycursor.execute(sql1)
        mydb.commit()
    except Exception as e:
        # messagebox.showinfo("Notes Keeper", e)
        pass
    try:
        sql2="create table pdf(id int(11) not null,filename varchar(200),filedata longblob,date datetime)"
        mycursor.execute(sql2)
        mydb.commit()
    except Exception as e:
        # messagebox.showinfo("Notes Keeper", e)
        pass
    try:
        sql3="create table audio(id int(11) not null,filename varchar(200),filedata longblob,date datetime)"
        mycursor.execute(sql3)
        mydb.commit()
    except Exception as e:
        # messagebox.showinfo("Notes Keeper", e)
        pass
    try:
        sql4="create table OtherFiles(id int(11) not null,filename varchar(200),filedata longblob,date datetime)"
        mycursor.execute(sql4)
        mydb.commit()
    except Exception as e:
        # messagebox.showinfo("Notes Keeper", e)
        pass

        

    def show_save_msg():
        messagebox.showinfo("Notes Keeper", "File Saved Successfully")

    def upload():
        # access file from drive
        global filename
        try:

            f_type = [('All files', '*.*')]
            filename = filedialog.askopenfilename(filetype=f_type)
            print(filename)
        except Exception as e:
            messagebox.showerror("Notes Keeper", "please try again ...")

        # add file button
        addbtn = Button(root, text="Add file", font=(
            'casetaller', 15, 'bold'), bg="#fcc02c", fg="black", relief="groove", bd=5, command=add_file)
        addbtn.place(x=450, y=420)

# function will open the file in binary format

    def add_file():
        global filename
        # getting blob file
        fob = open(filename, 'rb')
        fob = fob.read()
        print(fob)
        filenamelist = filename.split("/")

# getting current date

        now = datetime.now()
        date = now.strftime("%d/%m/%Y")
        time = now.strftime("%H:%M:%S")

        # connecting database
        if filename.endswith(('.png', '.jpg', '.jpeg', '.ico')):
            file_name = filenamelist[-1]
            args = (file_name, fob)
            try:
                sql = "insert into image(id, filename, filedata , date)values(1,%s,%s,NOW())"
                mycursor.execute(sql, args)
                print(sql, args)
                print("filename is : ", file_name)
                show_save_msg()

                mydb.commit()
            except Exception as e:
                messagebox.showerror("Notes Keeper", "please try again ...")
                print(e)
        elif filename.endswith(('.pdf',)):
            file_name = filenamelist[-1]
            args = (file_name, fob)
            try:
                sql = "insert into pdf(id, filename, filedata , date)values(NULL,%s,%s,NOW())"
                mycursor.execute(sql, args)
                print(sql, args)
                print("pdf saved filename is : ", file_name)
                show_save_msg()
                mydb.commit()
            except Exception as e:
                messagebox.showerror("Notes Keeper", "please try again ...")

        elif filename.endswith(('.avi', '.flv', '.wmv', '.mov', '.mp4', 'webm', '.vob', '.mng', '.qt', '.mpg', '.mpeg', '.3gp')):
            # file compressionrelief="raised",bd=10,

            file_name = filenamelist[-1]
            args = (file_name, fob)
            try:
                sql = "insert into video(id, filename, filedata , date)values(NULL,%s,%s,NOW())"
                mycursor.execute(sql, args)
                print(sql, args)
                print("video saved filename is : ", file_name)
                show_save_msg()

                mydb.commit()
            except Exception as e:
                messagebox.showerror("Notes Keeper", "please try again ...")

        elif filename.endswith(('.aac', '.aa', '.dvi', '.m4a', '.m4b', '.m4p', '.mp3', '.msv', '.ogg', '.oga', '.raw', '.vox', '.wav', '.wma')):
            file_name = filenamelist[-1]
            args = (file_name, fob)
            try:
                sql = "insert into audio(id, filename, filedata , date)values(NULL,%s,%s,NOW())"
                mycursor.execute(sql, args)
                print(sql, args)
                print("audio saved filename is : ", file_name)
                show_save_msg()
                mydb.commit()
            except Exception as e:
                messagebox.showerror("Notes Keeper", "please try again ...")

        else:
            file_name = filenamelist[-1]
            args = (file_name, fob)
            try:

                sql = "insert into otherFiles(id, filename, filedata , date)values(NULL,%s,%s,NOW())"
                mycursor.execute(sql, args)
                print(sql, args)
                print("other saved filename is : ", file_name)
                show_save_msg()

                mydb.commit()
            except Exception as e:
                messagebox.showerror("Notes Keeper", "please try again ...")

# Reading the data from database

    def read_image_data():  # read data
        try:
            # Creating a directory in system to save files

            # Directory
            folder = "Images"

# Parent Directory path
            Parent_dir = f"{os.getcwd()}/Notes Keeper File/"

# Path
            folder_path = os.path.join(Parent_dir, folder)
            print("dir path is", folder_path)

            os.mkdir(folder_path, mode=0o777)
        except Exception as e:
            pass

        fn = filedialog.asksaveasfilename(initialdir=folder_path, title="save file", filetypes=(
            ("Image File", "*.jpg"), ("All Files", "*.*")))
        print("path is", path)
        try:
            sql = "Select filedata from image LiMIT 1"
            mycursor.execute(sql)
            r = mycursor.fetchall()
            for i in r:
                data = i[0]  # this is a binary from database

            with open(fn, "wb") as f:
                f.write(data)
            f.close()
            print("file saved")
            show_save_msg()

            mydb.commit()

        except Exception as e:
            messagebox.showerror("Notes Keeper", "please try again ...")

    def read_audio_data():  # read data

        try:
            # Creating a directory in system to save files

            # Directory
            folder = "Audio Files"

# Parent Directory path
            Parent_dir = f"{os.getcwd()}/Notes Keeper File/"

# Path
            folder_path = os.path.join(Parent_dir, folder)
            print("dir path is", folder_path)

            os.mkdir(folder_path, mode=0o777)
        except Exception as e:
            pass

        fn = filedialog.asksaveasfilename(initialdir=folder_path, title="save file", filetypes=(
            ("Audio File", "*.mp3"), ("All Files", "*.*")))
        print("path is", path)
        try:
            sql = "Select filedata from audio LiMIT 1"
            mycursor.execute(sql)
            r = mycursor.fetchall()
            for i in r:
                data = i[0]  # this is a binary from database

            with open(fn, "wb") as f:
                f.write(data)
            f.close()
            print("file saved")
            show_save_msg()

            mydb.commit()

        except Exception as e:
            messagebox.showerror("Notes Keeper", "please try again ...")

    def read_video_data():  # read data

        try:
            # Creating a directory in system to save files

            # Directory
            folder = "Video Files"

# Parent Directory path
            Parent_dir = f"{os.getcwd()}/Notes Keeper File/"

# Path
            folder_path = os.path.join(Parent_dir, folder)
            print("dir path is", folder_path)

            os.mkdir(folder_path, mode=0o777)
        except Exception as e:
            pass

        fn = filedialog.asksaveasfilename(initialdir=folder_path, title="save file", filetypes=(
            ("Video File", "*.mp4"), ("All Files", "*.*")))
        print("path is", path)
        try:
            sql = "Select filedata from video LiMIT 1"
            mycursor.execute(sql)
            r = mycursor.fetchall()
            for i in r:
                data = i[0]  # this is a binary from database

            with open(fn, "wb") as f:
                f.write(data)
            f.close()
            print("file saved")
            show_save_msg()

            mydb.commit()

        except Exception as e:
            messagebox.showerror("Notes Keeper", "please try again ...")

    def read_pdf_data():  # read data

        try:
            # Creating a directory in system to save files

            # Directory
            folder = "PDF Files"

# Parent Directory path
            Parent_dir = f"{os.getcwd()}/Notes Keeper File/"

# Path
            folder_path = os.path.join(Parent_dir, folder)
            print("dir path is", folder_path)

            os.mkdir(folder_path, mode=0o777)
        except Exception as e:
            pass

        fn = filedialog.asksaveasfilename(initialdir=folder_path, title="save file", filetypes=(
            ("PDF File", "*.pdf"), ("All Files", "*.*")))
        print("path is", path)
        try:
            sql = "Select filedata from pdf LiMIT 1"
            mycursor.execute(sql)
            r = mycursor.fetchall()
            for i in r:
                data = i[0]  # this is a binary from database

            with open(fn, "wb") as f:
                f.write(data)
            f.close()
            print("file saved")
            show_save_msg()

            mydb.commit()

        except Exception as e:
            messagebox.showerror("Notes Keeper", "please try again ...")

    def read_otheFiles_data():  # read data

        try:
            # Creating a directory in system to save files

            # Directory
            folder = "Other Files"

# Parent Directory path
            Parent_dir = f"{os.getcwd()}/Notes Keeper File/"

# Path
            folder_path = os.path.join(Parent_dir, folder)
            print("dir path is", folder_path)

            os.mkdir(folder_path, mode=0o777)
        except Exception as e:
            pass

        fn = filedialog.asksaveasfilename(initialdir=folder_path, title="save file", filetypes=(
            ("All Files", "*.*")))
        print("path is", path)
        try:
            sql = "Select filedata from OtherFiles LiMIT 1"
            mycursor.execute(sql)
            r = mycursor.fetchall()
            for i in r:
                data = i[0]  # this is a binary from database

            with open(fn, "wb") as f:
                f.write(data)
            f.close()
            print("file saved")
            show_save_msg()

            mydb.commit()

        except Exception as e:
            messagebox.showerror("Notes Keeper", "please try again ...")

        # showing database saved data in Tk window

    def show_window():
        window = Tk()
        window.title("Stored Data")
        w = 800
        h = 600
        ws = window.winfo_screenwidth()
        hs = window.winfo_screenheight()
        x = (ws/2)-(w/2)
        y = (hs/2)-(h/2)

        window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        window.resizable(0, 0)
        window.config(bg="white")

        lbl1 = Label(window, text="Get The Stored Data From Database",
                     justify="center", fg="black", bg="white", font=('casetaller', 25, 'bold'))
        lbl1.place(x=110, y=100)

        btnimage = Button(window, text="image", command=show_image_data, font=(
            'casetaller', 15, 'bold'), relief="raised", bd=10, bg="#c70053")
        btnimage.place(x=190, y=200, width=200, height=80)
        btnimage = Button(window, text="video", command=show_video_data, font=(
            'casetaller', 15, 'bold'), relief="raised", bd=10, bg="#c70053")
        btnimage.place(x=430, y=200, width=200, height=80)
        btnimage = Button(window, text="audio", command=show_audio_data, font=(
            'casetaller', 15, 'bold'), relief="raised", bd=10, bg="#f7e401")
        btnimage.place(x=190, y=420, width=200, height=80)
        btnimage = Button(window, text="pdf", command=show_pdf_data,
                          font=('casetaller', 15, 'bold'), relief="raised", bd=10, bg="#f7e401")
        btnimage.place(x=430, y=420, width=200, height=80)
        btnimage = Button(window, text="other files", command=show_other_data, font=(
            'casetaller', 15, 'bold'), relief="raised", bd=10, bg="#0079be")
        btnimage.place(x=300, y=310, width=200, height=80)

        window.mainloop()

# show data windpw start

    def show_image_data():

        win = Tk()

        win.title("show data")
        w = 800
        h = 600
        ws = win.winfo_screenwidth()
        hs = win.winfo_screenheight()

        x = (ws/2)-(w/2)

        y = (hs/2)-(h/2)

        win.geometry('%dx%d+%d+%d' % (w, h, x, y))
        win.resizable(0, 0)
        # win.config(bg="yellow")
        main_frame = Frame(win)
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
            sql = "Select * from image"
            mycursor.execute(sql)
            r = mycursor.fetchall()
            mydb.commit()

            Button(second_frame, text=" S.no."+"                  "+"File Name"+"                "+"Date"+"             ", font=('casetaller', 20, 'bold'), bg="#ffec3c", fg="#c70053", relief="raised", bd=10).pack(fill='x', expand=True,
                                                                                                                                                                                                                     padx=5, pady=10)

            for i in r:
                Button(second_frame, text=""+str(
                    i[0])+"                                 "+i[1]+"              "+str(i[3]), font=('casetaller', 15, 'bold'), width=62, bg="white", fg="#c70053", command=read_image_data, relief="raised", bd=5).pack(padx=15, pady=3)
                print(i[0], i[1], i[3])
                height = height+50

        except Exception as e:
            messagebox.showerror("Notes Keeper", "please try again ...")

        win.mainloop()

    def show_pdf_data():

        win = Tk()

        win.title("show data")
        w = 800
        h = 600
        ws = win.winfo_screenwidth()
        hs = win.winfo_screenheight()

        x = (ws/2)-(w/2)

        y = (hs/2)-(h/2)

        win.geometry('%dx%d+%d+%d' % (w, h, x, y))
        win.resizable(0, 0)
        # win.config(bg="#1765c1")
        main_frame = Frame(win)
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
            sql = "Select * from pdf"
            mycursor.execute(sql)
            r = mycursor.fetchall()
            mydb.commit()

            Button(second_frame, text=" S.no."+"                  "+"File Name"+"                "+"Date"+"             ", font=(
                'casetaller', 20, 'bold'), bg="#ffec3c", fg="#0079be", relief="raised", bd=10).pack(fill='x', expand=True, padx=5, pady=10)

            for i in r:
                Button(second_frame, text=""+str(
                    i[0])+"                                 "+i[1]+"              "+str(i[3]), font=('casetaller', 15, 'bold'), width=62, bg="white", fg="#0079be", command=read_pdf_data, relief="raised", bd=5).pack(padx=15, pady=3)
                print(i[0], i[1], i[3])
                height = height+50

        except Exception as e:
            messagebox.showerror("Notes Keeper", "please try again ...")
        win.mainloop()

    def show_audio_data():

        win = Tk()

        win.title("show data")

        w = 800
        h = 600
        ws = win.winfo_screenwidth()
        hs = win.winfo_screenheight()

        x = (ws/2)-(w/2)

        y = (hs/2)-(h/2)

        win.geometry('%dx%d+%d+%d' % (w, h, x, y))
        win.resizable(0, 0)
        win.config(bg="#c70053")
        main_frame = Frame(win)
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
            sql = "Select * from audio"
            mycursor.execute(sql)
            r = mycursor.fetchall()
            mydb.commit()

            Button(second_frame, text=" S.no."+"                  "+"File Name"+"                "+"Date"+"             ", font=('casetaller', 20, 'bold'), bg="#ffec3c", fg="#c70053", relief="raised", bd=10).pack(fill='x', expand=True,
                                                                                                                                                                                                                     padx=5, pady=10)

            for i in r:
                Button(second_frame, text=""+str(
                    i[0])+"                                 "+i[1]+"              "+str(i[3]), font=('casetaller', 15, 'bold'), width=62, bg="white", fg="#c70053", command=read_audio_data, relief="raised", bd=5).pack(padx=15, pady=3)
                print(i[0], i[1], i[3])
                height = height+50
        except Exception as e:
            messagebox.showerror("Notes Keeper", "please try again ...")

        win.mainloop()

    def show_video_data():

        win = Tk()

        win.title("show data")
        w = 800
        h = 600
        ws = win.winfo_screenwidth()
        hs = win.winfo_screenheight()

        x = (ws/2)-(w/2)

        y = (hs/2)-(h/2)

        win.geometry('%dx%d+%d+%d' % (w, h, x, y))
        win.resizable(0, 0)
        win.config(bg="#1765c1")
        main_frame = Frame(win)
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
            sql = "Select * from video"
            mycursor.execute(sql)
            r = mycursor.fetchall()
            mydb.commit()

            Button(second_frame, text=" S.no."+"                  "+"File Name"+"                "+"Date"+"             ", font=('casetaller', 20, 'bold'), bg="#ffec3c", fg="#0079be", relief="raised", bd=10).pack(fill='x', expand=True,
                                                                                                                                                                                                                     padx=5, pady=10)

            for i in r:
                Button(second_frame, text=""+str(
                    i[0])+"                                 "+i[1]+"              "+str(i[3]), font=('casetaller', 15, 'bold'), width=62, bg="#0d47a1", fg="#0079be", command=read_video_data, relief="raised", bd=5).pack(padx=15, pady=3)
                print(i[0], i[1], i[3])
                height = height+50
        except Exception as e:
            messagebox.showerror("Notes Keeper", "please try again ...")

        win.mainloop()

    def show_other_data():

        win = Tk()

        win.title("show data")
        w = 800
        h = 600
        ws = win.winfo_screenwidth()
        hs = win.winfo_screenheight()

        x = (ws/2)-(w/2)

        y = (hs/2)-(h/2)

        win.geometry('%dx%d+%d+%d' % (w, h, x, y))
        win.resizable(0, 0)
        # win.config(bg="#1765c1")
        main_frame = Frame(win)
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
            sql = "Select * from otherFiles"
            mycursor.execute(sql)
            r = mycursor.fetchall()
            mydb.commit()

            Button(second_frame, text=" S.no."+"                  "+"File Name"+"                "+"Date"+"             ", font=('casetaller', 20, 'bold',), bg="#ffec3c", fg="#c70053", relief="raised", bd=10).pack(fill='x', expand=True,
                                                                                                                                                                                                                      padx=5, pady=10)

            for i in r:
                Button(second_frame, text=""+str(
                    i[0])+"                                 "+i[1]+"              "+str(i[3]), font=('casetaller', 15, 'bold'), width=62, bg="#0d47a1", fg="#c70053", command=read_otheFiles_data, relief="raised", bd=5).pack(padx=15, pady=3)
                print(i[0], i[1], i[3])
                height = height+50
        except Exception as e:
            messagebox.showerror("Notes Keeper", "please try again ...")

        win.mainloop()

    def uploadImage():
        btn = Button(root, text="Upload Image", font=(
            'casetaller', 15, 'bold'), bg="#fcc02c", command=upload, relief="groove", bd=5)
        btn.place(x=280, y=420, height=50, width=150)

    def uploadaudio():
        btn = Button(root, text="Upload Audio", bg="#fcc02c",
                     font=('casetaller', 15, 'bold'), command=upload, relief="groove", bd=5)
        btn.place(x=280, y=420, height=50, width=150)

    def uploadvideo():
        btn = Button(root, text="Upload Video", bg="#fcc02c",
                     font=('casetaller', 15, 'bold'), command=upload, relief="groove", bd=5)
        btn.place(x=280, y=420, height=50, width=150)

    def uploadpdf():
        btn = Button(root, text="Upload PDF", bg="#fcc02c",
                     font=('casetaller', 15, 'bold'), command=upload, relief="groove", bd=5)
        btn.place(x=280, y=420, height=50, width=150)

    def uploadotherFiles():
        btn = Button(root, text="Upload Any Files", bg="#fcc02c",
                     font=('casetaller', 12, 'bold'), command=upload, relief="groove", bd=5)
        btn.place(x=280, y=420, height=50, width=150)

    def callback(*arg):
        val = str(var.get())
        if val == 'Image':
            uploadImage()
        if val == 'Audio':
            uploadaudio()
        if val == 'Video':
            uploadvideo()
        if val == 'PDF':
            uploadpdf()
        if val == 'Other Files':
            uploadotherFiles()

    root.title("Notes keeper")
    w = 800
    h = 600
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()

    x = (ws/2)-(w/2)
    y = (hs/2)-(h/2)

    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(0, 0)
    root.config(bg="white")

# applying background image to the window

    path = f'{os.getcwd()}/images/folders.png'
    img = ImageTk.PhotoImage(Image.open(path))  # image access from path
    lblp = Label(root, image=img)
    lblp.image = img  # keep image reference
    lblp.place(x=110, y=40)

    lab_text = Label(root, text="Welcome!!",
                     bg='white', fg='black', font=('casetaller', 20, 'bold'))
    lab_text.place(x=320, y=50, height=30, width=150)

    lbl = Label(root, text="Select the type of your file.",
                font=('casetaller', 20, 'bold'), fg='black', bg="#c70053")
    lbl.place(x=230, y=290)

# creating combobox
    type = ('Image', 'Audio', 'Video', 'PDF', 'Other Files')
    var = StringVar()
    cb = ttk.Combobox(root, justify="center", textvariable=var,
                      font=('casetaller', 20, 'bold'))
    cb['values'] = type
    cb.place(x=260, y=350, width=300, height=40)
    var.trace('w', callback)

# readbtn = Button(text="read data", command=read_image_data)
# readbtn.place(x=450, y=220)
# showbtn = Button(text="show data", command=show_data)
# showbtn.place(x=450, y=280)

    showwinbtn = Button(text="Stored Data ", command=show_window,
                        font=('casetaller', 12, 'bold'), bg="#fdd835", relief="raised", bd=5)
    showwinbtn.place(x=650, y=540, width=130, height=40)

# try:
#     os.system('cmd /k "gt.png"')
# except:
#     print("error occurred")

    root.mainloop()

noteskeeper()