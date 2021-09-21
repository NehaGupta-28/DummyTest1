import shelve

# with shelve.open('ShelfTest') as fruit:
#     fruit['orange'] = "a sweet, orange, citrus fruit"
#     fruit['apple'] = "good for making cider"
#     fruit['lemon'] = "a sour, yellow citrus fruit"
#     fruit['grape'] = "a small, sweet fruit growing in bunches"
#     fruit['lime'] = "a sour, green citrus fruit"
#
#     print(fruit["lemon"])
#     print(fruit["grape"])

# NOTE : with automatically closes the file for us if you wanna do that manually then see the following:

fruit = shelve.open('ShelfTest')
fruit['orange'] = "a sweet, orange, citrus fruit"
fruit['apple'] = "good for making cider"
fruit['lemon'] = "a sour, yellow citrus fruit"
fruit['grape'] = "a small, sweet fruit growing in bunches"
fruit['lime'] = "a sour, green citrus fruit"

# print(fruit["lemon"])
# print(fruit["grape"])
for key in fruit:
    print(key, fruit[key])

while True:
    shelf_key = input("Please enter a fruit: ")
    if shelf_key == "quit":
        break
    description = fruit.get(shelf_key, "We don't have " +shelf_key)
    print(description)
fruit.close()

print(fruit)
