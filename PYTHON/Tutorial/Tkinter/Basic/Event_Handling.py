import tkinter as tk
from tkinter import ttk

Event=tk.Tk()
Event.title('EVENT')
Event.geometry(f'500x500')
Event.iconbitmap("C:/Users/USER/OneDrive/Desktop/programs/PYTHON/Python_ GUI/Tkinter/icon.ico")
btn=ttk.Button(Event, text='Button 1')
btn.pack()
btn2=ttk.Button(Event, text='Button 2')
btn2.pack(pady=10)
Entry1=ttk.Entry(Event)
Entry1.pack()
Entry2=ttk.Entry(Event)
Entry2.pack()
#Entry
btn.bind('<Enter>', lambda event:print('Button is selected')) 
btn.bind('<Leave>', lambda event:print('Button is deselected'))
#key
btn2.bind('<Key>', lambda event:print('Hello!')) #press eny key to control after the select 2nd button
#motion
Entry1.bind('<Motion>', lambda entry:print('Moving'))
#focus(in/out)
Entry2.bind('<FocusIn>', lambda entry:print('Enter to the Entry Feild'))
Entry2.bind('<FocusOut>', lambda entry:print('Leave from the Entry Feild'))
Event.mainloop()