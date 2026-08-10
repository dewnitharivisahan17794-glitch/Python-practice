n =int(input("enter your raw count "))

for i in range(n):
    for j in range(i+1):
        print('*', end=' ')
    print()        

y =int(input("enter your raw count "))

for i in range(y):
    for j in range(y-i):
        print('*', end=' ')
    print()        

y=int(input("enter your raw count "))

for i in range(y):
    for j in range(y-i-1):
        print(' ', end=' ')  
    for k in range (2*i+1):
        print('*', end=' ')
    print()     