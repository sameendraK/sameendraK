#python_program_to_check_prime_number
s=int(input("Enter a number"))
for i in range(2,s-1):
	c=s%i
if c!=0:
        print(" prime")
else:
	print("not prime")