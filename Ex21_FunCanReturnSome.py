def add(a,b):
	print(f'adding {a} and {b}')
	return a+b

def subtract(a,b):
	print(f'subtracting {a} and {b}')
	return a-b

def multiply(a,b):
	print(f'multiply {a} and {b}')
	return a * b

def divide(a,b):
	print(f'divide {a} and {b}')
	return a/b

age = add(30 , 5)
height = subtract(70, 20)
weight = multiply(50, 2)
iq = divide(100, 2)
print(f'age: {age}, height: {height}, weight: {weight}, iq: {iq}')

print(add(age, subtract(height, multiply(weight, divide(iq, 2)))))
