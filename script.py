import socket
import json

def parseData(data):
    data = data.decode('utf-8')
    data = data.strip()
    data = data.split("\n")
    ndata = []
    for i in data:
        ndata.append(i[0:-1])
    data = {}
    for i in ndata[1:]:
        sp = i.split(": ")
        data[sp[0]] = sp[1]
    return data

file = open("body.html", "r").read()


host, port = '', 8080

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((host, port))
listen_socket.listen(1)
print("Serving HTTP on port",port)

while True:
    client_connection, client_address = listen_socket.accept()
    request_data = client_connection.recv(1024)
    args = {"Referer": "Smith"}
    #args = parseData(request_data)

    try:
        client_connection.sendall(file.format(**args).encode())
    except KeyError as e:
        print(e)
        continue
    client_connection.close()


