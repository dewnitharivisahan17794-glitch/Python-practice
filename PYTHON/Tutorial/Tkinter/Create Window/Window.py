import tkinter as tk

Window = tk.Tk()
Window.title('My GUI')#add a title
Window.iconbitmap(r"C:\Users\USER\OneDrive\Desktop\programs\PYTHON\Python_ GUI\Tkinter\icon.ico")
width = 400
Height = 400
#center window
screenwidth = Window.winfo_screenwidth()#get screen width
screenheight = Window.winfo_screenheight()#get screen height
left= int(screenwidth/2  - width/2)
top= int(screenheight/2 - Height/2)

Window.resizable(True, False)#Width is changeable but Height isn't

Window.geometry(f'{width}x{Height}+{left}+{top}')#manage open interface

Window.mainloop()