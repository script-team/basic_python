import socket

host = 'localhost', 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    data = input("Enter a sentence: ")
    if data == "q":
        break
    sock.sendto(data.encode('utf-8'), host)
    ret, server = sock.recvfrom(4096)
    print(ret)
sock.close()
