import socket

HOST = 'localhost'
PORT = 8009
OUTPUT_FILE = "/home/admin-it/hackrush/FTP/files/down_file.wma"

_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
_socket.connect((HOST, PORT))

print ("Client is downloading")

f = open(OUTPUT_FILE, 'wb')

while 1:
    recv_file = _socket.recv(1024)

    while recv_file:
        f.write(recv_file)
        recv_file = _socket.recv(1024)

    break

f.close()
_socket.close()

print ("Download complete")
