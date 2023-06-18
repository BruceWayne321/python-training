
def multiples(n):
	list = []
	for i in range(2, n):
		if n%i==0:
			list.append(i)
			n //= i
			break
	return list

num1 = int(input("enter num1: "))
num2 = int(input)"enter num2: "))

list1 = multiples(num1)
list2 = multiples(num2)
hcf = 1

for 

