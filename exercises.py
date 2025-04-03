# Exercise 1: List and Indexing
#
# Create a list named students containing at least three student names (strings).
# Assign the second student’s name to a variable named first_student.
# Assign the last student’s name to a variable named last_student.

def manage_students():
    students = ['student zero', 'student one', 'student two']
    student_one_index = students.index('student one')
    last_student_index = students.index('student two')
    first_student = students[student_one_index]
    last_student = students[last_student_index]
    return first_student, last_student


# Call the function and print the result
print('Exercise 1:', manage_students())



# Exercise 2: Loop and String Concatenation
#
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Create a variable named meal and assign an empty string to it.
# Use a for loop to iterate over the strings in foods and append each string to meal.

def combine_foods():
    foods = ('cake', 'grapes', 'pizza')
    meal = ''

    for food in foods:
        meal += food + ' '
    return meal 

# Call the function and print the result
print('Exercise 2:', combine_foods())

