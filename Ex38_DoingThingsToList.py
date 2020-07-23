ten_things = 'Apples Oranges crows telephone light sugar'
print('there are not 10 things in the list')

stuff = ten_things.split(' ')
more_stuff = ['day', 'night', 'song', 'frisbee', 'corn', 'banana', 'girl', 'boy']

while len(stuff) != 10:
	next_stuff = more_stuff.pop()
	print('adding: ',next_stuff)
	stuff.append(next_stuff)
	print('total items in list: ',len(stuff))

print('updated items in list: ', stuff)

print('lets have some fun with stuff')

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
