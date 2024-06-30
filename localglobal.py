x = 10  #global variable

def my_variable():
    y = 5
    print("the local variable y is ",y)

my_variable()
print("the global variable x is ",x)
# print("the global variable y is ",y)  #this will cause an error