from figurs-1 import Rectangle, Square, Circle

rec1 = Rectangle(10,5)
rec2 = Rectangle(15,7)
# print("rec1.width = ", rec1.width)
# print("rec1.heigth = ", rec1.height)
# print("rec2.width = ", rec2.width)
# print("rec2.heigth = ", rec2.height)
# print(rec1.getArea(), rec2.getArea())

square_1 = Square(5)
square_2 = Square(10)

circle_1 = Circle(3)
circle_2 = Circle(5)

# print(square_1.getAreaSquare(), square_2.getAreaSquare())

# figures = [rec1, rec2, square_1, square_2]
#
# for figure in figures:
#     if isinstance(figure,Square):
#         print(figure.getAreaSquare())
#     else:
#         print(figure.getArea())

figures = [rec1, rec2, square_1, square_2, circle_1, circle_2]

for figure in figures:
    if isinstance(figure,Square):
        print(figure.getAreaSquare())
    elif isinstance(figure,Circle):
        print(figure.getCircleArea())
    else:
        print(figure.getArea())

# print(circle_1.getCircleArea(), circle_2.getCircleArea())