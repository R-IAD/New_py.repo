# Resturant menu
#       -> Fries , Burger , Chicken  (price) (stock)
#       -> oreder : (Total price)
#       -> receipt

import mResturant


def main():
    App_Mode = str(input("Please select the mode (Admin)/(User) : "))
    if App_Mode == "Admin":
        print(
            "|To add an element press 1\n|To delete an element press 2\n|To chnage the price press 3"
        )
        while True:
            mResturant.Add_Menu(int(input("Enter your Choice: ")))

    elif App_Mode == "User":
        mResturant.Show_menu()
        price = mResturant.customer_order()

        con = input("To oreder other thing press '+' if you Done press '0' : ")
        while con != "0" and con == "+":
            price += mResturant.customer_order()
            con = input("To oreder other thing press '+' if you Done press '0' : ")
        print(f"Total price is {price} EGP")


if __name__ == "__main__":
    main()
