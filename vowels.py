
a = input("enter a string: ")
count = 0
for i in a:
    if str(i)=='a' or str(i)=='e' or str(i)=='i' or str(i)=='o' or str(i)=='u':
        count += 1
print(count)
