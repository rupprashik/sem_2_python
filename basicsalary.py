'''
problem:basic salary calculator
name:Rupprashik Anand Khare
class:FE CMPUTER branch 
div :C  C2
roll no : 31
'''
basic=int(input("enter basic salary:"))
hra=(0.10)*basic
ta=(0.05)*basic
total=hra+ta+basic
ptax=(0.02)*total
print("hra is :",hra)
print("ta is :",ta)
print("tatal is :",total)
print("tax is :",ptax)
netsalary=total-ptax
print("net salary is :",netsalary,"(after ruducing tax)")
'''
enter basic salary:10000
hra is : 1000.0
ta is : 500.0
tatal is : 11500.0
net salary is : 11270.0
'''
