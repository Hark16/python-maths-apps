p = int(input("enter the principle:" ))
r = int(input("enter the rate of intrest:" ))
n = int(input("enter the number of year:" ))
pr = 100

si = int((p*r*n)/pr)

print ("the simple intrest is:", si)

A = p+si

print ("the amount is:", A)
months = n*12
EMI = A/months

print ("the E M I is:", EMI)

z = int(input("press enter  to exit"))