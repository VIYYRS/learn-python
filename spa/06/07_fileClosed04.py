try:
  file = open('/spa/06/04_basic.txt', 'w')
  예외.발생해라()
except:
  print('오류가 발생했습니다.')

file.close()
print('# 파일이 제대로 닫쳤는지 확인하기')
print('file.closed:', file.closed)