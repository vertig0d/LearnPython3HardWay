def break_words(sentence):
	return sentence.split(' ')

def sortedWords(words):
	return sorted(words)

def printFirstWord(words):
	word = words.pop(0)
	print(word)

def printLastWord(words):
	word = words.pop(-1)
	print(word)

def sortSentence(sentence):
	words = break_words(sentence)
	return sortedWords(words)

def printFirstLastWord(sentence):
	words = break_words(sentence)
	printFirstWord(words)
	printLastWord(words)

def printFirstLastSorted(sentence):
	words = sortSentence(sentence)
	printFirstWord(words)
	printLastWord(words)
