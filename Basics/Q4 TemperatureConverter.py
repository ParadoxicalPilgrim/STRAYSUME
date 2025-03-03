def convert(x,y):
    f=(x*9/5)+32
    c=(y-32)*5/9
    return c,f


x=float(input("Enter the temperature in celsius: "))
y=float(input("Enter the temperature in fahrenheit: "))
c,f=convert(x,y)
print(x,"C in fahrenheit is:",f)
print(y,"F in degree celsius is:",c)