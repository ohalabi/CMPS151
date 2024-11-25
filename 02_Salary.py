# Input: Read the gross salary of the employee
gross_salary = float(input("Enter the gross salary of the employee: "))

# Process: Calculate the tax amount and net salary
tax_rate = 0.15
tax = gross_salary * tax_rate
net_salary = gross_salary - tax

# Output: Display the net salary
print(f"The net salary after deducting 15% tax is: {net_salary:.2f}")
