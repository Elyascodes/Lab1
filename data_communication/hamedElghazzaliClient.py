import socket
import sys

HOST = sys.argv[1]
PORT = int(sys.argv[2])

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connected!")

    while True:
        word = input("Enter in a word (end to quit): ")
        byte_data = word.encode('utf-8')
        s.sendall(byte_data)
        response = s.recv(1024).decode('utf-8').strip()
        print(f"Response: {response}")
        if response == "dne":
            break

