import socket


host = 'localhost', 12345
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(host)

while True:
    data, address = sock.recvfrom(4096)
    if data:
        sock.sendto(data, address)
        print(data)
sock.close()
