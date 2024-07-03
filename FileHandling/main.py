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


# f = open('FileHandling/myfile2.txt', 'w')
# lines = ['line 1\n', 'line 2\n', 'line 3\n']
# f.writelines(lines)
# f.close()

# with open('FileHandling/file.txt','r') as f:
#     # Move to the 10th byte in file
#     f.seek(10)

#     #Read the next 5 bytes
#     data = f.read(5)

#     print(data)

# with open('FileHandling/file.txt', 'r') as f:
#   # Read the first 10 bytes
#   data = f.read(10)

#   # Save the current position
#   current_position = f.tell()

#   # Seek to the saved position
#   f.seek(current_position)

#   print(current_position)

with open('FileHandling/sample.txt', 'w') as f:
  f.write('Hello World!')
  f.truncate(5)

with open('FileHandling/sample.txt', 'r') as f:
  print(f.read())