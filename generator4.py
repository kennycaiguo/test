# 利用yield from完成股票的计算，yield from能够完成一个委派生成器的作用，在子生成器和调用者之间建立起一个双向通道。


def son_gen():
    avg_num = 0
    sum_num = 0
    count = 1
    while True:
        num = yield avg_num
        if num:
            sum_num += num
            avg_num = sum_num/count
            count += 1
        else:break
    return avg_num

def depute_gen(key):
    while True:
        ret = yield from son_gen()
        print(key,ret)

def main():
    shares_list= {
        'sogou':[6.4,6.5,6.6,6.2,6.1,6.6,6.7],
        'alibaba':[181.72,184.58,183.54,180,88,169.88,178.21,189.32],
        '美团':[59.7,52.6,47.2,55.4,60.7,66.1,74.0]
    }
    for key in shares_list:
        g = depute_gen(key)
        next(g)
        for v in shares_list[key]:
            g.send(v)
        g.send(None)

main()