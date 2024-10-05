import subprocess
from tkinter import*

root=Tk()
root.geometry('300x200')
root.title("Reset Password")

def resetpass():
 Password=open("pass",'r').read()
 if (Password==n.get()):
  open("pass",'w').write(n1.get())
  root.destroy()
 else:
  Passtext1.delete(0,END)
  Passtext2.delete(0,END)
  
  
lb1=Label(root,font=('arial',8,'bold'),text="Enter Old Password:")
lb1.place(x=60,y=20)

n=StringVar()
Passtext1=Entry(root,width=30,textvariable=n)
Passtext1.place(x=50,y=50)

lb2=Label(root,font=('arial',8,'bold'),text="Enter New Password:")
lb2.place(x=60,y=90)

n1=StringVar()
Passtext2=Entry(root,width=30,textvariable=n1)
Passtext2.place(x=50,y=120)

btn=Button(root,text="Reset",command=resetpass)
btn.place(x=120,y=150)

root.mainloop()
