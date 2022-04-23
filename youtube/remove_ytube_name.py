import re
import os
import subprocess

path = r"C:\songs"

os.chdir(path)
songs_list = subprocess.check_output("ls")
# print(songs_list)
list = []
list.append(songs_list.decode())
# print(list)
# print(list)
final_list = []
for i in list:
    # i.split("\n")
    final_list.append(i.split("\n"))

output = []
src = []
length = len(final_list[0])
for loop in range(length):
    src.append(final_list[0][loop])
    output.append(final_list[0][loop].split("y2mate.com - "))

print(src)
print(len(output))
des = []
for loop in range(len(output) - 1):
    des.append(output[loop][1])
print(des)
for i in range(len((des))):
    print(src[i], des[i])
    # os.rename(src[i], des[i])





