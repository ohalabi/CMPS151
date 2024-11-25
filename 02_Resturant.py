
# Enter the charges for the food
food_charge = float(input("Enter the charge for the food: QR "))

# Calculate the tip
tip = food_charge * 0.18

# Calculate the tax
tax = food_charge * 0.07

# # Calculate the total amount
total = food_charge + tip + tax

# Display the amounts
print(f"Tip: QR{tip:.2f}")
print(f"Sales Tax: QR{tax:.2f}")
print(f"Total Amount: QR{total:.2f}")
