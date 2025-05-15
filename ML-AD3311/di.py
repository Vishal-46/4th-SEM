import math
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Distance between points:", distance)


n = int(input("Enter number of variables: "))
values = []
for i in range(n):
    val = input(f"Enter value {i+1}: ")
    values.append(val)
k = int(input("Enter number of steps to circulate: "))
rotated = values[-k:] + values[:-k]
print("Values after circulation:", rotated)

