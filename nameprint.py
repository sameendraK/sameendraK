d="sameee"
a=int(input("enter range"))
b=int(input("enter number"))
m=range(1,a+1)
for i in m:
    n=i%b
    if n==0:
        print(d)
    else:
        print(i)