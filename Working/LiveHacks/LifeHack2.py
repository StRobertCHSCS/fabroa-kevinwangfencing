weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))

BMI = "#1 / #2^2"

if BMI > 25.0:
    print ("You are overweight")

elif BMI >= 18.5 or <= 25.0:
    print("You are normal weight")

else:
    print("you are underweight")