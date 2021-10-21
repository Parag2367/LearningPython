#1:
name = input("Hi, what is your name: ")
age = int(input("What is your age: "))

if 18 <= age <= 30:
    print("Hi {} you are welcome".format(name))
else:
    print("As you are {} you are not welcome".format(age))



