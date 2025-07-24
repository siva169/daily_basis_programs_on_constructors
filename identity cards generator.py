#inthis program we will be writing a program which generates identity cards automatically based on the info and designation

class Employee:
    id_counter=243


    def __init__(self,name):
        Employee.id_counter+=1
        self.id=Employee.id_counter
        self.name=name
        print(f"the ID card of the employee named {self.name} is ID: {self.id}")


    def __del__(self):
        print(f" employee {self.id} record deleted")

e1=Employee("viraj")
e2=Employee("jhansi")
e3=Employee("rani")
e4=Employee("shivaji")























