class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, empid, salary):
        super().__init__(name, age)
        self.empid = empid
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, age, empid, salary, dept):
        super().__init__(name, age, empid, salary)
        self.dept = dept

class Certification:
    def __init__(self, cert):
        self.cert = cert

class Trainer(Employee, Certification):
    def __init__(self, name, age, empid, salary, cert):
        Employee.__init__(self, name, age, empid, salary)
        Certification.__init__(self, cert)

a = Person("Anuj", 19)
b = Employee("Anujj", 20, "B101", 2000)
c = Manager("Hello", 22, "C102", 3000, "CSE")
d = Trainer("Hello2", 23, "D103", 4000, "Python")

print(a.name, a.age)
print(b.name, b.age, b.empid, b.salary)
print(c.name, c.age, c.empid, c.salary, c.dept)
print(d.name, d.age, d.empid, d.salary, d.cert)
