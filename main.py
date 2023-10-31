#Nafiaz Chowdhury
def encode(password):
    encoded = ""
    for digit in password:
        encoded_digit = (int(digit) + 3) % 10
        encoded += str(encoded_digit)
    return encoded
#I just used a simple for loop to go through each digit and encode it
def print_menu():
    return (f"Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
print(print_menu())
#This just prints the menu
value = True
ec = 0
encoded = 0
menu_option = int(input("Please enter an option: "))
#This stores some values and asks for a menu option
while value == True:
    if menu_option == 1:
        ec = input("Please enter your password to encode: ")
        if len(str(ec)) >= 8:
            print("Your password has been encoded and stored!")
            encoded = encode(str(ec))
            print(f'\n{print_menu()}')
            menu_option = int(input("Please enter an option: "))
        else:
            print("It has to be 8 Digits. ")
    elif menu_option == 2:
        print(f"The encoded password is {encoded}, and the original password is {ec}")
        print(f'\n{print_menu()}')
        menu_option = int(input("Please enter an option: "))
    elif menu_option == 3:
        value = False
#This uses a while loop to go through the first 3 options
    elif menu_option <=0 or menu_option >3:
        print(f"\nInvalid Menu Option\n{print_menu()}")
        menu_option = int(input("Please enter an option: "))
#This is in case they pick a wrong number.,