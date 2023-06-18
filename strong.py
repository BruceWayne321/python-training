num = int(input("enter a number: "))
temp = num
total = 0

while num>0:
	b = num%10
	fact = 1
	for i in range(1, b+1):
		fact = fact*i
	total = total + fact
	num = num//10

if temp == total: print(True)
else: print(False)