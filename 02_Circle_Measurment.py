"""
Write a program that asks the user to enter the radius of a circle. The program should calculate
and display the area and circumference of the circle using πr2 for the area and 2πr
for the circumference.
Hint: You can either use 3.14159 as the value of pi (π), or add the statement "import math"
to the start of the program and then use "math.pi" wherever you need the value of pi in
the program.
"""

# Import the math module to use math.pi
import math

### Input ###
# Ask the user to enter the radius of the circle
radius = float(input("Enter the radius of the circle:\n"))

### Processing ###
# Calculate the area  
area = math.pi * radius ** 2

# Calculate the circumference
circumference = 2 * math.pi * radius

### Output ###
# Display the results
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")
