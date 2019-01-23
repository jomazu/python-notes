# LOOPS
my_variable = "Hello"
print("Python interprets the String in the following variable as a sequence of characters: my_variable = \"Hello\"\n")

print(
    "Like with a LIST, you can print the specific characters in a String.\nFor instance, first_letter = my_variable[0]\n")

first_letter = my_variable[0]
print("The first_letter variable will return the letter \"{}\" from the my_variable String.\n".format(first_letter))

# Iterate - go over each of the characters in the String
print("-----------------\nFOR loop\n-----------------")

# The word "character" if the following FOR loop is basically a new variable.
# The variable "my_variable" is called an ITERABLE in the context of the following FOR loop.
for character in my_variable:
    print(character)

# Iterables are Strings, Lists, Sets, Tuples, and more...
my_list = [1, 3, 5, 7, 9]

for number in my_list:
    print(number)

# Do the same as above, but multiply by the power of 2

for number in my_list:
    print(number ** 2)

# A loop that we can run WHILE something is True.

# The == sign is used for comparison

user_wants_number = True

while user_wants_number == True:
    print(3)

    user_input = input("Should we print again? (y/n) ")
    if user_input == 'n':
        user_wants_number = False
