# Program Name: Assignment1.py (use the name the program is saved as)
# Course: IT3883/Section 01
# Student Name: David Dinh
# Assignment Number: Assignment #2
# Due Date: 09/28/2025
# Purpose:
# List Specific resources used to complete the assignment.
#https://www.tutorialspoint.com/python/tk_entry.htm
#https://www.tutorialspoint.com/python/python_gui_programming.htm
#https://www.askpython.com/python-modules/tkinter/stringvar-with-examples
#https://www.geeksforgeeks.org/python/args-kwargs-python/
#https://www.geeksforgeeks.org/python/tracing-tkinter-variables-in-python/

import tkinter as tk

def calculate(*args):
    try:
        number = float(number_box.get())
        total = number * 0.425143707
        final.config(text=f"Result: {total} KPL")
    except:
        final.config(text="Invalid")

window = tk.Tk()
window.title("MPG to KPL Converter")
window.geometry("300x300")

number_box = tk.StringVar()
number_box.trace_add('write', calculate)

tk.Label(window, text="Miles per Gallon:").pack()
entry = tk.Entry(window, textvariable=number_box)
entry.pack()

final = tk.Label(window, text="Result: ")
final.pack()

window.mainloop()

