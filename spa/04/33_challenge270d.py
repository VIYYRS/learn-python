array = [1, 2, [3, 4], 5, [6, 7], [8, 9]]

for i in array:
  if type(i) == list:
    for x in i:
      print(x)
  else:
    print(i)