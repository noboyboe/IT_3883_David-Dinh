# Program Name: Assignment1.py (use the name the program is saved as)
# Course: IT3883/Section 01
# Student Name: David Dinh
# Assignment Number: Assignment #1
# Due Date: 09/5/2025
# Purpose: This program gives you 4 choices. You can input a string to save, display that string, clear it so it is empty, and end the program. You can use the program continuously until you are done.
# List Specific resources used to complete the assignment.

print("\n1) Append data into input buffer. \n2) Clear input buffer. \n3) Display input buffer. \n4) Exit program. ")

while True: #The program will remain true which allows the program to loop continuously until the user wishes to finish.
    question = int(input("\nPlease select an option(1-4): "))
    #The program asks the user for an integer which will trigger one of the 4 choices below.

    if question == 1:
        append = input("Type anything into the input buffer: ")
        print("Received.")
    elif question == 2:
        append = ''
        print("Input buffer has been cleared.")
    elif question == 3:
        print(f"Here is your input: '{append}'")
    elif question == 4:
        print("Goodbye!")
        break
        #Break stops the while true statement to completely stop the program.
    else:
        print("Invalid.")
        #If the user inputs anything other than 1-4, it will come up as invalid.




