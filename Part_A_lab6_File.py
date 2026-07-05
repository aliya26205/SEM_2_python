with open("Source.txt","w") as file:
    file.write("HEllo jii")
    file.write("\nKidar hooo app??")
    print("source file createdd")

with open("Source.txt","r") as source:
    data=source.read()

with open("destination.txt","w") as desti:
    desti.write(data)
    print("Copied successfullyy")
    