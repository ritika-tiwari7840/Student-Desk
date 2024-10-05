from tkinter import*
from tkinter import ttk ,messagebox
from PIL import Image , ImageTk
import pymysql
import os
import subprocess
# from new import*

def reg():
    win=Tk()
    win.title("Locker")
    w = 800
    h = 600
    ws = win.winfo_screenwidth()
    hs = win.winfo_screenheight()

    x = (ws/2)-(w/2)

    y = (hs/2)-(h/2)

    win.geometry('%dx%d+%d+%d' % (w, h, x, y))
    win.resizable(0, 0)

    #function
    def click():
        win.destroy()   
        subprocess.run(['python',f'{os.getcwd()}/submodules/new.py'])
        

    def reg():
        if id.get()==" " or num.get()==" " or passw.get()==" " or passw1.get()=="":
            messagebox.showerror("Error","all field are required",parent=win)
        elif passw.get()!= passw1.get():  
            messagebox.showerror("Error","Password $ Confirm Password should be same")  
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="locker")
                cur=con.cursor()
                try:
                    cur.execute("create table desklock(user varchar(200),id varchar(200) primary key,password varchar(200))")
                except Exception as e:
                    messagebox.showerror("Error",e)
                cur.execute("select * from desklock where id=%s",num.get())
                name=cur.fetchone()
                print(name)
                if name!=None:
                    messagebox.showerror("Error","User already Exist")
                    id.delete(0,END)
                    num.delete(0,END)
                    passw.delete(0,END)
                    passw1.delete(0,END)
                else:    
                    cur.execute("insert into desklock (user,id,password) values(%s,%s,%s)",
                            (
                            id.get(),
                            num.get(),
                            passw.get()
                             ) )
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Locker Created Successfully",parent=win)
                    win.destroy()   
                    subprocess.run(['python',f'{os.getcwd()}/submodules/new.py'])
                              
            
            except Exception as es:
                messagebox.showerror("Error",f"Error due to:{str(es)}",parent=win)    

    #backgroundimage
    bg3=PhotoImage(file=f'{os.getcwd()}/images/lc1.png')
    label1=Label(win,image=bg3)
    label1.place(x=0, y=100)

    #frames
    f1=Frame(win,border=2,bg='#2c5e82' ,height=40,width=238)
    f1.place(x=160,y=60)


    #label

    lb=Label(f1,text="CREATE LOCKER",font=('ALGERIAN',20,'bold'),fg='#367faf')
    lb.place(x=2,y=0)

    lb1=Label(win,text="NAME",font=('arial',12,'bold'),bg='#fcfcfc',fg='#2c5e82')
    lb1.place(x=60,y=140)

    lb2=Label(win,text="Email",font=('arial',12,'bold'),bg='#fcfcfc',fg='#2c5e82')
    lb2.place(x=60,y=200)

    lb3=Label(win,text="PASSWORD",font=('arial',12,'bold'),bg='#fcfcfc',fg='#2c5e82')
    lb3.place(x=60,y=260)

    lb4=Label(win,text="CONFIRM",font=('arial',12,'bold'),bg='#fcfcfc',fg='#2c5e82')
    lb4.place(x=60,y=320)

    lb5=Label(win,text="Already have locker?",font=('arial',11,'bold'),fg='#214560')
    lb5.place(x=480, y=530)


     #ENTRY
    id=Entry(win,font=('arial',12,'bold'),width=25)
    id.place(x=220,y=140)

    num=Entry(win,font=('arial',12,'bold'),width=25)
    num.place(x=220,y=200)

    passw=Entry(win,font=('arial',12,'bold'),width=25)
    passw.place(x=220,y=260)

    passw1=Entry(win,font=('arial',12,'bold'),width=25)
    passw1.place(x=220,y=320)

    #button
    reg=Button(win,text='Create',font=('arial',12,'bold'),bg='#fcfcfc',cursor='hand2',fg='#214560',relief='groove',width=12,command=reg)
    reg.place(x=200,y=400)
    
    reg1=Button(win,text='Click here',font=('arial',10,'bold'),fg='#214560',cursor='hand2',relief='groove',width=12,command=click)
    reg1.place(x=650, y=530)

    win.mainloop()

reg()    