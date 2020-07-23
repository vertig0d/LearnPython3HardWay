i = 0
numbers = []
while i < 6:
	print('i at the top: ',i)
	numbers.append(i)
	
	i += 1
	print('values present in list: ',numbers)
	print('i at the bottom: ',i)

print('numbers in list:')
for val in numbers:
	print(val)
