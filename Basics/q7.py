# SERIES SUM

x= int(input("Enter the value of x: "))
n=int(input("Enter the value of n: "))

sum=0


for i in range(0,n+1):
    term=(-x)**i
    sum+=term

print(f"Sum of the series is: {sum}")
