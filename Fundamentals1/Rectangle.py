class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return "Area: " + str(self.area()) + " Perimeter: " + str(self.perimeter())

class ShapeList:
    def __init__(self):
        self.shapes = []
        self.index = 0

    # adds a single Rectangle to the shapes
    def add(self, shape):
        if len(self.shapes) < 10:
            self.shapes.append(shape)
            print("Shape added successfully")
            self.index += 1
        else:
            print("List is full")


    def print_shapes(self):
        for shape in self.shapes:
            print(shape)

class TestRectangle:
    @staticmethod
    def main():
        sl = ShapeList()
        rect1 = Rectangle(10, 20)
        sl.add(rect1)
        sl.add(Rectangle(10, 20))
        sl.print_shapes()


        print(f"Rectangle area: {rect1.area()}")
        print(f"Rectangle perimeter: {rect1.perimeter()}")
        print(rect1)

        rect_list = [
            Rectangle(10, 20),
            Rectangle(5, 10),
            Rectangle(2, 4),
        ]
        for rec in rect_list:
            print(f"Area: {rec.area()}")

        rect_dictionary = {1: "Area: " + str(rect1.area()), 2: "Perimeter: " + str(rect1.perimeter())}

        for rec in rect_dictionary:
            print(rec, rect_dictionary[rec])


TestRectangle.main()