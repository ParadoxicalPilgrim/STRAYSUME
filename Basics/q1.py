#PRT

p=float(input("Enter the principal amount: "))
r=float(input("Enter the rate of interest: "))
t=float(input("Enter the duration of the interest: "))

roi=r//100

si=(p*roi*t)/100

print(f"The simple interest will be: {si}")
