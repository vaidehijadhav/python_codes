import time
timestamp = time.strftime("%H:%M:%S")
print(timestamp)

h = int(time.strftime("%H"))
n = input("Enter Your name: ")

if(4>=h and h<12):
    print("Good morning,", n.capitalize(), "its", timestamp)
elif(12>=h and h<=16):
    print("Good Afternoon,", n.capitalize(), "its", timestamp)
elif(17>=h and h<=19):
    print("Good Evening,", n.capitalize(), "its", timestamp)
else:
    print("Good night,", n.capitalize(),"its", timestamp)