import socket

def receive_and_save_messages(host, port):
    # Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Bind the socket to a specific host and port
        server_socket.bind((host, port))
        print(f"Server listening on {host}:{port}")

        # Enable the server to accept connections
        server_socket.listen()

        while True:
            # Accept a connection from a client
            client_socket, client_address = server_socket.accept()
            print(f"Accepted connection from {client_address}")

            try:
                # Receive the message from the client
                message = client_socket.recv(1024).decode('utf-8')
                print(f"Received message: {message}")

                # Write the message to the .env file
                with open(".env", "w") as env_file:
                    env_file.write(message + "\n")
                    print("Message written to .env file")

            except Exception as e:
                print(f"Error: {e}")

            finally:
                # Close the client socket
                client_socket.close()

# Replace these with your server details
server_host = "0.0.0.0"  # Listen on all available interfaces
server_port = 8080

receive_and_save_messages(server_host, server_port)
