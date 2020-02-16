import numbers
def cal_sum():
    sum_num = 0
    while True:
        num = yield
        if isinstance(num,numbers.Integral):
            sum_num += num
            print('sum :',sum_num)
        elif num is None:
            break
    # yield 1000
g = cal_sum()
g.send(None)   # 相当于next(g),预激活生成器
g.send(31)
g.send(25)
g.send(17)
g.send(8)


# print(next(g))

