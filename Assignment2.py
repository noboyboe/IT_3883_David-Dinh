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

#Bob 100 34 25 22 76 87
#Jack 43 54 99 63 101 44
#Jane 78 98 45 74 65 23
#Pete 99 65 101 56 33 47
#Ann 78 21 22 101 44 100
#Alice 100 102 89 99 92 85
#John 45 66 99 99 89 78
#Ben 45 85 99 99 89 88
#Henry 45 12 78 98 65 32

students = []
grade_av = 0
name = " "


for x in range(9):
    grade_total = 0

    grades = input("").split()

    input_name = grades[0]
    input_grades = grades[1:]

    for i in input_grades:
        grade_total += int(i)
    grade_av = grade_total / len(input_grades)
    students.append((input_name, grade_av))

students.sort(key=lambda x: x[1], reverse=True)

for input_name, grade_av in students:
    print(f"{input_name} {grade_av:.2f}")



