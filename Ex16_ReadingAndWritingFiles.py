from sys import argv
script, filename = argv

print('we are going to clear ',filename)
print('hit ctrl-c to quit')
print('return to continue')
input('?')
target = open(filename, 'w')

#truncating file content
target.truncate()

print('enter 3 lines')
line1 = input('line1: ')
line2 = input('line2: ')
line3 = input('line3: ')

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)

print('now we close file')
target.close()
