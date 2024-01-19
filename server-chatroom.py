import threading
import socket

host = '127.0.0.1'
port = 59000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host, port))
server.listen()
clients = []
aliases = []


def boardcast(pesan):
    for client in clients:
        client.send(pesan)

def handle_clients(client):
    while True:
        try:
            pesan = client.recv(1024)
            boardcast(pesan)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            boardcast(f"{alias} sudah meninggalkan chat room !!".encode('utf-8'))
            aliases.remove(alias)
            break

def receive():
    while True:
        print('server berjalan dan mendengarkan...')
        client, address = server.accept()
        print(f"terhubung dengan {str(address)}")
        client.send("alias ? ".encode('utf-8'))
        alias = client.recv(1024)
        aliases.append(alias)
        clients.append(client)
        print(f"seseorang dari client ini adalah {alias}".encode('utf-8'))
        boardcast(f"{alias} sudah terhubung kedalam chat room".encode('utf-8'))
        thread = threading.Thread(target=handle_clients, args=(client,))
        thread.start()

if __name__ == "__main__":
    receive()