#lambda function is a small anonymous function

#without lambda function calculate area of square
def area_of_square(side):
    return side * side

#with lambda function calculate area of square
area_of_square_lambda = lambda side: side * side

print("Area of square using normal function:", area_of_square(5))
print("Area of square using lambda function:", area_of_square_lambda(5))

#Example

def apple(unit_price):
  return lambda number_of_apples: unit_price * number_of_apples

x = apple(2)  # unit price of apple is 2
print("Cost of 5 apples:", x(5))  # output: 10