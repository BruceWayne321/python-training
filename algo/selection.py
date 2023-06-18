list = [10, 15, 1, 5, 9, 2]

for i in range(0,len(list)-1):
	min_id = i
	for j in range(i+1, len(list)):
		if list[min_id]>list[j]:
			min_id = j
	print(min_id, list[min_id])
	list[i], list[min_id] = list[min_id], list[i]

print(list)