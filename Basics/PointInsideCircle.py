x=float(input("Enter the x coordinate of the point: "))
y=float(input("Enter the y coordinate of the point: "))
r=float(input("Enter the radius of the circle: "))

dist=(x**2 + y**2)**0.5

if dist>r:
    print("The point is outside the circle.")
elif dist==r:
    print("The point lies on the circumference of the circle.")
else:
    print("The point lies inside the circle.")

    
