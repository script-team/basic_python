import socket


host = 'localhost', 12345
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(host)
sock.listen(5)

while True:
    so, address = sock.accept()

    while True:
        data = so.recv(4096)
        if data:
            print(data.decode('utf-8'))
            so.send(data)
            if data == b'hello world':
                break
    so.close()
sock.close()
