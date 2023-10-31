i = 0

while True:
  print('{}번째 반복문입니다.'.format(i))
  i += 1
  input_text = input('> 종료하시겠습니까?(y/n): ')
  if input_text in ['y', 'Y']:
    print('반복문을 종료합니다.')
    break