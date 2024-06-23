# a = input("Enter the number: ")
# print(f"Multiplication table of {a} is: ")
# try:
#     for i in range(1, 11):
#         print(f"{int(a)} X {i} = {int(a)*i}")
# except:
#     print("Invalid Input!")

# print("above program is completed")


# Finally keyword
def fun1():
    try:
        l = [1,5,6,7]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Some error occurred")
        return 0
    
    finally:
        print("I am always executed")
    
    # print("I am always executed")

x = fun1()
print(x)