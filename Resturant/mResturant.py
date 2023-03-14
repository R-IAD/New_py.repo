"""
Menu module
"""
import os


"""
Admin mode
"""
########################################################################################
spaces = "    ->  "
menu_list = []


def Clear_spaces():
    global spaces
    # Clear_spaces from storage file
    with open("storage.txt", "r") as input_2:
        with open("tempSto.txt", "w") as output_2:
            # iterate all lines from file
            for line in input_2:
                # if substring contain in a line then don't write it
                if "," in line:
                    output_2.write(line)
    # replace file with original name
    os.replace("tempSto.txt", "storage.txt")
    ####################################################################
    # Clear_spaces from menu file
    with open("Menu.txt", "r") as input_:
        with open("temp.txt", "w") as output:
            # iterate all lines from file
            for line in input_:
                # if substring contain in a line then don't write it
                if spaces in line:
                    output.write(line)
                    # list to store file lines
    # replace file with original name
    os.replace("temp.txt", "Menu.txt")


def Delete_item(Deletable, file_selection, Additional_file):
    global spaces
    if file_selection == "storage" or Additional_file == "storage":
        # Delete from storage file
        with open("storage.txt", "r") as input_2:
            with open("tempSto.txt", "w") as output_2:
                # iterate all lines from file
                for line in input_2:
                    # if substring contain in a line then don't write it
                    if Deletable not in line.strip("\n"):
                        output_2.write(line)
        # replace file with original name
        os.replace("tempSto.txt", "storage.txt")

    if file_selection == "menu" or Additional_file == "menu":
        # Delete from Menu file
        with open("Menu.txt", "r") as input_:
            with open("temp.txt", "w") as output:
                # iterate all lines from file
                for line in input_:
                    # if substring contain in a line then don't write it
                    if Deletable not in line.strip("\n"):
                        output.write(line)
                        # list to store file lines
        # replace file with original name
        os.replace("temp.txt", "Menu.txt")
    Clear_spaces()


def Add_item(Addable, file_selection, Additional_file, new_quan=None):
    global menu_list
    spaces = "    ->  "
    if file_selection == "storage" or Additional_file == "storage":
        storage_dict = {"name": "", "price": "", "quantity": ""}

        # Menu = open("Menu.txt", "a")
        Storage_file = open("storage.txt", "a")

        storage_dict["name"] = Addable
        if new_quan == None:
            storage_dict["quantity"] = int(input("please enter the Number in stock: "))
        else:
            storage_dict["quantity"] = new_quan
        # storage_dict["price"] = int(input("please enter the new element price: "))
        menu_list.append(storage_dict)
        # ListOfAdd = [
        #     "\n" + storage_dict["name"] + spaces + str(storage_dict["price"]) + "  EGP"
        # ].copy()

        # Menu.writelines(ListOfAdd)
        ListOfAdd = [
            "\n" + storage_dict["name"] + "," + str(storage_dict["quantity"])
        ].copy()
        Storage_file.writelines(ListOfAdd)
        # Menu.close()
        Storage_file.close()

    if file_selection == "menu" or Additional_file == "menu":
        storage_dict = {"name": "", "price": "", "quantity": ""}
        Menu = open("Menu.txt", "a")
        storage_dict["name"] = Addable
        storage_dict["price"] = int(input("please enter the new price: "))
        menu_list.append(storage_dict)
        ListOfAdd = [
            "\n" + storage_dict["name"] + spaces + str(storage_dict["price"]) + "  EGP"
        ].copy()
        Menu.writelines(ListOfAdd)
        Menu.close()
    Clear_spaces()


def Add_Menu(op):
    global menu_list
    if op == 1:
        Addable = input("please enter the new element name: ")
        Add_item(Addable, "storage", "menu")
    elif op == 2:
        Deletable = str(input("Enter the element you want to delete: "))
        Delete_item(Deletable, "storage", "menu")

    elif op == 3:
        Changable = str(input("Enter the element you want to Change price: "))
        Delete_item(Changable, "menu", "menu")
        Add_item(Changable, "menu", "menu")

    else:
        print("Wrong Choise")


########################################################################################
"""
User mode
"""
########################################################################################

existance = True


def Show_menu():
    Menu = open("Menu.txt", "r")

    print("|" + "*" * 30 + "|\n" + Menu.read() + "\n" + "|" + "*" * 30 + "|\n")
    Menu.close


def search_for_item(item_name):
    global existance
    MEN = open("Menu.txt", "r")

    for line in MEN:
        line = line.strip("\n")
        line = line.split(spaces)

        for _ in line:
            if item_name in _:
                existance = False
            else:
                pass

    MEN.close()
    return existance


def update_storage(item_name, item_no):
    Delete_item(item_name, "storage", "storage")
    Add_item(item_name, "storage", "storage", item_no)
    ################################################################################


def search_for_stock(item_name, item_no):
    global existance

    ST = open("storage.txt", "r")
    for line in ST:
        line = line.strip("\n")
        line = line.split(",")

        for _ in line:
            if item_name in _:
                qun = int(line[1])

                if qun < item_no:
                    updated_quan = False
                else:
                    # ST.close()
                    updated_quan = qun - item_no
    ST.close()
    return updated_quan


def count_price(item_name, item_no):
    global spaces
    MEN = open("Menu.txt", "r")
    for line in MEN:
        # line = ST.readline().strip("\n")
        line = line.strip("\n")
        line = line.split(spaces)

        for _ in line:
            if item_name in _:
                price = line[1].split(" ")
                Int_price = int(price[0])
                #  int([0]) * item_no
                # print(price[0])

    MEN.close()
    return Int_price * item_no


price = int()


def Take_order():
    global existance
    global price
    order = {"item": "", "no": int()}
    ST = open("storage.txt", "r")
    MEN = open("Menu.txt", "r")

    item_name = input("please enter the item you need : ")
    # check for exsitance

    if search_for_item(item_name) == False:
        order["item"] = item_name

        item_no = int(input("please enter the quantity : "))
        if search_for_stock(item_name, item_no):
            order["no"] = item_no

            price = count_price(item_name, item_no)
        elif search_for_stock(item_name, item_no) == False:
            print("The quantity doesnt existe!")
            existance = True
        existance = True
    elif search_for_item(item_name) == True:
        print("This item doesnt existe!!")

    # print(order)

    ST.close()
    MEN.close()
    return price, search_for_stock(item_name, item_no), item_name


def customer_order():
    price, newup, item_name = Take_order()
    update_storage(item_name, newup)
    return price


def main():
    print(price)


if __name__ == "__main__":
    main()
