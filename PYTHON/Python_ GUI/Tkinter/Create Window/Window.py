import tkinter as tk

#open a window
window = tk.Tk()
window.title("My GUI 1") #Title of the window
window.iconbitmap("C:/Users/USER/OneDrive/Desktop/programs/PYTHON/Python_ GUI/Tkinter/icon.ico") #Icon of the window
Width = 500 #Width of the window
Height = 300 #Height of the window
Screenwidth = window.winfo_screenwidth()
Screenhight = window.winfo_screenheight()
left = int(Screenwidth/2 - Width/2)
top = int(Screenhight/2 - Height/2)
window.resizable(True,False)#width is changerble but hight isn't.

window.geometry(f"{Width}x{Height}+{left}+{top}") #Set the size of the window
window.mainloop() #For keeping the window open
