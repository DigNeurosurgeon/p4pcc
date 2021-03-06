# A little number guessing game

import random

# Create a random solution
solution = random.randint(0, 100)

# Set guess to a start value that cannot be the solution
guess = -1

print 'This is a number guessing game'
print 'Enter a whole number between 0 and 100...'

# Now keep asking until the user guessed the correct answer
while guess != solution:

	# Ask user for a guess
	guess = int(raw_input('Your guess: '))
	print 'You guessed: %i' % guess
	
	# Compare guess with solution
	if guess > solution:
		print 'Too high!'
	elif guess < solution:
		print 'Too low!'
	else:
		print 'Congratulations, %i is the correct answer!' % guess