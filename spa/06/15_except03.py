list_input_a = ['52', '273', '32', '72', '100']

try:
  number_input = int(input('정수 입력 > '))
  print('{}번째 요소: {}'.format(number_input, list_input_a[number_input]))
  예외를.발생해주세요()
except ValueError as exception:
  print('정수를 입력해 주세요!')
  print('type(exception):', type(exception))
except IndexError as exception:
  print('리스트의 인덱스를 벗어났어요!')
  print('type(exception):', type(exception))