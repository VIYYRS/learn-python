array = [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]
dict = {}

for i in array:
  if i in dict:
    dict[i] += 1
  else:
    dict[i] = 1

print('{}에서\n사용된 숫자의 종류는 {}개입니다.\n참고: {}'.format(array, len(dict), dict))