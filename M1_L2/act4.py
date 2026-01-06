# Swap Numbers using Temporary Variable

a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))
temp = 0

print(f"Before Swapping : a ={a}, b={b}")

temp = a 
a = b 
b = temp 

print(f"After Swapping : a ={a}, b={b}")