class Shape:
    def __init__(self, *args):
        self.sides = args

class Triangle(Shape):
    def __init__(self, *args):
        super().__init__(*args)
    
    def validate_triangle(self):
        a, b, c = sorted(self.sides)
        if a + b > c:
            print("Valid Triangle")
        else:
            print("Invalid Triangle")

class Rectangle(Shape):
    def __init__(self, *args):
        super().__init__(*args)
    
    def validate_rectangle(self):
        if len(self.sides) != 4:
            print("Invalid Rectangle")
        elif self.sides[0] == self.sides[1] and self.sides[2] == self.sides[3]:
            print("Valid Rectangle")
        elif self.sides[0] == self.sides[2] and self.sides[1] == self.sides[3]:
            print("Valid Rectangle")
        elif self.sides[0] == self.sides[3] and self.sides[1] == self.sides[2]:
            print("Valid Rectangle")
        else:
            print("Invalid Rectangle")

# Reading inputs and creating objects
t = list(map(int, input().split()))
triangle = Triangle(*t)
r = list(map(int, input().split()))
rectangle = Rectangle(*r)

# Validating shapes
triangle.validate_triangle()
rectangle.validate_rectangle()
