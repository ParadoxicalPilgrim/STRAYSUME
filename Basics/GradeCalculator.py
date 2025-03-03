print("GRADE CALCULATOR!")

phy=float(input("Enter your physics marks: "))
chem=float(input("Enter your chemistry marks: "))
cse=float(input("Enter your computer science marks: "))
eng=float(input("Enter your English marks: "))

avg=(phy+chem+cse+eng)/4

if avg>90 and avg<=100:
    print("Grade: A+")
elif avg>80 and avg<=90:
    print("Grade: A")
elif avg>70 and avg<=80:
    print("Grade: B+")
elif avg>60 and avg<=70:
    print("Grade: B")
elif avg>50 and avg<=60:
    print("Grade: C")
elif avg>40 and avg<=50:
    print("Grade: D")
elif avg<40:
    print("Grade: F")


