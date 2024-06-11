# lst1 = [1,3,4,5,6]
# print(lst1)

# details = ["Abhijeet", 18, "FYBScIT", 9.8]
# print(details)

# Positive Indexing
# colors = ["Red", "Green", "Blue", "Yellow", "Green"]
# #          [0]      [1]     [2]      [3]      [4]
# print(colors[2])
# print(colors[4])
# print(colors[0])

# Negative Indexing
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [-5]    [-4]    [-3]     [-2]      [-1]
# print(colors[-1])
# print(colors[-3])
# print(colors[-5])

# if "Yellow" in colors:
#     print("Yellow is present.")
# else:
#     print("Yellow is absent.")

# if "Orange" in colors:
#     print("Orange is present.")
# else:
#     print("Orange is absent.")


# Range of index:

# printing elements within a particular range:
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(animals[3:7])	#using positive indexes
# print(animals[-7:-2])	#using negative indexes'

# printing all element from a given index till the end
# print(animals[4:]) #using positive indexes
# print(animals[-4:])  #using negative indexes

# printing all elements from start to a given index
# print(animals[:6])
# print(animals[:-3])

# Printing alternate values
# print(animals[::2])
# print(animals[-8:-1:2])

# printing every 3rd consecutive value withing a given range
# print(animals[1:8:3])


# Accepts items with the small letter “o” in the new list
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)