import math

#calculate the Circumference and area of a circle

radius = float(input("Enter the radius of a circle: "))

circumference = 2 * math.pi *radius
area = math.pi * pow(radius,2)

print(f"The circumference is: {round(circumference,2)}cm.")
print(f"The Area is: {round(area,2)}cm.")
print("===================================================")


#Calculate the Hypotenuse of a right triangle

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a,2) + pow(b,2))

print(f"Side C = {round(c,2)}cm.")