import socket

HOST = '127.0.0.1'
PORT = 5555

def receive():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Bind the socket to the address and port
        server_socket.bind((HOST, PORT))

        # Listen for incoming connections
        server_socket.listen()
        print(f"Server is listening on {HOST}:{PORT}")

        while True:
            # Accept a new connection
            client_socket, client_address = server_socket.accept()
            print(f"New connection from {client_address}")

            # Handle the client connection in a separate function or thread
            handle_client(client_socket, client_address)

    except OSError as e:
        print(f"Error: {e}")

    finally:
        # Close the server socket
        server_socket.close()

def handle_client(client_socket, client_address):
    try:
        while True:
            # Receive data from the client
            data = client_socket.recv(1024)
            if not data:
                break

            # Process the received data (e.g., echo back to client)
            message = data.decode('utf-8')
            print(f"Received from {client_address}: {message}")

            # Echo back to the client
            client_socket.sendall(data)

    except OSError as e:
        print(f"Error handling client: {e}")

    finally:
        # Close the client socket
        client_socket.close()
        print(f"Connection closed with {client_address}")

if __name__ == "__main__":
    receive()
