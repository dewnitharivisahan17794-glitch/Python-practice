Name=input('What is your name?')
print(f'Hello,{Name}!')
Age=input("How old are you?")
Gender=input("Are you male or female?")
x=Gender
if x == "male":
    print("Welcome to my Python program, handsome!")
else:
    print("Welcome to my Python program, beautiful!")

if int(Age)>40:
    print("Are you wearing spectacles?")
    Answer1=input("Yes or No?")
    if Answer1 == "yes":
        print("it's good to take care of your eyes!")
    else:
        print("You look younger than your age, keep it up!")   
         



#input() is a built-in function in Python that allows you to take user input from the console.
#  The string inside the parentheses is a prompt that will be displayed to the user when asking for input.
#  The input() function returns the user's input as a string, which can be stored in a variable for further processing.  

Num1=input("Enter the first number:")
Num2=input("Enter the second number:")
Sum=int(Num1)+int(Num2)
print(f"The sum of {Num1} and {Num2} is: {Sum}")

#we can change data type of the input by using type conversion functions like int(), float(), etc.
#  In this example, we convert the input strings to integers before performing the addition.