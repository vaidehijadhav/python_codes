# a = int(input("Enter your age: "))
# print("Your age is:",a)

# If else condition
# if(a>18):
#     print("You can drive")
# else:
#     print("You cannot drive")


# if elif else 
# num = int(input("Enter the value of num: "))
# if(num < 0):
#     print("Number is negative.")
# elif(num == 0):
#     print("Number is zero.")
# elif(num == 999):
#     print("Number is special.")
# else:
#     print("Number is positive.")

# print("I am happy now.")

# nested if statements
num = 18
if(num < 0):
    print("Number is negative.")
elif(num>0):
    if(num <= 10):
        print("Number is between 1-10")
    elif(num > 10 and num <=20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero.")
