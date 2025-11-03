class Person:
    def get_roll(self):
        return "Roll information not available for general person."


class Student(Person):
    def __init__(self, roll_no):
        self.roll_no = roll_no

    def get_roll(self):
        return f"Student Roll Number: {self.roll_no}"


class Staff(Person):
    def __init__(self, staff_id):
        self.staff_id = staff_id

    def get_roll(self):
        return f"Staff ID: {self.staff_id}"

class Grade:
    def Calculate(self, mark1, mark2=None, mark3=None):
        if mark2 is None and mark3 is None:
            return f"Single Subject Grade: {mark1}"
        elif mark3 is None:
            avg = (mark1 + mark2) / 2
            return f"Average Grade of 2 Subjects: {avg}"
        else:
            avg = (mark1 + mark2 + mark3) / 3
            return f"Average Grade of 3 Subjects: {avg}"

class Score:
    def __init__(self, marks):
        self.marks = marks

    def __add__(self, other):
        return Score(self.marks + other.marks)

    def __str__(self):
        return f"Total Marks: {self.marks}"

p1 = Person()
s1 = Student(101)
st1 = Staff("S-202")

print("=== Method Overriding ===")
print(p1.get_roll())
print(s1.get_roll())
print(st1.get_roll())


g = Grade()
print("\n=== Method Overloading ===")
print(g.Calculate(85))
print(g.Calculate(80, 90))
print(g.Calculate(75, 85, 95))

print("\n=== Operator Overloading ===")
score1 = Score(88)
score2 = Score(92)
total = score1 + score2
print(score1)
print(score2)
print(total)