# f = open("FileHandling/myfile.txt", 'r')
# f = open("FileHandling/myfile2.txt", 'w')
# print(f)
# text = f.write("Hey, Python is awesome programming langauage")
# print(text)
# f.close()

# with open("FileHandling/myfile.txt", 'a') as f:
#     f.write("Let's get started!!")


# f = open("FileHandling/myfile.txt", 'r')
# i = 0
# while True:
#     i = i + 1
#     line = f.readline()
#     if not line:
#         break

#     m1 = int(line.split(",")[0])
#     m2 = int(line.split(",")[1])
#     m3 = int(line.split(",")[2])

#     print(f"Marks of studnet {i} in Maths is: {m1}")
#     print(f"Marks of studnet {i} in Maths is: {m2}")
#     print(f"Marks of studnet {i} in Maths is: {m3}")
# print(line)


f = open('FileHandling/myfile2.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()