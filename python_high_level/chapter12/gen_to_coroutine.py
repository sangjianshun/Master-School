# 生成器是可以暂停的函数

import inspect
def gen_func():
    yield 1  # 返回值给调用方；调用方通过send方式返回值给gen  value = yield  这就是协程
    return "test"
# 用同步的方式编写异步的代码；在适当的时候暂停函数并在适当的时候启动函数

def get_socket_data():
    yield "test"

def downloader(url):
    a = yield from get_socket_data()
    print(a)

def download_html(html):
    html = yield from downloader()

# 携程的调度仍然是  事件循环+携程模式   携程是单线程模式

if __name__ == '__main__':
    gen = gen_func()
    print(inspect.getgeneratorstate(gen))
    next(gen)
    print(inspect.getgeneratorstate(gen))
    try:
        next(gen)
    except StopIteration:
        pass
    print(inspect.getgeneratorstate(gen))