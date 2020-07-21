from sys import argv
script, inputFile = argv

def printAll(f):
	print(f.read())

def rewind(f):
	f.seek(0)

def printLine(line, f):
	print(line, f.readline())

filename = open(inputFile)

printAll(filename)
rewind(filename)

lineNum= 1
printLine(lineNum, filename)

lineNum += 1
printLine(lineNum, filename)

lineNum += 1
printLine(lineNum, filename)
