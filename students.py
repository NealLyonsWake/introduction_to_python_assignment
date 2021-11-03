"""
We have a dict with the results of various students:
students = { "Bob": 12, "Sue": 10, "Joe": 14, "Sally": 8, "Sarah": 18}

We'll create several function that can work on such a dict.
Remember the values are just an example - your functions should be able to work with any dict following that structure.

Define the following functions:

- best_student(students) that output the name of the student with the best result

- grade_students(students) that output a list of students, from the best result to the worse one

- success_students(students) that output a dict with only the students that have 12 or more
"""
students = { "Bob": 12, "Sue": 10, "Joe": 14, "Sally": 8, "Sarah": 18}

# best_student(students) that output the name of the student with the best result
def best_students(students):
    name = max(students, key = students.get)
    result = max(students.values())
    return f'{name} has the best result of: {result}'

print(best_students(students))


# grade_students(students) that output a list of students, from the best result to the worse one
def grade_students(students):
    return sorted(students, key = students.get, reverse=True)

print(grade_students(students))


# success_students(students) that output a dict with only the students that have 12 or more

def success_students(students):
    successDict = dict()
    for (key, value) in students.items():
        if value >= 12:
            successDict[key] = value
    return successDict

print(success_students(students))