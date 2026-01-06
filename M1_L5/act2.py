#Factorial of a number
def factorial(number):
    if number == 0 or number == 1 : 
        return 1
    else:
        return number * factorial(number-1)
        

number = int(input("Enter the number you want factorial of : "))
if number < 0:
    print("Number can't be negative")
else :    
    print(f"The Factorial of {number} : ", factorial(number))

