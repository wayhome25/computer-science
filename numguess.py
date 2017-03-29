import random


answer = random.randint(1, 100)
print(answer)

username = input("what is you name?")

while True:
	guess = eval(input('hello %s Guess the number : ' % username))
	if guess == answer:
		print("Correct")
		break
	elif guess > answer:
		print("Too High")
	elif guess < answer:
		print("Too low")
	else:
		print("You are wrong")
		
