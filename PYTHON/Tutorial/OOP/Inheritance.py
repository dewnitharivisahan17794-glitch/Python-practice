####Inheritance
# Inheritance is a mechanism in OOP that allows a class (called a child or subclass) to inherit attributes 
# and methods from another class (called a parent or superclass).

#single inheritance
class Vehicle_1:
    def feature1(self):
        print("manual transmission, air conditioning, power steering")

class vehicle_2(Vehicle_1):
    def feature2(self):
        print("automatic transmission, air conditioning, power steering, sunroof")

car1 = Vehicle_1()
car1.feature1()  # Output: manual transmission, air conditioning, power steering
car1.feature2()  # This will raise an AttributeError because feature2 is not defined in Vehicle_1.

car2 = vehicle_2()
car2.feature1()  # Output: automatic transmission, air conditioning, power steering, sunroof
car2.feature2()  # Output: automatic transmission, air conditioning, power steering, sunroof

#multiple inheritance

class Vehicle_1:
    def feature1(self):
        print("manual transmission, air conditioning, power steering")

class vehicle_2:
    def feature2(self):
        print("automatic transmission, air conditioning, power steering, sunroof")

class vehicle_3(Vehicle_1, vehicle_2):
    def feature3(self):
        print("electric transmission, air conditioning, power steering, sunroof, autopilot")

car1 = vehicle_3()
car1.feature1()  # Output: manual transmission, air conditioning, power steering
car1.feature2()  # Output: automatic transmission, air conditioning, power steering, sunroof
car1.feature3()  # Output: electric transmission, air conditioning, power steering, sunroof, autopilot

#multilevel inheritance(multilevel inheritance is a type of inheritance where a class is derived from another class, which is also derived from another class. In other words, it forms a chain of inheritance.)


class Vehicle_1:
    def feature1(self):
        print("manual transmission, air conditioning, power steering")

class vehicle_2(Vehicle_1):
    def feature2(self):
        print("automatic transmission, air conditioning, power steering, sunroof")

class vehicle_3(vehicle_2):
    def feature3(self):
        print("electric transmission, air conditioning, power steering, sunroof, autopilot")

car1 = vehicle_3()
car1.feature1()  # Output: manual transmission, air conditioning, power steering
car1.feature2()  # Output: automatic transmission, air conditioning, power steering, sunroof
car1.feature3()  # Output: electric transmission, air conditioning, power steering, sunroof, autopilot

#super() function
# The super() function is used to call a method from the parent class. It is commonly used in the constructor of a subclass to initialize the parent class.

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, doors): # by using super() function we can call the constructor of the parent class and initialize the brand and model attributes.
                                            #without adding the super() function, we would have to manually set the brand and model attributes in the Car class, which would be redundant and error-prone.
        super().__init__(brand, model)
        self.doors = doors

car1 = Car("Toyota", "Camry", 4)
print(car1.brand)  # Output: Toyota
print(car1.model)  # Output: Camry
print(car1.doors)  # Output: 4

vehicle1 = Vehicle("Honda", "Civic")
print(vehicle1.brand)  # Output: Honda
print(vehicle1.model)  # Output: Civic

#overriding methods
# Method overriding is a feature in OOP that allows a subclass to provide a specific implementation of a method that is already defined in its parent class. When a method in a subclass has the same name, return type, and parameters as a method in the parent class, the method in the subclass overrides the method in the parent class.

class Vehicle:
    def start_engine(self):
        print("Starting the engine of the vehicle.")
        
class Car(Vehicle):
    def close_doors(self):
        print("Closing the doors of the car.")
    def start_engine(self):
        print("Starting the engine of the car.")

vehicle1 = Vehicle()
vehicle1.start_engine()  # Output: Starting the engine of the vehicle.

car1 = Car()
car1.start_engine()  # Output: Starting the engine of the car.
car1.close_doors()  # Output: Closing the doors of the car.