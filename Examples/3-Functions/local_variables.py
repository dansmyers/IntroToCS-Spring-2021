"""
Examples of local variables
"""

### Key ideas:
#
# Variables declared within a function are LOCAL to that function
#
# Local variables are only visible ("in scope") while the function executes
#
# When the function returns, local variables go "out of scope" and are no longer accessible
#
# Different functions may use the SAME NAMES for their local variables -- these do not
# interfere with each other because they are stored in DIFFERENT MEMORY LOCATIONS


from math import pi

def area_of_circle(radius):
    return radius ** 2 * pi
    
def perimeter_of_circle(radius):
    diameter = 2 * radius
    return pi * diameter
    
    
### Main
radius = float(input("Enter the radius of a circle: "))

area = area_of_circle(radius)
perimeter = perimeter_of_circle(radius)

print('The area is %.2f and the perimeter is %.2f.' % (area, perimeter))


# The next line will generate an error because diameter is a local variable
# It is only visible while the perimeter_of_circle function is executing
# and cannot be accessed outside of the function

print('The diameter is %.2f.' % diameter)  ### Error
