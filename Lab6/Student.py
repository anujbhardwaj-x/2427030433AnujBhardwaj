class Student:
    def __init__(self,name,rn,marks):
        self.name=name
        self.rn=rn
        self.marks=marks

    def g(self):
        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"
        
    def display(self):
        print("\n --- Student Info --- \n")
        print(f"Name: {self.name}")
        print(f"Roll No.: {self.rn}")
        print(f"Marks: {self.marks}")
        print(f"Result: {self.g()}")
        print("---------------------")

s1= Student("Anuj",1,100)
s2= Student("Anujj",2,10)
s3= Student("Anujjj",3,1)

s1.display()
s2.display()
s3.display()
