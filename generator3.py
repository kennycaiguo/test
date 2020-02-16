# l = ['h','e','l']
# dic = {'l':'v1','o':'v2'}
# s = 'eva'
# def yield_from_gen():
#     for i in l:
#         yield i
#     for j in dic:
#         yield j
#         # yield dic[j]
#     for k in s:
#         yield k
# for item in yield_from_gen():
#     print(item,end='')


# l = ['h','e','l']
# dic = {'l':'v1','o':'v2'}
# s = 'eva'
# def yield_from_gen():
#     yield from l
#     yield from dic
#     yield from s
# for item in yield_from_gen():
#     print(item,end='')

from itertools import chain
l = ['h','e','l']
dic = {'l':'v1','o':'v2'}
s = 'eva'
def yield_from_gen():
    yield from chain(l,dic,s)

for item in yield_from_gen():
    print(item,end='')