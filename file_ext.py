import glob
import os
import pickle

dir_path = "E:\dirc"
# # file_name, file_extension = os.path.splitext("Users/USER/Desktop/abc.txt")
# if os.path.isfile(file_name):
#          print(file_name)
#          print(file_extension)
# else:
#         print("file not found")
if os.path.isdir(dir_path):
    print("dir present")
    os.chdir(dir_path)
    path = os.getcwd()
    print(path)
    for file_name in glob.glob("*.txt"):
        print(file_name)
    for file_name in glob.glob("*.py"):
        print(file_name)
    for file_name in glob.glob("*.doc"):
        print(file_name)

else:
    print("file is not present")

with open("abc.txt", "r") as f:
    print(len(f.readline()))

f = open("abc.txt", "w")
f.write("Hello word, \n HI this is next line \n this is 3rd line")
f.close()

# f = open("abc.txt", "r")

# # print(f.read())
# for line in f:
#     print(line)
#     count = count + 1
#     print(count)

# f = open("abc.txt", "w")
# count = 1
# l1 = ["hi", "hello", "well", "come", "new"]
# for ln in l1:
#     f.write(str(count) + " : " + ln + "\n")
#     count = count + 1
# f.close()


# f = open("abc.txt", "r")
# result = []
# for ln in f:
#    print(ln)
#    part = ln.partition(":")
#    print(part[2])
#    result.append(part[2].strip())
#    print(result)

f = open("abc.txt", "w")
l1 = ["hi", "hello", "well", "come", "new"]
l1.sort()
for ln in l1:
    f.write(ln + " " + "\n")
f.close()
















