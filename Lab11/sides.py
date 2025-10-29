class Shape:
    def sides(self):
        print("not defined")

class Colour:
    def sides(self):
        print ("Red")

class child(Shape, Colour):
    def sides(self):
        print("4 Sides")

obj = square()
obj.sides()