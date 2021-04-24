import socket
import threading
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("0.0.0.0", 8000))
server.listen()

def handle_sock(sock,addr):
    while True:
        data = sock.recv(1024)
        print(data.decode("utf8"))
        re_data = input()
        sock.send(re_data.encode("utf8"))

# 获取从客户端发送的数据
# 一次性获取1K的数据
while True:
    sock,addr = server.accept()
    # 用线程去处理新接收的连接（用户）
    client_thread = threading.Thread(target=handle_sock, args = (sock,addr))
    client_thread.start()

    # data = sock.recv(1024)
    # print(data.decode("utf8"))
    # re_data = input()
    # sock.send(re_data.encode("utf8"))


    # sock.send("hello {}".format(data.decode("utf8")).encode("utf8"))

# server.close()
# sock.close()