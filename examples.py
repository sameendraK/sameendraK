"""i=-40.3
print("absolute value of int is:",abs(i))
print(type(i))"""
#output:absolute value of int is: 40.3
#<class 'float'>
#ABSOLUTE VALUE EXAPMLE



"""i=range(1,10)
for k in i:
 continue
print (list((i)))
"""
#output:[1,2,3,4,5,6,7,8,9]
#ALL() in python


"""
k = [0, False]  
print(all(k))  """



"""
x=9
y=bin(x)
print(y)
"""
#bin prints the binary equivalent of the given integer
#output:0b1001



"""
string = "Hello World."  
array = bytes(string, 'utf-8')  
print(array)  
"""


"""
x=9
print(callable(x))
"""
#returns true if it is callable else returns false
#callable means any object that can be called as a function
#output:false


"""
code_str = 'x=5\ny=10\nprint("sum =",x+y)'  
code = compile(code_str, 'sum.py', 'exec')  
print(type(code))  
exec(code)  
exec(x) 
 """
 
 
"""
x = 8  
exec('print(x==8)')  
exec('print(x+4)')  
"""




"""
s=sum([2,34,5,4])
print(s)
s = sum([1, 2, 4], 10)  
print(s)  
"""
#output:45 17
#sum prints the sum of the objects


"""
l = [4, 3, 2, 0]                              
print(any(l))                                   
  
l = [0, False]  
print(any(l))  
  
l = [0, False, 4]  
print(any(l))  
  
l = []  
print(any(l))  
"""



String = 'abcde'       
print(list(String)) 