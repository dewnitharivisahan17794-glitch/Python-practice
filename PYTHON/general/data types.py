##################################################### numeric data types ######################################################
#import numbers
#from shutil import which


#Integer numbers, both positive and negative, without a decimal point. Examples: 1, -5, 0.
#example:
x = 10
y = -3
z = 345569596939559694
print(x.__sizeof__())  # Output: 28 bytes
print(y.__sizeof__())  # Output: 28 bytes
print(z.__sizeof__())  # Output: 32 bytes

#Floating-point numbers, which include a decimal point. Examples: 3.14, -0.001, 2.0.
#example:
a = 3.14
b = -0.001
c = 2.0
print(a.__sizeof__())  # Output: 24 bytes
print(b.__sizeof__())  # Output: 24 bytes
print(c.__sizeof__())  # Output: 24 bytes

#boolean values, which can be either True or False. These are often used in conditional statements and logical operations.
#example:
is_raining = True
is_sunny = False
print(is_raining.__sizeof__())  # Output: 28 bytes
print(is_sunny.__sizeof__())    # Output: 28 bytes  
print(type(is_raining))  # Output: <class 'bool'>
print(type(is_sunny))    # Output: <class 'bool'>

#complex numbers, which consist of a real part and an imaginary part. They are represented in the form a + bj, where a is the real part and b is the imaginary part. Examples: 2 + 3j, -1 - 4j.
#example:
c1 = 2 + 3j
c2 = -1 - 4j
c3 = complex(5, 6)  # Using the complex() function to create a complex number
print(c1.__sizeof__())  # Output: 32 bytes
print(c2.__sizeof__())  # Output: 32 bytes
print(c3.__sizeof__())  # Output: 32 bytes
print(type(c1))  # Output: <class 'complex'>
print(type(c2))  # Output: <class 'complex'>
print(type(c3))  # Output: <class 'complex'>
print("Real part of c1:", c1.real)  # Output: Real part of c1: 2.0
print("Imaginary part of c1:", c1.imag)  # Output: Imaginary part of c1: 3.0
print("Real part of c2:", c2.real)  # Output: Real part of c2: -1.0
print("Imaginary part of c2:", c2.imag)  # Output: Imaginary part of c2: -4.0
print("Real part of c3:", c3.real)  # Output: Real part of c3: 5.0
print("Imaginary part of c3:", c3.imag)  # Output: Imaginary part of c3: 6.0 

################################################################String data types ######################################################
#Strings are sequences of characters enclosed in single quotes (' '), double quotes (" "), or triple
#quotes (''' ''' or """ """). They are used to represent text. Examples: 'Hello', "Python", '''This is a string''', """Another string""".

#(String indexing and slicing)
#example:
str1 = 'Hello'
str2 = "Python " 
print(str1[0])  # Output: H
print(str2[1:4])  # Output: yth (but last index is not included,bcz when we add range in string it will not include last index)
print(str1 + " " + str2)  # Output: Hello Python
print(str2* 3)  # Output: Python Python Python

#(String methods)
#example:
str3 = "  Hello, World!  "  
print(str3.strip())  # Output: Hello, World! (removes leading and trailing whitespace)
print(str3.lstrip())  # Output: Hello, World!   (removes leading whitespace)
print(str3.rstrip())  # Output:   Hello, World! (removes trailing whitespace)
print(str3.upper())  # Output:   HELLO, WORLD!   (converts to uppercase)
print(str3.lower())  # Output:   hello, world!   (converts to lowercase)
print(str3.replace("Hello", "Hi"))  # Output:   Hi, World!   (replaces "Hello" with "Hi")
print(str3.split(","))  # Output: ['  Hello', ' World!  '] (splits the string into a list based on the comma)
print(str3.find("World"))  # Output: 8 (returns the index of the first occurrence of "World")
print(str3.startswith("  Hello"))  # Output: True (checks if the string starts with "  Hello")
print(str3.endswith("!  "))  # Output: True (checks if the string ends with "!  ")  
print(str3.capitalize())  # Output:   hello, world!    (capitalizes the first character of the string)
print(str3.title())  # Output:   Hello, World!    (capitalizes the first character of each word in the string)
print(str3.index("o"))  # Output: 4 (returns the index of the first occurrence of "o")

#Difference between find() and index() is that if the substring is not found, find() returns -1,
#  while index() raises a ValueError.

print(str3.find("Python"))  # Output: -1 (returns -1 because "Python" is not found)
#print(str3.index("Python"))  # Output: ValueError: substring not found (raises an error because "Python" is not found)

#There are various types of strings in Python, including single-line strings, multi-line strings, and raw strings.


###########################################################List data types ######################################################
#Lists are ordered collections of items that can be of different data types. They are defined using
#square brackets [ ] and can contain elements such as numbers, strings, or even other lists. Examples: [1, 2, 3], ['a', 'b', 'c'], [1, 'hello', 3.14].
#example:
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [1, 'hello', 3.14, [4, 5, 6]]  # A list containing another list
 
print(list1[0])  # Output: 1
print(list2[1])  # Output: b
print(list3[2])  # Output: 3.14
print(list1[0:2])  # Output: [1, 2]
print(list3[3])  # Output: [4, 5, 6] (accessing the nested list)
print(list3[3][1])  # Output: 5 (accessing an element from the nested list)

#In run time we can change the list because list is mutable data type.
#example:
list4 = [1, 2, 3]
print(list4)  # Output: [1, 2, 3]
list4[0] = 10  # Modifying the first element of the list
print(list4)  # Output: [10, 2, 3] (the first element has been changed to 10)

#list methods:
list5 = [1, 2, 3]
list5.append(4)  # Adds an element to the end of the list,only one element can be added at a time
print(list5)  # Output: [1, 2, 3, 4]
list5.extend([5, 6])  # Adds multiple elements to the end of the list but we have to pass list as an argument
print(list5)  # Output: [1, 2, 3, 4, 5, 6]  
list5.insert(2, 10)  # Inserts an element at a specific index (index 2 in this case)
print(list5)  # Output: [1, 2, 10, 3, 4, 5, 6]

list5.remove(10)  # Removes the first occurrence of the specified value (10 in this case)
print(list5)  # Output: [1, 2, 3, 4, 5, 6] (the value 10 has been removed)
list5.pop()  # Removes and returns the last element of the list
print(list5)  # Output: [1, 2, 3, 4, 5] (the last element, which is 6, has been removed)
list5.pop(1)  # Removes and returns the element at index 1
print(list5)  # Output: [1, 3, 4, 5] (the element at index 1, which is 2, has been removed)
list5.clear()  # Removes all elements from the list 
print(list5)  # Output: [] (the list is now empty)


######################################################### tuple data types ######################################################
#Tuples are similar to lists but are immutable, meaning their elements cannot be changed after they are defined.
#Tuples are defined using parentheses ( ) and can contain elements of different data types. Examples: (1, 2, 3), ('a', 'b', 'c'), (1, 'hello', 3.14).
#example:
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
tuple3 = (1, 'hello', 3.14, (4, 5, 6))  # A tuple containing another tuple
print(tuple1[0])  # Output: 1
print(tuple2[1])  # Output: b
print(tuple3[2])  # Output: 3.14
print(tuple1[0:2])  # Output: (1, 2)
print(tuple3[3])  # Output: (4, 5, 6) (accessing the nested tuple)
print(tuple3[3][1])  # Output: 5 (accessing an element from the nested tuple)


####################################################### set data types ######################################################
#Sets are unordered collections of unique elements. They are defined using curly braces { } and can contain elements of different data types. Examples: {1, 2, 3}, {'a', 'b', 'c'}, {1, 'hello', 3.14}.
#example:
set1 = {1, 2, 3,'a','d','q'}
set2 = {'a', 'b', 'c',1,7,6}

print(set1.union(set2))  # Output: {1, 2, 3, 'a', 'b', 'c'} (combines the elements of both sets)    
print(set1.intersection(set2))  # Output: {1, 'a'} (returns the elements that are in both sets)
print(set1.difference(set2))  # Output: {2, 3, 'd', 'q'} (returns the elements that are in set1 but not in set2)
print(set2.difference(set1))  # Output: {'b', 'c', 7, 6} (returns the elements that are in either set1 or set2 but not in both)

#set methods:
set1.add(4)  # Adds an element to the set   
print(set1)  # Output: {1, 2, 3, 'a', 'd', 'q', 4} (the element 4 has been added to the set)
set1.remove(2)  # Removes a specific element from the set(*if the element is not found, it raises a KeyError)
print(set1)  # Output: {1, 3, 'a', 'd', 'q', 4} (the element 2 has been removed from the set)
set1.discard(5)  # Removes a specific element from the set if it exists, does nothing if the element is not found
print(set1)  # Output: {1, 3, 'a', 'd', 'q', 4} (the set remains unchanged because the element 5 was not found)
set1.pop()  # Removes and returns an arbitrary element from the set
print(set1)  # Output: {3, 'a', 'd', 'q', 4} (an arbitrary element has been removed from the set)
set1.clear()  # Removes all elements from the set
print(set1)  # Output: set() (the set is now empty)


#################################################################### Dictionary data types ######################################################
#Dictionaries are collections of key-value pairs. They are defined using curly braces { } 
#and consist of keys and their corresponding values. Keys must be unique and immutable, 
# while values can be of any data type. Examples: {'name': 'Alice', 'age': 30}, {1: 'one', 2: 'two'} .
#example:
dict1 = {'name': 'Alice', 'age': 30}
dict2 = {1: 'one', 2: 'two', 3: 'three'}
print(dict1['name'])  # Output: Alice (accessing the value associated with the key 'name')
print(dict2[2])  # Output: two (accessing the value associated with the key 2)
print(dict1.get('age'))  # Output: 30 (accessing the value associated with the key 'age' using the get() method)
print(dict1.keys())  # Output: dict_keys(['name', 'age']) (returns a view object containing the keys of the dictionary)
print(dict1.values())  # Output: dict_values(['Alice', 30]) (returns a view object containing the values of the dictionary)
print(dict1.items())  # Output: dict_items([('name', 'Alice'), ('age', 30)]) (returns a view object containing the key-value pairs of the dictionary)

#dictionary methods:
dict1['city'] = 'New York'  # Adding a new key-value pair to the dictionary
dict.update({'country': 'USA'})  # Adding a new key-value pair using the update() method
print(dict1)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'country': 'USA'} (the new key-value pairs have been added to the dictionary)
dict1['age'] = 31  # Modifying the value associated with the key 'age'
print(dict1)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'country': 'USA'} (the value associated with the key 'age' has been updated to 31)
dict1.pop('city')  # Removes the key-value pair with the specified key ('city' in this case)
print(dict1)  # Output: {'name': 'Alice', 'age': 31, 'country': 'USA'} (the key-value pair with the key 'city' has been removed from the dictionary)
dict1.clear()  # Removes all key-value pairs from the dictionary   
print(dict1)  # Output: {} (the dictionary is now empty)
del dict1  # Deletes the dictionary from memory
#print(dict1)  # Output: NameError: name 'dict1' is not defined (the dictionary has been deleted and is no longer accessible)    


############################################ Arrays ######################################################
from array import *

x=array('i',[1,2,-3,5,0])
y=array('i',[1,3,4,6,7,5])
print(x)
x.append(78) # only can add one element
print(x)
x.extend([9,65,71]) #can extend array by useing this version
print(x)
x.insert(2,77) #in this way we can insert value to the place we wanted to.
print(x)

x.pop(4) #we can remove a value what is in place num 4(left to 5)
print(x)
x.pop() #in this way we can remove last value in right
print(x)
x.remove(77) #then 77 is removed from the array(in this case we have to use what we want to remove value in parthences)
print(x)

z=x+y #for do this , all arrays must be in same data type.
print(z)

for i in x:
    print(i)

################################################ End #####################################################

#Zip function

Name=["kamal","sunil","Nimal","Ranil","sunimal"]
Age=[23,25,67,78,54]

details=list(zip(Name,Age))
print(details)
