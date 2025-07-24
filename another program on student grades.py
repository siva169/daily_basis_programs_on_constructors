#in this program we will writing a program by creating a class that takes subject marks and calculates average in constructor



class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        self.avg=sum(marks)/len(marks)
        print(f"{self.name}'s average is {self.avg:.2f}")



    def __del__(self):
        print(f"{self.name}'s data is deleted from storage")


s=Student("raviteja",[73,85,95,45,69,89])
del s