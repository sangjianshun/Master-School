
# 需要一个可以暂停的函数，并且可以在适当的时候回复该函数的继续执行
# 协程：可以暂停的函数（可以向暂停的地方传入值），或者有多个入口的函数即生成器



def get_func():
    # 可以产出值，可以接收值（调用方传递进来的值）
    html = yield "test11"
    print(html)
    yield 2
    yield 3
    return "test"

# 生成器不只可以产出值，还可以接收值

if __name__ == '__main__':
    gen = get_func()
    url = next(gen) # 在调用send发送非none值之前，我们必须启动一次生成器，方式有两种，gen.send(None)或者next(gen)
    # download url
    html="html"
    gen.send(html) # send可以传递值进入生成器内部，同时还可以重启生成器执行到下一个yield位置
    # 启动生成器的方式有两种，next和send
    print(next(gen))
    # print(next(gen))
    # print(next(gen))
