class person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age

    def show(self):
        print("Name =",self.name)
        print("Age =",self.__age)

class student(person):
    def __init__(self,name,age,marks):
        super().__init__(name,age)
        self.marks=marks

    def show(self):
        super().show()
        print("Marks=",self.marks)

students=[]
while True:
    print("-----Menu-----")
    print("1.Enter Student")
    print("2.Display students")
    print("3.Exit")
    ch=int(input("Enter your choice:"))

    if ch==1:
        name=input("Enter name :")
        age=int(input("Enter age:"))
        marks=int(input("Enter marks:"))
        s=student(name,age,marks)
        students.append(s)
        print("Enter student Successfully!!")

    elif ch==2:
        if len(students)==0:
            print("No record foundd!!")
        else:
            for i in students:
                s.show()

    elif ch==3:
        print("Exiting the proogramm!!")
        break
    else:
        print("Enter correct choiceee")