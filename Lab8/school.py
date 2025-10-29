class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

class ClassTeacher(Teacher):
    def __init__(self, name, age, subject, ac):
        super().__init__(name, age, subject)
        self.ac = ac

a = Person("Anuj", 20)
b = Teacher("Hello", 22, "Science")
c = ClassTeacher("Hello2", 25, "Maths", "K")

print(a.name, a.age)
print(b.name, b.age, b.subject)
print(c.name, c.age, c.subject, c.ac)
