t = float(input("Enter temperature: "))
unit = input("Is this in (C)elsius or (F)ahrenheit? ").strip().upper()
if unit == "C":
    print("In Fahrenheit:", (t * 9/5) + 32)
elif unit == "F":
    print("In Celsius:", (t - 32) * 5/9)
else:
    print("Invalid unit")
