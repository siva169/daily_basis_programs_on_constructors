# in this program we will be writing  a code using constructor based on students info


class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(f"name of the student is {self.name} ,age of the student is {self.age}")


s1=Student("phanindra",18)
s1.display()
print()
s2=Student("sivadarshini",6)
s2.display()
print()
s3=Student("manohar",22)
s3.display()
print()
s4=Student("akhil",15)
s4.display()




