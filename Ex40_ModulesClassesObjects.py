class Song(object):
	
	def __init__(self,lyrics):
		self.lyrics = lyrics
	
	def sing_me(self):
		for line in self.lyrics:
			print(line)
	
happy_bday = Song(['happy bday to you',
'happy bday t o you',
'happy bday dear something'])

bulls_on_parade = Song(['they rally around tha family',
'with pockets full of shells'])

happy_bday.sing_me()
bulls_on_parade.sing_me()
