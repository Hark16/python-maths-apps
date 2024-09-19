a=int(input("enter an year"))

if (a%400==0):
    print ("the year is century leap year")
elif(a%100==0):
    print ("the year is century but non leap year")
elif(a%4==0):
    print ("the year is lleap year")
else:
    print ("non leap")
z=input("press enter for quit")