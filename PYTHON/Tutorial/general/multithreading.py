#Without multithreading

def func1():
    for i in range(5):
        print("Good")

def func2():
    for i in range(5):
        print("Bye")    

func1()
func2()

#With multithreading and Without Freeze time
import threading
def func1():
    for i in range(100):
        print("Good")

def func2():
    for i in range(100):
        print("Bye")    

t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)

t1.start()
t2.start()

#With Freeze time
from time import sleep
def func1():
    for i in range(5):
        print("Good")
        sleep(1)
def func2():
    for i in range(5):
        print("Bye")    
        sleep(1)
t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)

t1.start()
sleep(0.2)
t2.start()

sleep(5) #by adding this rule we can seperate both of them.

#multithreading use to classes
from threading import *
from time import sleep

class A(Thread):
    def run(self):
        for i in range(3):
            print("Hello")
            sleep(1)
class B(Thread):
    def run(self):
        for i in range(3):
            print("Welcome")
            sleep(1)
Obj1=A()
Obj2=B()
Obj1.start()
sleep(0.2)
Obj2.start()
Obj1.join()
Obj2.join()
print("See you Later")
    