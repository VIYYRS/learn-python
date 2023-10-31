import datetime

now = datetime.datetime.now()
month = now.month
if 3 <= month <= 5:
  print('현재는 봄입니다.')
elif 6 <= month <= 8:
  print('현재는 여름입니다.')
elif 9 <= month <= 11:
  print('현재는 가을입니다.')
else:
  print('현재는 겨울입니다.')