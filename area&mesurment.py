a=int(input("enter 1 for area and 2 for perameter: "))

circul=int(input("enter 1 for circul and 2 for square: "))



if (a==2 and circul==1):
    radius =float(input("please enter radius of circul: "))
    pcir=2*radius*3.14285

    print("the perameter of circul is: ", pcir)
elif (a==1 and circul==1):
    radius =float(input("please enter radius of circul: "))
    rfora=radius**2
    acir=rfora*3.14285

    print("the area of circul is: ", acir)
else:
    pass

if (a==1 and circul==2):
    side= int(input("enter side of squaer "))
    asq= side**2
    print("the area of squaer is: ", asq)
    
elif (a==2 and circul==2):
    side= int(input("enter side of squaer "))
    ps=4*side
    print("the perameter of squaer is: ", ps)
    
else:
    pass

z=input()