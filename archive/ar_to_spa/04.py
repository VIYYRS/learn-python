# spa/04/12
# for i in range(5):
#   print(str(i) + ' = 반복변수')
# print()
# for i in range(5, 10):
#   print(str(i) + ' = 반복변수')
# print()
# for i in range(0, 10, 3):
#   print(str(i) + ' = 반복변수')
# print()

# spa/04/13
# array = [273, 32, 103, 57, 52]
# for i in range(len(array)):
#   print('{}번째 반복: {}'.format(i, array[i]))

# # spa/04/14
# for i in range(4, 0 - 1, -1):
#   print('현재 반복 변수: {}'.format(i))

# spa/04/15
# for i in reversed(range(5)):
#   print('현재 반복 변수: {}'.format(i))

# spa/04/16
# output = ''
# for i in range(1, 10):
#   for j in range(0, i):
#     output += '*'
#   output += '\n'
# print(output)

# spa/04/17
# output = ''
# for i in range(1, 15):
#   for j in range(14, i, -1):
#     output += ' '
#   for k in range(0, 2 * i - 1):
#     output += '*'
#   output += '\n'
# print(output)

# spa/04/18
# while True:
#   print('.', end='')

# spa/04/19
# i = 0
# while i < 10:
#   print('{}번째 반복입니다.'.format(i))
#   i += 1

# spa/04/20
# list_test = [1, 2, 1, 2]
# value = 2
# while value in list_test:
#   list_test.remove(value)
# print(list_test)

# spa/04/21
# import time as a
# number = 0
# target_tick = a.time() + 5
# while a.time() < target_tick:
#   number += 1
# print('5초 동안 {}번 반복했습니다.'.format(number))

# spa/04/22
# i = 0
# while True:
#   print('{}번째 반복문입니다.'.format(i))
#   i += 1
#   input_text = input('> 종료하시겠습니까?(y/n): ')
#   if input_text in ['y', 'Y']:
#     print('반복문을 종료합니다.')
#     break

#spa/04/23
# numbers = [5, 15, 6, 20, 7, 25]
# for number in numbers:
#   if number < 10:
#     continue
#   print(number)

# key_list = ['name', 'hp', 'mp', 'level']
# value_list = ['기사', '200', '30', '5']
# character = {}
# for i in range(4):
#   character[key_list[i]] = value_list[i]
# print(character)

# limit = 10000
# i = 1
# while True:
#   sum_value = 0
#   for x in range(1, i):
#     sum_value += x
#   i += 1
#   if sum_value > limit:
#     break
# print('{}을 더할 때 {}을 넘으며 그때의 값은 {}입니다.'.format(i, limit, sum_value))

# max_value = 0
# a = 0
# b = 0

# for i in range(1, 100):
#   j = 100 - i
#   if (i*j > max_value):
#     max_value = i*j
#     a = i
#     b = j
# print('최대가 되는 경우: {} * {} = {}'.format(a, b, max_value))

# spa/04/24
# list_a = [1, 2, 3, 4, 5]
# list_reversed = reversed(list_a)
# print('# reversed() 함수')
# print('reversed([1, 2, 3, 4, 5])', list_reversed)
# print('list(reversed([1, 2, 3, 4, 5]))', list(list_reversed))
# print()
# print('# reversed() 함수와 반복문')
# print('for i in reversed([1, 2, 3, 4, 5]):')
# for i in reversed([1, 2, 3, 4, 5]):
#   print('-', i)

# spa/04/25
# example_list = ['요소A', '요소B', '요소C']
# print('# 단순 출력')
# print(example_list)
# print()
# print('# enumerate() 함수 적용 출력')
# print(enumerate(example_list))
# print()
# print('# enumerate() 함수로 강제 변환 출력')
# print(list(enumerate(example_list)))
# print()
# print('# 반복문과 조합하기')
# for i, value in enumerate(example_list):
#   print('{}번째 요소는 {}입니다.'.format(i, value))

# spa/04/26
# example_dictionary = {
#   '키A': '값A',
#   '키B': '값B',
#   '키C': '값C'
# }
# print('# 딕셔너리의 items() 함수')
# print('items():', example_dictionary.items())
# print()
# print('# 딕셔너리의 items() 함수와 반복문 조합하기')
# for key, element in example_dictionary.items():
#   print('dictionary[{}] = {}'.format(key, element))

# spa/04/27
# array = []
# for i in range(0, 20, 2):
#   array.append(i*i)
# print(array)

# spa/04/28
# array = [i*i for i in range(0, 20, 2)]
# print(array)

# spa/04/29
# array = ['사과', '자두', '초콜릿', '바나나', '체리']
# output = [fruit for fruit in array if fruit != '초콜릿']
# print(output)

# output = ''
# for i in range(1, 100):
#   v = '{:b}'.format(i)
#   x = v.count('0')
#   if x == 1:
#     print(i, v)

# output = [i for i in range(1, 100) if '{:b}'.format(i).count('0') == 1]
# for i in output:
#   print('{} : {}'.format(i, '{:b}'.format(i)))
# print('합계:', sum(output))

# spa/04/30
# array = [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]
# dict = {}
# for i in array:
#   if i in dict:
#     dict[i] += 1
#   else:
#     dict[i] = 1
# print('{}에서\n사용된 숫자의 종류는 {}개입니다.\n참고: {}'.format(array, len(dict), dict))

# spa/04/31
# ord = input('염기서열을 입력해주세요: ') # ctacaatgtcagtatacccattgcattagccgg
# print('a의 개수: {}\nt의 개수: {}\ng의 개수: {}\nc의 개수: {}\n'.format(ord.count('a'), ord.count('t'), ord.count('g'), ord.count('c')))

# spa/04/32
# ord = input('염기서열을 입력해주세요: ') # ctacaatgtcagtatacccattgcattagccgg
# x = 0 # 3씩 증가하게\
# y = 3 # x 공통
# dict = {}
# for i in range(int(len(ord) / 3)):
#   val = str(ord)[x:y]
#   if val in dict:
#     dict[val] += 1
#   else:
#     dict[val] = 1
#   x += 3
#   y += 3
# print(dict)

# spa/04/33
# array = [1, 2, [3, 4], 5, [6, 7], [8, 9]]
# for i in array:
#   if type(i) == list:
#     for x in i:
#       print(x)
#   else:
#     print(i)