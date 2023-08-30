#!/usr/bin/python3
"""Module providing class 'MagicClass' to replicate bytecode for Holberton"""
import math

class MagicClass:
    """
    Definition of a class to replicate the aforementioned bytecode
    """
    def __init__(self, radius=0):
        """
        Instantiate a MagicClass object to represent a circle
        """
        self.__radius = 0  # Initialize radius to 0

        # Check if radius is a valid number (int or float)
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')

        self.__radius = radius  # Assign the provided radius

    def area(self):
        """
        Compute the area of a circle
        """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """
        Compute the circumference of a circle
        """
        return 2 * math.pi * self.__radius
