print("adelaide".strip("ade"))
a = "Adelaide"
a.strip("A")
print(a)


# not part of course:
def check_amount(amt: int) -> bool:
    return amt >= 10


print(check_amount(810))