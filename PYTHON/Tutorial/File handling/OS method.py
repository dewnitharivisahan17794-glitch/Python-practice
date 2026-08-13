import os
from tkinter.filedialog import test 

#os.path.rename("PYTHON/File handling/Hello.txt", "PYTHON/File handling/Renamed_Hello.txt") #renames the file Hello.txt to Renamed_Hello.txt
print(os.path.exists("PYTHON/File handling/Hello.txt")) #checks if the file Hello.txt exists in the current directory
print(os.path.getsize("PYTHON/File handling/Hello.txt")) #returns the size of the file Hello.txt in bytes
print(os.path.abspath("PYTHON/File handling/Hello.txt")) #returns the absolute path of the file Hello.txt
#os.remove("PYTHON/File handling/new_test.txt") #removes the file named new_test.txt from the current directory
print(os.getcwd())
os.chdir('C:/Users/USER/OneDrive/Desktop/programs')
print(os.getcwd())