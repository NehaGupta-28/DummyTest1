for i in range(1,13):
    print("No. {0} squared is {1} and cubed is {2}".format(i, i**2, i**3))

print("===========================\n===========================")

for i in range(1,13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i**2, i**3))


print("===========================\n===========================")

for i in range(1,13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:4}".format(i, i**2, i**3))

print("===========================\n===========================")

for i in range(1,13):
    print("No. {0:2} squared is {1:^3} and cubed is {2:4}".format(i, i**2, i**3))


print("Pi is approx {0:12}".format(22/7))
print("pi is approx {0:12f}".format(22/7))
print("pi is aprox {0:12.50f}".format(22/7))
print("pi is approx {0:70.50f}".format(22/7))
print("pi is approx {0:.50f}".format(22/7))

for i in range(1,13):
    print("No. {} squared is {} and square is {}".format(i, i**2, i**2))
