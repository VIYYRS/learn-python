def power(item):
  return item * item
def under_3(item):
  return item < 3

list_input_a = [1, 2, 3, 4, 5]

output_a = map(power, list_input_a)
print('# map() 함수 실행 결과')
print('map(power, list_input_a):', output_a)
print('map(power, list_input_a):', list(output_a))
print()

output_b = filter(under_3, list_input_a)
print('# filter() 함수 실행 결과')
print('filter(under_3, list_input_a):', output_b)
print('filter(under_3, list_input_a):', list(output_b))