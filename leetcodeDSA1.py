from collections import Counter
a=[1,1,1,1,2,3,4,5,3,2,4,4,5,5,6,6,4,2,3,4,4,5,3,2,3]
b=Counter(a)

if b[1]>1:
    print("true")
else:
    print("false")
