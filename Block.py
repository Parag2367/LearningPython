# block of codes
##############################
# usage of if statement
name = input("what is your name: ")
age = int(input("what is your age , {0}? ".format(name)))
print(age)

# if age >=18:
#     print("you are eligible to vote")
#     print("please put X in the box")
# else :
#     print("please come back after {} years".format(18 - age))

if age < 18:  # we used breakpoint here, we also used debugger in this code
    print("you can come back after {0}".format(18-age))
elif age == 900:
    print("Age not properly given")
else :
    print("{0} , you are eligible to vote".format(name))




