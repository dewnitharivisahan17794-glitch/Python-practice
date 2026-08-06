######################################################## While loop ########################################################
# while condition:
    # code to execute as long as condition is true  
#Example: Print numbers from 1 to 5 using a while loop
from ast import While


i=1
while i<=5:
    print(i)
    i+=1  # Increment i to avoid infinite loop

#Example: Calculate the factorial of a number using a while loop
num = int(input("Enter a number to calculate its factorial: "))
factorial = 1
while num>1 :
    factorial *= num
    num -= 1
print("The factorial is:", factorial)


############################################################### For loop ########################################################
# for variable in iterable:
    # code to execute for each item in the iterable
#Example: Print each item in a list using a for loop
favorite_fruits = ["apple", "banana", "cherry"]
for fruit in favorite_fruits:
    print(fruit)    

#Example: Calculate the sum of numbers from 1 to 10 using a for loop
total_sum = 0
for num in range(1, 11):
    total_sum += num
print("The sum is:", total_sum)

#Example: calculate the sum of even numbers from 1 to 10
even_sum = 0
for num in range(2, 11, 2):# This loop iterates through even numbers starting from 2 up to 10 (inclusive) with a step of 2
    even_sum += num
print("The sum of even numbers is:", even_sum)

#if_continue and break statements in loops
#Example: Using continue to skip even numbers and print only odd numbers from 1 to 10
for num in range(1, 11):
    if num % 2 == 0:
        continue  # Skip the rest of the loop for even numbers
    print(num)  # This will print only odd numbers 

#Example: Using break to exit a loop when a certain condition is met
for num in range(1, 11):
    if num == 5:
        break  # Exit the loop when num is 5
    print(num)  # This will print numbers from 1 to 4
