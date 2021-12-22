# Julio Claros
# 114153234
# 2018-05-11
# Exercise

"""
Script that passes dimensions width and height of shape, calculates area and
perimeter
"""


class Shape:
    """
    Shape passes values and creates attributes width and height to object for
    calculating area and perimeter.

    Arg 1: Width (Int): Width dimension for object
    Arg 2: Height (Int): Height dimension for object

    Returns:
        Area (int): Area of object
        Parameter (int): Parameter of object
    """
    def __init__(self, width, height):
        self.width = int(width)
        self.height = int(height)

    def perimeter(self):
        perimeter = (self.width * 2) + (self.height * 2)
        return float(perimeter)
        raise NotImplementedError

    def area(self):
        area = self.height * self.width
        return float(area)
        raise NotImplementedError


if __name__ == '__main__':
    import sys
    shape = Shape(sys.argv[1], sys.argv[2])
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
