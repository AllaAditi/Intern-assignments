class Circle():
    """
    This is ths calculation of Area and Perimeter of a circle
    """
    # r is radius of a circle
    def __init__(self, r):
        self.radius = r

    def area(self):
        """
        area
        :return:
        """
        return self.radius ** 2 * 3.14

    def perimeter(self):
        """
        perimeter
        :return:
        """
        return 2 * self.radius * 3.14


class Rectangle():
    """
    This is the calculation of Area and Perimeter of a Rectangle
    """
    # l_r is length of a rectangle
    # b_r is breadth of a rectangle
    def __init__(self, l_r, b_r):
        self.length = l_r
        self.breadth = b_r

    def area(self):
        """
        area
        :return:
        """
        return self.length * self.breadth

    def perimeter(self):
        """
        perimeter
        :return:
        """
        return 2 * self.length * self.breadth


class square():
    """
    Area and Perimeter of a square
    """
    def __init__(self, s):
        self.side = s

    def area(self):
        """

        :return:
        """
        return self.side * self.side

    def perimeter(self):
        """

        :return:
        """
        return 4 * self.side


class parallelogram():
    """
    Area and perimeter of a parallelogram
    """
    # b_p breadth of a parallelogram
    # h_p height of a parallelogram
    # s_p side of a parallelogram

    def __init__(self, b_p, h_p, s_p):
        self.base = b_p
        self.height = h_p
        self.side = s_p

    def area(self):
        """
        area
        :return:
        """
        return self.base * self.height

    def perimeter(self):
        """
        perimeter
        :return:
        """
        return 2 * (self.base + self.side)


if __name__ == '__main__':
    while True:
        try:
            shape = input(" select (circle/rectangle/square/parallelogram): ").lower()
            """
            select the shape from the above shapes
            """
            if shape == 'circle':
                radius = float(input("Enter the radius of the circle: "))
                circle = Circle(radius)
                print(f"Area of circle  {radius} is {circle.area()}")
                print(f"Perimeter of circle  {radius} is {circle.perimeter()}")

            elif shape == 'rectangle':
                length = float(input("Enter the length of rectangle: "))
                breadth = float(input("Enter the breadth of rectangle: "))
                rectangle = Rectangle(length, breadth)
                print(f"Area of rectangle  is {rectangle.area()}")
                print(f"Perimeter of the rectangle  is {rectangle.perimeter()}")

            elif shape == 'square':
                Side = float(input("Enter the side of Square: "))
                square = square(Side)
                print(f"Area of Square with  Side {Side} is {square.area()}")
                print(f"Perimeter of Square with {Side} is {square.perimeter()}")


            elif shape == 'parallelogram':
                base = float(input("Enter the base of parallelogram : "))
                heigth = float(input("Enter the heigth of parallelogram : "))
                Side = float(input("Enter the side of parallelogram : "))
                prl = parallelogram(base, heigth, Side)
                print(f"Area of parallelogram  is {prl.area()}")
                print(f"Perimeter of parallelogram  is {prl.perimeter()}")

            else:
                raise ValueError("Invalid shape entered. Please enter either 'circle' or 'rectangle' or 'Square'")
        except ValueError as e:
            print(e)
