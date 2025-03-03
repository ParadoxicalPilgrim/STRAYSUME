def converter(s):
    if s[-3:]=='ing':
        s=s+'ly'
        return s
    elif len(s)>=3:
        s=s+'ing'
        return s
    else:
        return s

s=input("Enter a string: ")
print("The modified string is: ",converter(s))
