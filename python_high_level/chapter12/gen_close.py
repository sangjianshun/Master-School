def gen_func():
    try:
        yield "test11"
    except GeneratorExit:
        pass  #RuntimeError: generator ignored GeneratorExit
        # raise StopIteration 这样不会抛出异常
    yield 2
    yield 3
    return "test"

if __name__ == '__main__':
    gen = gen_func()
    print(next(gen))
    gen.close()
    next(gen)

    # GeneratorExit是继承自BaseException，而不是Exception