# Program Name: Assignment4.py (use the name the program is saved as)
# Course: IT3883/Section 01
# Student Name: David Dinh
# Assignment Number: Assignment 4
# Due Date: 10/26/2025
# Purpose: What does the program do (in a few sentences)? Program A sends a message to Program B to uppercase the message. Program B then sends back the message to Program A with an uppercased message.
# List Specific resources used to complete the assignment.
#https://www.geeksforgeeks.org/python/socket-programming-python/
#https://www.datacamp.com/tutorial/a-complete-guide-to-socket-programming-in-python

#PROGRAM A

#Program B needs to be ran first then Program A.

import socket

#Creates a socket
s = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

message = input("Enter a string to send: ")
print("Program A sends message to Program B...")

s.connect(("127.0.0.1", 46767))
# IP Address and Port number of both programs.

byte_array = message.encode('utf-8')
s.sendall(byte_array)
# Converts message into code and sends message to Program B.

# Waits for Program B to respond and prints response.
print("Program B returns Program A with:", s.recv(256).decode('utf-8'))

#Socket closes
s.close()
