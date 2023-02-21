# import time
# print(time.time())

# import turtle
# turtle.forward(1000)
# turtle.left(1200)
# turtle.forward(1000)
# turtle.left(1200)
# turtle.forward(1000)

# name = "a"
# p = "Hello, {n}"
# print(p.format(n=name))

# print("hello ooo ")
# print("hello ooo ", end="")
# print("not change line")

# a, b, c = 1, True, False
# # print(type(a))
# # print(type(b))
# print(isinstance(b, bool))
# print(isinstance(b, int))
# print(type(b))

# print(2/4) # float result
# print(2//4) # int result
# print(2**4)

# list1 = [1, 'abc', 2.3, True]
# list2 = ['wahaha', False]
# print(list2)
# print(list1[1:3])
# print(list1[-3:-1])
# print(list1 + list2)
# print(list2*2)
# list2[1] = 567
# print(list2)

# tuple1 = (1, 'abc', 2.3, True)
# tuple2 = (1, 2.3)
# print(tuple2 * 2)
# print(tuple1[1:3])
# tup1 = ()  # empty tuple
# tup2 = (2, )  # one element in tuple, need ','
# print(tup1)
# print(tup2)

# Set
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


# dict1 = {}
# dict1['one'] = 'hello'
# dict1[2] = 34
# print(dict1)
# print(dict1.keys())
# print(dict1.values())
# print(dict1["one"])


# names = ['Alice', 'Bob', 'wendy']
# new_names = [name.upper() for name in names if len(name) > 3]
# print(new_names)

# multiples = [i for i in range(20) if i % 3 == 0]
# print(multiples)

# dic = {x: x**2 for x in (2, 4, 6) if x > 2}
# print(dic)

# setnew = {i**2 for i in (1, 2, 3) if i < 3}
# print(setnew)

# lst = [1, 2]
# lst.append(3)
# print(lst)
# lst.extend([4])
# print(lst)

# tup = tuple(lst)
# print(tup)

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


for number in range(1, 6, 2):
    print(number, end=', ')
else:
    print('finish')
