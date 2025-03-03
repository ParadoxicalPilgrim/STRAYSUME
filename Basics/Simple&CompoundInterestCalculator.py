p=float(input("Enter the principle amount: "))
roi=float(input("Enter the rate of interest: "))
t=float(input("Enter the time in years: "))
n=int(input("Enter the number of times the interest is compounded per year: "))

si=(p*roi*t)/100
ci=p*(1+roi/n)**n*t


print(f"The simple interest is: {si}")
print(f"The compound interest is: {ci}")

