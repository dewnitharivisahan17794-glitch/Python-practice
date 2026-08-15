
import json


class PD():
    def __init__(self):
        self._Account_Number = 11234566783
        self._Account_Holder_Name = "B C P Rathnayake"
        self._Serial_Num = "2700-56"
        self.file_path = "Update.json"
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
                self.Balance = data["Balance"]

        except FileNotFoundError:
            self.Balance = 234467.97
            self.up_b() 

    def up_b(self):
        with open(self.file_path, "w") as file:
            json.dump({"Balance": self.Balance}, file, indent=4)
