from shapes.circle import Circle
from shapes.rectangle import Rectangle
from shapes.triangle import Triangle
from shapes.square import Square

shapes = [
    Circle(6),
    Triangle(8, 4, 5),
    Rectangle(10, 5),
    Square(7)
]

for shape in shapes:
    print(shape.__repr__())
    print(shape)
    print(f"Area is equal to: {shape.area()}\n")