
list = [15, 10, 1, 5, 9, 2]

for i in range(0, len(list)):
	for j in range(0, len(list)-1-i):
		if list[j] > list[j+1]:
			list[j], list[j+1] = list[j+1], list[j]

print(list)