#we can create class by using "class" methord.
class printhello():
    print("Hello")

Obj1=printhello

class Calculator():
    def __init__ (self,x,y):
        self.x=x
        self.y=y
        sum=x+y
        print(sum)

Obj2=Calculator(5,7)

#Abstract class

from abc import ABC, abstractmethod

class Phone(ABC):
    @abstractmethod
    def func1():
        pass

Obj1=Phone()
Obj1.func1 #in abstract method we can not directly call to abstracted class





        
    