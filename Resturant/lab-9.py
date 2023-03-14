# r for read
# w for write
# r+ for read and write
# rb for read binary
# rb+ for read and write binary
# file.write("this is the text")
# w+ write and read
# a for append

# _ = int()
################################################################
# file = open("file_test.txt", "r+")

# lst = ["hi i found hhim"]
# for _ in file:
#     i = file.readline()
#     txt = i.split()
#     for x, it in enumerate(txt):
#         if "Riad" in it:
#             file.writelines(lst)

#     # lst.append("0" * 30)
# # newlines = []

# file.close()


################################################################


# import os

# with open("file_test.txt", "r") as input:
#     with open("temp.txt", "w") as output:
#         # iterate all lines from file
#         for line in input:
#             # if substring contain in a line then don't write it
#             if "Riad" not in line.strip("\n"):
#                 output.write(line)

# # replace file with original name
# os.replace("temp.txt", "file_test.txt")


####################################################################


# for _ in range(10):
#     newlines.append(f"{_}-: my name is Riad\n")


# file.writelines(newlines)
# print(file.read())

# i = "hi , my nam is Riads"

# # if "Riad" in i:
# print(i.split())


# txt = "hi my nam is Riads"

# txt = txt.split()

# print(txt)

##


# def Add_Menu(op):
#     # global menu_list
#     storage_dict = {"name": "", "price": "", "quantity": ""}

#     if op == 1:
#         # Menu = open("Menu.txt", "a")
#         # Storage_file = open("storage.txt", "a")
#         # spaces = "    ->  "
#         item = input("please enter the new element name: ")
#         storage_dict["name"] = item
#         storage_dict["quantity"] = int(input("please enter the Number in stock: "))
#         storage_dict["price"] = int(input("please enter the new element price: "))
#         # menu_list.append(storage_dict)
#         # ListOfAdd = [storage_dict["name"] + spaces + storage_dict["price"]].copy()
#         # Menu.writelines(ListOfAdd)

#         # ListOfAdd = [storage_dict["name"] + "," + storage_dict["quantity"]].copy()
#         # Storage_file.write(ListOfAdd)

#         # Menu.close()
#         # Storage_file.close()


# def main():
#     App_Mode = ""
#     App_Mode = str(input("Please select the mode (Admin)/(User) : "))
#     if App_Mode == "Admin":
#         print(
#             "|To add an element press 1\n|To delete an element press 2\n|To chnage the price press 3"
#         )

#         Add_Menu(int(input("Enter your Choice: ")))

#     elif App_Mode == "User":
#         Menu = open("Menu.txt", "r")
#         print(Menu.read())


# if __name__ == "__main__":
#     main()
####################################################################
# # list to store file lines
# lines = []
# # read file
# with open(r"file_test.txt", "r") as fp:
#     # read an store all lines into list
#     lines = fp.readlines()

# # Write file
# with open(r"file_test.txt", "w") as fp:
#     # iterate each line
#     for number, line in enumerate(lines):
#         # delete line 5 and 8. or pass any Nth line you want to remove
#         # note list index starts from 0
#         if number not in [4, 7]:
#             fp.write(line)


####################################################################################
"""
el searching el tmaaaaaam
"""
# ST = open("file_test.txt", "r")
# for line in ST:
#     # line = ST.readline().strip("\n")
#     line = line.strip("\n")
#     line = line.split(",")

#     for _ in line:
#         if "gg" in _:
#             print(line[1])


####################################################################################


def func(go, jj=None):
    gg = go
    if jj == None:
        print("hala")


def main():
    func(5, 4)


if __name__ == "__main__":
    main()
