from collections import Iterable

# l = [1, 2, 3, 4]
# t = (1, 2, 3, 4)
# d = {1: 2, 3: 4}
# s = {1, 2, 3, 4}
#
# str='hello pussy'

# print(isinstance(l, Iterable))
# print(isinstance(t, Iterable))
# print(isinstance(d, Iterable))
# print(isinstance(s, Iterable))
# print(isinstance(str, Iterable))

# print(dir([1,2]))
# # print(dir((2,3)))
# # print(dir({1:2}))
# # print(dir({1,2}))

# print(set(dir([1,2].__iter__()))-set(dir([1,2])))

# iter_l = [1,2,3,4,5,6].__iter__()
# #获取迭代器中元素的长度
# print(iter_l.__length_hint__())
# #根据索引值指定从哪里开始迭代
# print('*',iter_l.__setstate__(4))
# #一个一个的取值
# print('**',iter_l.__next__())
# print('***',iter_l.__next__())

l = [1,2,3,4]
l_iter = l.__iter__()
item = l_iter.__next__()
print(item)
item = l_iter.__next__()
print(item)
item = l_iter.__next__()
print(item)
item = l_iter.__next__()
print(item)
item = l_iter.__next__()
print(item)