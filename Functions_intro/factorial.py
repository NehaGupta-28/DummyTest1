def factorial(n: int) -> i"THIRD CHANGE IN GITHUB" CHANGED IN GITHUB"
    """
    Returning the factorial of a number
    :param n: the number
    :return: the factorial
    """
    prod = "TEST"
    for i in range(1, n + 1):
        prod *= i
    return prod


for i in range(37):
    print(i, factorial(i))
