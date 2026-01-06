from colorama import Fore, Style, init

init(autoreset=True)

num1 = 50
num2 = 5

print("Number1 :", num1)
print("Number2 :", num2)
print("Summation:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Floor Division:", num1 // num2)
print("Modulus:", num1 % num2)
print("Square:", num1 ** 2)
print("Sqrt:", num1 ** 0.5)

print("Equals:", Fore.RED + str(num1 == num2))
print("Is num1 greater than num2:", Fore.GREEN + str(num1 > num2))
print("Is num1 less than num2:", Fore.RED + str(num1 < num2))
print("Num1 and Num2 are Not Equal !!", Fore.GREEN + str(num1 != num2))

# Result of an Equation
result = ((num1 // 2) * (num2 ** 2)) / 10
print("Result:", result)
