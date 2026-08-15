from Package1.BWD import Withdrow
from Package1.BDD import Diposit
Option=input("Input Withdrow As 'w' Or Diposit As 'd'")
if Option == "w":
   Acc = int(input("Input Account Number:"))
   With = int(input("Input Withdrow Ammount:"))
   serial_N = input("Input Serial Number:")
   withdrow = Withdrow(Acc,With,serial_N)
else :
    Acc = int(input("Input Account Number:"))
    Dip = int(input("Input Diposit Ammount:"))
    Name = input("Input Account holder's Name:")
    diposit = Diposit (Acc,Dip,Name)