# in this program we will be writing a code that executes an ATM session where constructor starts transaction and destructor ends it with a thank you message


class ATM:
    def __init__(self,user):
        self.user=user
        print(f"welcome Ms/Mr {self.user}, your transaction initiated")


    def __del__(self):
        print(f"thank you {self.user},your transaction is successful")


atm1=ATM("siva")
atm2=ATM("rahul sipligunj")
atm3=ATM("anushka shetty")
del atm1
del atm2
del atm3