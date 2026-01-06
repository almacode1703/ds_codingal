# Calculate BMI

weight = float(input("Enter your body weight in kg: "))
height = float(input("Enter your height in cm : "))

bmi = weight / (height /100) ** 2

if bmi <= 18.4:
    print("You are under weight")
elif (bmi > 18.4) and (bmi <= 24.9):
    print("You are healthy")
elif (bmi > 24.9) and (bmi <=29.9):
    print("You are overweight")
elif (bmi > 29.9) and (bmi <=34.9):
    print("You are severely overweight ")
elif (bmi > 34.9) and (bmi <=39.9):
    print("You are obese")
else :
    print("You are severely obese")
