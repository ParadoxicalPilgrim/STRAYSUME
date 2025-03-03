# SUM EXCLUDING MULTIPLES

n=int(input("Enter n: "))
x=int(input("Enter x: "))

for i in range (0,n+1):
    if i%x==0:
        continue
    sum+=i

print("The sum from 1 to ",n,"by excluding the multiples of",x,"is",sum)


