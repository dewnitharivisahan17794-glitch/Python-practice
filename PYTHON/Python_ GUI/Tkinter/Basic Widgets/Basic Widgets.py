import tkinter as tk
from tkinter import ttk
from button_function import BF

def BF():
                                    #Get_entry=entry.get()
                                    #lable.configure(text=Get_entry)
    lable.configure(text=entry.get())
    button.configure(state='disabled')

widgets = tk.Tk()
widgets.title("Widgets")
widgets.iconbitmap("C:/Users/USER/OneDrive/Desktop/programs/PYTHON/Python_ GUI/Tkinter/icon.ico")
width = 400
hight = 400
widgets.geometry (f"{width}x{hight}")
entry = ttk.Entry(widgets)
entry.pack()
button = ttk.Button(widgets, text="click Me", command=BF)
button.pack()
lable = ttk.Label(widgets)
lable.pack()



widgets.mainloop()