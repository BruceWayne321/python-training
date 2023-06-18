a = int(input("enter first number: "))
b = int(input("enter second number: "))
#print(a,b)
sum1 = 0
sum2 = 0
for i in range(1, a):
	if a%i==0:
		sum1 += i
for i in range(1, b):
	if b%i==0:
		sum2 += i
print(sum1)
print(sum2)
if sum1/a == sum2/b : print(True)
else: print(False)