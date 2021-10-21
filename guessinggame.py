answer = 5

print("please guess a number between 1 and 10")
guess = int(input())


if guess == answer:
    print("you got it right in the first time")
else:
    if guess < answer:
        print("guess higher")
    else:
        print("guess lower")
    guess = int(input("guess again : "))
    if guess == answer:
        print("you got it right this time")
    else:
        print("sorry please try after 15 minutes")

# if guess != answer:
#     if guess > answer:
#         print("please guess lower")
#     else:
#         print("please guess higher")
#     guess = int(input("guess again: "))
#     if guess == answer:
#         print("you guessed it")
#     else:
#         print("sorry your guess is wrong")
# else:
#     print("you got it in first time")
# if guess < answer:
#     print("please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("you got it correct this time")
#     else:
#         print("sorry, guess is wrong")
# elif guess > answer:
#     print("please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("you got it correct this time")
#     else:
#         print("sorry.guess is wrong")
# else:
#     print("you guessed it right")



