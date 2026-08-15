from .PD import PD
class Withdrow(PD):
        def __init__(self,Account_Num,Withdrow_Ammount,serial_Num):
            self.Account_Num = Account_Num
            self.Withdrow__Ammount = Withdrow_Ammount
            self.serial_Num = serial_Num
            super().__init__()

            if Account_Num == self._Account_Number:
                if serial_Num == self._Serial_Num:
                    Withdrow_Ammount+=5
                else :
                    Withdrow_Ammount+=30

                if Withdrow_Ammount < self.Balance:
                    self.Balance -= Withdrow_Ammount
                    print (f"your New Account Balance Is :{self.Balance}")
                    self.up_b()
                else:
                    print(f"incufficient Account Balance\nyour Account Balance is :{self.Balance}")
            else:

                print("Account Number is unmatched!")
                




        