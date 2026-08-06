#conditional statements
#if condition:    # code to execute if condition is true
   # pass
#elif another_condition:    # code to execute if another_condition is true
    # pass
#else:    # code to execute if all conditions are false
   # pass



#Let's say we have a variable `x` and we want to check if it's positive, negative, or zero:
x = 10
if(x>0):
    print("x is positive number")
elif(x<0):
    print("x is negative number")
else:
    print("x is zero")


#You can also use nested if statements to check multiple conditions:
y = 5
if(y>0):
    if(y%2==0):
        print("y is a positive even number")
    else:
        print("y is a positive odd number")
elif(y<0):
    if(y%2==0):
        print("y is a negative even number")
    else:
        print("y is a negative odd number")
else:
    print("y is zero")        