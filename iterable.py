from collections import Iterable

l = [1, 2, 3, 4]
t = (1, 2, 3, 4)
d = {1: 2, 3: 4}
s = {1, 2, 3, 4}

str='hello pussy'

# print(isinstance(l, Iterable))
# print(isinstance(t, Iterable))
# print(isinstance(d, Iterable))
# print(isinstance(s, Iterable))
# print(isinstance(str, Iterable))

# print(dir([1,2]))
# # print(dir((2,3)))
# # print(dir({1:2}))
# # print(dir({1,2}))

print(set(dir([1,2].__iter__()))-set(dir([1,2])))
