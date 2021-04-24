from threading import Condition
import threading

# 条件变量，用于复杂的线程间同步
class XiaoAi(threading.Thread):
    def __init__(self, cond):
        super().__init__(name = "xiaoai")
        self.cond = cond
    def run(self) -> None:
        with self.cond:
            self.cond.wait()
            print("{}:在".format(self.name))
            self.cond.notify()
            print("{}:我们来对古诗吧".format(self.name))

class TianMao(threading.Thread):
    def __init__(self, cond):
        super().__init__(name = "tianmao")
        self.cond = cond
    def run(self) -> None:
        with self.cond:
            print("{}:小爱同学".format(self.name))
            self.cond.notify()
            self.cond.wait()
            print("{}:好啊".format(self.name))


if __name__ == '__main__':
    cond = Condition()
    xiaoAi = XiaoAi(cond=cond)
    tianMao = TianMao(cond=cond)

    # 1. 启动顺序很重要
    # 2. 在调用with cond之后才能调用wait或者notify方法，with自动实现了acquire和release，否则需要自己输入这两者
    # 3. condition有两层锁，一把底层锁会在线程调用了wait方法的时候释放，上面的锁会在每次调用wait的时候分配一把并发
    # 到cond的等待队列中，等待notify方法的唤醒。

    xiaoAi.start()  # 必须先启动xiaoai，不然notify唤醒不了xiaoai。
    tianMao.start()
