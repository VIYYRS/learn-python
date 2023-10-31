def flatten(data):
  output = []
  for item in data:
    if type(item) == list:
      output += flatten(item) # 함수만 호출하면 output이 초기화 됨 (함수안에 배열 초기화 코드가 있기 때문)
    else:
      output.append(item)
  return output

example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print('원본: ', example)
print('변환: ', flatten(example))

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