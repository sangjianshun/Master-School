import socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(("127.0.0.1", 8000))
client.send("t1".encode("utf8"))
client.close()