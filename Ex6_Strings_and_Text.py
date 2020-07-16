types_of_people = 10
x = f"There are {types_of_people} types of people"
 
binary = 'binary'
dont = "don't"
y = f"Those who know {binary} and those who {dont}"
print(y)

print(f"I said {x}")
print(f"I also said {y}")

hilarious = False
joke_eval = "Isn't this joke funny {}"
print(joke_eval.format(hilarious))

w = "This is the left side.."
e = "of a string with right side"
print(w + e) 