import socket

def run_receiver(host, port):
    # Create a TCP/IP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    print(f"Listening on {host}:{port}...")

    conn, addr = s.accept()  # Wait for a connection
    print(f"Connected by {addr}")

    with conn:
        data = b""  # Initialize an empty byte string for data accumulation
        while True:
            packet = conn.recv(1024)  # Receive data in chunks of 1024 bytes
            if not packet:  # If no more data is received
                break
            data += packet  # Accumulate received data

        print(f"Received: {data}")  # Process the received data

def send_data(host: str, port: int, data: bytes):
    # Create a TCP/IP socket and send data
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))  # Connect to the server
        s.sendall(data)  # Send the entire data

def receive_data(host: str, port: int, buffer_size: int = 1024):
    # Create a TCP/IP socket and receive data
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        print(f"Listening for incoming data on {host}:{port}...")
        conn, addr = s.accept()  # Accept incoming connections
        with conn:
            data = b""  # Initialize an empty byte string for data accumulation
            while True:
                packet = conn.recv(buffer_size)
                if not packet:  # If no more data is received
                    break
                data += packet  # Accumulate received data
    return data  # Return the accumulated data
