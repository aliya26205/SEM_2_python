def fact(n):
    if n==0 or n==1:
        return 1
    else :
        return n*fact(n-1)

n=int(input("Enter number:"))
if n<0:
    print("no factorial of negative number!!")
else:
    print("Factorial of",n,"is=",fact(n))