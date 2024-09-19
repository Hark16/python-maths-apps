p = float(input("मूलधन :" ))
r = float(input("ब्याज कि दर:" ))
n = int(input("वर्ष :" ))
pr = 100

si = int((p*r*n)/pr)

print ("सधारण ब्याज :", si)

A = p+si

print ("मिश्रधन :", A)
months = n*12
EMI = A/months
print("मासिक किस्त: ", EMI)

z = int(input("press enter  to exit"))