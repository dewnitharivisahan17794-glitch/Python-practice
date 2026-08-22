import tkinter as tk
from tkinter import ttk

Table=tk.Tk()
Table.title('TABLE')
Table.geometry(f'600x500')
Table.iconbitmap("C:/Users/USER/OneDrive/Desktop/programs/PYTHON/Python_ GUI/Tkinter/icon.ico")
table=ttk.Treeview(Table, columns=('name', 'age', 'email'), show='headings')
table.pack()
table.heading('name', text="Name")
table.heading('age', text="Age")
table.heading('email', text="Email")
table.column('age', width=100)
#table.insert('', 0 , values=['kamal', 23, 'kamal@gmail.com'])
#table.insert('', 1 , values=['Ranil', 56, 'Ranil@gmail.com'])
#table.insert('', 2 , values=['Sunil', 54, 'Sunil@gmail.com'])
#table.insert('', 3 , values=['kasun', 27, 'Kasun@gmail.com'])
#table.insert('', 4 , values=['Anil', 29, 'Anil@gmail.com'])
name=['kamal','Ranil','Sunil', 'kasun','Anil']
age=[23,56,54,27,29]
for idx, value in enumerate(name):
    table.insert('', idx , values=[value ,age[idx] ,f'{value}@gmail.com'])
Table.mainloop()