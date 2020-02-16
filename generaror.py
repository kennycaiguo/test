def generator_func():
    print('a')
    yield 1
    print('b')
    yield 2
    print('c')
    yield 3
    print('d')

g = generator_func()
# ret1 = next(g)
# print(ret1)
# ret2 = next(g)
# print(ret2)
# ret3 = next(g)
# print(ret3)
for i in range(3):
   ret=next(g)
   print(ret)