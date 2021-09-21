# cities = ["Adelaide", "ALice Springs", "Darwin", "Melbourne", "Sydney"]
#
# with open("cities.txt", 'w') as city_file:
#     for city in cities:
#         print(city, file=city_file)

# reading the file I had created by the above process
# cities = []
#
# with open("cities.txt", 'r') as cities_file:
#     for city in cities_file:
#         cities.append(city.strip('\n'))
#
# print(cities)
# for city in cities:
#     print(city)

imelda = "More Mayhem", "Imelda May", "2021", (
    (1, "Pulling the rug"), (2, "Psycho"), (3,"Mayhem"), (4, "Kentish town waltz")
)

# with open("imelda3.txt", 'w') as imelda_file:
#     print(imelda, file=imelda_file)
#
# print(type(imelda_file))

with open("imelda3.txt", 'r') as imelda_file:
    contents = imelda_file.readline()

imelda = eval(contents)
print(imelda)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
print(tracks)