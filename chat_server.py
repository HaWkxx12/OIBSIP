import socket
import threading

# Server configuration
HOST = '127.0.0.1'
PORT = 5555

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

def receive_messages():
    """Receives and displays messages from the server."""
    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(message)
    except ConnectionResetError:
        print("Disconnected from the server.")

def send_message():
    """Prompts the user to enter messages and sends them to the server."""
    try:
        while True:
            message = input()
            if message.lower() == 'exit':
                break
            client_socket.sendall(message.encode('utf-8'))
    except ConnectionResetError:
        print("Disconnected from the server.")

# Start threads for sending and receiving messages
receive_thread = threading.Thread(target=receive_messages, daemon=True)
send_thread = threading.Thread(target=send_message, daemon=True)

receive_thread.start()
send_thread.start()

# Wait for send thread to finish (user exits with 'exit')
send_thread.join()

# Close the socket
client_socket.close()
