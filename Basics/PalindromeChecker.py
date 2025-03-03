strr=input("Enter the word to check for palindrome: ")
str1=''

for i in range(len(strr)-1,-1,-1):
    str1+=strr[i]

if strr==str1:
    print("The entered word is a palindrome!")
else:
    print("The entered word is not a palindrome!")

    
