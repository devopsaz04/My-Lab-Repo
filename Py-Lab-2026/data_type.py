# # def greeting(name):
# #     print("Hello, " + name)


# # person1 = {"name": "John", "age": 36, "country": "Norway"}

# import json

# x = {
#     "name": "John",
#     "age": 30,
#     "married": True,
#     "divorced": False,
#     "children": ("Ann", "Billy"),
#     "pets": None,
#     "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}],
# }

# print(json.dumps(x, indent=4, sort_keys=True))

# import re

# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# print(x)

# import camelcase

# c = camelcase.CamelCase()
# txt = "hello world"
# print(c.hump(txt))

# print("Enter your name:")
# x = input()
# print("Hello, " + x)

import os
folder = input("Enter folder name: ")


files = os.listdir(folder)
print("Files in " + folder + ":")
for file in files:
    print("The file name is:",file)