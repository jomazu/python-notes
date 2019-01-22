# Integers
student_count = 500

# Float
rating = 4.99

# Boolean
qty_is_entered = True

# String
product_type = "Glove"

print("*" * 20)
print("There are " + str(student_count) + " students in the class.")

qty = 503 * 4.99
print(round(qty, 2))

## Variables and Methods

style = ["T193", "Y10CFC", "GPD590"]


def product_details(style):
    print("Style: " + style)


product_details(style[0])
product_details(style[1])
product_details(style[2])


# Multiply Method

def my_print_method(my_argument):
    print(my_argument)


def my_multiply_method(num1, num2):
    return num1 * num2


def markup_method(cost, percent):
    markup = cost / percent
    return "\nThe price is ${:0.2f}\n".format(markup)


# result = my_multiply_method(5, 3)
# my_print_method(result)
my_print_method(my_multiply_method(5, 3))


# markup = markup_method(2.13, 0.10)
my_print_method(markup_method(9.97, 0.12))
