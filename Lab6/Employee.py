class Employee:
    def __init__(self,empid,name,sal):
        self.empid=empid
        self.name=name
        self.sal=sal

    def calcsal(self):
        DA=0.20*self.sal
        HRA=0.15*self.sal
        salary=self.sal+DA+HRA
        return salary
    
    def display(self):
        salary=self.calcsal()
        print("\n --- Salary --- \n")
        print(f"Emp ID: {self.empid}")
        print(f"Name: {self.name}")
        print(f"Salary in hand: {self.sal}")
        print(f"Salary CTC: {salary:.2f}")
        print("---------------------")

e1= Employee("AB1","Anuj",1500)
e2= Employee("AB2","Anujj",2500)
e1.display()
e2.display()
