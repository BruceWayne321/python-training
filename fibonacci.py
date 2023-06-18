'''
num = int(input("enter a number: "))
n1 = 0
n2 = 1

if num==0: print(n1)
elif num==1: print(n2)
else:
	print(n1)
	print(n2)
	for i in range(2, num+1):
		sum = n1 + n2
		n1 = n2
		n2 = sum
		print(sum)

'''

num = int(input("enter a number: "))
n1 = 0
n2 = 1

for i in range (0,num+1):
	print(n1)
	sum = n1 + n2
	n1 = n2
	n2 = sum
