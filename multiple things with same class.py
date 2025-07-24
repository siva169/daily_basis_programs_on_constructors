#in this program we will be writing code which deals with multiple things with same class

class Tiger:
    def __init__(self,name,years):
        self.name=name
        self.years=years
        print(f"{self.name} is born")


    def __del__(self):
        print(f"after {self.years} years")
        print(f"{self.name} is no more ")


a=Tiger("rocket",16)
b=Tiger("romeo",18)
del a
del b