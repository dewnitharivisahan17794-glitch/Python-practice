import tkinter as tk
from tkinter import ttk
from calendar import month_name

Choices=tk.Tk()
Choices.title('Choices')
Choices.geometry(f'500x500')
Choices.iconbitmap("C:/Users/USER/OneDrive/Desktop/programs/PYTHON/Python_ GUI/Tkinter/icon.ico")
checkboxes=[tk.StringVar(), tk.StringVar(), tk.StringVar()]
radiobutton=tk.StringVar()
scale_var=tk.DoubleVar(value=50)
i=0
monthname=[month_name[i] for i in range (1,13)]

lable1=ttk.Label(Choices, text="Welcome to Choices")
lable1.pack()

lable1=ttk.Label(Choices, text="Check Box")
lable1.pack(pady=10)

Checkbox1 = ttk.Checkbutton(Choices, onvalue='A', offvalue=' ', variable=checkboxes[0], text="A")
Checkbox1.pack()
Checkbox2 = ttk.Checkbutton(Choices, onvalue='B', offvalue=' ', variable=checkboxes[1], text="B")
Checkbox2.pack()
Checkbox3 = ttk.Checkbutton(Choices, onvalue='C', offvalue=' ', variable=checkboxes[2], text="C")
Checkbox3.pack()

lable1=ttk.Label(Choices, text="Radio Buttons")
lable1.pack(pady=10)

Radiobutton1 = ttk.Radiobutton(Choices, text='1', value=1, variable=radiobutton)
Radiobutton1.pack()
Radiobutton2 = ttk.Radiobutton(Choices, text='2', value=2, variable=radiobutton)
Radiobutton2.pack()
Radiobutton1 = ttk.Radiobutton(Choices, text='3', value=3, variable=radiobutton)
Radiobutton1.pack()

lable1=ttk.Label(Choices, text="Combo Box")
lable1.pack(pady=10)

combo=ttk.Combobox(Choices, values=monthname)
combo.pack()


lable1=ttk.Label(Choices, text="Spin Box")
lable1.pack(pady=10)

spin1=ttk.Spinbox(Choices,from_=1, to= 14, increment=2)
spin1.pack()

spin2=ttk.Spinbox(Choices, values=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
spin2.pack(pady=10)

lable1=ttk.Label(Choices, text="progressbar With scaler")
lable1.pack(pady=10)

progressbar=ttk.Progressbar(Choices, length=250, variable=scale_var)
progressbar.pack()
scaler=ttk.Scale(Choices, command=lambda value:print(value),variable=scale_var, from_=1, to=100, orient="horizontal", length=250)
scaler.pack()

Choices.mainloop()
