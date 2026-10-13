# chat_client.py

# Allows the program to communicate over network connections (TCP/IP). Needed to connect to the chat server
# Allows running multiple tasks simultaneously. Since we want to send and receive at the same time!
import socket
import threading

#	HOST = server IP address.
# 127.0.0.1 means connect to server running on same machine.
# PORT = communication channel number.
# Must match server settings.
HOST = "127.0.0.1"
PORT = 5555

username = input("Choose your username: ")

# Creates a TCP socket.
# AF_INET = IPv4.
# SOCK_STREAM = TCP (reliable connection).
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#	Establishes connection to chat server.
#	If server is not running → connection fails.
client.connect((HOST, PORT))

#	Defines function responsible for listening to server messages.
def receive_messages():
    while True: # infinite loop, client always listens for the incoming messages
        try:
            message = client.recv(1024).decode("utf-8") # Waits for message from server. Receives up to 1024 bytes. Converts binary data → readable text.

            #handle handshake
            if message == "USERNAME": #	Server sends “USERNAME” when a new client connects. This is a signal asking for the user’s name.
                client.send(username.encode("utf-8")) # Sends username back to server. Encodes text into bytes for network transmission.
            else:
                print(message) # If message is normal chat text → display it.

        except: #handling connection errors
            print("Connection closed.")
            client.close() #close socket
            break

# function: sending message
def write_messages():
    while True:
        msg = input("") #	Wait for user to type message.
        message = f"{username}: {msg}" # Adds username prefix before message
        client.send(message.encode("utf-8")) # Converts text into bytes.

threading.Thread(target=receive_messages).start() # Start background thread for receiving messages. Allows messages to appear while user types.
threading.Thread(target=write_messages).start() # Start another thread for sending messages.