def rec_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return(rec_fib(n-1) + rec_fib(n-2))
terms = int(input("Enter the number of terms you want: "))
if terms <= 0:
    print("Enter a positive term.")
else:
    for i in range(terms):
        print(rec_fib(i))
