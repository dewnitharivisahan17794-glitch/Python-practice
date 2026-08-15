from .PD import PD
class Diposit(PD):
        def __init__(self,Account_Num,Diposit_Ammount,Account_holder_Name):
            self.Account_Num = Account_Num
            self.Diposit__Ammount = Diposit_Ammount
            self._Account_Holder_Name = Account_holder_Name
            super().__init__()

            if Account_Num == self._Account_Number:
                if Account_holder_Name == self._Account_Holder_Name:
                     if Diposit_Ammount > 0:
                          self.Balance += Diposit_Ammount
                          self.up_b()
                          print(f"Your New Account Balance is:{self.Balance}")
                     else:
                          print("Diposit Ammount is invalid!") 
                else:
                    print("Account Holder Name is Unmatched!")
            else:

                print("Account Number is unmatched!")
                