# import sys

def check(answer, guess):
	bulls = 0
	cows = 0
	answer = str(answer)
	guess = str(guess)
	for x in range(0, len(answer)):
		# foundX = false;
		for y in range(0, len(guess)):
			if answer[x] == guess[y]:
				if x == y:
					bulls += 1
				else:
					cows += 1
	retVal = {'bulls': bulls, 'cows': cows}
	return retVal


# print "Enter your next guess:"
# guess = raw_input()
# result = check(9370, guess)
# print result
