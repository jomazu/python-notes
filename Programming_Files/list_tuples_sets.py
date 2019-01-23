# LISTS
# Unlike tuples, lists can be changed.
# List items are always returned in the order they were created in (i.e. not in ascending order).

list_grades = [92, 83, 77, 97, 100, 102, 109]


def average():
    sum_of_grades = sum(list_grades)
    length_of_grades = len(list_grades)
    average_of_grades = (sum_of_grades / length_of_grades)
    return "The average of all grades is{: 0.1f}%".format(average_of_grades)


def length():
    length_of_grades = len(list_grades)
    return "The number of grades in the list is {}\n".format(length_of_grades)


print("****** LISTS ******")
print(average())
print(length())
list_grades.append(125)
print(average())
print(length())

print("\nThe current LIST: {}\n".format(list_grades))
list_grades.append(202)
print("The current LIST after APPENDING 202 to it: {}\n".format(list_grades))

print("The first element in the LIST is: {}\n".format(list_grades[0]))
print("Assign 60 to the first element in the LIST: list_grades[0] = 60\n")
list_grades[0] = 60
print("The current LIST after changing the first element: {}\n".format(list_grades))

# TUPLES
# Immutable - cannot change their size.
# Also, you cannot add items to (append) a current tuple.
# However, you can create a new tuple altogether with a new item

tuple_grades = (77, 83, 92, 97, 100, 102, 109)

print("****** TUPLES ******")
print("The current TUPLE: {}\n".format(tuple_grades))
tuple_grades = tuple_grades + (555, 213)
print("The current TUPLE with another containing 555 and 213 added to it: {}\n".format(tuple_grades))
print("Note, if adding a tuple with only one value, it MUST look like such with an ending comma: (9,) etc.\n")

# SETS
# Unique (no duplicates) and Unordered.

set_grades = {77, 80, 90, 100, 100}

print("****** SETS ******")
# Notice the missing 100... because there are two of them in the set, only one is printed.  Unique values only.
print("The contents of the set: {}\n".format(set_grades))

print("Add 312 to the unordered SET: set_grades.add(312)\n")
set_grades.add(312)
print("The current LIST after adding 312 to it: {}\n".format(set_grades))
print("If we try to add 312 again, it will still only show one 312.  Because SETS can only contain unique values (no duplicates).\n")

# Advanced SET operations

print("****** SET OPERATIONS ******")
your_lottery_numbers = {1, 2, 3, 4, 5}
winning_numbers = {1, 3, 5, 7, 9, 11}

# Check to see which numbers match
print("These are your lottery numbers: {}\n".format(your_lottery_numbers))
print("These are the winning lottery numbers: {}\n".format(winning_numbers))
number_matches = your_lottery_numbers.intersection(winning_numbers)
print("---------------------------")
print("INTERSECTION method")
print("---------------------------\n")
print("This will produce the matching numbers between both SETS: your_lottery_numbers.intersection(winning_numbers)")
print("The matching numbers between both SETS are: {}\n".format(number_matches))

print("---------------------------")
print("UNION method")
print("---------------------------\n")
united_set = your_lottery_numbers.union(winning_numbers)
print("This will produce a combined SET with no duplicates: your_lottery_numbers.union(winning_numbers)")
print("UNITING your lottery numbers and the winning numbers produce the following SET with no duplicates: {}\n".format(united_set))

print("---------------------------")
print("DIFFERENCE method")
print("---------------------------\n")
difference_set = your_lottery_numbers.difference(winning_numbers)
print("This will produce a SET with non-duplicate elements: your_lottery_numbers.difference(winning_numbers)")
print("The DIFFERENCE between both SETS are: {}\n".format(difference_set))
