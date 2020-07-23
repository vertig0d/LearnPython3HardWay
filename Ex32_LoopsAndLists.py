the_count = range(0,6)
fruits = ['apple', 'orange', 'pear', 'apricot']
changes = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for i in the_count:
	print('the count: ',i)

for fruit in fruits:
	print('i have fruit of type: ', fruit)

for change in changes:
	print('i got: ', change)

element = []

for i in range(0,6):
	print('adding ',i,' to the list')
	element.append(i)

for i in element:
	print('element was ',i)
