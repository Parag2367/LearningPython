# replacement fields we can use str function to convert any data type
age = 24
print("my age is " +str(age) + " years")

# same as above this changes whatever is in {} known as replacement fields and it replaces value in .format
print(" My age is {0} years".format(age))
print("There are {0} days in {1}, {2},{3},{4},{5},{6},{7} "
      .format(31,"Jan","Mar", "May", "Jul", "Aug","Oct", "Dec"))

print("Jan : {1}{3}Feb : {0}{3}Mar : {2}{3}".format(28,30,31,"\n"))

# string Formatting

for i in range(1,13):
      print("{0} squared is {1}, cubed is {2}".format(i,i**2,i**3))

#formatting
for i in range(1,13):
      print("{0:2} squared is {1:4}, cubed is {2:4}".format(i,i**2,i**3))

# formatting left align, centre align
for i in range(1,13):
      print("{0:2} squared is {1:<3}, cubed is {2:<4}".format(i,i**2,i**3))

for i in range(1,13):
      print("{0:2} squared is {1:^3}, cubed is {2:^4}".format(i,i**2,i**3))

# formatting for floats using precision etc
print()
print(" pi is equal to {0:12}".format(22/7))
print(" pi is equal to {0:12f}".format(22/7))
print(" pi is equal to {0:12.50f}".format(22/7))
print(" pi is equal to {0:52.50f}".format(22/7))
print(" pi is equal to {0:62.50f}".format(22/7))
print(" pi is equal to {0:<72.50f}".format(22/7))

for i in range(1,13):
      print("{} squared is {}, cubed is {:4}".format(i,i**2,i**3))

#f-strings
age = 12
print(f"my age is {age}")

print(f"pi is {(22/7):12.50f}")


name = input("what is your name")
age = input("what is your age, {0}".format(name))
print(age)


