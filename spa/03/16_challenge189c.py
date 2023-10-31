input = input('정수를 입력해주세요:')
inputLength = len(input)
isMTP = 0 # 각 자리 수의 합을 구하기 위한 변수
isMPT3 = 0 # 3의 배수인지 확인

for i in range(inputLength):
  isMTP += int(input[i]) # 각 자리 수를 모두 더하고, isMTP에 최종 저장됨

# 여기서 부터 if문 시작

if isMTP % 3 == 0:
  print('3의 배수입니다.')
  isMPT3 = True

if int(input[-1]) % 4 == 0 \
or int(input[-2:]) % 4 == 0:
  print('4의 배수입니다.')

if int(input[-1]) == 0 \
or int(input[-1]) == 5:
  print('5의 배수입니다.')

if int(input) % 2 == 0 and isMPT3:
  print('6의 배수입니다.')

if isMTP % 9 == 0:
  print('9의 배수입니다.')

if int(input[-1]) == 0:
  print('10의 배수입니다.')