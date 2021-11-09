#hacekrrank3
import re
a=input()
b=input()
m=re.findall(b,a)
for i in range(len(m)):
    print(m.start())
#print(m.start())

