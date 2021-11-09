details={"username":"sameendra","password":"samee123"}
usr=details.get("username")
psw=details.get("password")
n=input("Enter the name")
m=input("ENter the password")
if (n==usr) & (m==psw):
    print("Login succesfull")
else:
    print("unsucessful")