import tkinter as tk
from tkinter import ttk

Variables = tk.Tk()
Variables.title("variables")
Variables.iconbitmap("C:/Users/USER/OneDrive/Desktop/programs/PYTHON/Python_ GUI/Tkinter/icon.ico")
Width = 400
Height = 400
Variables.geometry(f'{Width}x{Height}')
Text_variable = tk.StringVar(value= 'Welcome')
Lable = ttk.Label(Variables, textvariable= Text_variable)
Lable.pack()
entry = ttk.Entry(Variables)
entry.pack()
Button = ttk.Button(Variables, text="Click Me", command= lambda:print(entry.get()))
Button.pack()


Variables.mainloop()

Cal = tk.Tk()
Cal.title("variables")
Cal.iconbitmap("C:/Users/USER/OneDrive/Desktop/programs/PYTHON/Python_ GUI/Tkinter/icon.ico")
Width = 400
Height = 400
Cal.geometry(f'{Width}x{Height}')
Num1=tk.IntVar()
Num2=tk.IntVar()
answer = tk.StringVar()
def sum_cal(Num1,Num2):
    sum= Num1 + Num2
    answer.set(f'Answer is :{sum}')
Sum = tk.StringVar(value= 'calculate Sum')
lab= ttk.Label(Cal, textvariable=Sum)
lab.pack()
entry1=ttk.Entry(Cal, text="Enter Num1", textvariable=Num1)
entry1.pack()
entry2=ttk.Entry(Cal, text="Enter Num2", textvariable=Num2)
entry2.pack()
button1 = ttk.Button(Cal,text="Click Me", command=lambda:sum_cal(Num1.get(),Num2.get()))
button1.pack()
lable1 = ttk.Label(Cal, textvariable=answer)
lable1.pack()
Cal.mainloop()