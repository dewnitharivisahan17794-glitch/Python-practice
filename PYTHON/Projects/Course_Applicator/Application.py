import tkinter as tk
from tkinter import ttk

Choices=tk.Tk()
Choices.title('Choices')
Choices.geometry(f'500x500')
Choices.iconbitmap("C:/Users/USER/OneDrive/Desktop/programs/PYTHON/Python_ GUI/Tkinter/icon.ico")
checkboxes=[tk.StringVar(), tk.StringVar(), tk.StringVar()]
radiobutton=tk.StringVar()

lable1=ttk.Label(Choices, text="Welcome to Choices")
lable1.pack()
name= ttk.Label()
lable2=ttk.Label(Choices, text="Choose what you wamt to study: ", anchor='w')
lable2.pack(fill='x', padx=10, pady=10)
Checkbox1 = ttk.Checkbutton(Choices, onvalue='Python', offvalue=' ', variable=checkboxes[0], text="Python")
Checkbox1.pack(anchor='w', padx=200)
Checkbox2 = ttk.Checkbutton(Choices, onvalue='Java', offvalue=' ', variable=checkboxes[1], text="Java")
Checkbox2.pack(anchor='w', padx=200)
Checkbox3 = ttk.Checkbutton(Choices, onvalue='C++', offvalue=' ', variable=checkboxes[2], text="C++")
Checkbox3.pack(anchor='w', padx=200)
lable2=ttk.Label(Choices, text="Choose Level(at one time only can apply one level for all languages): ", anchor='w')
lable2.pack(fill='x', padx=10, pady=10)
Radiobutton1 = ttk.Radiobutton(Choices, text='Beginner', value=1, variable=radiobutton)
Radiobutton1.pack(anchor='w', padx=200)
Radiobutton2 = ttk.Radiobutton(Choices, text='Intermediate', value=2, variable=radiobutton)
Radiobutton2.pack(anchor='w', padx=200)
Radiobutton1 = ttk.Radiobutton(Choices, text='Advance', value=3, variable=radiobutton)
Radiobutton1.pack(anchor='w', padx=200)



Choices.mainloop()
