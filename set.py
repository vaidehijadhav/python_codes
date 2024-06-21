# s = {2, 4, 6, 4}
# print(s)

# ray = {}   #dic
# ray = set()  #empty set
# print(type(ray))

# info = {"vaidehi", 22 , 10.3, "India"}
# # print(info)

# for value in info:
#     print(value)

# Joining of set
set1 = {1,2,3,4}
set2 = {2,4,6,8}

## union() and update()
# set3 = set1.union(set2)
# set1.update(set2)

## intersection() and intersection_update()
# set3 = set1.intersection(set2)
# set1.intersection_update(set2)

##symmetric_difference and symmetric_difference_update()
# set3 = set1.symmetric_difference(set2)
# set1.symmetric_difference_update(set2)


## difference() and difference_update()
set3 =set1.difference(set2)
set1.difference_update(set2)
print(set1)
print(set3)