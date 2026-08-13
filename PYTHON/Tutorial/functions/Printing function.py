
#print function with sep and end parameters
print("Hello", "World", sep="-") # Output: Hello-World (sep parameter specifies the separator between the arguments)
print("Hello", end=" ") # Output: Hello (end parameter specifies what to print at the end of the output, in this case a space)
print("World") # Output: World (this will be printed on the same line as "Hello" because of the end parameter in the previous print statement)
print("Hello", "World", sep="*", end="!") # Output: Hello*World! (sep parameter specifies the separator and end parameter specifies what to print at the end)






###################################################################formatted printting#############################################################

name = "Alice"
age = 30
z_score = 95.52343

#Using f-strings for formatted printing(modern and recommended way)
print(f"My name is {name}, I am {age} years old and my z score is {z_score}.") # Output: My name is Alice, I am 30 years old and my z score is 95.52343. 

#Using f-strings with formatting options
print(f"My name is {name}, I am {age} years old and my z score is {z_score:.2f}.") # Output: My name is Alice, I am 30 years old and my z score is 95.52.

#Using format() method for formatted printing
print("My name is {}, I am {} years old and my z score is {}.".format(name, age, z_score)) # Output: My name is Alice, I am 30 years old and my z score is 95.52343.

                  #spiceally, the {} are placeholders that will be replaced by the values passed to the format() method in the order they are provided.

print("My name is {0}, I am {2} years old and my z score is {1}.".format(name, z_score, age)) # Output: My name is Alice, I am 30 years old and my z score is 95.52343.

#Using % operator for formatted printing
print("My name is %s, I am %d years old and my z score is %.2f." % (name, age, z_score)) # Output: My name is Alice, I am 30 years old and my z score is 95.52.
#  *s is used to specify the number of decimal places for floating-point numbers. In this case, %.2f means that the z score will be formatted to 2 decimal places.

# Why use formatted printing?
# 1. It allows you to create more readable and organized output by controlling the format of the data being printed.
# 2. It provides flexibility in how you display data, such as controlling the number of decimal places for floating-point numbers or aligning text in a specific way.
# 3. It can help prevent errors by ensuring that the data is formatted correctly before being printed, especially when dealing with user input or data from external sources.
# 4. In GUI applications, formatted printing can be used to create dynamic and visually appealing interfaces by controlling the layout and appearance of text and data.