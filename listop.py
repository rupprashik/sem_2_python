'''
problem:list oprations
name=Rupprashik Anand Khare
div=C
Roll num=31
class=FE
'''
l=[]
n=int(input("enter a no of element in list:"))
for i in range (n):
	e=int(input("enter a no:"))
	l.append(e)
print(l)
sum=0
for i in l:
	sum=sum+i
print("sum is ",sum)

avg=0
print("avg is ",sum//len(l))

max=l[0]
for i in l:
	if max<i:
		max=i
print("max is ",max)

min=l[0]
for i in l:
	if min<i:
		min=i
print("min is ",min)

y=0
Y=0
q=input("do you want to add no in list,yY or nN:")
if q=='y':
	e=int(input("enter a no:"))
	i=int(input("enter a index:"))
	l.insert(i,e)
print(l)
	
