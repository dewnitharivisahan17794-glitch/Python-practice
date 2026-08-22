import tkinter as tk
from tkinter import ttk

Canves=tk.Tk()
Canves.title('CANVES')
Canves.geometry(f'600x500')
Canves.iconbitmap("C:/Users/USER/OneDrive/Desktop/programs/PYTHON/Python_ GUI/Tkinter/icon.ico")
canves=tk.Canvas(Canves, background='Yellow', width='500', height='400')
canves.pack()
##Incert shapes

#canves.create_line(0,0,500,400,width=5,fill='Red')
#canves.create_oval(125,125,275,275)#create Circle(x,x,y,y)
#canves.create_oval(400,175,25,18)#create ovel(X,x,Y,y)
#canves.create_rectangle(500,500,125,125)#create Rectangle(x,x,y,y)
#canves.create_rectangle(120,190,190,120)#create Squre(x,z,z,x)
#canves.create_polygon(20,50,160,90,20,58)#by manageing can create eny type of polygon.

##Create Drowing space
Change_Width=2
def drow(event):
    x=event.x
    y=event.y
    canves.create_oval(x-Change_Width,y-Change_Width,x+Change_Width,y+Change_Width, fill='Black')
    canves.bind('<B1-Motion>', drow) #Now only can drow with clicking courser point

# canves.bind('<MOtion>', drow)
canves.bind('<Button-1>',  drow )#Now only can drow with clicking courser point

Canves.mainloop()
