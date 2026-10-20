import socket

HOST = '0.0.0.0'
PORT = 6000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("listening...")
    conn, addr = s.accept()
    with conn:
        print(f"Connected to: {addr}")
        while True:
            data = conn.recv(1024).decode('utf-8').strip()
            if not data:
                break
            elif data.lower() != 'end':
                print(f"Recieved: {data}")
                rev_msg = data[::-1]
                print(f"Sending: {rev_msg}")
                conn.sendall(rev_msg.encode('utf-8'))
            else:
                rev_msg = data[::-1]
                conn.sendall(rev_msg.encode('utf-8'))
                break