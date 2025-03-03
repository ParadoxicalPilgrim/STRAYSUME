a= float(input("Enter the cost price of the scooter: "))
b= float(input("Enter the repair cost : "))
c= float(input("Enter the selling price : "))

cp=a+b

p=c-cp

gainperc = (p/cp) * 100

gainperc= "{:.2f}".format(gainperc)

print("The gain percentage is:", gainperc, "%")
