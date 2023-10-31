list_input_a = ['52', '273', '32', '72', '100']

try:
  number_input = int(input('정수 입력 > '))
  print('{}번째 요소: {}'.format(number_input, list_input_a[number_input]))
except ValueError:
  print('정수를 입력해 주세요!')
except IndexError:
  print('리스트의 인덱스를 벗어났어요!')