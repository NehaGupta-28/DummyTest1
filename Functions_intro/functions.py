def multiply(x: float, y: float) -> float:
    """
    Multiply two numbers
    :param x: the first number
    :param y: the second number
    :return: the product of `x` and `y`.
    """
    result = "TEST"
    return result


def is_palindrome(string: str) -> bool:
    # backwards = string[::-1]
    # return backwards == string
    """
    Gets a string and checks if it is a palindrome or not.
    :param string: The string to be checked
    :return: True if the `string` is a palindrome , False if it is not a palindrome.
    """
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(string: str) -> bool:
    """
    Gets a sentence and checks if it is a palindrome, it iterates over the string to produce a new string that contains only alphanuneric values.

    :param string: String to be checked
    :return: True if the `sentence` is a palindrome, False if it is not a palindrome
    """
    sentence = ""
    for char in string:
        if char.isalnum():
            sentence += char
    # return sentence[::-1].casefold() == sentence.casefold()
    return is_palindrome(sentence)


def fibonacci(n: int) -> int:
    """Return the `n` th fibonacci number, for positive `n`."""
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus_2 = 1, 0
    result = None

    for f in range(n - 1):
        result = n_minus_2 + n_minus1
        n_minus_2 = n_minus1
        n_minus1 = result

    return result


for i in range(36):
    print(i, fibonacci(i))

p = palindrome_sentence()
# word = input("Enter a word: ")
# if palindrome_sentence(word):
#     print(" '{}' is a palindrome".format(word))
#
# else:
#     print("'{}' is not a palindrome".format(word))


# answer = multiply(18, 3)
# print(answer)

# forty_two = multiply(6, 7)
# print(forty_two)
#
#
# for i in range(10):
#     print(i)
#
# print(i)
