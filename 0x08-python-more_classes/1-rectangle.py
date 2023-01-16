#!/usr/bin/python3
""" A class Rectangle that defines a rectangle """

class Rectangle:
    """class rectangle"""
    def __init__(self, width=0, heigth=0):
        """Initializing the instances"""
        self.width = width
        self.heigth = heigth

    @property
    def width(self):
        """width"""
        return self.__width

    @property
    def heigth(self):
        """heigth"""
        return self.__heigth

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
