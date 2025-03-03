n=int(input("Enter the number you want to calculate the factorial for: "))

factorial=1

for i in range (1,n+1):
    factorial*=i

print(factorial)