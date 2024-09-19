a=int(input("enter number to get its table"))
table=[x*a for x in range (11)]
table.pop(0)
print("the table of", a)
print("is: ", table)
z=input("press enter to quit")