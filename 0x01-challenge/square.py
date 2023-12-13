#!/usr/bin/python3
"""Create a class Square"""


class Square():
    """Define a class Square"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Define a constructor"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """Define a Perimter method"""
        return (self.width * 4)

    def __str__(self):
        """Define str method"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
