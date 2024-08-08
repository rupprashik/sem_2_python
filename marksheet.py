'''
problem:grossary calculator
name=Rupprashik Anand Khare
div=C
Roll num=31
class=FE
'''
m1=int(input("enter physics marks:"))
m2=int(input("enter maths marks:"))
m3=int(input("enter chemistry marks:"))
m4=int(input("enter pps marks:"))
m5=int(input("enter bee marks:"))
print("phy	\tmaths	\tchem	\tpps	\tbee")
print(m1,"/100" ,"\t", m2,"/100","\t", m3,"/100", "\t", m4,"/100", "\t", m5,"/100")
total=m1+m2+m3+m4+m5
p=total/5
print("parcent:",p,"%")
if m1<40 or m2<40 or m3<40 or m4<40 or m5<40:
	print("failed")
else:
	if p>=40 and p<49:
		print("pass")
	if p>=50 and p<69:
		print("avarag")
	if p>=70 and p<79:
		print("good")
	if p>=80 :
		print("Rushikesh TOPER")	
'''
enter physics marks:70
enter maths marks:78
enter chemistry marks:90
enter pps marks:76
enter bee marks:98
phy	maths	chem	pps	bee
70 	 78 	 90 	 76 	 98
percent: 82.4 %
'''
'''
enter physics marks:90
enter maths marks:75
enter chemistry marks:87 
enter pps marks:82
enter bee marks:84
phy	maths	chem	pps	bee
90 	 75 	 87 	 82 	 84
parcent: 83.6 %
Rushikesh TOPER
'''

