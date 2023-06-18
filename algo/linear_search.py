target = 1
list = [13, 19, 23, 9, 10, 1]

for i in range(0, len(list)):
	if i==len(list)-1 and list[i]!=target:
		print(f"{target} not found in array")
	elif list[i] == target: 
		print(f"position of {target} is {i+1}")
		break

