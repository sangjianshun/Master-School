def fun():
    try:
        print("code start")
        raise KeyError
        return 1
    except KeyError as e:
        print("key error")
        return 2
    else:
        print("other error")
        return 3
    finally:
        print("finally")
        return 4

# 上下文管理器协议
class Sample():
    def __enter__(self):
        print("enter")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")
    def do_something(self):
        print("doing something")

with Sample() as sample:
    sample.do_something()

# if __name__ == '__main__':
#     result = fun()
#     print(result) #注意这里返回的是4，不是2，底层是一个栈的结构[2,4]
