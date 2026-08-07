#exception handling use for escape from user input erorrs.
try:

    a=int(input("enter first number: "))
    b=int(input("enter second number: "))
    print(a/b)
except ZeroDivisionError as E:
    print("devied by zero is not defined.")
except ValueError as E:
    print("please only try with integers.")
except Exception as E:
    print("something went wrong ",E)

finally:
    print("bye")
