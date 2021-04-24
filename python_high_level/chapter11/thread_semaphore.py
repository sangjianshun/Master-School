# Semaphore 是用于控制进入数量的锁
# 文件，读，写，写一般只适用于一个线程写，读可以允许有多个

# 做爬虫，

import threading
import time


class HtmlSpider(threading.Thread):
    def __init__(self, url,sem):
        super(HtmlSpider, self).__init__()
        self.url = url
        self.sem = sem
    def run(self) -> None:
        time.sleep(2)
        print("get html text success")
        self.sem.release()

class UrlProducer():
    def __init__(self, sem):
        super(UrlProducer, self).__init__()
        self.sem = sem

    def run(self):
        for i in range(20):
            self.sem.acquire()
            html_thread = HtmlSpider("https://baidu.com/{}".format(i),self.sem)
            html_thread.start()

if __name__ == '__main__':
    sem = threading.Semaphore(3)
    urlProducer = UrlProducer(sem)
    urlProducer.run()
