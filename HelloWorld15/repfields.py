age = 24
print("My age is",age,"years")
#or
print("My age is "+str(age)+" years")
#or
print("My age is {0} years".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, and {7}"
      .format(31,"Jan","march","may","jul","Aug","oct","Dec"))

print("Jan:{2}, Feb:{0}, March:{2}, April:{1}".format(28,30,31))
print()
print("""Jan:{2}
Feb:{0}
March:{2}
April:{1}""".format(28,30,31))
