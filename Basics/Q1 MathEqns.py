import math as m

def calc(x):
    f=m.tan(2*x)
    f1=-2*(m.sin(2*x))
    f2=-4*(m.cos(2*x))
    tupp=tuple([f,f1,f2])
    return tupp


y=float(input("Enter the value of x: "))
f1,f2,f3=calc(y)    
print("The value of tan(2x) is: ",f1)
print("The value of -2sin(2x) is: ",f2)
print("The value of -4cos(2x) is: ",f3)
