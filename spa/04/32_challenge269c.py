ord = input('염기서열을 입력해주세요: ') # ctacaatgtcagtatacccattgcattagccgg
x = 0 # 3씩 증가하게\
y = 3 # x 공통
dict = {}

for i in range(int(len(ord) / 3)):
  val = str(ord)[x:y]
  if val in dict:
    dict[val] += 1
  else:
    dict[val] = 1
  x += 3
  y += 3
  
print(dict)