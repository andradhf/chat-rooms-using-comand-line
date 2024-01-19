import threading
import socket

alias = input("masukkan nama alias anda >> ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 59000
client.connect((host, port))

def client_receive():
    while True:
        try:
            pesan = client.recv(1024).decode('utf-8')
            if pesan == "alias ?":
                client.send(alias.encode('utf-8'))
            else:
                print(pesan)
        except:
            print("error!!")
            client.close()
            break

def client_send():
    while True:
        pesan = (f'{alias}: {input(">> ")}')
        client.send(pesan.encode('utf-8'))

receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()