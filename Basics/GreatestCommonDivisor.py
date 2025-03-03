n1=int(input("Enter a number: "))
n2=int(input("Enter another number: "))

if n1>n2:
    larger=n1
else:
    larger=n2

for i in range (1,larger+1):
    if (n1%i==0 and n2%i==0):
        gcd=i

print(f"The greatest common divisor is: {gcd}")

