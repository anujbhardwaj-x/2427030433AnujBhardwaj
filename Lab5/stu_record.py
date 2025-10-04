# Function with course, *subjects, **details
def stuRecord(course, *subjects, **details):
    print("Course:", course)
    print("Subjects:", subjects)
    for k, v in details.items():
        print(f"{k}: {v}")

# Example call
stuRecord("B.Tech", "Maths", "Python", "DBMS", name="Anuj", age=18, grade="A")
