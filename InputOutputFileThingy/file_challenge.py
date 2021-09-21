with open("sample.txt", 'a') as jabber:
    for i in range(1,13):
        print("{0:2} times 2 is {1:<2}".format(i, i*2), file=jabber)


with open("sample.txt", 'r') as jabber1:
    for line in jabber1:
        print(line.strip('\n'))

