def fizz_buzz(n: int) -> "THIRD CHANGE IN GITHUB" CHANGED IN GITHUB"
    """
    Printing fizzbuzz
    :param n: the value n
    :return: fizz or buzz or the number
    """
    if n % 3 == 0 and n % 5 == 0:
        return "fizz buzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        return str(n)


count = 1

# for i in range(1, 101):
#     if count % 2 != 0:
#         print(i, fizz_buzz(i))
#         count += 1
#     else:
#         user_input = input("whats the solution of {} ? ".format(i))
#         solution = fizz_buzz(i)
#         if user_input != solution:
#             print("Wrong answer! Exiting....")
#             break
#         else:
#             print("Solution is {}, you got it right!".format(solution))
#             count += 1

for i in range(1, 101):
    if count % 2 != 0:
        print("Player 1: {}".format(fizz_buzz(i)))
        count += 1
    else:
        #user_input = input("Player 2 : ")
        user_input = fizz_buzz(i)
        if user_input != fizz_buzz(i):
            print("wrong!")
            break
        count += 1

else:
    print("Well done , you reached the end!")

