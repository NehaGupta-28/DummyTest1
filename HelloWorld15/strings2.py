#parrot = "Norwegian Blue"
# print(parrot)
# print(parrot[3])
# print(parrot[4])
# print(parrot[9])
# print(parrot[3])
# print(parrot[6])
# print(parrot[8])
#
# print()
#
# print(parrot[-11])
# print(parrot[-1])
# print(parrot[-5])
# print(parrot[-11])
# print(parrot[-8])
# print(parrot[-14])

# print(parrot[0:6])
# print(parrot[3:5])
# print(parrot[10:])

# print(parrot[-4:-2]) #Bl
# print(parrot[-4:12])#Bl

# print(parrot[0:6:2])#Nre

number = input("enter number using any amount of separators: ")
separators = ""

for char in number:
    if not char.isnumeric():
        separators += char

# print(separators)


values = "".join(char if char not in separators else " "for char in number).split()
print(sum([int(val) for val in values]))