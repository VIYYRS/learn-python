# spa/05/00
# def print_3_times():
#   print('안녕하세요')
#   print('안녕하세요')
#   print('안녕하세요')
# print_3_times()

# spa/05/01
# def print_n_times(value, n):
#   for i in range(n):
#     print(value)
# print_n_times('안녕하세요', 5)

# spa/05/02
# def print_n_times(n, *values):
#   for i in range(n):
#     for value in values:
#       print(value)
#     print()
# print_n_times(3, '안녕하세요', '즐거운', '프로그래밍')

# spa/05/03
# def print_n_times(value, n=2):
#   for i in range(n):
#     print(value)
# print_n_times('안녕하세요')

# spa/05/04
# def print_n_times(*values, n=2):
#   for i in range(n):
#     for value in values:
#       print(value)
#     print()
# print_n_times('안녕하세요', '즐거운', '파이썬 프로그래밍', n=3)

# spa/05/05
# def test(a, b=10, c=100):
#   print(a + b + c)
# test(10, 20, 30)
# test(a=10, b=100, c=200)
# test(c=10, a=100, b=200)
# test(10, c=200)

# spa/05/06
# def return_test():
#   print('A 위치입니다.')
#   return
#   print('B 위치입니다.')
# return_test()

# spa/05/07
# def return_test():
#   return 100
# value = return_test()
# print(value)

# spa/05/08
# def return_test():
#   return
# value = return_test()
# print(value)

# spa/05/09
# def sum_all(start, end):
#   output = 0
#   for i in range(start, end + 1):
#     output += i
#   return output
# print('0 to 100:', sum_all(0, 100))
# print('0 to 1000:', sum_all(0, 1000))
# print('50 to 100:', sum_all(50, 100))
# print('500 to 1000:', sum_all(500, 1000))

# spa/05/10
# def sum_all(start=0, end=100, step=1):
#   output = 0
#   for i in range(start, end + 1, step):
#     output += i
#   return output
# print('A.', sum_all(0, 100, 10))
# print('B.', sum_all(end=100))
# print('C.', sum_all(end=100, step=2))

# def mul(*values):
#   result = 1
#   for value in values:
#     result *= value
#   return result
# print(mul(5, 7, 9, 10))

# spa/05/11
# def factorial(n):
#   output = 1
#   for i in range(1, n + 1):
#     output *= i
#   return output
# print('1!:', factorial(1))
# print('2!:', factorial(2))
# print('3!:', factorial(3))
# print('4!:', factorial(4))
# print('5!:', factorial(5))

# spa/05/12
# def factorial(n):
#   if n == 0:
#     return 1
#   else:
#     return n * factorial(n - 1)
# print('1!:', factorial(1))
# print('2!:', factorial(2))
# print('3!:', factorial(3))
# print('4!:', factorial(4))
# print('5!:', factorial(5))

# spa/05/13
# def fibonacci(n):
#   if n == 1:
#     return 1
#   if n ==2:
#     return 1
#   else:
#     return fibonacci(n - 1) + fibonacci(n - 2)
# print('fibonacci(1):', fibonacci(1))
# print('fibonacci(2):', fibonacci(2))
# print('fibonacci(3):', fibonacci(3))
# print('fibonacci(4):', fibonacci(4))
# print('fibonacci(5):', fibonacci(5))

# spa/05/14
# counter = 0
# def fibonacci(n):
#   print('fibonacci({})를 구합니다'.format(n))
#   global counter
#   counter += 1
#   if n == 1:
#     return 1
#   if n == 2:
#     return 1
#   else:
#     return fibonacci(n - 1) + fibonacci(n - 2)
# fibonacci(10)
# print('---')
# print('fibonacci(10) 계산에 활용된 덧셈 횟수는 {}번입니다.'.format(counter))

# spa/05/15
# counter = 0
# def fibonacci(n):
#   print('fibonacci({})를 구합니다'.format(n))
#   counter += 1
#   if n == 1:
#     return 1
#   if n == 2:
#     return 1
#   else:
#     return fibonacci(n - 1) + fibonacci(n - 2)
# print(fibonacci(10))

# spa/05/16
# dictionary = {
#   1: 1,
#   2: 1
# }
# def fibonacci(n):
#   if n in dictionary:
#     return dictionary[n]
#   else:
#     output = fibonacci(n - 1) + fibonacci(n - 2)
#     dictionary[n] = output
#     return output
# print('fibonacci(10):', fibonacci(10))
# print('fibonacci(20):', fibonacci(20))
# print('fibonacci(30):', fibonacci(30))
# print('fibonacci(40):', fibonacci(40))
# print('fibonacci(50):', fibonacci(50))

# spa/05/17
# def flatten(data):
#   print(data)
#   output = []
#   for item in data:
#     print(item)
#     if type(item) == list:
#       output += item
#     else:
#       output.append(item)
#   return output
# example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
# print('원본: ', example)
# print('변환: ', flatten(example))

# spa/05/18
# def flatten(data):
#   output = []
#   for item in data:
#     if type(item) == list:
#       output += flatten(item) # 함수만 호출하면 output이 초기화 됨 (함수안에 배열 초기화 코드가 있기 때문)
#     else:
#       output.append(item)
#   return output
# example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
# print('원본: ', example)
# print('변환: ', flatten(example))

# spa/05/18 - 실험
# output = [] # 함수안(flatten)에서 자신(flatten)이 실행될때 배열 초기화 방지
# def flatten(data):
#   for item in data:
#     if type(item) == list:
#       flatten(item) # 초기화 되지 않기 때문에 함수 호출만 해도됨
#     else:
#       output.append(item)
#   return output
# example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
# print('원본: ', example)
# print('변환: ', flatten(example))

# 앉힐수있는최소사람수 = 2
# 앉힐수있는최대사람수 = 10
# 전체사람의수 = 100
# memo = {}
# def 문제(남은사람수, 앉힌사람수):
#   key = str([남은사람수, 앉힌사람수])
#   if key in memo:
#     return memo[key]
#   if 남은사람수 < 0:
#     return 0
#   if 남은사람수 == 0:
#     return 1
#   x = 0
#   for i in range(앉힌사람수, 앉힐수있는최대사람수 + 1):
#     x += 문제(남은사람수-i, i)
#   memo[key] = x
#   return x
# print(문제(전체사람의수, 앉힐수있는최소사람수))
# print(memo)

# spa/05/19
# [a, b] = [10, 20]
# (c, d) = (30, 40)
# print('a:', a)
# print('b:', b)
# print('c:', c)
# print('d:', d)

# spa/05/20
# tuple_test = 10, 20, 30, 40
# print('# 괄호가 없는 튜플의 값과 자료형 출력')
# print('tuple_test:', tuple_test)
# print('type(tuple_test)', type(tuple_test))
# print()
# a, b, c = 10, 20, 30
# print('# 괄호가 없는 튜플을 활용한 할당')
# print('a:', a)
# print('b:', b)
# print('c:', c)

# spa/05/21
# a, b = 10, 20
# print('# 교환 전 값')
# print('a:', a)
# print('b:', b)
# print()
# a, b = b, a
# print('# 교환 후 값')
# print('a:', a)
# print('b:', b)
# print()

# spa/05/22
# def test():
#   return (10, 20)
# a, b = test()
# print('a:', a)
# print('b:', b)

# spa/05/23
# def call_10_times(func):
#   for i in range(10):
#     func()
# def print_hello():
#   print('안녕하세요')
# call_10_times(print_hello)

# spa/05/24
# def power(item):
#   return item * item
# def under_3(item):
#   return item < 3
# list_input_a = [1, 2, 3, 4, 5]
# output_a = map(power, list_input_a)
# print('# map() 함수 실행 결과')
# print('map(power, list_input_a):', output_a)
# print('map(power, list_input_a):', list(output_a))
# print()
# output_b = filter(under_3, list_input_a)
# print('# filter() 함수 실행 결과')
# print('filter(under_3, list_input_a):', output_b)
# print('filter(under_3, list_input_a):', list(output_b))

# spa/05/25
# power = lambda x: x * x
# under_3 = lambda x: x < 3
# list_input_a = [1, 2, 3, 4, 5]
# output_a = map(power, list_input_a)
# print('# map() 함수 실행 결과')
# print('map(power, list_input_a):', output_a)
# print('map(power, list_input_a):', list(output_a))
# print()
# output_b = filter(under_3, list_input_a)
# print('# filter() 함수 실행 결과')
# print('filter(under_3, list_input_a):', output_b)
# print('filter(under_3, list_input_a):', list(output_b))

# spa/05/26
# list_input_a = [1, 2, 3, 4, 5]
# output_a = map(lambda x: x * x, list_input_a)
# print('# map() 함수 실행 결과')
# print('map(power, list_input_a):', output_a)
# print('map(power, list_input_a):', list(output_a))
# print()
# output_b = filter(lambda x: x < 3, list_input_a)
# print('# filter() 함수 실행 결과')
# print('filter(under_3, list_input_a):', output_b)
# print('filter(under_3, list_input_a):', list(output_b))

# spa/05/27
# file = open('spa/05/27_basic.txt', 'w')
# file.write('Hello Python Programming...!')
# file.close()

# spa/05/28
# with open('spa/05/27_basic.txt') as file:
#   contents = file.read()
# print(contents)

# spa/05/29
# import random
# hanguls = list('가나다라마바사아자차카타파하')
# with open('spa/05/29_data.txt', 'w') as file:
#   for i in range(1000):
#     name = random.choice(hanguls) + random.choice(hanguls)
#     weight = random.randrange(40, 100)
#     height = random.randrange(140, 200)
#     file.write('{}, {}, {}\n'.format(name, weight, height))

# spa/05/30
# with open('spa/05/29_data.txt', 'r') as file:
#   for line in file:
#     (name, weight, height) = line.strip().split(', ')
#     if (not name) or (not weight) or (not height):
#       continue
#     bmi = int(weight) / ((int(height)/100)**2)
#     result = ''
#     if 25 <= bmi:
#       result = '과체중'
#     elif 18.5 <= bmi:
#       result = '정상체중'
#     else:
#       result = '저체중'
#     print('\n'.join([
#       '이름: {}',
#       '몸무게: {}',
#       '키: {}',
#       'BMI: {}',
#       '결과: {}'
#     ]).format(name, weight, height, bmi, result))
#     print()

# spa/05/31
# def test():
#   print('A 지점 통과')
#   yield 1
#   print('B 지점 통과')
#   yield 2
#   print('C 지점 통과')
# output = test()
# print('D 지점 통과')
# a = next(output)
# print(a)
# print('E 지점 통과')
# b = next(output)
# print(b)
# print('F 지점 통과')
# c = next(output)
# print(c)
# next(output)

# spa/05/32
# books = [{
#   '제목': '혼자 공부하는 파이썬',
#   '가격': 18000
# }, {
#   '제목': '혼자 공부하는 머신러닝 + 딥러닝',
#   '가격': 26000
# }, {
#   '제목': '혼자 공부하는 자바스크립트',
#   '가격': 24000
# }]
# def 가격추출함수(book):
#   return book['가격']
# print('# 가장 저렴한 책')
# print(min(books, key=가격추출함수))
# print()
# print('# 가장 비싼 책')
# print(max(books, key=가격추출함수))

# spa/05/33
# books = [{
#   '제목': '혼자 공부하는 파이썬',
#   '가격': 18000
# }, {
#   '제목': '혼자 공부하는 머신러닝 + 딥러닝',
#   '가격': 26000
# }, {
#   '제목': '혼자 공부하는 자바스크립트',
#   '가격': 24000
# }]
# print('# 가장 저렴한 책')
# print(min(books, key=lambda book: book['가격']))
# print()
# print('# 가장 비싼 책')
# print(max(books, key=lambda book: book['가격']))

# spa/05/34
# books = [{
#   '제목': '혼자 공부하는 파이썬',
#   '가격': 18000
# }, {
#   '제목': '혼자 공부하는 머신러닝 + 딥러닝',
#   '가격': 26000
# }, {
#   '제목': '혼자 공부하는 자바스크립트',
#   '가격': 24000
# }]
# print('가격 오름차순 정렬')
# books.sort(key=lambda book: book['가격'])
# for book in books:
#   print(book)