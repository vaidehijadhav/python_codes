# f = open("FileHandling/myfile.txt", 'r')
# f = open("FileHandling/myfile2.txt", 'w')
# print(f)
# text = f.write("Hey, Python is awesome programming langauage")
# print(text)
# f.close()

with open("FileHandling/myfile.txt", 'a') as f:
    f.write("Let's get started!!")

