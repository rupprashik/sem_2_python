f1=open("fil1.txt","r")
f2=open("fil2.txt","w")
for l in f1:
	l=l.replace(",",".")
	l=l.swapcase()
	f2.write(l)
