## Map

# numbers = [1,2,3,4,5]
# doubled = map(lambda x:x*2, numbers)
# # print(doubled)                  #<map object at 0x0000020BFAF2F5E0>
# print(list(doubled))               #[2, 4, 6, 8, 10]

## Filter

# numbers = [1,2,3,4,5]
# evens = filter(lambda x: x%2 == 0, numbers)
# print(list(evens))                 


## Reduce
from functools import reduce
numbers = [1,2,3,4,5]
sum = reduce(lambda x,y: x + y,numbers)
print (sum)