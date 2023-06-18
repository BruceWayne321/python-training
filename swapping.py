'''
a = input("enter a number a: ")
b = input("enter a number b: ")
'''
'''
print("a is: ", a)
print("b is: ", b)
# a, b = b, a
temp = a 
a = b
b = temp
print("a is: ", a)
print("b is: ", b)
'''

def swap(a, b):
	return b, a