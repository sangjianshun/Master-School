def gen_func():
    try:
        yield "test11"
    except Exception as e:
        pass
    yield 2
    yield 3
    return "test"

if __name__ == '__main__':
    gen = gen_func()
    print(next(gen))
    gen.throw(Exception,"down load error")
    next(gen)

    # GeneratorExit是继承自BaseException，而不是Exception