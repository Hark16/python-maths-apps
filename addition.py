def script():
    f=int(input("how many time you wanna run this program"))
    for script in range(f):
        a=int(input())
b=int(input())
        c=a+b 
        print(c)
        d=input("wanna continue")
        if d=="y":script()
        if d=="n":
            print("good bye")

script()