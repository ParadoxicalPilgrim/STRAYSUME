print("AREA CALCULATOR!")

tri_b=float(input("Enter the base of the triangle: "))
tri_h=float(input("Enter the height of the triangle: "))

parl_b=float(input("Enter the base of the parallelogram: "))
parl_h=float(input("Enter the height of the parallelogram: "))

cyl_r=float(input("Enter the radius of the cylinder: "))
cyl_h=float(input("Enter the height of the cylinder: "))

tri_a=0.5*tri_b*tri_h
parl_a=parl_b*parl_h
cyl_a=2*3.14*cyl_r*cyl_h + 2*3.14*cyl_r*cyl_r

print(f"The area of the triangle is: {tri_a}")
print(f"The area of the parallelogram is: {parl_a}")
print(f"The area of the cylinder is: {cyl_a}")

