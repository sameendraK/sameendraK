a=int(input("enter number"))
b=int(input("enter range"))
for i in range (1,b+1):
        c=a*i
        print(c)
con=input("enter y or n")
while con=="y":
    a=int(input("enter number"))
    b=int(input("enter range"))
    for i in range (1,b+1):
        c=a*i
        print(c)
    con=input("enter y or n")
else:
    print("done")
