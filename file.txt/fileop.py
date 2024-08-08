f1=open("file1.txt","r")
f2=open("file2.txt","w")
for l in f1:
	l=l.replace(",",".")
	l=l.swapcase()
	f2.write(l)
