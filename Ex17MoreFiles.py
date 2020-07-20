from sys import argv
from os.path import exists
script, fromFile, toFile = argv

print(f'copying file from {fromFile} to {toFile}')
infile = open(fromFile)
infile_data = infile.read()

print(f'input file has {len(infile_data)} bytes data')
print(f'does outfile exist {exists(toFile)}')
print('hit enter to continue, cntrl C to exit')

input()
outFile = open(toFile, 'w')
outFile.write(infile_data)

print('finished copying')

outFile.close()
infile.close()
