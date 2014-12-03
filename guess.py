# A little number guessing game

import random

# Create a random solution
solution = random.randint(0, 100)

# Set guess to a start value
guess = -1

# Now keep asking until the user guessed the correct answer
while guess != solution:

	# Ask user for a guess
	guess = int(raw_input('Enter a whole number between 0 and 100:'))
	print 'You guessed: %i' % guess
	
	# Compare guess with solution
	if guess > solution:
		print 'Too high!'
	elif guess < solution:
		print 'Too low!'
	else:
		print 'Congratulations, %i is the correct answer!' % guess