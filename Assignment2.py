# Program Name: Assignment1.py (use the name the program is saved as)
# Course: IT3883/Section 01
# Student Name: David Dinh
# Assignment Number: Assignment #2
# Due Date: 09/19/2025
# Purpose:
# List Specific resources used to complete the assignment.
#https://www.w3schools.com/python/python_dictionaries.asp
#https://www.w3schools.com/python/ref_dictionary_keys.asp
#https://www.w3schools.com/python/ref_string_split.asp
#https://www.geeksforgeeks.org/python/python-program-to-sort-the-list-according-to-the-column-using-lambda/

students = []
grade_av = 0
name = " "
#This stores the values of a student and their grade. Once that student's value has been printed, that value will be replaced by the next student.

with open("Assignment2input.txt", 'r') as grades:
    for x in grades:
        grade_total = 0
        separate = x.split()
#Values are separated into multiple different lists.
        input_name = separate[0]
        input_grades = separate[1:]
# This allows the function below what information to use. ['Bob', '100', '34', '25', '22', '76', '87'] 'input_name' only takes the name, and input_grades only gathers numbers.
        for i in input_grades:
            grade_total += int(i)
        grade_av = grade_total / len(input_grades)
        students.append((input_name, grade_av))
#This function calculates the grade average for each student.
#The average grade is appended to the list 'students' from the beginning of the code.

students.sort(key=lambda x: x[1], reverse=True)
# "[('Bob', 57.333333333333336)..." This numerically sorts each grade in descending order. "reverse=True" allows the grades to be displayed in descending order.
# x[1] only looks at the grades from each student to sort.

for input_name, grade_av in students:
    print(f"{input_name} {grade_av:.2f}")




