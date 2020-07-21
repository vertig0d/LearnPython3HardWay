def cheeseNcrackers(numCheese, boxesOfCrackers):
	print(f'you have {numCheese} of cheese')
	print(f'you have {boxesOfCrackers} boxes of crackers')

#function can be called in following ways
cheeseNcrackers(10,20) #method1 
cheeseNcrackers(100 + 10, 200 + 20) #method2

amt_cheese = 30
amt_boxCrackers = 40
cheeseNcrackers(amt_cheese, amt_boxCrackers) #method3
cheeseNcrackers(amt_cheese + 100, amt_boxCrackers + 100) #method4
