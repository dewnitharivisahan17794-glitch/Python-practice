#OOP=Object Oriented Programming,the concept of OOP is to use objects to represent real-world entities and their interactions.
#  It allows for better organization of code, reusability, and scalability.
#  In OOP, we define classes that serve as blueprints for creating objects.
#  Each object can have attributes (data) and methods (functions) that define its behavior.



class car:
    def modal(self,model,year):
        self.x=model
        self.y=year #self is a reference to the current instance of the class,
                    #and it is used to access variables that belong to the class.
        print(f"Car model is: {self.x}, Year: {self.y}")

car1=car()
car1.modal("Toyota",2020)
print(car1.x)
print(car1.y)

#using init method (in into method is a special method in Python classes that is automatically called when an object of the class is created. It is used to initialize the attributes of the object.)

class car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def print_car_details(self):
        print(f"Car Name: {self.name}, Model: {self.model}, Year: {self.year}")

car1 = car("Toyota", "Camry", 2020)
car1.print_car_details()

car2 = car("Honda", "Civic", 2019)
car2.print_car_details()


# use of inheritance in OOP
# Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class 

##in supermarket;

class Fruit:
    Count_of_fruits=None
    price_of_per_unit=None
    def __init__(self, x, y):
        self.count_of_fruits = x
        self.price_of_per_unit = y

class Apple(Fruit):
    def __init__(self, x, y):
        super().__init__(x, y)

    def total_price(self):
        return self.count_of_fruits * self.price_of_per_unit

class orange(Fruit):
    def __init__(self, x, y):
        super().__init__(x, y)

    def total_price(self):
        return self.count_of_fruits * self.price_of_per_unit 

class pineapple(Fruit):
    def __init__(self, x, y):
        super().__init__(x, y)

    def total_price(self):
        return self.count_of_fruits * self.price_of_per_unit 

myObj1 = Apple(5, 2.5)
print("Total price of apples:", myObj1.total_price())

myObj2 = orange(3, 1.5)
print("Total price of oranges:", myObj2.total_price())

myObj3 = pineapple(2, 3.0)
print("Total price of pineapples:", myObj3.total_price())
