# Lists (Unlike tuples, lists can be changed)
grades = [77, 83, 92, 97, 100, 102, 109]


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


# Tuples (Immutable - cannot change their size)
grades = (77, 83, 92, 97, 100, 102, 109)


# Sets (Unique and Unordered)
set_grades = {77, 80, 90, 100, 100}

# Notice the missing 100... because there are two of them in the set, only one is printed.  Unique values only.
print(set_grades)
