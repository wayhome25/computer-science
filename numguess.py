import random


answer = random.randint(1, 100)
print(answer)

username = input("what is you name?")
chance = 3
while True:
	guess = eval(input('hello %s Guess the number : ' % username))
	if guess == answer:
		print("Correct")
		break
	elif guess > answer:
		chance -= 1
		print("Too High, (%d times left)" % (chance))
	elif guess < answer:
		chance -= 1
		print("Too low, (%d times left)" % (chance))
	if chance == 0:
		print("The End")
		break	
