print()
# define function
def welcome():
	print("hey, welcome back!")

# print 1 to 10
def count():
	for i in range(1,11):
		print(i, end=" ")
	print()

# default arg
def userWelcome(username="Guest"):
	print("welcome back", username)

# positional arg
def info(fname,lname,city):
	print("firstname is:", fname)
	print("lastname is:", lname)
	print("City is:", city)

# keyword arg
def func(fname, lname):
	print("firstname is:", fname)
	print("lastname is:", lname)

# variable length args
def vary(**name):
	print("name is:", name["fname"])
vary(fname="Bruce", lname="Wayne")

welcome()
print()
count()
print()
userWelcome()
print()
firstname = "Bruce"
lastname = "Wayne"
func(lastname, firstname)
func(lname=lastname, fname=firstname)
print()
count()
print()
userWelcome(username="Bruce")
print()
info("Bruce", "Wayne", "Gotham")
print()

