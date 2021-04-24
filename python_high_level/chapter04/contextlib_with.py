import contextlib

@contextlib.contextmanager
def file_open(file_name):
    print("file open") # enter
    yield {} # 生成器的特性后面讲
    print("file end") # exit

with file_open("xxx.txt") as file:
    print("file processing") # file open  file processing  file end 
