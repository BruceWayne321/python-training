a = int(input("enter a number: "))
temp = a
reverse = 0
while a>0:
    b = a%10
    reverse = reverse*10 + b
    a = int(a/10)
print(reverse)
