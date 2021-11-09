#amstrong_number
"""a=int(input("Enter value"))
c=0
d=a
if a<=0:
    print ("Enter +ve value")
elif d>0:
    b=d%10
    e=b**3
    c+=e
elif c==a:
    print ("ams")
else:
    print("no") """
    
    

sm=0
a=int(input("Enter number"))
c=a
while c>0:
    b=c%10
    c//=10  
    sm=sm+b*b*b
if sm==a:
    print ("ams")
elif c!=a:
    print("not an ams")