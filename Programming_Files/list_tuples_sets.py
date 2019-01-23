# LISTS
# Unlike tuples, lists can be changed.
# List items are always returned in the order they were put in.

grades = [92, 83, 77, 97, 100, 102, 109]


def average():
    sum_of_grades = sum(grades)
    length_of_grades = len(grades)
    average_of_grades = (sum_of_grades / length_of_grades)
    return "\nThe average of all grades is{: 0.1f}%".format(average_of_grades)


def length():
    length_of_grades = len(grades)
    return "The number of grades in the list is {}\n".format(length_of_grades)


print(average())
print(length())
grades.append(125)
print(average())
print(length())

print("Before append has been applied to list: {}\n".format(grades))
grades.append(202)
print("After append has been applied to list: {}\n".format(grades))


# TUPLES
# Immutable - cannot change their size.

grades = (77, 83, 92, 97, 100, 102, 109)


# SETS
# Unique and Unordered.

set_grades = {77, 80, 90, 100, 100}

# Notice the missing 100... because there are two of them in the set, only one is printed.  Unique values only.
print("The contents of the set: {}\n".format(set_grades))
