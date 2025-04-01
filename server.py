'''
Andrew Amidei
ID: 010923073
'''

import sys

# Import socket library
from socket import *

# Set port number by converting argument string to integer
# If no arguments set a default port number
# Defaults
if sys.argv.__len__() != 2:
    serverPort = 10273
# Get port number from command line
else:
    serverPort = int(sys.argv[1])

# Choose SOCK_STREAM, which is TCP
# This is a welcome socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# The SO_REUSEADDR flag tells the kernel to reuse a local socket
# in TIME_WAIT state, without waiting for its natural timeout to expire.
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# Start listening on specified port
serverSocket.bind(('', serverPort))

# Listener begins listening
serverSocket.listen(1)

print("The server is ready to receive")

bankBalance = 100

while 1:
    loggedIn = True

    # Wait for connection and create a new socket
    # It blocks here waiting for connection
    connectionSocket, addr = serverSocket.accept()

    while (loggedIn):
        print("Connected to client")
        # Read bytes from socket
        sentence = connectionSocket.recv(1024)


        sentenceString = sentence.decode('utf-8')
        print("received: ", sentenceString)

        response = 0

        if sentenceString[0] == 'l': # l for log out
            loggedIn = False
            response = "Bye!".encode('utf-8')
        elif sentenceString[0] == 'c': # c for check balance
            response = ("Your Current balance: $" +  str(bankBalance)).encode('utf-8')
        elif sentenceString[0] == 'e': # e for edit balance
            num = int(sentenceString[1:])
            if bankBalance + num >= 0:
                bankBalance += num
                response = ("Your Current balance: $" + str(bankBalance)).encode('utf-8')
            else:
                response = ("Error! You can't take out $" + str(-1 * num) + " you only have $" + str(bankBalance)).encode('utf-8')
        else:
            response = "Error".encode('utf-8')


        # Send it into established connection
        connectionSocket.send(response)

    print("closing connection to client")
    # Close connection to client but do not close welcome socket
    connectionSocket.close()
