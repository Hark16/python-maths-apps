def script():
    p = int(input("enter the principle :"))
    r = int(input("enter the rate of intrest :"))
    n = int(input("enter the number of years :"))
    d = 100
    rc = d+r 
    full = rc/d 
    year = full**n 
    A= int(p*year)
    print ("the amount of compount intrest is: ", A)
    ci = A-p 
    print ("the compound intrest is:", ci)
    restart =input("Would you like to restart this program?")
    if restart == "yes" or restart == "y":script()
    if restart == "n" or restart == "no":
        print ("Script terminating. Goodbye.")
script()