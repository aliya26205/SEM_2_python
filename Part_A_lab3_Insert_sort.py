def insert(ls,s):
    ls.sort()
    for i in range(len(ls)):
        if ls[i]>s:
            ls.insert(i,s)
            return ls
    ls.append(s)
    return ls

n=int(input("Enter the number of elemets:"))
ls=[]
print("Enter",n,"Elemets to the list:")
for i in range(n):
    ls.append(int(input()))
s=int(input("Enter the element to be inserted"))
print("List before inserting :")
print(ls)
print("List after inserting:")
result=insert(ls,s)
print(result)