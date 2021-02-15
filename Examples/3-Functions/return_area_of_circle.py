"""
Another version of the area of a circle program
RETURN the calculated area so it can be used in another part of the program

CMS 120
"""

from math import pi

def area_of_circle(radius):
    """
    Calculate and return the area of a circle with the given input radius
    """
    
    area = radius ** 2 * pi
    return area
    
    
### Main

# Call area_of_circle multiple times, like in the previous example
#
# Now, the area calculated by the method is RETURNED so that it can
# be saved in a variable and used in another part of the program

a = area_of_circle(1)
print(a)

a = area_of_circle(10)
print(a)

a = area_of_circle(100)
print(a)
