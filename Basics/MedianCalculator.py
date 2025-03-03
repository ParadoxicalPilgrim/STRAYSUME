a=[23,4,234,667,97,23,67,90,80,81]


if len(a)%2==0:
    median=(a[int(len(a)/2)]+a[int(len(a)/2)-1])/2
    print(f"The median of the entered list is: {median}")
    
else:
    median=a[int(len(a)/2)]
    print(f"The median of the given list is: {median}")
    
    







