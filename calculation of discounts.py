class Item:
    def __init__(self,name,price,discount):
        self.name=name
        self.price=price
        self.discount=discount
        self.final_price=self.price-(self.price*self.discount/100)
        print(f"{self.name} after discount : {self.final_price}")


    def __del__(self):
        print(f"{self.name} removed from the shopping cart")




p1=Item("playstation 5 ",50000,10)
del p1
p2=Item("X box controller",2500,15)
