a = input("Enter number between 5 and 9 or quit. ")

if a.lower() == "quit":        
    print("Goodbye!")
elif int(a) < 5 or int(a)> 9:
    raise ValueError("Please enter correct value")
else:
    print("You entered", a)


    # print("Invalid input. Please enter a number between 5 and 9 or type 'quit")
