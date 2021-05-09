# 1. epoll并不代表一定比select好
# 在并发高的情况下，连接或于都不是很高，epoll比select好 （网站场景下，用户建立连接随时可能断掉）
# 并发性不高，同时连接很活跃，select比epoll好 （比如游戏开发场景，游戏建立连接一般不会断）


# 通过非阻塞IO实现http请求

# requests -> urlib -> socket
import socket
from urllib.parse import urlparse



# 使用非阻塞式IO完成http请求
# client.setblocking(False)

def get_url(url):
    # 通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"
    #建立socket连接
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.setblocking(False)
    try:
        client.connect((host, 80))  # OSError: [WinError 10057] 由于套接字没有连接并且(当使用一个 sendto 调用发送数据报套接字时)没有提供地址，发送或接收数据的请求没有被接受。
    except BlockingIOError as e:
        pass

    while True:
        try:
            client.send("GET {} HTTP/1.1\r\nhost:{}\r\nConnection:close\r\n\r\n".format(path,host).encode("utf8"))
            break
        except OSError as e:
            pass

    data = b""
    while True:
        try:
            d = client.recv(1024)
        except BlockingIOError as e:
            continue

        if d:
            data += d
        else:
            break
    data =data.decode("utf8")
    html_data = data.split("\r\n\r\n")[1]
    print(html_data)
    client.close()
if __name__ == '__main__':
    get_url("http://www.baidu.com")
