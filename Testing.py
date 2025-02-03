Chp 1 Input and Output
############### Ex 1 #####################
### Write a program that asks the user to enter an integer number 
### composed of three digits. Your program should print the total of the digits.

# Prompt the user to enter a three-digit integer number
number = int(input("Enter a three-digit integer: "))

# Extract the digits
hundreds = number // 100
remaining = number % 100
tens = remaining // 10
units = remaining % 10

# Calculate the total of the digits
total = hundreds + tens + units

# Display the result
print(f"The total of the digits is: {total}")

############### Ex 2 #####################
# Surface and volume of cone 
import math

# Define the value of PI
PI = 3.1415

# Prompt the user for radius and height
radius = float(input("Enter the radius of the cone: "))
height = float(input("Enter the height of the cone: "))

# Calculate the slant height of the cone
slant_height = math.sqrt(radius**2 + height**2)

# Calculate the volume of the cone
volume = (1/3) * PI * radius**2 * height

# Calculate the total surface area of the cone
lateral_surface_area = PI * radius * slant_height
base_area = PI * radius**2
total_surface_area = lateral_surface_area + base_area

# Display the results
print(f"Volume of the cone: {volume:.2f}")
print(f"Total surface area of the cone: {total_surface_area:.2f}")