n=20

a,b=0,1

for i in range(n):
    if not(a==1 and b==1):
        print(a)
    a,b=b,a+b