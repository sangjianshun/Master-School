# 事件循环+回调（驱动生成器） + epoll(IO多路复用)
# asyncio是python用于解决异步io编程的一整套解决方法
# tornado、gevent、twisted(scrapy， django channels)
# tornado（实现web服务器），django+flask(uwsgi, gunicorn+nginx)
# tornado可以直接部署，nginx + tornado
#
# 使用asyncio

import asyncio
import time


async def get_html(url):
    print("start get url")
    await asyncio.sleep(2) # 不能使用time.sleep  要接一个awaitable
    print("end get url")


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    tasks = [get_html("test1") for i in range(10)]
    loop.run_until_complete(asyncio.wait(tasks))
    print(time.time() - start_time)


# 获取协程的返回值
import asyncio
import time


async def get_html(url):
    print("start get url")
    await asyncio.sleep(2) # 不能使用time.sleep  要接一个awaitable
    return "hahah"

from functools import partial  # 解决传参的问题
def callback(url,future):
    print(url)
    print("send email")

if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    # get_future = asyncio.ensure_future(get_html("test1"))
    get_future = loop.create_task(get_html("test1"))  # 和上一句话等价
    get_future.add_done_callback(partial(callback, "url"))
    loop.run_until_complete(get_future)
    print(get_future.result())

#wait和gather的区别

async def get_html(url):
    print("start get url")
    await asyncio.sleep(2) # 不能使用time.sleep  要接一个awaitable
    print("end get url")


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    tasks = [get_html("test1") for i in range(10)]
    # loop.run_until_complete(asyncio.wait(tasks))
    # loop.run_until_complete(asyncio.gather(*tasks)) # 和上面那句话等价
    # print(time.time() - start_time)

    # gather和wait的区别
    # gather更加high-level
    tasks1 = [get_html("test1") for i in range(10)]
    tasks2 = [get_html("test2") for i in range(10)]

    loop.run_until_complete(asyncio.gather(*tasks1, * tasks2))



    print(time.time() - start_time)