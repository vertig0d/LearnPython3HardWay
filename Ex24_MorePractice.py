print('includes everything used till now')
print("you\'d need to know \'bout escapes with \\ that do:")
print('\n newlines and \t tabs')
poem = """
line1
line2
line3
"""

print('------')
print(poem)
print('------')

five = 10 -2 + 3 - 6
print(f'this should be five {five}')

def secretFormula(started):
	jellyBeans = started * 500
	jars = jellyBeans / 1000
	crates = jars / 100
	return jellyBeans, jars, crates

startingPoint = 10000
beans, jars, crates = secretFormula(startingPoint)
print('with starting point of {}'.format(startingPoint))
print(f'we have {beans} beans, {jars} jars and {crates} crates')
startingPoint = startingPoint / 100

print('we can do this another way')
formula = secretFormula(startingPoint)
print('we have {} beans, {} jars, {} crates.'.format(*formula))
