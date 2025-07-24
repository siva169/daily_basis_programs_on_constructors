# in this program we will be making a code that constructs and destructs simple object

class Person:
    def __init__(self):
        print("simple object is created")


    def __del__(self):
        print("object ius destroyed")


p=Person()
del p