Chp 1 Input and Output
""" >A computer store is offering discounts on laptops and tablets. 
The store has announced a 10% discount on laptops and a 25% discount on tablets. 
The original price of a laptop is QR 5000, and for a tablet, it’s QR 1500. 
Write a Python program to read the number of laptops and tablets bought 
by the customer, then print the total discount amount for each item and 
the total price for all items. """

tablet_discount = 0.25
laptop_discount = 0.10

tablet_price = 1500
laptop_price = 5000

num_laptops = int(input('Enter the number of laptops: '))
num_tablets = int(input('Enter the number of tablets: '))

laptops_total_discount = num_laptops * laptop_price * laptop_discount
tablet_total_discount = num_tablets * tablet_price * tablet_discount

laptop_total_price = (laptop_price*num_laptops) - laptops_total_discount
tablet_total_price = (tablet_price*num_tablets) - tablet_total_discount

total_price = laptop_total_price + tablet_total_price

print(f'laptop total discount: {laptops_total_discount}')
print(f'tablet total discount: {tablet_total_discount}')
print(f'total price {total_price}')
