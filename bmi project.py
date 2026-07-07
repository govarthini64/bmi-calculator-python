weight = float(input("Enter your weight(kg):"))
height = float(input("Enter your height(cm):"))

height = height/100
BMI = weight/(height*height)

print(f"Your BMI is: {BMI:.2f}")

if BMI < 18.5:
    print("Underweight")
elif 18.5 <= BMI <= 24.9:
    print("Normal weight")
elif 25.0 <= BMI <= 29.9:
    print("Over weight")
else:
    print("Obese")
