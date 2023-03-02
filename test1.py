# import time
# print(time.time())

# import turtle
# turtle.forward(1000)
# turtle.left(1200)
# turtle.forward(1000)
# turtle.left(1200)
# turtle.forward(1000)

''' String '''
# name = "a"
# p = "Hello, {n}"
# print(p.format(n=name))

# print("hello ooo ")
# print("hello ooo ", end="")
# print("not change line")

''' variable type '''
# a, b, c = 1, True, False
# # print(type(a))
# # print(type(b))
# print(isinstance(b, bool))
# print(isinstance(b, int))
# print(type(b))

''' math '''
# print(2/4) # float result
# print(2//4) # int result
# print(2**4)

''' List '''
# list1 = [1, 'abc', 2.3, True]
# list2 = ['wahaha', False]
# print(list2)
# print(list1[1:3])
# print(list1[-3:-1])
# print(list1 + list2)
# print(list2*2)
# list2[1] = 567
# print(list2)

""" list method """
# a = [3, 5, 1, 3]
# print(a.count(3), a.count('x'))
# print(a.index(1))
# a.insert(2, -1)
# print(a.index(1))
# a.sort()
# print(a)
# a.reverse()
# print(a)


''' Tuple '''
# tuple1 = (1, 'abc', 2.3, True)
# tuple2 = (1, 2.3)
# print(tuple2 * 2)
# print(tuple1[1:3])
# tup1 = ()  # empty tuple
# tup2 = (2, )  # one element in tuple, need ','
# print(tup1)
# print(tup2)

""" nested tuple """
# t = 1, 23, 'hello'
# print(t[0])
# print(t)
# # nested tuple
# u = t, (1, 2, 3)
# print(u)

''' Set '''
# sites = set()
# print(sites)
# sites = {'Google', 'Facebook', "Google"}
# print(sites)
# if 'Google' in sites:
#     print('Google is in sites')
# else:
#     print('Google is not in sites')
# a = set('abcde')
# b = set('bcdfg')
# print(a - b)
# print(a | b)
# print(a & b)
# print(a ^ b)

# a = set('abracadabra')
# b = set('alacazam')
# print(a)
# print(b)
# print(a - b)
# a = {e for e in 'abracadabra' if e not in 'abc'}
# print(a)
# a.add('l')
# a.update({1, 2})
# a.update([3, 4], [5, 6])
# print(a)
# a.remove(1)
# a.discard(7)
# print(a)
# a.pop()
# print(a)

''' Dictionary '''
# dict1 = {}
# dict1['one'] = 'hello'
# dict1[2] = 34
# print(dict1)
# print(dict1.keys())
# print(dict1.values())
# print(dict1["one"])

''' for-loop, if-condition '''
# names = ['Alice', 'Bob', 'wendy']
# new_names = [name.upper() for name in names if len(name) > 3]
# print(new_names)

# multiples = [i for i in range(20) if i % 3 == 0]
# print(multiples)

# dic = {x: x**2 for x in (2, 4, 6) if x > 2}
# print(dic)

# setnew = {i**2 for i in (1, 2, 3) if i < 3}
# print(setnew)

# for number in range(1, 6, 2):
#     print(number, end=', ')
# else:
#     print('finish')


''' list -> tup '''
# lst = [1, 2]
# lst.append(3)
# print(lst)
# lst.extend([4])
# print(lst)

# tup = tuple(lst)
# print(tup)


''' iterator, next()'''
# import sys
# lst = [1, 2, 3]
# it = iter(lst)
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()

''' iterator, yield '''
# fibonacci use yield
# import sys
# def fibonacci(n):
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         yield a
#         a, b = b, a + b
#         counter += 1
# f = fibonacci(10)
# while True:
#     try:
#         print(next(f), end=' ')
#     except StopIteration:
#         sys.exit()

''' Function '''
# def printinfo(arg1, *vartuple):
#     "print all the input arguments"
#     print("Output:")
#     print(arg1)
#     for x in vartuple:
#         print(x)
#     return
# printinfo(1)
# printinfo(2, 3, 4)

# def f(a, b, *, c):
#     return a + b + c
# print(f(1, 2, c=3))

# x = lambda a, b: a + b
# print(x(2,3))


''' List used as Queue '''
# from collections import deque
# queue = deque(['Eric', 'John', 'Micheal'])
# queue.append('Ted')
# queue.append('George')
# print(queue)
# print(queue.popleft())  # The FIFO
# print(queue.popleft())
# print(queue)

# vec = [2, 4, 6]
# print([[x, x**2] for x in vec if x > 3])

''' transfer a 3x4 matrix into a 4x3 matrix '''
# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(matrix)
# print(len(matrix[0]))
# # method 1:
# martix1 = [[row[i] for row in matrix] for i in range(4)]
# print(martix1)
# method 2:
# transposed = []
# for i in range(4):
#     transposed.append([row[i] for row in matrix])
# print(transposed)
