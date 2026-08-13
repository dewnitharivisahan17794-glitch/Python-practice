for raw in range(6):
    for column in range(7):
        if raw==0 and column%3!=0:
            print("*", end=" ")
        elif raw==1 and column%3==0:
            print("*", end=" ")
        elif raw - column==2:
            print("*", end=" ")
        elif raw + column==8:
            print("*", end=" ") 
        else:
            print(" ", end=" ")
    print()