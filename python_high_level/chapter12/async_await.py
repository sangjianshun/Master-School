# python 3.5以后，为了将语义变得更加明确，就引入了async和await关键词用于定义原生的携程

from collections import Awaitable

async def downloader(url):
    return "test"

# import types
# @types.coroutine # 必须加上装饰器，否则会报错
# def downloader(url):
#     yield "test"

# 不能在内部使用yield
# await只能出现在async

async def download_url(url):
    # dosomethins
    html = await downloader(url)

    return html

if __name__ == '__main__':
    coro = download_url("test_url")
    # next(None)
    coro.send(None)