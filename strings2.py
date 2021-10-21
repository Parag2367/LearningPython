# indexing
parrot = "Norwegian Blue"

print(parrot)

print(parrot[3])
print(parrot[4])
print(parrot[3])
print(parrot[6])
print(parrot[0])

print(parrot[-11])
print(parrot[-10])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

# slicing use square brackets : this is always there for slicing
print(parrot[0:6])   # upto last int but not including
print(parrot[3:5])
print(parrot[10:])
print(parrot[:8])
print(parrot[10:16])

print(parrot[-4:-2])

#steps in slicing
print(parrot[0:6:2])   # start : end : steps
print(parrot[::2])




number = "9,253,345,654,765,89"
separators = number[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])


# backward slice note(for this start value should be greater than end value
letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[::-1]
print(backwards)

task = letters[-10:-13:-1]
print(task)

task2 = letters[4::-1]
print(task2)

task3 = print(letters[:-9:-1])

# idioms
print(letters[::-1])
print(letters[-4:])
print(letters[-1:])
print(letters[:1]) # print(letters[0])