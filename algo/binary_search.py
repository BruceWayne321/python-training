
target = 31
list = [12, 18, 24, 30, 31, 89]
i = 0
j = len(list) - 1

while (i<=j):
	mid = (i+j)//2
	if list[mid] == target:
		print(f"{target} is in position {mid}")
		break
	
	elif list[mid] < target:
		i = mid+1
	elif list[mid] > target:
		j = mid-1
		
		