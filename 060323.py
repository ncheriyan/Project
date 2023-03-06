# examGradesList = ["A", "B", "C", "D", "E", "F"]
#
# exam_grade = input("What is your grade?")
# examGradeUpper = exam_grade.upper()
#
# if examGradeUpper in examGradesList:
#     print("Grade is valid.")
# else:
#     print("Grade invalid.")

# test_techniques = ["Decision Table", "Equivalence Partitioning", "Statement Coverage", "Boundary Value Analysis",
# "State Transition Diagrams"]
#
# for x in test_techniques:
#     print(x)
#
# for i in range(len(test_techniques)):
#     print(test_techniques[i])
#
# a=0
# while a < len(test_techniques):
#     print(test_techniques[a])
#     a = a + 1
#
# [print(x) for x in test_techniques]
#
#
# car_reg = ["NH72 GYR", "BH65 TRE", "P1 TTY", "V11 GSS", "JAG1", "ACD 765T"]
# car_reg6 = []
# for x in car_reg:
#     if len(x.replace(" ","")) < 6:
#         car_reg6.append(x)
#
# print(car_reg6)
#
#
#
# countries_in_Africa = ["Angola", "Nigeria", "Ghana", "Egypt", "Niger", "Kenya"]
# countries_in_Africa.append("Chad")
# print(countries_in_Africa)
#
# countries_in_Africa.insert(0, "Liberia")
# print(countries_in_Africa)
#
# countries_in_Africa.pop(2)
# print(countries_in_Africa)
#
# countries_in_Africa.sort()
# print(countries_in_Africa)
#
# countries_in_Africa.reverse()
# print(countries_in_Africa)
#

# marbleColours = ("yellow", "green", "blue", "blue", "green", "blue")
# print(marbleColours.count("blue"))


# months = ("January", "April", "March")
# y = list(months)
# y[1] = "February"
# months = tuple(y)
#
# print(months)


# veg = {"carrot", "cabbage", "onion"}
# veg.add("cauliflower")
# print(veg)
#
# veg.remove("cabbage")
# print(veg)
#
# veg.pop()
# print(veg)


# years1 = {1977, 1982, 1966}
# years2 = {1988, 1977, 1966, 1981}
# print(years2.difference(years1))
# #Finds the data that is not in years1 but is in years2
#
# years2.difference_update(years1)
# print(years2)
# #Removes the data that is shared in both sets
#
# years1 = {1977, 1982, 1966}
# years2 = {1988, 1977, 1966, 1981}
# years2.intersection(years1)
# print(years2)
# #Returns the set of data shared in both sets
#
# years2.intersection_update(years1)
# print(years2)
# #Removes all the data that is not shared in both sets
#
# years1 = {1977, 1982, 1966}
# years2 = {1988, 1977, 1966, 1981}
# a = years2.issuperset(years1)
# print(a)
#
# years1 = {1977, 1982, 1966}
# years2 = {1988, 1977, 1966, 1981}
# print(years2.union(years1))

# phone = {
#     "model": "iphone 14",
#     "release_year": 2022,
#     "brand": "apple"
# }
# x = phone.keys()
# print(x)
#
# x = phone.values()
# print(x)
#
# x = phone.items()
# print(x)

# pub_fig ={
#     "name": "Whoopi Goldberg",
#     "profession": "Actress"
# }
# name = pub_fig["name"]
# print(name)
#
# pub_fig["profession"] = "comedian"
# print(pub_fig)
#
# pub_fig["age"] = "67"
# print(pub_fig)
#
# pub_fig.pop("profession")
# print(pub_fig)

# def areaCircle(x):
#     return math.pi * (radius * radius)
#
# radius = float(input("Input radius: "))
#
# area = areaCircle(radius)
# print(area)

# def search_movies(movie):
#     movie_list = ["Die Hard", "John Wick", "Kingsman"]
#     if movie in movie_list:
#         print(movie + " is in the list.")
#     else:
#         print(movie + " is not in the list.")
#
# title = input("Input movie title: ")
#
# search_movies(title)

def search_list(guest):
    guest_list = ["Matt", "Dan", "Amy", "James", "Laura", "Beth"]
    if guest in guest_list:
        print(guest + ", you are on the list.")
    else:
        print(guest + ", you are not on the list.")
name = input("Input name: ")
search_list(name)


