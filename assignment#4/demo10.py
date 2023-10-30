#Emma Collins
#Dictionaries demo

#Dictioaries are pythons built in mappping type
#the association, or mapping, is from a key, which can be any immutable type, to a value, which any be any python data type

# trains = {}

# trains["Thomas"] = "Blue"
# trains["Percy"] = "Green"
# trains["James"] = "Red"

# print(trains)

# movies = {}

# movies["Sci Fi"] = "Star Wars"
# movies["Comedy"] = "Lego Batman"
# movies["Thriller"] = "The Hunt for red october"
# movies["Comedy"] = "Ferris Bueller's Day Off"

# print(movies)
# print(movies["Sci Fi"])

# listDict = {}

# listDict["Panzers"] = []
# listDict["Games"] = []

# listDict["Panzers"].append("Panzer 1")
# listDict["Panzers"].append("Water tank")
# listDict["Panzers"].append("Air tank")

# listDict["Games"].append("Hollow Knight")
# listDict["Games"].append("Mario Cart")
# listDict["Games"].append("Tetris")

# print(listDict)
# print(listDict["Games"])
# print(listDict["Games"][2])


# d1 = {1: "one", 2: "two", 3: "three"}
# d2 = {3: "tree", 2: "two", 1: "one"}

# print(d1.items)

# print(1 in d1.items())
# print("one" in d1.items())
# print((1, "one") in d1.items())


# for k, v in d1.items():
    # print (d1[k]==v)

    # print(d1)
# print(d2)
# print(d1==d2)

# del d1[3]
# print(d1)


#Emma Collins        10-26-2023
#Exceptions


# try:
#     x= 12/0
# except Exception as e:
#     print("ERROR:",e)

# petsDict = {"Scratch": "Cat", "Fido": "Dog"}

# try:
#     print(petsDict["Erwin"])
# except Exception as e:
#     print("ERROR:", e)
# print("I'm HERE!")




def foo():
    try:
        foo2()
    except Exception:
        print("foo2 did not work")

def foo2():
    if True:
        raise Exception
    print("Hello from foo2")

def main():
    foo()

if __name__ == "__main__":
    main()