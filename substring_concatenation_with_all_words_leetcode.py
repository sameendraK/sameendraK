#substring_concatenation_with_all_words_leetcode
a="zbarfoofoobarthefoobarman"
b=["bar","foo","the"]
e=[]
#['bar', 'foo', 'foo', 'bar', 'the', 'foo', 'bar', 'man']
t=b
r=[]
#[['bar', 'foo', 'foo'], ['foo', 'foo', 'bar'], ['foo', 'bar', 'the'], ['bar', 'the', 'foo'], ['the', 'foo', #'bar'], ['foo', 'bar', 'man'], ['bar', 'man'], ['man']]
c= len(b[0])
for j in range(int(len(a)/c)):
    if j==0:
        o=j
        p=c
        print(o,p)
    elif j!=0:
        o=p
        p=p+c
        print(o,p)
    d=a[o:p]
    e.append(d)
for w in range(len(e)):
    r.append(e[w:w+c])
for m in range(len(r)):
    print("match" if sorted(b)==sorted(r[m]) else print("no match"))
print(r)    
for i in range(len(e)):
    pass
    for j in range(len(b)):
        if e[i]==b[j]:
            t.remove(b[j])
            r+=e[j]
            break
        else:
            d=b
"""a=["ssa","dfaf","efasdf"]
for i in range(len(a)):
    print(len(a[i]))
"""
