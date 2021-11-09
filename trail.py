"""yes=1
c=input("Enter %s if you want to continue and no if you want to exit:"%yes)
while con=="yes":
        product=input("enter the product  ")
        quantity=int(input("Enter the quantity  "))
        check=input("Enter yes to continue and no to stop ")
        if check=="yes":
            item_total(product,quantity)
        if check=="no":          
            print("Thanks for shopping ")
            break
if con=="no":
    print("Thanks for shopping")"""
    
"""
a=[]
for i in range(1,41):    
    a.append(i)
print(a)"""
"""
lis=[]
count=1
for i in range(count):
    count+=1
    lis.append(i)
    print(count)
    print(lis)"""  
"""def test():
    o=[]
    c=1
    con=input("Enter yes to continue and no to stop ")
    while con=="yes":
        c+=1
        print(c)
test()   """    



"""    
o=[]
con=input("enter yes or no")
def recursion():
    while con=="yes":
        c+=1
        o.append(c)
        recursion()
    if con=="no":
        print(c)
recursion()
print(o)"""

"""



#compare elements in a list
l=[1,23,23,1,4,5,21,42,23,1]
a=len(l)
for i in a:
    if a[0]=a[i]:
        print ("same")"""



"""cc=gst_caluculation(product)
        o.append(cc)
        l.append(product)
                item_total=item_total1(product,quantity)
        grand_total=float(grand_total+item_total)
print("oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo",o)
print(l)
lo=len(l)
print(lo)
for i in range(0,lo):
    
    v=products.get(l[i])
    w=gst.get(l[i])
    y=v*quantity
    print("product  :  ",l[i])
    print("Cost per unit is: ",v)
    print("qunatiny = ",quantity)
    print("Item total is:",y)
    print("G.S.T of the item (in percentage)is:",w)
    print("Item price with G.S.T is:",y+o[i])
    print("***************************************************************")   """ 
"""
lis=[]
count=1
for i in range(count):
    count+=1
    lis.append(i)
    print(count)
    print(lis)"""
"""    
    
def ns(n):
    if n>0:    
        ns(n-1)
        print(n,end='   ')
p=int(input("enter a value"))
ns(p)
"""

"""
GIT
GIT HUB PAGES
MARK DOWN
MKDOCS
"""

"""
l=lambda a,b:a if a>b else b
print (l(223,34))"""

"""    
#program to sort odd numbers using kambda
lsit=(2,3,4,11,21,32,4,6,8,44,43)
order_lsit=tuple(filter(lambda x:(x%2!=0),lsit)
print(order_lsit)
"""
"""
lst = (10,22,37,41,100,123,29)  

oddlist = tuple(filter(lambda x:(x%3 == 0),lst)) # the tuple contains all the items of the tuple for which the lambda function evaluates to true    

print(oddlist)    
"""
"""
a=int(input("enter value"))
b=input("enter number")
if a==b:
    print("equal")
else:
    print("not equal")"""
"""a=int(input("enter number"))
if a<100:print("hi")"""



"""
x=5
y=20
#if x < y: print('foo'); print('bar'); print('baz')
if x < y: print('foo') else: print('bar')
"""


"""
w='a' + 'x' if '123'.isdigit() else 'y' + 'b'
print(w)"""




"""
w='a' + ('x' if '123'.isdigit() else 'y') + 'b'
print(w)    """


"""
x=10
y=40
if x<y:
    continue
else:
    continue"""
    
    
"""
n=int(input("enter the number"))
if n>0:
    for i in range(1,n):
        c=i*i
        print(c)
elif i<=0:
    print("enter a value greater than zero")
"""


"""
def is_leap(year):
    leap = False
    if year%4==0 and year%4==0:
        while true:
            print("true")
        else:
            print("false")
    # Write your logic here
    
    return leap

year = int(input())
print(is_leap(year))"""


"""
if __name__ == '__main__':
    print(*range(1, int(input())+1), sep='')
"""
    


"""
a=int(input("Enter number"))
for i in range(1,a+1):
        for j in range(1,i+1):
            pass
print(j,end="")
print("\n")
"""
        
        
        
"""        
n = int(input(""))
s = set(map(int,input("").split())
N=int(input(""))
s.pop(3)
s.pop(4)
s.remove(1)
s.discard(5)
sum_=sum(s)
print(sum_)
"""



"""
#printing the last element of a list
a=[1,2,3,4,5,6,4,3,2,5,2,3]
for i in a:
    pass
print(i)"""


"""
#printing the last but one element of a list:
a=[1,2,3,3,1,4,1,4,4,5,6,7,8,9,10,11,3,4,12]
b=len(a)
c=b-2   
print(a[c])
"""


"""
# Find the number of elements of a list.
a=[1,2,3,3,1,4,1,4,4,5,6,7,8,9,10,11,3,4,12]
b=0
for i in a:
    b+=1
print(b)
c=len(a)
print(c)
"""


"""
Find the kth item in a list
a=[1,2,3,3,1,4,1,4,4,5,6,7,8,9,10,11,3,4,12]
k=int(input("Enter the element ot be searched"))
for i in [k]:
    print(a[i])
print("list",a)
"""



"""
#print a list in reverse order
a=[1,2,3,4,5,6]
#a[::-1]
b=[]
z=len(a)-1
for i in range(len(a)):
    a.pop()
    b.insert(0,i)
print(b)
"""



"""
#palindrome list
a=[1,2,2,1]
if a[:]==a[::-1]:
    print("palindrome")
else:
    print("NOt a palindrome")
"""





"""
#flatten a list
def flatten_list(_2d_list):
    flat_list = []
    # Iterate through the outer list
    for e in _2d_list:
        if type(e) is list:
            # If the element is of type list, iterate through the sublist
            for item in e:
                flat_list.append(item)
        else:
            flat_list.append(e)
    return flat_list

nested_list = [[1, 2, 3, 4], [5, 6, 7], [8, 9]]
print('Original List', nested_list)
print('Transformed Flat List', flatten_list(nested_list))
"""
"""
#flatten a list, my veresion:
def flatten_list(_2d_list):
    flat_list=[]
    for element in (_2d_list):
        if type(element) is list:
            for i in element:
                flat_list.append(i)
        elif type(element) is not list:
            flat_list.append(element)
    return flat_list
        
lsit=[[1,3,4,2],[32,5,3,2,4],[3,5,2,4,5,2,4,4,2,4],[32,4,2,1],[3]]
print("original list",lsit)
print("modified list: ",flatten_list(lsit))
for 
"""
"""
#using itertools,flattening a list:
import itertools
lsit=[[1,3,4,2],[32,5,3,2,4],[3,5,2,4,5,2,4,4,2,4],[32,4,2,1],[3]]
a=list(itertools.chain(*lsit))
print(a)
"""




#checking and eliminating the consecutive list elements in a list:
#sample input:* (compress '(a a a a b c c a a d e e e e))
#sample output:(a b c a d e)
"""
l=[1,1,2,2,3,3,2,3,4]
b=len(l)
for i in b:
    b=[]
    l[i]
    for j in b :
        l[j]=l[j+1]
        if l[i]==l[j]:
            b.append(j)
        elif l[i]!=l[j]:
            b.append(i)
        print(b)"""
        
"""
  #b=6   
         #c=5  
con=input("enter y or n")    #y   
while con=="y":              #yes    
    a=int(input("enter number")) #4       
    b=int(input("enter range"))  #5       
    for i in range (1,b+1):      #i=1   
        c=a*i                    #        
        print(c)                 #                               
    con=input("enter y or n")                           
else:                                                  
    print("done")     

"""    
    


"""
L=[]
sum=0
n=int(input("enter number of values"))
for i in range(n):
    num=int(input("enter the value"))
    L.append(num)
print (L)
for i in range(n):
    sum=sum+L[i]
    avg=sum/n
print("average is ",avg)"""
    
    
    


"""
array=[3,5,6,2,12,9]
value=15
c=len(array)
for i in range (0,c):
    continue
     for j in range(0,c):
        if i==j:
            pass
            check=array[i]+array[j]
            if check==value:
                print("equal")
            else:
                print("not equal")
#print(d)
"""
"""

for i in range(1,c):
    e=array[0]+a[i] 
if value==sum_of_elements:#soe: sum of elements 
    print("sum of two elements of an array are equal")
else:
    print("sum of two elements are not equal")
"""

    
    
"""    
def subsequence(string):
    result = []
    l = len(string)
    if l == 0:
        result.append("")
        return(result)
    else:
        for i in subsequence(string[1:l]):
            result.append(i)
            result.append(string[0]+i)
    return(result)
a=input("")
lst = []
n = int(input(""))
for i in range (0,n):
    v=input()
    lst.append(v)
ea=[]
lent=len(lst)
ea=subsequence(a)
for j in range(0,lent):
    existsVar = lst[j] in ea
    if existsVar:
        print("POSITIVE")
    else:
        print("NEGATIVE")
"""











"""
continue
    for j in range (0,1):
        if str1[i]==str2[j]:
            print("HI")
"""









"""
n=[]
a=[12,10,3,1,5,6,7,8]
b=len(a)
por=a[b]
for i in range(1,b):
    por=a[i]
    for j in range (1,b):
        if a[i]>a[j]:
            n.insert(0,a[i])
            
print(n)
"""

"""
str1="hi i am someone"
revfn(str1)
def revfn(str1):
    str2=""
    for i in str1:
        str2=str1+i
    return str2
"""

"""
a={1,2,3,4,5}
b={1,3,6,8,9}
print(intersection_update(a,b))

"""


lis=[]
count=1
for i in range(count):
    count+=1
    lis.append(i)
    print(count)
    print(lis)