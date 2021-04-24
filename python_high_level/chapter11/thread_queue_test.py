# 线程间的通信方式：通过queue的方式进行线程间的同步
from queue import Queue
# Queue是线程安全的

import threading
import time


def get_detail_html(queue):
    # 爬取文章详情页
    while True:
        url = queue.get()
        print("get detail html started")
        time.sleep(2)
        print("get detail htm end")

def get_detail_url(queue):
    # 爬取文章列表页
    while True:
        print("get detail html started")
        time.sleep(2)
        for i in range(20):
            queue.put("thhp://projectsedu.com/{id}".format(id=i))
        print("get detail htm end")



if __name__ == '__main__':
    detail_url_queue = Queue(maxsize=1000)


    thread_detail_url = threading.Thread(target=get_detail_url, args = (detail_url_queue,))
    for i in range(10):
        html_thread = threading.Thread(target = get_detail_html, args = (detail_url_queue,))
        html_thread.start()
    start_time = time.time()
    detail_url_queue.task_done() # 退出主线程
    detail_url_queue.join() # 从queue的角度阻塞进程
    print("last time: {}".format(time.time() - start_time))
