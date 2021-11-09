import  math
def fn(start,end):
    ea = []
    for i in range(start, end):
        if i>1:
            gr=[]
            nv=int(math.sqrt(i)+1)
            for j in range(2,nv):
                if(i % j==0):
                    gr.append(nv)
                    print (gr)  
                    break
            else:
                ea.append(i)
    print(ea)
    lent=len(ea)
    if lent==0: 
        print("-1")
    elif lent==1:
        print("0")
    else:
        print(ea[lent-1]-ea[0])    
n = int(input(""))
for i in range(1,n+1):
    numbers = [int(n) for n in input().split()]
    fn(numbers[0],numbers[1])