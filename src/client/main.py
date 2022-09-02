# CLIENT is the app running on the pi, which dials into the single central server

# HowTo from Yeti/Arch: https://docs.google.com/document/d/1li2G_2u5xTFF4rm5u4trYuiAlvXyD4TKvUp1g5Hk5vc/edit

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    data = s.recv(1024)


print(f"Received {data!r}")