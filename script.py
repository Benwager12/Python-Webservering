from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

def parseData(data):
    ndata = dict()
    for i in data.decode("utf-8").strip().split("\n"):
        sp0, sp1 = i[0:-1].split(": ")
        ndata[sp0] = sp1
    return ndata

def main(html = str()):
    with open("body.html") as file:
        html = file.read()

    host, port = '', 8080

    listen_socket = socket(AF_INET, SOCK_STREAM)
    listen_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    listen_socket.bind((host, port))
    listen_socket.listen(1)
    print(f"Serving HTTP on port {port}")

    client_connection, client_address = listen_accept()
    try:
        while True:
            request_data = client_connection.recv(1024)
            args = {"Referer": "Smith"}
            #args = parseData(request_data)

            try:
                client_connection.sendall(html.format(**args).encode())
            except KeyError as e:
                print(e)
                continue
    except KeyboardInterrupt:
        client_connection.close()

if __name__ == "__main__":
    main()
