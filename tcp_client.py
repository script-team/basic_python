import socket

host = 'localhost', 12345
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(host)

while True:
    data = input("Enter a sentence (hello world to quit):")
    if data == "hello world":
        break
    else:
        sock.send(data.encode("utf-8"))
        ret = sock.recv(1024)
        print(ret.decode("utf-8"))
sock.close()
