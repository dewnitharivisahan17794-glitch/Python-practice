
class Bank_Account():
        def __init__(self,Account_Num,Withdrow_Ammount,serial_Num):
            self.__Account_Number = 11234566783
            self.__Account_Holder_Name = "B C P Rathnayake"
            self._Serial_Num = "2700-56"
            self._Balance = 234374.27
            self.Account_Num = Account_Num
            self.Withdrow__Ammount = Withdrow_Ammount
            self.serial_Num = serial_Num


            if Account_Num == self.__Account_Number:
                if serial_Num == self._Serial_Num:
                    Withdrow_Ammount+=5
                else :
                    Withdrow_Ammount+=30

                if Withdrow_Ammount < self._Balance:
                    self._Balance -= Withdrow_Ammount
                    print (f"your New Account Balance Is :{self._Balance}") 
                else:
                    print(f"incufficient Account Balance\nyour Account Balance is :{self._Balance}")
            else:

                print("Account Number is unmatched!")




        