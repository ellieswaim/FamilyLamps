import socket
import os
from dotenv import load_dotenv

def send_tcp_message(server_ip, server_port, message):
    # Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            # Connect to the server
            s.connect((server_ip, server_port))
            print(f"Connected to {server_ip}:{server_port}, ", os.environ.get("PYTHON_MSG"))

            # Send the message
            s.sendall(message.encode('utf-8'))
            print(f"Message sent: {message}")

            # Receive response (optional)
            response = s.recv(1024)
            # print(f"Received response: {response.decode('utf-8')}", os.environ.get("PYTHON_MSG"))
            print( "LAMP_R: " + str(os.environ.get("LAMP_R")) + "\nLAMP_G: " + str(os.environ.get("LAMP_G")) + "\nLAMP_B: " + str(os.environ.get("LAMP_B")) + "\nLAST_CHAGED_BY: " + str(os.environ.get("LAST_CHANGED_BY")))

        except Exception as e:
            print(f"Error: {e}")

# Replace these with your server details
server_ip = "127.0.0.1"
server_port = 8080
lamp_r = 255
lamp_g = 255
lamp_b = 0
last_changed_by="Thomas"
message_to_send = "LAMP_R=" + str(lamp_r) + "\nLAMP_G=" + str(lamp_g) + "\nLAMP_B=" + str(lamp_b) + "\nLAST_CHANGED_BY=" + last_changed_by

load_dotenv()

send_tcp_message(server_ip, server_port, message_to_send)
