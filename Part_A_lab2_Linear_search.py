def linear_search(ls,s):
    for i in range(len(ls)):
        if s==ls[i]:
            return i+1
    else:
        return 0


n=int(input("Enter the number of elemets:"))
ls=[]
print("Enter",n,"Elemets to the list:")
for i in range(n):
    ls.append(int(input()))
s=int(input("Enter the search elements"))
result=linear_search(ls,s)
if result==0:
    print("No element found!!")
else:
   print("Elemets found at :",result)
    