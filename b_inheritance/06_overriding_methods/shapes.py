# Import the math module
import math


class Circle:
    # Constructor defining attributes / instance variables for each Circle
    # Colour is an optional parameter, if it's not supplied then the default value ("Blue") is used
    def __init__(self, radius, colour="Blue"):
        # Store radius and colour information
        self.radius = radius
        self.colour = colour

    # Create a function to calculate the area of the circle
    def calc_area(self):
        # Formula for area of a circle: pi * r^2
        # Return calculation of area using math.pi as value for pi
        return math.pi * (self.radius * self.radius)

    # Create a function to display the circle's data
    def display(self):
        # Print out the pieces of the circle
        print(f"Circle[radius={self.radius}, colour={self.colour}]")


# Define a Sphere class that inherits from (is based on) our Circle class
class Sphere(Circle):
    # Constructor defining attributes / instance variables for each Sphere
    # Colour is an optional parameter, if it's not supplied then the default value ("Blue") is used
    def __init__(self, radius, colour="Blue"):
        # Pass the circle core attributes to the superclass section
        super().__init__(radius, colour)

    # Create a function to calculate the area of the sphere
    def calc_area(self):
        return 4 * super().calc_area()

    # Create a function to display the sphere's data
    def display(self):
        # Print out the pieces of the sphere
        print(f"Sphere[radius={self.radius}, colour={self.colour}]")
