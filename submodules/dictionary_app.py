from tkinter import *
from tkinter import messagebox
from pydictionary import Dictionary
import mysql.connector
import subprocess


def history():
    subprocess.run(['python', 'E:/Minor Project/submodules/dict_history.py'])

def dictionary():
  root=Tk()
  w=1000
  h=628
  ws = root.winfo_screenwidth() # width of the screen
  hs = root.winfo_screenheight() # height of the screen

  # calculate x and y coordinates for the Tk win window
  x = (ws/2) - (w/2)
  y = (hs/2) - (h/2)

  root.geometry('%dx%d+%d+%d' % (w, h, x, y))

  root.resizable(0,0)
  root.title('Dictionary')
  image_icon=PhotoImage(file='E:/Minor Project/images/dict_logo.png')
  root.iconphoto(0, image_icon)
  
  global mean, syn, ant
  try:
  
    connection = mysql.connector.connect(host = 'localhost', user='root', password='', port='3306', database = 'dictionary')
    c=connection.cursor()
  except:
    print('connection failed')
  #function
  def search():
    global mean, syn, ant
    textmeaning.config(state=NORMAL)
    textmeaning.delete(1.0, END)
    w=word.get()
    try:
      i=Dictionary(w)
      meanings_list=i.meanings()
      # textmeaning.insert(END, meanings_list)
      one=Dictionary(w,1)
      mean = str(one.meanings()[0])
      try:
        syn = str(one.synonyms()[0])
      except:
        syn='Not Found!!!'
      try:
        ant = str(one.antonyms()[0])
      except:
        ant='Not Found!!!'
      count=1
      for a in meanings_list:
        textmeaning.insert(END, f'{count}. {a}\n\n')
        count=count+1
      textmeaning.config(state=DISABLED)
    except:
      messagebox.showerror('Error', 'Word does not found.')
      textmeaning.config(state=NORMAL)
      textmeaning.delete(1.0, END)
      entword.delete(0, END)

  def synonym():
    textmeaning.config(state=NORMAL)
    textmeaning.delete(1.0, END)
    w=word.get()
    try:
      i=Dictionary(w)
      synonyms_list=i.synonyms()
      # textmeaning.insert(END, meanings_list)
      count=1
      if synonyms_list:
        for a in synonyms_list:
          textmeaning.insert(END, f'{count}. {a}\n\n')
          count=count+1
      else:
        textmeaning.insert(END, 'No synonym found')
      textmeaning.config(state=DISABLED)
    except:
      messagebox.showerror('Error', 'Word does not found.')
      textmeaning.config(state=NORMAL)
      textmeaning.delete(1.0, END)
      entword.delete(0, END)

  def antonym():
    textmeaning.config(state=NORMAL)
    textmeaning.delete(1.0, END)
    w=word.get()
    try:
      i=Dictionary(w)
      antonyms_list=i.antonyms()
      count=1
      if antonyms_list:
        for a in antonyms_list:
          textmeaning.insert(END, f'{count}. {a}\n\n')
          count=count+1
      else:
        textmeaning.insert(END, 'No antonym found')
      textmeaning.config(state=DISABLED)
    except:
      messagebox.showerror('Error', 'Word does not found.')
      textmeaning.config(state=NORMAL)
      textmeaning.delete(1.0, END)
      entword.delete(0, END)

  def insertData():
        
    try:
      sql="create table dict(word varchar(200),meaning varchar(200),synonym varchar(200),antonym varchar(200))"
      c.execute(sql)
      connection.commit()
    except:
      print("table not created")


    try:
      global mean, syn, ant
      word = entword.get()
      insert_query = "INSERT INTO `dict`(`word`, `meaning`, `synonym`, `antonym`) VALUES (%s,%s,%s,%s)"
      vals=(word, mean, syn, ant)
      c.execute(insert_query, vals)
      connection.commit()
    except:
      print('Word already exist in Database')

  def clear():
    textmeaning.config(state=NORMAL)
    entword.delete(0, END)
    textmeaning.delete(1.0, END)

  def iexit():
    res=messagebox.askyesno('Confirm', 'Are you sure to exit?')
    if res==True:
      root.destroy()
    else:
      pass

  #Label
  bgimage=PhotoImage(file='E:/Minor Project/images/dict_bg.png')
  lblbg=Label(root, image=bgimage)
  lblbg.place(x=0, y=0)

  lblword=Label(root, text='Enter word ', font=('castellar', 30, 'bold'), fg='purple', bg='#e4dcd3')
  lblword.place(x=150, y=15)

  #Entry
  word=StringVar()
  entword=Entry(root, textvariable=word, bg='white', font=('arial', 25, 'bold'), justify='center', relief='groove', bd=8)
  entword.place(x=120, y=85)

  #button

  btnsearch=Button(root, text='Meaning', bd='6', justify='center', font=('arial', 15, 'bold'), fg='purple', relief='raised', command=lambda:[search(), insertData()])
  btnsearch.place(x=85, y=190)


  btnsynonym=Button(root, text='Synonym', bd='6', justify='center', font=('arial', 15, 'bold'), fg='purple', relief='raised', command=synonym)
  btnsynonym.place(x=268, y=190)

  btnantonym=Button(root, text='Antonym', bd='6', justify='center', font=('arial', 15, 'bold'), fg='purple', relief='raised', command=antonym)
  btnantonym.place(x=445, y=190)

  #textarea
  textmeaning=Text(root, height=11, width=38, bd=8, relief='groove', bg='white', font=('arial', 16))
  textmeaning.place(x=85, y=240)

  clearimg=PhotoImage(file='E:/Minor Project/images/clear.png')
  btnclear=Button(root, image=clearimg, bg='#dac3f4', bd=0, cursor='hand2', command=clear)
  btnclear.place(x=200, y=540)
  exitimg=PhotoImage(file='E:/Minor Project/images/exit.png')
  btnexit=Button(root, image=exitimg, bg='#ebeddf', bd=0, cursor='hand2', command=iexit)
  btnexit.place(x=400, y=540)
  btn_history=Button(root,text="History",width=7,height=1,bg="purple",fg="#d0bcef",font=('arial',13, 'bold'),bd=8,relief="groove", activebackground="#d0bcef",activeforeground="purple", cursor="hand2", command=history)
  btn_history.place(x=855, y=560) 

  root.mainloop()

dictionary()