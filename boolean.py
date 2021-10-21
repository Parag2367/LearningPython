# day = input("which day is today ? ")
# temperature = int(input("what is today's temperature? "))
# raining = True
#
# if day == "Saturday" and temperature >= 27 or not raining:
#     print("let us all go swimming")
# else:
#     print("learn something")

## Truth Value Testing
# link : https://docs.python.org/3/library/stdtypes.html
# constants defined to be false: None and False.
# zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
# empty sequences and collections: '', (), [], {}, set(), range(0)
if 0:
    print("true")
else:
    print("false")

name = input("what is your name? ")
if name:
    print("Hello , how are you {}".format(name))
else:
    print("Are you with no name? ")