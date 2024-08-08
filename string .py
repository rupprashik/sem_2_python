ch=int(input("enetr your choice \n 1.calculating length of srting \n 2.string revarsal \n 3.equality check of two string \n 4.pelendrom 5.substring check \n enter choice:")
 
if ch>0 and ch<6 :
	if ch==1:
		str=input("enter srting:)
		print("length of string is:",len(str))	
	elif ch==2:
		str=input("enter srting:)
		print("revarse string is:",str[::-1])	
	elif ch==3:
		str=input("enter srting:)
		str1=input("enter srting:)
		if str==str1:
			print("string is equal")
		else:
			print("string is not equal")	
	elif ch==4:
		str=input("enter srting:)
		if str==str[::-1]:
			print("string is pelendrom")
		else:
			print("string is not pelendrom")
	elif ch==5:
		str=input("enter srting:)
		str1=input("enter srting:)
		if str1 in str:
			print("string is substring ")
		else:
			print("string is not substring")
else:
	print("envalid choice")
	
		
													
