try:
    import binascii
    from socket import socket, AF_INET, SOCK_STREAM
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('172.16.127.233', 1234))

    while True:
        if s.recv(512) != None:
            print(s.recv(512))
        else:
            continue
    # s.send(b'Hello')
    # print(int.from_bytes(s.recv(5), byteorder='little'))
    # s.close()

except Exception as e:
    print(e)
