#####################################################Arithmetic  operators: +, -, *, /, //, %, **################################################
#from ast import For
#from turtle import left


#floor division operator: // The floor division operator (//) performs division and rounds down the result to the nearest whole number.
#modulus operator: % The modulus operator (%) returns the remainder of a division operation.
# Example of arithmetic operators
#from ast import For
#import operator


from ast import For, operator


a = 10
b = 3
print(a + b)  # Output: 13
print(a - b)  # Output: 7
print(a * b)  # Output: 30
print(a / b)  # Output: 3.3333333333333335
print(a // b) # Output: 3, because 10 divided by 3 is 3 with a remainder of 1
print(a % b)  # Output: 1, because 10 divided by 3 leaves a remainder of 1
print(a ** b) # Output: 1000, because 10 raised to the power of 3 is 1000
#
#
#
#operator precedence: The order in which operators are evaluated in an expression. 
#For example, in the expression 3 + 4 * 2, the multiplication operator (*) has higher precedence than the addition operator (+), 
#so the multiplication is performed first, resulting in 3 + (4 * 2) = 3 + 8 = 11.
#1. Parentheses ( )
#2. Exponentiation ( ** )
#3. Multiplication ( * ), Division ( / ), Floor Division ( // ), Modulus ( % )
#4. Addition ( + ), Subtraction ( - )

#like 3,4 we give priority to left to right, so in the expression 10 - 5 + 2, the subtraction operator (-) is evaluated first,
#followed by the addition operator (+), resulting in (10 - 5) + 2 = 5 + 2 = 7.


############################################assingment operators: =, +=, -=, *=, /=, //=, %=, **=################################################
# = operator is used to assign a value to a variable. The other operators (+=, -=, *=, /=, //=, %=, **=) are compound assignment operators that perform an operation and assign the result back to the variable.
# Example of assignment operators
x = 5
#if x == 5:
print("x += 3:", x + 3)  # Equivalent to x = (x + 3), so x becomes 8
print("x -= 2:", x - 2)  # Equivalent to x = (x - 2), so x becomes 6
print("x *= 4:", x * 4)  # Equivalent to x = (x * 4), so x becomes 24
print("x /= 6:", x / 6)  # Equivalent to x = (x / 6), so x becomes 4.0
print("x //= 2:", x // 2) # Equivalent to x = (x // 2), so x becomes 2
print("x %= 2:", x % 2)  # Equivalent to x = (x % 2), so x becomes 0
print("x **= 3:", x ** 3) # Equivalent to x = (x ** 3), so x becomes 8


####################################################################Comparison operators: ==, !=, >, <, >=, <=################################################
#Comparison operators are used to compare two values and return a boolean result (True or False) based on the comparison.
# Example of comparison operators
a = 10
b = 5
print(a == b)  # Output: False, because 10 is not equal to 5
print(a != b)  # Output: True, because 10 is not equal to 5
print(a > b)   # Output: True, because 10 is greater than 5
print(a < b)   # Output: False, because 10 is not less than 5
print(a >= b)  # Output: True, because 10 is greater than or equal to 5
print(a <= b)  # Output: False, because 10 is not less than or equal to 5
 


###########################################################Logical operators: and, or, not################################################
#logical operators are used to combine multiple boolean expressions and return a boolean result based on the logic of the expressions.
# Example of logical operators
x = 5
y = 10
print(x > 3 and y < 15)  # Output: True, because both conditions are true(both conditions are must be true to return true)
print(x > 3 or y < 5)    # Output: True, because at least one condition is true(at least one condition must be true to return true)
print(not(x > 3))        # Output: False, because x > 3 is true, and not operator negates it to false(a;ways returns the opposite of the boolean value it is applied to)

                    #AND
print(True and True)   # Output: True
print(True and False)  # Output: False
print(False and True)  # Output: False
print(False and False) # Output: False

                    #OR
print(True or True)   # Output: True
print(True or False)  # Output: True
print(False or True)  # Output: True
print(False or False) # Output: False

                    #NOT
print(not True)   # Output: False
print(not False)  # Output: True



##########################################################Identity operators: is, is not##############################################################################################################
#Identity operators are used to compare the memory locations of two objects. The is operator returns True if both operands refer to the same object,
#while the is not operator returns True if they refer to different objects.
# Example of identity operators
a=10
b=10
c=8
print(a is b)  # Output: True, because small integers are cached by Python and a and b refer to the same object in memory
print(a is c)  # Output: False, because a and c refer to different objects in memory
print(a is not c)  # Output: True, because a and c refer to different objects in memory
print(a is not b)  # Output: False, because a and b refer to the same object in memory

#special type of object is list, tuple, set, dict etc. for these type of object python does not cache them,
#  so even if they have the same content they will be different objects in memory.
#  because of this, the identity operator will return False when comparing two lists with the same content,
#  while the equality operator will return True.

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # Output: True, because the contents of the lists are the same
print(a is b)  # Output: False, because a and b refer to different list objects in memory
b = a  # b refers to the same list object as a
print(a is b)  # Output: True, because a and b refer to the same list object in memory
