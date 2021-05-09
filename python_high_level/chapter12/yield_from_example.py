

def sales_sum(pro_Name):
    total = 0
    nums = []
    while True:
        x = yield
        if not x:
            break
        total += x
        nums.append(total)
    return total,nums

if __name__ == '__main__':
    my_gen = sales_sum("test")
    my_gen.send(None)
    my_gen.send(100)
    my_gen.send(200)
    my_gen.send(300)
    try:
        my_gen.send(None)
    except StopIteration as e:  # 如果使用yield from就不需要这一步的处理
        result = e.value
        print(result)