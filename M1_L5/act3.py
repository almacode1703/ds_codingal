number1 = int(input("Enter first number : "))
number2 = int(input("Enter second number : "))

def add_num(n1,n2):
    return n1+n2

def sub_num(n1,n2):
    return n1-n2

def mul_num(n1,n2):
    return n1*n2

def div_num(n1,n2):
    return n1/n2

print(f"Summation : ", add_num(number1, number2))
print(f"Subtraction : ", sub_num(number1, number2))
print(f"Multiplication : ", mul_num(number1, number2))
print(f"Division : ", div_num(number1, number2))