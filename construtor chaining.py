# in this program we will be creating class called animal with a constructor and destructor and inherit from a class girafee

class Animal:
    def __init__(self):
        print("animal is created")


    def __del__(self):
        print("animal removed")


class Girafee(Animal):
    def __init__(self):
        super().__init__()
        print("girafee is created")


    def __del__(self):
        print("girafee removed")
        super().__del__()


g=Girafee()
del g




