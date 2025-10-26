# Program Name: Assignment4.py (use the name the program is saved as)
# Course: IT3883/Section 01
# Student Name: David Dinh
# Assignment Number: Assignment 4
# Due Date: 10/26/2025
# Purpose: What does the program do (in  few sentences)? Program A sends a message to Program B to uppercase the message. Program B then sends back the message to Program A with an uppercased message.
# List Specific resources used to complete the assignment.
#https://www.geeksforgeeks.org/python/socket-programming-python/
#https://www.datacamp.com/tutorial/a-complete-guide-to-socket-programming-in-python

#PROGRAM B

#Program B needs to be ran first then Program A.

import socket

#Creates a socket
s = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

# Binds IP address and port to socket.
s.bind(("127.0.0.1", 46767))
s.listen()

# Accepts connection from Program A.
conn, addr = s.accept()
data = conn.recv(256)

if data:
    message = data.decode('utf-8')
# Decodes message

#Makes message uppercase and encodes again to respond.
    response = message.upper().encode('utf-8')
    conn.sendall(response)

#Connection and socket closes.
conn.close()
s.close()