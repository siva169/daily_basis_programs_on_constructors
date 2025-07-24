# in this program we will doing a program by using workers in construction company

class Worker:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f"the name of the worker is {self.name},the age of the worker is {self.age}")

    def __del__(self):
        print(f"worker {self.name} removed from company")

w=Worker("venkat",25)
del w
w=Worker("subash",35)
del w
w=Worker("yedu kondalu",43)
del w