from shapes.circle import Circle
from shapes.rectangle import Rectangle
from shapes.triangle import Triangle

shapes = [
    Circle(6),
    Triangle(8, 4),
    Rectangle(10, 5)
]

for shape in shapes:
    print(shape)