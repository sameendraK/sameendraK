"""l=[]
sl=[]
di={}
count=0
a=input("enter string")
for i in a:
    l.append(i)
l.sort()
for i in range(len(l+1)):
    if l[i]==l[i+1]:
        count+=1
    else:
        di[l[i]]=count
        sl.append(count)
        count=0
sl.sort(reverse=True)
if sl[0]==sl[1]:
    print("0")
else:
    d=sl[0]
print(b)
print(l)
print(sl)"""

"""
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
"""
"""
nl=[]
a=int(input("Enter a number"))
for i in range(1,a):
    b=a%i
    if b==0:
        nl.append(i)
if len(nl)>1:          
    print("NOT prime")
else:
    print("Prime")
"""



a=int(input("Enter a number"))
for i in range(2,a):
    b=a%i
    if b==0:
        print("Not Prime")
        break
    else:
        print("Prime")
        break