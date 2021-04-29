# 好处，并发性高。速度非常快。性能差异非常大。单线程

import socket
from urllib.parse import urlparse
from selectors import DefaultSelector,EVENT_WRITE,EVENT_READ

# 1、DefaultSelector封装了select，
# 2、自动选择epoll（linux）还是select（windows），很好
# 3、提供注册的机制

selector = DefaultSelector()
urls = ["http://www.baidu.com"]
stop = False

# 回调
class Fetcher:
    def connected(self,key):
        selector.unregister(key.fd)
        self.client.send("GET {} HTTP/1.1\r\nhost:{}\r\nConnection:close\r\n\r\n".format(self.path,self.host).encode("utf8"))
        selector.register(self.client.fileno(),EVENT_READ,self.readable)  #self.client.fileno()文件描述符,,回调函数

    def readable(self,key):
        d = self.client.recv(1024)
        if d:
            print(d)
            self.data += d
        else:
            selector.unregister(key.fd)
            data =self.data.decode("utf8")
            html_data = data.split("\r\n\r\n")[1]
            print(html_data)
            self.client.close()
            urls.remove(self.spider_url)
            if not urls:
                global stop
                stop = True



    def get_url(self,url):
        self.spider_url = url
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        self.data = b""
        if self.path == "":
            self.path = "/"
        #建立socket连接
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.client.setblocking(False)

        try:
            self.client.connect((self.host, 80))  # OSError: [WinError 10057] 由于套接字没有连接并且(当使用一个 sendto 调用发送数据报套接字时)没有提供地址，发送或接收数据的请求没有被接受。
        except BlockingIOError as e:
            pass
        # 注册
        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)  #self.client.fileno()文件描述符,写事件,回调函数


def loop():
    # 事件循环，不听的请求socket的状态并调用对应的回调函数
    # 1. select本身不支持register模式,
    # 2. socket状态变化以后的回调是由程序员完成
    while not stop:
        ready = selector.select()  # 寻找已经好的url，单线程模式
        for key,mask in ready:
            call_back = key.data
            call_back(key)
    # 回调+事件循环+select(epoll)

if __name__ == '__main__':
    fetcher = Fetcher()
    fetcher.get_url("http://www.baidu.com")
    loop()

