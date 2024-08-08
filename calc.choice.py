
'''
problem:calculator
name=Rupprashik Anand Khare
div=C
Roll num=31
class=FE
'''


import math
c=0
while (c!=7):
	print("Enter 1 for addition")
	print("Enter 2 for substraction")
	print("Enter 3 for multiplication")
	print("Enter 4 for division")
	print("Enter 5 for exponential")
	print("Enter 6 for factorial")
	print("Enter 7 for exit")
	c=int(input("enter your choice:"))
	
	if c==1:
		num1=int(input("enter no 1:"))
		num2=int(input("enter no 2:"))
		ad=num1+num2
		print(" sum is :",ad)
	elif c==2:
		num1=int(input("enter no 1:"))
		num2=int(input("enter no 2:"))
		sub=num1-num2
		print(" sub is :",sub)
	elif c==3:
		num1=int(input("enter no 1:"))
		num2=int(input("enter no 2:"))
		ml=num1*num2
		print(" product is :",ml)
	elif c==4:
		num1=int(input("enter no 1:"))
		num2=int(input("enter no 2:"))
		div=num1/num2
		print(" div is :",div)
	elif c==5:
		num1=int(input("enter no:"))
		num2=int(input("enter power term:"))
		ex=num1**num2
		print("expone is :",ex)
	elif c==6:
		num1=int(input("enter no 1:"))
		num2=int(input("enter no 2:"))
		fact_1=math.factorial(num1)
		print("factorial is :",fact_1)
		fact_2=math.factorial(num2)
		print("factorial is :",fact_2)
		
	elif c==7:
		print("finish")
	else:
		print("invalid choice")
print("invalid choice")
'''
Enter 1 for addition
Enter 2 for substraction
Enter 3 for multiplication
Enter 4 for division
Enter 5 for exponential
Enter 6 for factorial
Enter 7 for exit
enter your choice:6
enter no 1:7
enter no 2:8
factorial is : 5040
factorial is : 40320
Enter 1 for addition
Enter 2 for substraction
Enter 3 for multiplication
Enter 4 for division
Enter 5 for exponential
Enter 6 for factorial
Enter 7 for exit
enter your choice:7
finish
'''


		
		
		
		
		
		
		
		
		
		
