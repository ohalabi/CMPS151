# mainModule.py

import mymodule

# Use the functions from mymodule
name = "Alice"
print(mymodule.greet(name))

a = 10
b = 5
print(f"{a} + {b} = {mymodule.add(a, b)}")
print(f"{a} - {b} = {mymodule.subtract(a, b)}")