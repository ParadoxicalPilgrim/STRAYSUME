# QUIZ BEE TEAM CREATION


rno=int(input("Enter registration number: "))


if rno<10:
    print("Invalid input!")


else:
    code=str(rno)
    first=int(code[0])
    last=int(code[-1])


    difference=abs(first-last)
    print(f"The participant is added to group {difference}")

