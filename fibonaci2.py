def fibonaci(n):
	j=int(input("enter no upto which you want fabonaci :"))
	a=0
	b=1
	while b<=j:
		c=a+b
		print(c,end=",")
		a,b=b,c


#example
print(fibonaci(5))
