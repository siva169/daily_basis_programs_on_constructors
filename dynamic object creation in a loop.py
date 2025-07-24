#in this program we will create a loop dynamically create and destroy objects
#observing storage cleanup

class Temp:
    def __init__(self,index):
        self.index=index
        print(f"object {self.index} created")


    def __del__(self):
        print(f"object {self.index} destroyed without any flaws")


for i in range(3):
    t=Temp(i)
    del t