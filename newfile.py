import random

number = random.randint(1, 999)
attempts = 0

while True:
	guess = int(input("Guess a number from 1 to 999: "))
	attempts += 1
	
	if guess == number:
		print("You guessed it in", attempts, "attempts!")
		break
	elif guess < number:
			print("Too low")
	else:
			print("Too high")