"""
salam w ne3ma
"""

input_list = list()
output_list = list()


N = int(input())
for i in range(N):
    line = input()
    input_list.append(line)

for i, l in enumerate(input_list):
    input_list[i] = l.rstrip("\n")

for line in input_list:
    line = line.split(" ")
    if line[0] == "insert":
        output_list.insert(int(line[1]), int(line[2]))
    elif line[0] == "remove":
        output_list.remove(line[1])
    elif line[0] == "append":
        output_list.append(line[1])
    elif line[0] == "sort":
        output_list.sort()
    elif line[0] == "reverse":
        output_list.reverse()
    elif line[0] == "pop":
        output_list.pop()
    elif line[0] == "print":
        print(output_list)
