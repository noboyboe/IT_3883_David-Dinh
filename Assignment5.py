# Program Name: Assignment5.py (use the name the program is saved as)
# Course: IT3883/Section 01
# Student Name: David Dinh
# Assignment Number: Assignment 5
# Due Date: 11/16/2025
# Purpose: What does the program do (in a few sentences)?
# List Specific resources used to complete the assignment.

import sqlite3

assign_obj = sqlite3.connect('Assignment5input.db')
#Connects to SQLite's database
cursor_obj = assign_obj.cursor()
#An interface that allows the user to send commands to it.


assign_obj.execute("""CREATE TABLE IF NOT EXISTS DAYS(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Day_Of_Week VARCHAR(255),
    Temperature_Value REAL
    );""")
#Creates a table with 3 columns.

sun_init = 0
counter = 0

thur_init = 0
counter2 = 0

with open('Assignment5input.txt', 'r') as f:
    #Reads and opens the txt file.
    for line in f:
        data = line.strip().split(' ')
        cursor_obj.execute("INSERT INTO DAYS (Day_Of_Week, Temperature_Value) VALUES (?, ?)", data)
        #The data from the text file for each line is split into two different items; day and temperature
        #These datas are then inserted into the database.

    cur_sun = cursor_obj.execute("SELECT * FROM DAYS WHERE Day_Of_Week = 'Sunday' ")
    res_sun = cursor_obj.fetchall()
    #The data is selectively obtaining data from Sunday.

    cur_thur = cursor_obj.execute("SELECT * FROM DAYS WHERE Day_Of_Week = 'Thursday' ")
    res_thur = cursor_obj.fetchall()
    # #The data is selectively obtaining data from Thursday.

    #Average temperature is calculated.
    for row in res_sun:
        counter += 1
        add = row[2]
        sun_init += add
        sun_avg = sun_init / counter

    for row in res_thur:
        counter += 1
        add = row[2]
        thur_init += add
        thur_avg = thur_init / counter

print(f'The average temperature on Sunday is: {sun_avg:.2f} Fahrenheit')
print(f'The average temperature on Thursday is: {thur_avg:.2f} Fahrenheit')

assign_obj.commit()
#Confirms the changes made for the database.
assign_obj.close()
#Closes the connection made to SQ Lite and cursor.


