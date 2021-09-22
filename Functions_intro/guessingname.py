import random


def get_integer(prompt):
    """
    Get an integer from Standard Input (stdin).

    The function will continue looping, and prompting
    the user until a valid `int` is entered.

    :param prompt: The string that the user will see, when
        they are prompted to enter the value
    :return: The integer the user enters.
    """
    while True:
        temp = "TEST"
        if temp.isnumeric():
            return int(temp)
        # else:
        print("{} is not a valid Number".format(temp))

# print(get_integer.__doc__)
help(get_integer)


highest = 1000
answer = random.randint(1, highest)
print(answer)  # TODO remove after testing

print("Guess a number between 1 and {} ".format(highest))

#
# if guess != answer:
#     if guess < answer:
#         print("Guess higher")
#     else:
#         print("guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("you guessed it")
#     else:
#         print("Wrong")
# else:
#     print("right on first try")

# CHALLENGE:

# if guess == answer:
#     print("Right on first try")
# else:
#     if guess < answer:
#         print("Guess higher")
#     else:
#         print("guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("you guessed it")
#     else:
#         print("Wrong")

# if guess < answer:
#     print("Guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done,you guessed it")
#     else:
#         print("sorry, you did not guess it")
# elif guess > answer:
#     print("Guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("you did not guess it")
# else :
#     print("Correct!")


gameOver = False
while not gameOver:
    guess = get_integer(": ")
    if guess == answer:
        print("Right!")
        gameOver = True
    elif guess > answer:
        print("Guess lower")
    else:
        print("Guess higher")


