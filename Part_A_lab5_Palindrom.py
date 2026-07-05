s=input("Enter a String to check palindorm:")
s=s.lower()
rev=s[::-1]
print("Orginal String:",s)
print("Reverse String:",rev)
if s==rev:
    print("Its a Palindrom!!!")
else:
    print("Not a Palindrom!!")