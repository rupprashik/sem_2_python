r=input("enter sentece:")
c=0
for i in r:
	if i.isalpha():
		c=c+1
print("no of characters are :",c)


l=r.split(" ")
print(l)

print("no of words in sentence:",len(l))
count=0
o=input("word which you wnt to check:")
for i in l:
	if i==o:
		count=count+1
print(o,"occurse in sentence", count ,"times")
