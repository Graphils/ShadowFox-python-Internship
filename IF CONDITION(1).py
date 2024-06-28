# BMI  category based on user input
height = float(input("ENTER HEIGHT IN METERS:"))
weight = float(input("ENTER WEIGHT IN KILOGRAMS:"))
BMI = weight / (height) * 2
if BMI >= 30:
    print("Obesity")

elif BMI >= 25:
    print("Overweight")

elif BMI >= 18.5:
    print("Normal")

elif BMI <= 18.5:
    print("Underweight")

else:
    print("Normal")