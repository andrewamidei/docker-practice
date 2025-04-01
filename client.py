'''
Andrew Amidei
ID: 010923073
'''

import sys

# Import socket library
from socket import *

# Set hostname or IP address from command line or default to localhost
# Set port number by converting argument string to integer or use default
# Use defaults
if sys.argv.__len__() != 3:
    serverName = 'localhost'
    serverPort = 10273
# Get from command line
else:
    serverName = sys.argv[1]
    serverPort = int(sys.argv[2])

# Choose SOCK_STREAM, which is TCP
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect to server using hostname/IP and port
clientSocket.connect((serverName, serverPort))

loggedIn = True

while (loggedIn):
    print("Select an Option:")
    print("[1] Check Balance")
    print("[2] Deposit")
    print("[3] Withdraw")
    print("[4] Logout\n")

    message = input('Input an int above: ')


    while (not message.isdigit()) or int(message) < 1 or int(message) > 4:
        message = input('Bad input! try a number [1-4]: ')

    num = int(message)

    if num == 4:
        loggedIn = False
        message = "l" # l for log out
    else:
        if num == 2:
            message = input('Input your deposit amount: $')
            if (not message.isdigit()) or int(message) <= 0:
                message = "c" # c for check balance
                print("\nNo changes were made.")
            else:
                message = "e" + message
        elif num == 1:
            message = "c"
        elif num == 3:
            message = input('Input your withdraw amount: $')
            if (not message.isdigit()) or int(message) <= 0:
                message = "c" # c for check balance
                print("\nNo changes were made.")
            else:
                message = "e-" + message

    # Send it into socket to server
    sentenceBytes = message.encode('utf-8')
    clientSocket.send(sentenceBytes)

    modifiedSentence = clientSocket.recv(1024)

    print('\n{0}'.format(modifiedSentence.decode('utf-8')))
    print()

clientSocket.close()
