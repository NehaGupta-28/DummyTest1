def func(p1, p2, *args, k, **kwargs):
    print("positional-or-keyword:...{}, {}".format(p1, p2))
    print("var-positional (*args):..{}".format(args))
    print("keyword..................{}".format(k))
    print("var-keyword:.............{}".format(kwargs))


func(1, 2, 3, 4, 5, k=6, key1=7, key2=8)


def sum_numbers(*n: float) -> float:
    """
    sum upto n
    :param n: n
    :return: sum upto n
    """
    return sum(n)


print(sum_numbers(1, 2, 3))
