from tkinter import *
from tkinter.ttk import Scale
from tkinter import colorchooser, filedialog, messagebox
import PIL.ImageGrab as ImageGrab
import os

#imp things
pen_color='black'
eraser_color='white'
current_x=0
current_y= 0


def paint():
   root=Tk()
   root.title('Student Pad')
   root.state('zoomed')
   root.geometry('800x520')
   root.configure(bg='#f2f3f5')
   image_icon=PhotoImage(file=f'{os.getcwd()}/images/logo.png')
   root.iconphoto(0, image_icon)
   root.resizable(0,0)
        
#Functions are defined here
   def locate_xy(event):
      global current_x, current_y
      current_x=event.x
      current_y=event.y
        
   def paint(event):
      global current_x, current_y
      canvas.create_line((current_x, current_y, event.x, event.y), fill=pen_color, width=size.get(), capstyle='round', smooth='True')
      current_x, current_y= event.x, event.y
        
   def select_color(col) :
      global pen_color
      pen_color=col
      canvas_color_button.configure(fg=pen_color)

   def eraser():
      global pen_color
      pen_color=eraser_color

   def more_color():
      global pen_color
      color=colorchooser.askcolor()
      pen_color=color[1]
      more_pen_color.configure(fg=pen_color)
      canvas_color_button.configure(fg=pen_color)

   def canvas_color():
      global eraser_color
      color=colorchooser.askcolor()
      canvas.configure(bg=color[1])
      eraser_color=color[1]
      canvas_color_button.configure(bg=color[1])

   def save_canvas():
      try:
        filename=filedialog.asksaveasfilename(initialfile='Untitled.jpg', defaultextension='.jpg', filetypes=[('PNG','.png'),('JPG', '.jpg')])
        #height with taskbar = 995
        ImageGrab.grab((123,43,1876,1045)).save(filename)
        messagebox.showinfo('Paint says', 'image is saved as'+str(filename))
      except:
        print('not save')

#adding widgets to tkinter window
   color_frame=LabelFrame(root, text='Color', font=('arial', 15), bd=5, relief='ridge', bg='whitesmoke')
   color_frame.place(x=0,y=10, width=85, height=290)

   colors=['#FF0000', 'purple', '#FFC0CB', '#FFA500', '#FFFF00', '#008000', '#0000FF', '#A52A2A', '#FFFFFF', '#000000', '#808080', 'cyan']
   i=j=0
   for color in colors:
      Button(color_frame, bg=color, bd=2, relief='ridge', width=3, command=lambda col=color:select_color(col)).grid(row=i, column=j, padx=2, pady=2)
      i+=1
      if i==6:
        i=0
        j=1
   more_pen_color=Button(color_frame, text='More...', bd=3,  relief='ridge', font=('arial', 12, 'bold'), width=6, command=more_color)
   more_pen_color.grid(row=6, columnspan=2)

   canvas_color_button=Button(root, text='Canvas', font=('arial', 12, 'bold'), bd=4, bg='white', command=canvas_color, width=7, relief='ridge')
   canvas_color_button.place(x=2.5, y=370)

   eraser_button=Button(root, text='Eraser', font=('arial', 12, 'bold'), bd=4, bg='white', command=eraser, width=7, relief='ridge')
   eraser_button.place(x=2.5, y=410)

   save_button=Button(root, text='Save', font=('arial', 12, 'bold'), bd=4, bg='white', command=save_canvas, width=7, relief='ridge')
   save_button.place(x=2.5, y=450)

   clear_button=Button(root, text='Clear', font=('arial', 12, 'bold'), bd=4, bg='white', command=lambda:canvas.delete('all'), width=7, relief='ridge')
   clear_button.place(x=2.5, y=490)


# create a scale for pen and eraser size.

   scale_frame=LabelFrame(root, text='Size', bd=5, bg='white', font=('arial', 15, 'bold'), relief='ridge')
   scale_frame.place(x=10, y=600, height=200, width=70)


   size=Scale(scale_frame, orient='vertical', from_=50, to=0, length=170)
   size.set(3)
   size.grid(row=0, column=1, padx=15)
        

   # crearting canvas
   # height of canvas with taskbar = 760
   canvas=Canvas(root, bg='white', bd=5, relief='groove', height=800, width=1405, cursor='hand2')
   canvas.place(x=90, y=5)

   # bind the canvas with mouse drag
   canvas.bind('<Button-1>', locate_xy)
   canvas.bind('<B1-Motion>', paint)

   root.mainloop()
        
paint()
