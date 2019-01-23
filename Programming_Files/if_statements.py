# IF statements
# should_continue = True

# if should_continue:
#     print("Hello")

known_products = ["Gloves", "Sleeves", "Boots", "Respirators"]
product = input("Enter the type of product: ")

if product in known_products:
    print("{} are available!".format(product))
else:
    print("Sorry, {} are currently unavailable.".format(product))


# FLOW CONTROL examples...

# Example 1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Modify the method below to make sure only even numbers are returned. Use the Modulo operator (%), which only returns the remainder rather than the quotient after division.


def even_numbers():
    evens = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    print(evens)


even_numbers()


# Example 2
def user_menu(choice):
    if choice == "a":
        # return "Add"
        print("Your selection will be Added")
    elif choice == "q":
        # return "Quit"
        print("You have chosen to Quit the program")


choice = input("Would you like to Add (a) or Quit (q)? ")
user_menu(choice)
